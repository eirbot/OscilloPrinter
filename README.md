# Display images on an oscilloscope

## How it works

We transform a list of 2d points into a stereo wav file. When played, the cursor
on the oscilloscope goes through all the points. If we repeat this process,
thanks to the persistance of vision it is possible to see an image.

## Get started

1. Use the examples file in the `examples` directory as input to create to wav files: `output_x.wav` and `output_y.wav\*\*.
2. Import the two files as _raw data_ in Audacity (8 bytes unsigned, 1 channel).
3. Transform the two track into one in stereo.
4. Play it to two channels of the Oscilloscope set on "XY" mode.
5. Enjoy !
