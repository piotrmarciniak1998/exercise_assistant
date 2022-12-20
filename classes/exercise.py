import json


class Exercise:
    def __init__(self, name, time):
        self.name = name
        self.time = time


class ExerciseParser:
    def __init__(self, json_str):
        self.exercises = []

        try:
            data = json.loads(json_str)
        except json.JSONDecodeError:
            print("Error: Invalid JSON string")
            return

        for exercise_dict in data["exercises_list"]:
            exercise = Exercise(exercise_dict["name"], exercise_dict["time"])
            self.exercises.append(exercise)
