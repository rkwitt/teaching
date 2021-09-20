"""Prepend video with short intro sequence.

rkwitt, Univ. of Salzburg, 2021
"""

import os
import sys
import time
import ffmpy
import argparse
import tempfile

from utils import get_video_meta_data
from utils import extract_audio_info, extract_video_info
from utils import prepare_image_for_video
from utils import term


def parse_args():
    parser = argparse.ArgumentParser(description='Create release video')
    parser.add_argument('--input_video', 
                        type=str, 
                        help='Input file')
    parser.add_argument('--output_video', 
                        type=str, 
                        help='Output file')                    
    parser.add_argument('--intro_image', 
                        type=str, 
                        help='Intro image to show')
    parser.add_argument('--intro_time', 
                        type=int, 
                        default=4,
                        help='Intro time (in sec) to show')
    parser.add_argument('--verbose', 
                        action='store_true',
                        help='Enable verbose output')
    parser.add_argument('--fade', 
                        action='store_true',
                        help='Enable intro fading')

    args = parser.parse_args()
    return args


def create_intro_video(args, intro_image_file_name: str, video_info: dict, audio_info: dict):

    file_base = os.path.dirname(intro_image_file_name)
    file_name = os.path.splitext(os.path.basename(intro_image_file_name))[0]
    out_file_name = os.path.join(file_base, file_name + '.mp4')

    ff = ffmpy.FFmpeg(
        inputs={intro_image_file_name: 
                [
                    '-hide_banner',
                    '-loglevel', 'error',
                    '-loop', '1',
                    '-framerate', str(video_info['r_frame_rate']),
                    '-t', str(args.intro_time),
                ]
            },
        outputs={
            out_file_name: 
            [
                '-f', 'lavfi',
                '-i', 'anullsrc=channel_layout=mono:sample_rate={}'.format(audio_info['sample_rate']),
                '-filter_complex', '[0]scale={}:{}:force_original_aspect_ratio=increase,crop={}:{},setsar=1,format=yuv420p[v]'.format(
                    video_info['width'],
                    video_info['height'],
                    video_info['width'],
                    video_info['height'],
                ),
                '-map', '[v]',
                '-map', '1',
                '-c:v', 'libx264',
                '-c:a', 'aac',
                '-shortest', 
                '-y'
            ]
        })
    t0 = time.time()
    ff.run()
    t1 = time.time()
    if args.verbose:
        print(term.green + "Created intro video {} [{:0.3f}s]".format(out_file_name, t1-t0) + term.normal)
    return out_file_name


def concat(args, intro_video_file_name: str):

    temp_name = next(tempfile._get_candidate_names())
    with open(temp_name, 'w') as fid:
        fid.write("file " + intro_video_file_name + '\n')
        fid.write("file " + args.input_video)

    ff = ffmpy.FFmpeg(
        inputs={temp_name: [
            '-hide_banner',
            '-loglevel', 'error', 
            '-f', 'concat', '-safe', '0']},
        outputs={args.output_video: ['-c', 'copy', '-y', '-movflags', '+faststart']})

    t0 = time.time()
    ff.run()
    t1 = time.time()
    if args.verbose:
        print(term.green + "Concatenated [{},{}] -> {} [{:0.3f}s] ".format(
            intro_video_file_name, 
            args.input_video,
            args.output_video,
            t1-t0) + term.normal)
    os.remove(temp_name)


def create_intro_video_fade(args, video_info, intro_video_file_name: str):

    file_base = os.path.dirname(intro_video_file_name)
    file_name = os.path.splitext(os.path.basename(intro_video_file_name))[0]
    out_file_name = os.path.join(file_base, file_name + '_Fade.mp4')

    # computing fading parameters
    n_frames = args.intro_time * int(video_info['r_frame_rate'])
    start_fade_at = int(float(n_frames) * 0.7)

    ff = ffmpy.FFmpeg(
        inputs={intro_video_file_name: [
              '-hide_banner',
              '-loglevel', 'error',
        ]}, 
        outputs={
            out_file_name: 
            [   
                '-filter:v', 'fade=out:{}:{}'.format(start_fade_at, (n_frames - start_fade_at)-10),
                '-c:v', 'libx264',
                '-preset', 'veryfast',
                '-c:a', 'copy',
                '-y'
            ]
        })

    t0 = time.time()
    ff.run()
    t1 = time.time()
    if args.verbose:
        print(term.green + "Added intro fading [{:0.3f}s]".format(t1-t0) + term.normal)
    return out_file_name

def main():

    args = parse_args()

    meta_data = get_video_meta_data(args.input_video)
    
    video_info = extract_video_info(meta_data, args.verbose)
    audio_info = extract_audio_info(meta_data, args.verbose)

    intro_image_file_name = prepare_image_for_video(args.intro_image, 
                                                    video_info)

    intro_video_file_name = create_intro_video(
        args,
        intro_image_file_name,
        video_info, 
        audio_info)

    if args.fade:
        intro_video_file_name = create_intro_video_fade(
            args,
            video_info,
            intro_video_file_name)

    # 
    # Rather use Quicktime for concatenation
    #
    #concat(args, intro_video_file_name)
    #print(term.red + term.bold + "DONE!" + term.normal)

if __name__ == "__main__":
    main()


