import datetime
import time
import pygame # for playing the alarm sound and stopping it

def set_alarm(alarm_time, sound_file):
    """
    Sets an alarm for the specified time and plays a sound when the alarm goes off.

    Parameters:
    alarm_time (str): The time to set the alarm in HH:MM:SS AM/PM format.
    sound_file (str): The path to the sound file to play when the alarm goes off.

    The function initializes the pygame mixer, converts the alarm time to a datetime object,
    and continuously checks the current time. When the current time matches the alarm time,
    it plays the specified sound file in a loop. The user can stop the alarm by pressing any key.
    """
    # initialize the mixer
    pygame.mixer.init()
    # convert the alarm time to a datetime object
    alarm_time = datetime.datetime.strptime(alarm_time, "%I:%M:%S %p").time()

    print(f"Alarm set for {alarm_time.strftime('%I:%M:%S %p')}")

    while True:
        # get the current time 
        current_time = datetime.datetime.now().time()

        # check if the current time is the same as the alarm time
        if current_time.hour == alarm_time.hour and current_time.minute == alarm_time.minute and current_time.second == alarm_time.second:
            print("\nWake up!")
            pygame.mixer.music.load(sound_file)
            pygame.mixer.music.play()
            break
        
        print(f"\r{current_time.strftime('%I:%M:%S %p')}", end="")
        # sleep for 1 second before checking again
        time.sleep(1)

    # wait for user input to stop the sound
    input("Press any key to stop the alarm.")
    pygame.mixer.music.stop()

if __name__ == "__main__":
    c_time = datetime.datetime.now().time()
    print(c_time.strftime('%I:%M:%S %p'))
    alarm_time = input("Enter the time for the alarm in HH:MM:SS AM/PM format: ")
    sound_file = 'alarm.mp3'
    set_alarm(alarm_time, sound_file)