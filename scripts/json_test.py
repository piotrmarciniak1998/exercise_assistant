import os
import json


if __name__ == "__main__":
    work_dir = os.getcwd()
    data_dir = os.path.join(work_dir, "data")
    file = "exercises.json"
    file_path = os.path.join(data_dir, file)

    with open(file_path, encoding="utf-8-sig") as f:
        data = json.load(f)

        exercises = data["exercises_list"]

        for exercise in exercises:
            name = exercise["name"]
            time = exercise["time"]

            print(name, time)