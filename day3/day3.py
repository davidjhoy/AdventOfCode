


with open('/Users/davidhoy/desktop/adventDay3.txt', 'r') as file:
    content = file.read()
    ruck_sack_list = "".join(list(content)).splitlines()
    priority_sum = 0
    rs_lst_idx = len(ruck_sack_list) - 1
    
    for i in range(0, len(ruck_sack_list), 3):
        first = ruck_sack_list[i]
        second = ruck_sack_list[i+1] 
        third = ruck_sack_list[i + 2]
        
        letter = list(set(first) & set(second) & set(third))[0]
        if letter.isupper():
            priority_sum += ord(letter) - 38
        else:
            priority_sum += ord(letter) - 96
        
    print(priority_sum)
        
    