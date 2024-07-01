students = ["Harry", "Ron", "Hermione", "Draco"]

for student in students:
    print (student)

for i in range(len(students)):
    print(i+1,students[i])

# Using Dictionary to attach students with their houses

houses = {
    "Hermione": "Gryffindor",
    "Harry": "Gryffindor",
    "Ron": "Gryffindor",
    "Draco": "Slytherin"
}

print(houses["Ron"])                                #print the values(house name)

for house in houses:
    print(house)                                    #print keys(name of students)

for house in houses:
    print(house, houses[house], sep=(", "))         #print keys and valuse

# Dictionary inside dictionary

student_info = [
    {"name": "Hermione", "house": 'Gryffindor', "patronus": "Otter"},
    {"name": "Harry", "house": 'Gryffindor', "patronus": "Stag"},
    {"name": "Ron", "house": 'Gryffindor', "patronus": "Jack Russell"},
    {"name": "Draco", "house": 'Slytherin', "patronus": None}
]

for student in student_info:
    print(student["name"], student["house"], student["patronus"], sep=(", "))