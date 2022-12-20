# Project `exercise_assistant`
The project's goal is to create application that manages your workout routines for you. It guides you through each exercise with audio messages (their text is also printed in terminal window).

# Current state
Project is in its starting phase and does not work in its intended way yet.

## Testing scripts
* `scripts/tts_test.py` - testing out `pyttsx3` module to provide speech.
* `scripts/json_test.py` - loading example exercise list file and reading its values.
* `scripts/parser_test.py` - testing if `ExcerciseParser` works properly.

# How is it supposed to work?
1. Specify exercise list file in `.json` format.
2. Specify configuration file in `.json` format.
3. Run the program.
4. Done!
