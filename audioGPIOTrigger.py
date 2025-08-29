import RPi.GPIO as GPIO
import os, random, signal, sys, time, vlc

# Set pin numbering mode
GPIO.setmode(GPIO.BCM)

# This script triggers a recording to be playeed vis VLC on a Raspberry Pi
# when a GPIO pin (default to pin 16 via variable gpioPi) goes to a high state.
# When triggered it randomly selects and plays a file from a directory specified at startup.
#
# Please see project README.md for use cases.
#

#
# Setup - Audio file location and GPIO pins settings
#

# Directory containing audio files.
audioDirectory = ""
audioLevel = 100

# Define the GPIO pin you want to monitor
gpioPin = 16

# Set the pin, using GPIO.PUD_DOWN in GPIO.setup should keep the pin state low
# at startup and when not triggered.
GPIO.setup(gpioPin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

try: 

  #
  # Setup - VLC initialization
  #

  vlcInstance = vlc.Instance()
  audioPlayer = vlcInstance.media_player_new()

  #
  # Function playAudio() randomly selects a file in directory audioDirectory
  # and plays it.
  #

  def playAudio():
    # Make a list of {audioDirectory} contents, error if {audioDirectory}  
    # is not a directory. Note: Directory {audioDirectory} is re-analyzed
    # each time playAudio() is invoked to allow for the contents of the 
    # audio directory to be updated and utilized  without restarting this
    # script.

    global audioDirectory

    dirContents = os.listdir(audioDirectory)

    # Remove anything from {dirContents} that is not a file.
    for index, file in enumerate(dirContents):
      fullPath = audioDirectory + "/" + file
      # print(f"fullPath: {fullPath}")

      if os.path.isfile(fullPath):
        # print(f"{fullPath} is a file")
        dirContents[index] = fullPath
      else:
        # print(f"{fullPath} is NOT a file")
        dirContents.pop(index)

    # From trimmed {dirContents} randomly select an audio file to play
    contentNum = len(dirContents)
    # print(f"contentNum: {contentNum}")
    randSel = random.randint(0, (contentNum - 1))

    # Set the media specification for the VLC player and play the audio.
    media = vlcInstance.media_new_path(dirContents[randSel])
    audioPlayer.set_media(media)
    # print(f"Playing {randSel}: {dirContents[randSel]}")
    audioPlayer.play()

    # Set the audio level to what is specified in variable audioLevel. This can
    # only happen when audioPlayer is in play state so wait until this is true
    # then set the level. Note interfacing with VLC player from a python script
    # is asynchronous so polling is needed to verify the play state.
    while not audioPlayer.get_state():
      # print("waiting on audioPlayer")
      continue
    time.sleep(0.1)

    audioPlayer.audio_set_volume(audioLevel)
    current_volume = audioPlayer.audio_get_volume()
    # print(f"Playing volume: {current_volume}")

    time.sleep(2) # Read it is best to pause a few seconds after triggering play

  #
  # Function stopAudio() stops VLC playback if it is current active.
  #

  def stopAudio():
    # print("stopAudio")
    if audioPlayer.is_playing():
      # print()
      # print("Stoping audio")
      audioPlayer.stop()

  #
  # Function pinEventCallback is called when GPIO.add_event_detect (below)
  # detects an event on gpioPin.
  #

  def pinEventCallback(channel):
      if GPIO.input(channel):
          # print(f"Pin {gpioPin} is HIGH")
          playAudio()
      else:
          # print(f"Pin {gpioPin} is LOW")
          stopAudio()



  #
  # Function main()
  # 

  def main():
    global audioDirectory

    if len(sys.argv) > 1:
      audioDirectory = sys.argv[1]
      # print(audioDirectory)

      if os.path.isdir(audioDirectory):
        print
        print(f"Starting " +  os.path.basename(__file__) + " using directory " + audioDirectory)
        print

        # Read gpioPin's initial state at startup
        pin_state = GPIO.input(gpioPin)
        if pin_state == GPIO.HIGH:
          # Trigger audio immediately at startup.
          # print(f"Pin {gpioPin} initial state is HIGH")
          playAudio()
        else:
          # There should be no audio playing at this point but, hey...
          # print(f"Pin {gpioPin} initial state is LOW")
          stopAudio()

        # Add event detection for gpioPin for subsequent gpioPin state changes.
        GPIO.add_event_detect(gpioPin, GPIO.BOTH, callback=pinEventCallback, bouncetime=200)

        print(f"Ready for events on GPIO pin {gpioPin}.")

        # Use signal.pause() to keep from exiting until signaled.
        signal.pause()
      else:
        print
        print(os.path.basename(__file__) + ": " + audioDirectory + " does not exist or is not a directory.")
        print
    else:
      print
      print("Please provide a directory that contains audio files")
      print

  if __name__ == "__main__":
    main()

# Exception handline and closing things out...
except FileNotFoundError:
  print(f"Error: Directory '{audioDirectory}' not found.")
except NotADirectoryError:
  print(f"Error: '{audioDirectory}' is not a directory.")
except KeyboardInterrupt:
  print("Exiting...")
except Exception as e:
  print(f"An error occurred: {e}")
finally:
    GPIO.cleanup()
