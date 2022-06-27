def activities_plus_surname_length(database):
    hobbies = []
    surnames_row = str()
    for i_value in database.values():
        hobbies += i_value['interests']
        surnames_row += i_value['surname']
    return hobbies, len(surnames_row)


students = {
    1: {
        'name': 'Bob',
        'surname': 'Vazovski',
        'age': 23,
        'interests': ['biology, swimming']
    },
    2: {
        'name': 'Rob',
        'surname': 'Stepanov',
        'age': 24,
        'interests': ['math', 'computer games', 'running']
    },
    3: {
        'name': 'Alexander',
        'surname': 'Krug',
        'age': 22,
        'interests': ['languages', 'health food']
    }
}


pairs = list()
for identify, student in students.items():
    pairs.append((identify, student['age']))

activities, length_surnames = activities_plus_surname_length(students)
print(activities, length_surnames)
print(pairs)
