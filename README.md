# audioGPIOTrigger

This script triggers a recording to be played via VLC on a Raspberry Pi
when a GPIO pin (default to pin 16 via variable gpioPin) goes to a high state.
When triggered it randomly selects and plays a file from a directory specified at startup.
