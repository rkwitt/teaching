# Prepending a short image-loop sequence to existing video

Sometimes you want to create an intro image for your video and show it for a few seconds (possibly with a fade-to-black effect at the end). It should also be quick
to do and not require to re-encode the full video. The following code does just that.

## Requirements

- **`ffmpy`** 
  - tested with v0.3.0
  - install via `pip install ffmpy`
- **`colorama`**
  - tested with v0.4.3
  - install via `pip install colorama`
- **`blessings`**
  - tested with v1.7
  - install via `pip install blessings`

The last two packages are just for cmdline formatting.

## Usage

Assume you already have a video file `video.mp4` and you created an intro image `dummy.png`, as shown below (e.g., using Powerpoint/Keynote, or whatever you desire). Assume they both reside in `/tmp/`.

![Dummy intro](Dummy.png "Dummy Intro")

*Currently, the code only suppors H.264 as video codec and AAC for audio (hardcoded). If you feel motivated, feel free to fix this.*

We are now going to prepend this slide for 4 seconds to the video, using

```bash
python create.py --input_video /tmp/video.mp4 \
    --intro_image /tmp/dummy.png \
    --verbose \
    --intro_time 4 \
    --output_video output.mp4
```

In case you want the intro to fade to black, use the `--fade` option (fade duration is hardcoded; again, feel free to fix) as follows:

```bash
python create.py --input_video /tmp/video.mp4 \
    --intro_image /tmp/dummy.png \
    --verbose \
    --intro_time 4 \
    --output_video output.mp4
```

`create.py` essentially (1) resizes the intro image (here: `dummy.png`) to the same spatial resolution as `video.mp4`, then (2) creates a short video sequence (at the same frame rate as `video.mp4` and adding a silent audio track with the same sample rate and mono/stereo set appropriately, as the audio track in `video.mp4`) that loops through the intro image. Next, (3) fading is added if required and (4) both clips are eventually concatenated. 

The whole process takes about 5 seconds to execute on a 90min video (running on a MacBook Air 2020). Try to get this done in that time using some fancy video editing software. Believe me, if you have to switch out intros regularly, this can be a pain to do.
