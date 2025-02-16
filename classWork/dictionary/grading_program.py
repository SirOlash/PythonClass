def student_score():
    student_scores = {"Gloria":88,"Divine":78,"Esther":65,"Mercy":75,"Uzo":71}
    for key,value in student_scores.items():
        if 91 <= value <= 100:
            print (key,"outstanding")
        elif 81 <= value <= 90:
            print (key,"Exceeds Expectations")
        elif 71 <= value <= 80:
            print (key,"Acceptable")
        elif value < 70:
            print (key,"fail")
student_score()





