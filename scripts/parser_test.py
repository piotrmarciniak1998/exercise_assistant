import os
import sys

sys.path.append(os.getcwd())
from classes.exercise import ExerciseParser


if __name__ == "__main__":
    work_dir = os.getcwd()
    data_dir = os.path.join(work_dir, "data")
    file_name = "exercises.json"
    file_path = os.path.join(data_dir, file_name)

    with open(file_path, 'r') as f:
        json_string = f.read()

    parser = ExerciseParser(json_string)

    for exercise in parser.exercises:
        print(f"Name: {exercise.name}, Time: {exercise.time}")
