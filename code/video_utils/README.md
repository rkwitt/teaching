# Prepend short image-loop sequence to video

Sometimes you want to create an intro image for your video and show it for a few seconds (possibly with a fade-to-black effect at the end). It should also be quick
to do and not require to re-encode the full video. The following code does just that.

## Requirements

- **`ffmpy`** (tested with v0.3.0), install via `pip install ffmpy`
- **`colorama`**, install via `pip install colorama`
- **`blessings`**, install via `pip install blessings`

The last two packages are just for cmdline formatting.

## Usage

Assume you already have a video file `Video.mp4` and you created an intro image `Intro.png`.
