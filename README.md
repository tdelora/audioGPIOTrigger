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
- RJ11 (6x6) Female Socket Modular Connector
  - https://a.co/d/aUCKzzk
- RJ9 Modular connector for a Princess Phone
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

In the steps below I put soldering flux on the joint before soldering and dielectric paste on the soldered joint before placing and heating the heat shrink tube. **Also you must place the heat shrink tubes in place before solding/connecting the various parts. Don't forget to do this!**

### Create 3.5mm plug Harness
![IMG_0423-3](https://github.com/user-attachments/assets/0611009d-8a9c-4c00-bcd3-f0ae9c2dc2b1)
![IMG_0426-3](https://github.com/user-attachments/assets/a17087b3-2e9e-499e-bc99-9120f189950e)
![IMG_0428-3](https://github.com/user-attachments/assets/50940c1f-5602-45a6-837e-eed4be2f923f)

The 3.5mm plug harness connects the Raspberry Pi to the LM386 Audio Amplifier. Since the 3.5mm Male Plug Bare Wire has two audio outs
and the LM386 Audio Amplifier has one audio in we need to combine the L & R wires from the 3.5mm Plug Bare Wire into one using 1K ohm
resistors to prevent distort and component damage.

On the bare end wires on the 3.5mm Male Plug Wire:
- Solder a 1K ohm resistor to the red (left channel) wire. Place heat shrink tube over the soldered joint leaving the unsolded side of the resistor exposed.
- Solder a 1K ohm resistor to the white (right channel) wire. Place heat shrink tube over the soldered joint leaving the unsolded side of the resistor exposed.
- Solder the exposed ends of the 1K ohm resistors to a wire that has a female Dupont connector on the other end. Place heat shrink tube over the soldered joint.
  - I used a white wire with a female Dupont connector.
- Solder a wire with a female Dupont connector to the black (Ground) wire.
  - I used a black wire with a female Dupont connector.
- (Optional) Solder a wire to the green (mic) wire. Place heat shrink tube over the soldered joint.
  - Although the audio wire is unused in this setup I am leaving open the possibility of a future need.
  - I used a green wire with no connector.
- (Optional) Place heat shrink tubing (no Dielectric Paste) over all heat shunk joints to provide extra protection and support.
  - I used white heat shrink tube.

### Create RJ12 Harness

![IMG_0634-2](https://github.com/user-attachments/assets/0099908f-1cf7-45db-815b-7caec83f8438)
![IMG_0699-2](https://github.com/user-attachments/assets/993f4532-e9e5-4fd3-bfef-e6697a69d0b3)

The RJ12 Harness connects the Raspberry Pi GPIO pins and the LM386 Audio Amplifier to the telephone.

On the bare end wires on the RJ12 (6x6) Flat Modular Cable:
- Solder a 330 ohm resistor to the yellow wire. Solder a wire with a female Dupont connector to the other end of the resister. Place heat shrink tube over the soldered joints and resistor.
  - I used a yellow wire with a female Dupont connector.
- Solder a wire with a female Dupont connector to the blue wire.
  - I used a blue wire with a female Dupont connector.
- Solder wires with a male Dupont connector to the green, white, red and black wires. Place heat shrink tube over the soldered joints.
  - I matched the color of the wires with a male Dupont connector to the respective colors of the wires on the RJ12 Cable.
- (Optional) Place heat shrink tubing (no Dielectric Paste) in the following pairing over the heat shunk joints to provide extra protection and support:
  - Blue and yellow (I used yellow heat shrink tube)
  - Green and white (I used green heat shrink tube)
  - Red and black (I used black heat shrink tube)

## Create the Internal (Princess) Phone Harness

This harness allows for direct acceess to the phone's internal line switch and handset.

![IMG_0668-2](https://github.com/user-attachments/assets/96162309-73bc-468e-9d9d-08f51c460b37)
![IMG_0674-2](https://github.com/user-attachments/assets/ff077a49-5119-43a0-a0d6-9a9be01b01fc)

Notes:
- The harness replaces has a 6x6 RJ11 connector replacing the stock 4x4 RJ11 connector. I also used a new RJ9 connector vs the stock conector in case I made a mistake...  All this allows all communications from the Raspberry Pi to/from the phone to flow through the connector giving the complete setup a clean look.
- Using Dupont connectors gives us the ability to replace parts as needed however I found using typical Dupont black plastic housings for male/female connections did not always seat well so I decided to utilize the Dupont pins substituting heat shrink tubing for the housing. This maintains the harness flexability with a little extra work.
- Using a 2 Position PCB Terminal Block allows us to connect to the phone's internal line switch without modifying the wiring from the switch which would be very hard to replace if things go wrong.

Phone Harness Build Steps:
- Connect female Dupont pins to the six wires on the RJ11 Female Socket Modular Connector.
  - You may need to remove any existing connectors first.
- Connect male Dupont pins to the wires four wires on the RJ9 Modular connector.
  - You may need to remove any existing connectors first.
- Cut 6 heat shrink tubing segments long enough to cover the male/female connections between the RJ11 Female Socket wires and the RJ9 Modular connector and male connectors on the 2 Position PCB Terminal Block. 
- Place the heat shrink tubing segments on the RJ11 Female Socket Modular Connector wires and connect as follows:
  - Connect the red, white, green and black RJ11 female Dupont pins to the same color wire male pins on the RJ9 Modular connector.
  - Connect the yellow and blue RJ11 female Dupont pins to male pins on the 2 Position PCB Terminal Block.
  - Coat each joint with Dielectric Paste, slide the heat shrink tubing segment over each joint and heat the shrink tube into place.

## Install the Internal (Princess) Phone Harness

![IMG_0678](https://github.com/user-attachments/assets/e66cf783-3fc0-4ae4-9831-b9c7820d5568)
![IMG_0682](https://github.com/user-attachments/assets/61ca4a2f-1376-4bc6-8386-99e39733ed43)

After removing the telephone cover:
- Remove the installed RJ9 and RJ11 Modular connectors
- Disconnect the orange wire from terminal 2 and the blue wire from terminal 4.
  - This will give us access to the phone switch.
  - <img width="266" alt="Screenshot 2025-07-07 at 16 40 40" src="https://github.com/user-attachments/assets/0b23ea7a-bc5f-4ca7-9dd5-206a7656238c" />
- Connect the 2 Position PCB Terminal Block to the wires from the line switch as follows:
  - The orange wire to the screw terminal for the yellow Dupont pin connected wire.
  - The blue wire to the screw terminal for the blue Dupont pin connected wire.
- Tuck the connected PCB Terminal Block under the wiring/equiment in the middle of the phone. Should fit easily.
- Place the RJ9 Modular connector in the slot in the front of the phone, tucking the wiring along the side of the phone and not impeding the mechanical operations.
- Place the RJ11 Modular connector in the slot in the back of the phone, tucking the wiring under the equiment to not impede the mechanical operations.

After checking the phone mechanical operations reconnect the telephone cover.

## Prep power for the LM386 Audio Amplifier Module
![IMG_0415](https://github.com/user-attachments/assets/529ef727-f049-40f1-8334-47439b1a7658)
![IMG_0715-2](https://github.com/user-attachments/assets/988329a9-d30f-445f-9c7f-e762ecdf1d01)

The LM386 Audio Amplifier Module requires power and there are two ways this can be done
- Obtain a 9V Battery Connector, and connect female female Dupont connectors to it.
  - I used prefabricated wires with female Dupont connectors and wire colors that match the wires on the 9V Battery Connector.
- Obtain a 12V Power Supply with a 12V 5A DC Female Power Plug and wires with a male Dupont connector on one end and a female Dupont connector on the other.
  - I used a red wire for the positive connection and a black wire for the ground.
 
Note: The LM386 Audio Amplifier Module has a minimum power need of 5 Volts and a maximum of 12 Volts. I experimented with utilizing a 5 Volt power pin on the Raspberry Pi and found it to be inatequate for this setup.

## Complete the System Setup
