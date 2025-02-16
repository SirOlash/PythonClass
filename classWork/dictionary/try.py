school_records = {
 "class_1": {
 "students": [
 {"name": "Harry", "scores": {"Math": 88, "English": 76}},
 {"name": "Solomon", "scores": {"Math": 95, "English": 89}},
 ]
 },
 "class_2": {
 "students": [
 {"name": "Daniel", "scores": {"Math": 78, "English": 72}},
 {"name": "Samuel", "scores": {"Math": 85, "English": 80}},
 ]
 }
}
total = 0
for index in range(len(school_records["class_1"]["students"])):
    for class_name, class_details in school_records.items():
        total += class_details["students"][index]["scores"]["Math"]
average = total / len(school_records["class_1"]["students"])
print(average)
    #students = class_details["students"]
    #print(students)

#print(total)
print(len(school_records))


