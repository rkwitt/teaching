This code is based upon this [GitHub repo](https://github.com/meetshah1995/pytorch-semseg).

## Data

The data used during the lecture (NYUv2 depth dataset) can be downloaded [here](https://drive.google.com/open?id=1nXw4qA3tCg-EjzDlxaQyuacBPHlaZO-w)

## Pretrained model

The pretrained model used during the lecture can be downloaded [here](https://drive.google.com/file/d/1w-44gOgVv8n8_wQ_orEzX2Bb2xQfv2nR/view?usp=sharing)

## Training

Unpack the data to some directory on your harddisk and modify the `data_path` variable in `train.py`. Then, run, e.g.,
```
CUDA_VISIBLE_DEVICES="0" python train.py
```
assuming you have a GPU available. One model per epoch is stored under `/tmp/`.
