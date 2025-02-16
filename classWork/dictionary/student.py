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


count = 0
total = 0
average = 0
for key in school_records.keys():
    print(key)
    for index in range(len(school_records[key]['students'])):
        total += school_records[key]['students'][index]['scores']['Math']
        count += 1
        average = total / count
print(f"The average Math score for all Students is: {average}")
