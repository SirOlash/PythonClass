def school_record():
    school_records ={
        "class_1":{
            "students":[
                {"name":"Harry","scores":{"Math":88,"English":76}},
                {"name":"Solomon","scores":{"Math":95,"English":89}},
            ]
        },
        "class_2":{
            "students":[
                {"name":"Daniel","scores":{"Math":78,"English":72}},
                {"name":"Samuel","scores":{"Math":85,"English":80}},
            ]
        }
    }
    for class_name, class_data in school_records.items():
        for student_data in class_data["students"]:
            for subject_scores in student_data["scores"].items():
                for subject_name, subject_score in subject_scores.items():

                    print(subject_score)


print(school_record())