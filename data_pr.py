def test1():
    data = {
        'id': 4, 'date': '2026-08-18', 'time': '14:55:39', 'sentToFlask': False, 'sentAt': None, 'data': [{'type': 'B', 'exercise1': {'name': 'Deadlift', 'notes': '', 'sets': [{'weight': 10, 'reps': 1}, {'weight': 200, 'reps': 1}, {'weight': None, 'reps': None}, {'weight': None, 'reps': None}, {'weight': None, 'reps': None}, {'weight': None, 'reps': None}]}, 'exercise2': {'name': 'Deadlift', 'notes': '', 'sets': [{'weight': None, 'reps': None}, {'weight': None, 'reps': None}, {'weight': None, 'reps': None}, {'weight': None, 'reps': None}, {'weight': None, 'reps': None}, {'weight': None, 'reps': None}]}}]}



    data2 =  {'id': 9, 'date': '2026-08-18', 'time': '17:52:02', 'sentToFlask': False, 'sentAt': None, 'data': [{'type': 'A', 'exercise1': {'name': 'Deadlift', 'notes': 'first one', 'sets': [{'weight': 100, 'reps': 10}, {'weight': 120, 'reps': 8}, {'weight': 130, 'reps': 5}, {'weight': None, 'reps': None}, {'weight': None, 'reps': None}, {'weight': None, 'reps': None}]}, 'exercise2': {'name': 'Press', 'notes': '', 'sets': [{'weight': 50, 'reps': 5}, {'weight': 60, 'reps': 5}, {'weight': 70, 'reps': 3}, {'weight': None, 'reps': None}, {'weight': None, 'reps': None}, {'weight': None, 'reps': None}]}}, {'type': 'A', 'exercise1': {'name': 'Pushup', 'notes': 'volume', 'sets': [{'weight': 90, 'reps': 10}, {'weight': 90, 'reps': 10}, {'weight': 90, 'reps': 10}, {'weight': None, 'reps': None}, {'weight': None, 'reps': None}, {'weight': None, 'reps': None}]}, 'exercise2': {'name': 'Pullup', 'notes': '', 'sets': [{'weight': 90, 'reps': 10}, {'weight': 90, 'reps': 10}, {'weight': 90, 'reps': 10}, {'weight': None, 'reps': None}, {'weight': None, 'reps': None}, {'weight': None, 'reps': None}]}}]}

    # for k, v in data.items():
    #     if k == "data":
    #         for workout in v:
    #             print(workout)
    #
    #             for ex, prop in workout.items():
    #                 print(f'xx {ex} xx')
    #                 for pp, zz in prop.items():
    #                     print(pp)
    #                 # print(f'\n {prop}')
    #
    # for item in data:
    #     for key, exercise in item.items():
    #         if isinstance(exercise, dict) and "name" in exercise:
    #             print(exercise["name"])
    #
    #             for set_data in exercise["sets"]:
    #                 print(set_data["weight"])
    #                 print(set_data["reps"])

    for item in data2["data"]:
        for key, exercise in item.items():
            if isinstance(exercise, dict) and 'notes' in exercise:
                print(exercise['notes'])
            if isinstance(exercise, dict) and "name" in exercise:
                # print(exercise["name"])

                for set_data in exercise["sets"]:
                    if set_data["reps"]:
                        # print(f"weight {set_data["weight"]}")
                        # print(f"reps {set_data["reps"]}")
                        print(f"{exercise["name"]} weight {set_data["weight"]} reps {set_data["reps"]}")



def test2():

    data = [{'type': '', 'exercise1': {'name': 'Deadlift', 'notes': '',
                                    'sets': [{'weight': 100, 'reps': 5}, {'weight': 120, 'reps': 5},
                                             {'weight': 130, 'reps': 5}, {'weight': None, 'reps': None},
                                             {'weight': None, 'reps': None}, {'weight': None, 'reps': None}]}}, {
        'type': '', 'exercise1': {'name': 'Press', 'notes': '',
                                  'sets': [{'weight': 50, 'reps': 10}, {'weight': 60, 'reps': 8},
                                           {'weight': 65, 'reps': 6}, {'weight': 70, 'reps': 5},
                                           {'weight': None, 'reps': None}, {'weight': None, 'reps': None}]}}]
    for item in data:
        count = 1
        for x,y in item.items():
            for key, exercise in item.items():
                if isinstance(exercise, dict) and 'notes' in exercise:
                    print(exercise['notes'])
                if isinstance(exercise, dict) and "name" in exercise:
                    # print(exercise["name"])
                    count += 1

                    for set_data in exercise["sets"]:
                        if set_data["reps"]:
                            print(f"{count} {exercise["name"]} weight {set_data["weight"]} reps {set_data["reps"]}")

            print(x)


