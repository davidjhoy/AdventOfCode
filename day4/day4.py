

with open('/users/davidhoy/Desktop/adventDay4.txt', 'r') as file:
    content = file.read()
    sections_list = [cont.split(",") for cont in content.splitlines()]
    running_sum = 0 
    for pair in sections_list:
        left_list = pair[0].split("-")
        right_list = pair[1].split("-")
        
        if int(right_list[0]) <= int(left_list[0]) <= int(right_list[1])  or int(right_list[0]) <= int(left_list[1]) <= int(right_list[1]):
            running_sum += 1
        elif int(left_list[0]) <= int(right_list[0]) <= int(left_list[1]) or int(left_list[0]) <= int(right_list[1]) <= int(left_list[1]):
            running_sum += 1
        
    print(running_sum)
    