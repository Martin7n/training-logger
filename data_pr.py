def test8():
    workout = {'id': 4, 'date': '2026-08-19', 'time': '17:26:28', 'sentToFlask': False, 'sentAt': None, 'data': {'Deadlift': {'notes': '', 'sets': [{'weight': 100, 'reps': 5}, {'weight': 120, 'reps': 4}, {'weight': 150, 'reps': 3}]}, 'CleanPress': {'notes': '', 'sets': [{'weight': 90, 'reps': 5}, {'weight': 100, 'reps': 4}, {'weight': 110, 'reps': 3}]}}}

    for exercise_name, exercise in workout["data"].items():

        for set_number, workout_set in enumerate(
                exercise["sets"],
                start=1
        ):
            weight = workout_set["weight"]
            reps = workout_set["reps"]

            print(
                exercise_name,
                set_number,
                weight,
                reps
            )

if __name__ == '__main__':
    test8()