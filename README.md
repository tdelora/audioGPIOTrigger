# audioGPIOTrigger

An extension of [simpleGPIO](https://github.com/tdelora/simpleGPIO/).

This script triggers a recording to be played via VLC on a Raspberry Pi
when a GPIO pin (default to pin 16 via variable {gpioPin}) goes to a high state.
When triggered it randomly selects and plays a file from a directory specified at startup.
Note: Directory {audioDirectory} is re-analyzed each time function playAudio() is invoked
to allow for the contents of the audio directory to be updated and utilized without
restarting this script.

## Applications
### Playing a recording on a telephone when handset is taken off the cradle.

![IMG_0690-3](https://github.com/user-attachments/assets/3579e806-ddcf-4b97-9c77-d0c4b0fc9580)

In this use case a modified Bell System 702BM (Princess) dial telephone is connected to a Raspberry Pi using bespoke harnesses.

Parts list (beyond the Raspberry Pi and telephone:
- 3.5mm Male Plug to Bare Wire Open End Headset TRRS Cord
  - https://a.co/d/dSmd9GR
- USB to 3.5mm Jack Audio Adapter (Optional)
  - https://a.co/d/4tLp2hc

