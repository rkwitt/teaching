#!/bin/bash

# DEPRECATED CODE (EXCEPT FOR STEREO->MONO CONVERSION)


SLIDE_IMG=$1
SLIDE_VID=$2
INP_VIDEO=$3
OUT_VIDEO=$4

# FIX LOW-VOLUME ISSUE
# ffmpeg -i 2-FormalModel_FiniteHypotheses-Part-II_Original.mp4 -codec:v copy -ac 1 -ab 192k -filter:a "volume=24dB" 2-FormalModel_FiniteHypotheses-Part-II_Original_FixedAudio.mp4


SLIDE_IMG_DIRN=`dirname ${SLIDE_IMG}`
SLIDE_IMG_FILE=`basename ${SLIDE_IMG} .png`

convert ${SLIDE_IMG} -resize 1920x1080! ${SLIDE_IMG_DIRN}/${SLIDE_IMG_FILE}_forVideo.png

ffmpeg -loop 1 \
	   -framerate 30 \
	   -t 4 \
	   -i ${SLIDE_IMG_DIRN}/${SLIDE_IMG_FILE}_forVideo.png \
	   -f lavfi \
	   -i anullsrc=channel_layout=mono:sample_rate=48000 \
	   -filter_complex "[0]scale=1920:1080:force_original_aspect_ratio=increase,crop=1920:1080,setsar=1,format=yuvj420p[v]" \
	   -map "[v]" \
	   -map 1 \
	   -c:v libx264 \
	   -c:a aac \
	   -shortest ${SLIDE_VID}

SLIDE_VID_DIRN=`dirname ${SLIDE_VID}`
SLIDE_VID_FILE=`basename ${SLIDE_VID} .mp4`

ffmpeg -i ${SLIDE_VID} \
	   -filter:v 'fade=out:80:30' \
	   -c:v libx264 \
	   -preset veryfast \
	   -c:a copy ${SLIDE_VID_DIRN}/${SLIDE_VID_FILE}_Fade.mp4

rm -rf tmp.txt
echo "file ${SLIDE_VID_DIRN}/${SLIDE_VID_FILE}_Fade.mp4" >> tmp.txt
echo "file ${INP_VIDEO}" >> tmp.txt

ffmpeg -f concat \
	   -i tmp.txt \
	   -c copy \
	   -movflags +faststart ${OUT_VIDEO}

rm -rf tmp.txt







