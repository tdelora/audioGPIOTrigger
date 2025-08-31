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
- RJ11 (6x) Female Socket Modular Connector
  - https://a.co/d/aUCKzzk
- RJ9 Modular connector for a Princess Phone.
  - [Princess Transformers and Parts](https://www.ericofon.com/catalog/parts/princess.htm)

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

In the steps below I put soldering flux on the joint before soldering and dielectric paste on the soldered joint before placing and heating the heat shrink tube. **Also you must place the heat srink tubes in place before solding/connecting the various parts. Don't forget to do this!**

### Create 3.5mm plug Harness
![IMG_0423-2](https://github.com/user-attachments/assets/6e1b76f7-941a-4c04-a12b-de625b68dee8)
![IMG_0426-2](https://github.com/user-attachments/assets/c43fde86-d6cd-4792-a106-a47137bb068b)
![IMG_0428-2](https://github.com/user-attachments/assets/a53e6c4d-43f0-42b9-aae7-da80548c95bc)

The 3.5mm plug harness connects the Raspberry Pi to the LM386 Audio Amplifier. Since the 3.5mm Male Plug Bare Wire has two audio outs
and the LM386 Audio Amplifier has one audio in we need to combine the L & R wires from the 3.5mm Plug Bare Wire into one using 1K ohm
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
![IMG_0634](https://github.com/user-attachments/assets/cb76d39f-5439-4135-8e8f-ca4b91e4f178)
![IMG_0699](https://github.com/user-attachments/assets/a32db50c-6aa1-4f78-ae12-297d6b2d8119)

The RJ12 Harness connects the Raspberry Pi GPIO pins and the LM386 Audio Amplifier to the telephone.

On the bare end wires on the RJ12 (6x6) Flat Modular Cable:
- Solder a 330 ohm resistor to the yellow wire. Solder a wire with a female Dupont connector to the other end of the resister. Place heat shrink tube over the soldered joints and resistor.
  - I used a yellow wire with a female Dupont connector.
- Solder a wire with a female Dupont connector to the blue wire.
  - I used a blue wire with a female Dupont connector.
- Solder wires with a male Dupont connector to the green, white, red and black wires. Place heat shrink tube over the soldered joints.
  - I matched the color of the wires with a male Dupont connector to the respective colors of the wires on the RJ12 Cable.
- (Optional) Place heat shrink tubing (no Dielectric Paste) in the following pairing over the heat shunk joints to provide extra protection an support:
  - Blue and yellow (I used yellow heat shrink tube)
  - Green and white (I used green heat shrink tube)
  - Red and black (I used green heat shrink tube)

## Create the Internal (Princess) Phone Harness

This harness allows for direct acceess to the phone's internal line switch and handset.

![IMG_0668](https://github.com/user-attachments/assets/a9ea1084-341f-453f-8503-a4e699e56e4e)
![IMG_0674](https://github.com/user-attachments/assets/1d9cce35-06b0-4172-bf1a-82855e93c6b4)

Notes:
- The harness replaces has a 6x6 RJ11 connector replacing the stock 4x4 RJ11 connector. I also used a new RJ9 connector vs the stock conector in case I made a mistake...  All this allows all communications from the Raspberry Pi to/from the phone to flow through the connector giving the complete setup a clean look.
- Using Dupont connectors gives us the ability to replace parts as needed however I found using typical Dupont black plastic housings for male/female connections did not always seat well so I decided to utilize the Dupont pins substituting heat shrink tubing for the housing. This maintains the harness flexability with a little extra work.
- Using a 2 Position PCB Terminal Block allows us to connect to the phone's internal line switch without modifying the wiring from the switch which would be very hard to replace if things go wrong.



