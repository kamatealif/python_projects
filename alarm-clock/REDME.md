# Alarm clock Script
this is a simple Python script that sets an alarm for a specified time 

## Features

- Set an alarm for a specific time in HH:MM:SS AM/PM Format.
- Plays a specified sound file when the alarmf goes off.
-Stops the alarm sound when the user presses any key.

## Requirments 

- Python 3.x
- `pygame` library

# Installation 

1. Install Python 3.x from [python.org](https://www.python.org/).
2. Install the `pygame` library using pip:

    ```sh
    pip install pygame
    ```

## Usage
1. save the script to a file, eg., alarm.py.
2. Run the script:
```sh
python alarm.py
```
3. Enter the time for the alarm in HH:MM:SS AM/PM format when prompted.

4. The script will continuously check the current time and play the specified sound file when the alarm time is reached.

5. Press any key to stop the alarm sound.

## example 

```sh
$ python alarm.py
02:30:00 PM
Enter the time for the alarm in HH:MM:SS AM/PM format: 02:31:00 PM
Alarm set for 02:31:00 PM
02:30:01 PM
02:30:02 PM
...
02:31:00 PM
Wake up!
Press any key to stop the alarm.
```