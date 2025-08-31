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
- RJ12 (6x6) Flat Modular Cable
  - [L-com Flat Modular Cable, RJ12 (6x6)](https://www.l-com.com/ethernet-flat-modular-cable-rj12-6x6-tinned-end-10-ft)
- 2 Position PCB Terminal Block
  - https://a.co/d/4GGZHqM
- 2 1K ohm Resistors
- Male Dupont jumper wires
- Female Dupont jumper wires
- Heat shrink tubing

In some places I used prefabricated wires with male/female Dupont connectors, removing the end I did not need.
This saved me time in manufacturing plus added some length to the overall harness.

Tool list and other items used for assembly: 
- Soldering Iron
- (Leadless) Solder
- Wire Strippers/Cutters
- Solder Flux (Optional)
- Dielectric Paste (Optional)

In the steps below I put soldering flux on the joint before soldering and dielectric paste on the soldered joint before placing and heating the heat shring tube.

### Create 3.5mm plug Harness
![IMG_0423-2](https://github.com/user-attachments/assets/6e1b76f7-941a-4c04-a12b-de625b68dee8)
![IMG_0426-2](https://github.com/user-attachments/assets/c43fde86-d6cd-4792-a106-a47137bb068b)
![IMG_0428-2](https://github.com/user-attachments/assets/a53e6c4d-43f0-42b9-aae7-da80548c95bc)

The 3.5mm plug harness connects the Raspberry Pi to the LM386 Audio Amplifier. Since the 3.5mm Male Plug Bare Wire has two audio outs
and the LM386 Audio Amplifie has one audio in we need to combine the L & R wires from the 3.5mm Plug Bare Wire into one using 1K ohm
resistors to prevent distort and component damage.

On the bare end wires on the 3.5mm Male Plug Wire:
- Solder a 1K ohm resistor to the red (left channel) wire. Place heat shrink tube over the soldered joint leaving the unsolded side of the resistor exposed.
- Solder a 1K ohm resistor to the white (right channel) wire. Place heat shrink tube over the soldered joint leaving the unsolded side of the resistor exposed.
- Solder the expossed ends of the 1K ohm resistors to a wire that has a female Dupont connector on the other end. Place heat shrink tube over the soldered joint.
  - I used a white wire with a female Dupont connector.
- Solder a wire with a female Dupont connector to the black (Ground) wire.
  - I used a black wire with a female Dupont connector.
- (Optional) Solder a wire to the green (mic) wire. Place heat shrink tube over the soldered joint.
  - Although the audio wire is unused in this setup I am leaving open the possibility of a future need.
  - I used a green wire with no connector.
- (Optional) Place heat shrink tubing (no Dielectric Paste) over all heat shunk joints to provide extra protection an support.
  - I used white heat shrink tube.

### Create RJ12 Harness

The RJ12 Harness connects the Raspberry Pi GPIO pins and the LM386 Audio Amplifier to the telephone.




