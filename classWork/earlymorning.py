def morning_task(number_list):
    #number_list = [3,4,2]
    for index in range(len(number_list),0,-1):
        number_list[index-1]= number_list[index-1] + 1
        if number_list[index - 1] <= 9:
            break
        number_list[index - 1] = 0
    if number_list[0] == 0:
        number_list.insert(0,1)
    return number_list