def test3(data2):

    data = [{'type': '', 'exercise1': {'name': 'Deadlift', 'notes': '',
                                    'sets': [{'weight': 100, 'reps': 5}, {'weight': 120, 'reps': 5},
                                             {'weight': 130, 'reps': 5}, {'weight': None, 'reps': None},
                                             {'weight': None, 'reps': None}, {'weight': None, 'reps': None}]}}, {
        'type': '', 'exercise1': {'name': 'Press', 'notes': '',
                                  'sets': [{'weight': 50, 'reps': 10}, {'weight': 60, 'reps': 8},
                                           {'weight': 65, 'reps': 6}, {'weight': 70, 'reps': 5},
                                           {'weight': None, 'reps': None}, {'weight': None, 'reps': None}]}}]
    for item in data2:
        count = 1
        for x,y in item.items():
            for key, exercise in item.items():
                if isinstance(exercise, dict) and 'notes' in exercise:
                    print(exercise['notes'])
                if isinstance(exercise, dict) and "name" in exercise:
                    # print(exercise["name"])
                    count += 1

                    for set_data in exercise["sets"]:
                        if set_data["reps"]:
                            print(f"{count} {exercise["name"]} weight {set_data["weight"]} reps {set_data["reps"]}")

            print(x)

def test4():
    workout_data = {}
    date = ""
    response = {'id': 23, 'date': '2026-08-19', 'time': '10:44:04', 'sentToFlask': False, 'sentAt': None, 'data': [{'type': 'A', 'exercise1': {'name': 'Deadlift', 'notes': '', 'sets': [{'weight': 111, 'reps': 1}, {'weight': 11111, 'reps': 1}, {'weight': None, 'reps': None}, {'weight': None, 'reps': None}, {'weight': None, 'reps': None}, {'weight': None, 'reps': None}]}}, {'type': 'A', 'exercise1': {'name': 'Pullup', 'notes': '', 'sets': [{'weight': 11, 'reps': 20}, {'weight': 3, 'reps': 13}, {'weight': None, 'reps': None}, {'weight': None, 'reps': None}, {'weight': None, 'reps': None}, {'weight': None, 'reps': None}]}}]}
    for k,v in response.items():
        if 'date' in k:
            date = v
        if 'data' in k:
            xrx = 1
            for x in v:
                workout_data[f'xrxP{xrx}']= x
    print(workout_data)
    print(date)

    count = 1
    for key, exercise in workout_data.items():

        if isinstance(exercise, dict) and 'notes' in exercise:
            print(exercise['notes'])
        if isinstance(exercise, dict) and "name" in exercise:
                    # print(exercise["name"])
            count += 1

            for set_data in exercise["sets"]:
                if set_data["reps"]:
                    print(f"{count} {exercise["name"]} weight {set_data["weight"]} reps {set_data["reps"]}")


def test6():
    data = {'id': 2, 'date': '2026-08-19', 'time': '11:25:08', 'sentToFlask': False, 'sentAt': None, 'data': {'exercise1': {'name': 'Deadlift', 'notes': '', 'sets': [{'weight': 80, 'reps': 5}, {'weight': 90, 'reps': 4}, {'weight': 100, 'reps': 3}, {'weight': None, 'reps': None}, {'weight': None, 'reps': None}, {'weight': None, 'reps': None}]}, 'exercise2': {'name': 'CleanPress', 'notes': '', 'sets': [{'weight': 50, 'reps': 5}, {'weight': 60, 'reps': 5}, {'weight': 70, 'reps': 5}, {'weight': 80, 'reps': 3}, {'weight': None, 'reps': None}, {'weight': None, 'reps': None}]}}}
    for k,v in data.items():
        if "data" in k:
            # print(v)
            for exercise, content in v.items():
                # print(content)
                for kk, vv in content.items():
                    if 'name' in kk:
                        exercise = vv
                        print(f"name: {vv}")
                    if 'sets' in kk:
                        for sets in vv:
                            if sets["weight"] and sets["reps"]:
                                print(sets["weight"])
                                print(sets["reps"])

                            # print(f"sets: {sets}")

                        print(vv)
                    # if isinstance(kk, dict) and "sets" in vv:
                    #     print(f"weight: {kk['sets']}")
                    # if isinstance(vv, dict) and 'notes' in kk:
                    #     print(vv['notes'])
                    # if isinstance(vv, dict) and "name" in kk:
                    #     print(vv["name"])

def test7():
    data = {'id': 3,  'date': '2026-08-19', 'time': '12:53:07', 'sentToFlask': False, 'sentAt': None, 'data': {'Deadlift': {'notes': '', 'sets': [{'weight': 100, 'reps': 5}, {'weight': 120, 'reps': 5}, {'weight': 130, 'reps': 5}, {'weight': None, 'reps': None}, {'weight': None, 'reps': None}, {'weight': None, 'reps': None}]}, 'CleanPress': {'notes': '', 'sets': [{'weight': 100, 'reps': 3}, {'weight': 90, 'reps': 4}, {'weight': 80, 'reps': 6}, {'weight': None, 'reps': None}, {'weight': None, 'reps': None}, {'weight': None, 'reps': None}]}}}
    data2 = {'id': 4, 'date': '2026-08-19', 'time': '17:26:28', 'sentToFlask': False, 'sentAt': None, 'data': {'Deadlift': {'notes': '', 'sets': [{'weight': 100, 'reps': 5}, {'weight': 120, 'reps': 4}, {'weight': 150, 'reps': 3}]}, 'CleanPress': {'notes': '', 'sets': [{'weight': 90, 'reps': 5}, {'weight': 100, 'reps': 4}, {'weight': 110, 'reps': 3}]}}}


    id = ""
    date = ""

    for k,v in data2.items():
        if "id" in k:
            id = v
        if 'data' in k:
            for exercise, content in v.items():
                print(content['sets'][0])
        print(f"{k} -- {v}")
    print(id)

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