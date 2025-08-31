# audioGPIOTrigger

An extension of [simpleGPIO](https://github.com/tdelora/simpleGPIO/).

This script triggers a recording to be played via VLC on a Raspberry Pi
when a GPIO pin (default to pin 16 via variable {gpioPin}) goes to a high state.
When triggered it randomly selects and plays a file from a directory specified at startup.
Note: Directory {audioDirectory} is re-analyzed each time function playAudio() is invoked
to allow for the contents of the audio directory to be updated and utilized without
restarting this script.

## Application: Playing a recording on a telephone when handset is taken off the cradle.

![IMG_0690-3](https://github.com/user-attachments/assets/3579e806-ddcf-4b97-9c77-d0c4b0fc9580)

In this use case a modified Bell System 702BM (Princess) dial telephone is connected to a Raspberry Pi using bespoke harnesses.

Parts list (beyond the Raspberry Pi and telephone):
- 3.5mm Male Plug to Bare Wire Open End Headset TRRS Cord
  - https://a.co/d/dSmd9GR
- USB to 3.5mm Jack Audio Adapter (Optional)
  - https://a.co/d/4tLp2hc
- LM386 Audio Amplifier Module
  - https://a.co/d/29zcTLq
  - Two ways to power for Audio Amplifier: 
    - Via 9V Battery:
      - 9V Battery
      - 9V Battery Connector
        - https://a.co/d/ivKIYgw
    - Via 12V Power Supply:
      - 12V 1A Power Supply
        - https://a.co/d/aEelxUA
      - 12V 5A DC Female Power Plug
        - https://a.co/d/06SYlDA
- 2 Position PCB Terminal Block
  - https://a.co/d/4GGZHqM
- 2 1K ohm Resistors
- Male Dupont jumper wires
- Female Dupont jumper wires
- Heat shrink tubing

Tool list and other items used for assembly: 
- Soldering Iron
- (Leadless) Solder
- Wire Strippers/Cutters
- Solder Flux (Optional)
- Dielectric Paste (Optional)

In the steps below I put soldering flux on the joint before soldering and dielectric paste on the soldered joint before placing and heating the heat shring tube.


### Create 3.5mm Harness
