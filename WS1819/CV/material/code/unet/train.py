"""
Training a UNET segmentation model on NYUv2.
"""

import os
import sys
import yaml
import time
import shutil
import torch
import random
import argparse
import datetime
import numpy as np
import torch.nn as nn
import torch.nn.functional as F
from torch.optim import SGD, Adam
import torchvision.models as models
from torch.utils import data
from tqdm import tqdm

from torch.optim.lr_scheduler import StepLR 

from unet import unet
from metrics import runningScore, averageMeter
from nyuv2 import NYUv2Loader


def cross_entropy2d(input, target, weight=None):
    n, c, h, w = input.size()
    nt, ht, wt = target.size()

    if h != ht or w != wt:
        input = F.interpolate(
            input, 
            size=(ht, wt), 
            mode="bilinear", 
            align_corners=True)

    input = input.transpose(1, 2).transpose(2, 3).contiguous().view(-1, c)
    target = target.view(-1)
    loss = F.cross_entropy(
        input, 
        target, 
        weight=weight, 
        reduction='elementwise_mean', 
        ignore_index=250
    )
    return loss


def setup_seeds(seed):
    torch.manual_seed(seed)
    torch.cuda.manual_seed(seed)
    np.random.seed(seed)
    random.seed(seed)


def train():
    
    setup_seeds(1337)
    
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

    data_loader = NYUv2Loader
    data_path   = '/scratch_ssd/rkwitt/NYUv2/' 

    t_loader = data_loader(
        data_path, 
        is_transform=True, 
        split='training', 
        img_size=(224, 320))
    
    v_loader = data_loader(
        data_path, 
        is_transform=True, 
        split='val', 
        img_size=(224, 320))

    n_classes = t_loader.n_classes

    trainloader = data.DataLoader(
        t_loader, 
        batch_size=2, 
        num_workers=16, 
        shuffle=True)

    valloader   = data.DataLoader(
        v_loader, 
        batch_size=2, 
        num_workers=16, 
        shuffle=False) 
                                
    model = unet(
        num_classes=n_classes, 
        is_deconv=True,
        pretrained=True).to(device)
    model = torch.nn.DataParallel(
        model, 
        device_ids=range(torch.cuda.device_count()))

    optimizer = SGD(
        model.parameters(), 
        lr=1e-3,
        weight_decay=0.0005,
        momentum=0.99)

    scheduler = StepLR(
        optimizer, 
        step_size=30, 
        gamma=0.1)

    val_loss_meter      = averageMeter()
    running_metrics_val = runningScore(n_classes)

    for epoch_i in range(100):
        
        scheduler.step()

        lrs = []
        for param_group in optimizer.param_groups:
            lrs.append(param_group['lr'])

        print("=>Training epoch {} [lr={}]".format(epoch_i, lrs))

        # Training
        for i_trn, (images, labels) in tqdm(enumerate(trainloader)):

            images = images.to(device)
            labels = labels.to(device)

            model.train()
            optimizer.zero_grad()
            outputs = model(images)
            loss = cross_entropy2d(input=outputs, target=labels)
            loss.backward()
            optimizer.step()
            

        # Validation
        model.eval()
        with torch.no_grad():
            for i_val, (images_val, labels_val) in tqdm(enumerate(valloader)):
                
                images_val = images_val.to(device)
                labels_val = labels_val.to(device)

                outputs = model(images_val)
                val_loss = cross_entropy2d(input=outputs, target=labels_val)

                pred = outputs.data.max(1)[1].cpu().numpy()
                gt = labels_val.data.cpu().numpy()

                running_metrics_val.update(gt, pred)
                val_loss_meter.update(val_loss.item())


            print('Validation loss (avg): ', val_loss_meter.avg)
            score, class_iou = running_metrics_val.get_scores()
            for k, v in score.items():
                print(k, v)
            for k, v in class_iou.items():
                print(k, v_loader.cls_idx_to_name[k], v)

            val_loss_meter.reset()
            running_metrics_val.reset()
        

        torch.save(model.state_dict(), os.path.join('/tmp', 'unet_epoch_{}.pkl'.format(epoch_i)))

    
if __name__ == "__main__":
    train()
