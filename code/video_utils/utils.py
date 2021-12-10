from colorama import Fore, Back, Style
from blessings import Terminal
import PIL
from PIL import Image
import subprocess
import ffmpy
import json
import os


term = Terminal()


def append_to_name(file_name, prefix=None):
    if prefix is None:
        return file_name
    
    file_base = os.path.dirname(file_name)
    file_name, ext = os.path.splitext(os.path.basename(file_name))
    out_file_name = os.path.join(file_base, file_name + prefix + ext)
    return out_file_name


def prepare_image_for_video(in_file_name: str, video_info: dict) -> str:
    out_file_name = append_to_name(in_file_name, '_forVideo')
    
    assert os.path.isfile(in_file_name)
    assert 'height' in video_info
    assert 'width' in video_info
    
    W = video_info['width']
    H = video_info['height']
    
    in_img = Image.open(in_file_name)
    in_img = in_img.resize((W,H))
    in_img.save(out_file_name)

    return out_file_name
    

def get_video_meta_data(filename: str):

    ff = ffmpy.FFprobe(
        inputs={filename: None},
        global_options=[
            '-v', 'quiet',
            '-print_format', 'json',
            '-show_format', 
            '-show_streams']).run(stdout=subprocess.PIPE)

    meta = json.loads(ff[0].decode('utf-8'))
    return meta


def extract_video_info(meta: dict, verbose = False):
    info = {}
    
    assert len(meta['streams']) == 2
    assert meta['streams'][0]['codec_name'] == 'h264'
    
    keys_fun = {
        'height': lambda x: int(x),
        'width': lambda x: int(x),
        'r_frame_rate': lambda x: x.split('/')[0]
    }

    if verbose:
        print(Fore.BLUE + \
              term.underline + term.bold + \
              "Video stream information:" + \
              term.normal)

    for k,f in keys_fun.items():
        info[k] = f(meta['streams'][0][k])
        if verbose:
            print(term.blue + \
                  "{:20s}: {}".format(k, str(info[k])) + \
                  term.normal)
                
    return info


def extract_audio_info(meta: dict, verbose = False):

    info = {}
    
    assert len(meta['streams']) == 2
    assert meta['streams'][1]['codec_name'] == 'aac'

    keys_fun = {
        'sample_rate': lambda x: int(x),
        'channel_layout': lambda x: x,
    }

    if verbose:
        print(term.blue + \
              term.underline + term.bold + \
              "Audio stream information:" + \
              term.normal)

    for k,f in keys_fun.items():
        info[k] = f(meta['streams'][1][k])
        if verbose:
            print(term.blue + \
                  "{:20s}: {}".format(k, str(info[k])) + \
                  term.normal)
    return info