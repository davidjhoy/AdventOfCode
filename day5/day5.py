import re

stack_dict = {
    "1": list('QWPSZRHD'),
    "2": list('VBRWQHF'),
    "3": list("CVSH"),
    "4": list("HFG"),
    "5": list("PGJBZ"),
    "6": list("QTJHWFL"),
    "7": list("ZTWDLVJN"),
    "8": list("DTZCJGHF"),
    "9": list("WPVMBH")
}
##move 1 from 3 to 9
print(stack_dict)
with open('input.txt', 'r') as file:
    content = file.read()
    moves_list = "".join(list(content)).splitlines()
    stripped_moves_list = []
    
    for move in moves_list:
       stripped_moves_list.append("".join(ch for ch in move if ch.isdigit() or ch == " "))
    
    for i in stripped_moves_list:
        moves = "".join(i).strip()
 
        moves_list = []
        intermediate = 0 

        for id, j in enumerate(moves):
            if j == " " or j == ",":
                intermediate = 0
                
            elif j.isdigit() and intermediate == 0:
                intermediate = int(j)
    
                if id + 1 == len(moves):
                    moves_list.append(intermediate)
                    intermediate = 0 
                elif moves[id +1] == " " or moves[id+1] == ",":
                    moves_list.append(intermediate)
                    intermediate = 0 
            
            elif j.isdigit() and intermediate > 0:
                intermediate = intermediate * 10 + int(j)
           
                if id + 1 == len(moves):
                    moves_list.append(intermediate)
                    intermediate = 0 
                elif moves[id +1] == " " or moves[id+1] == ",":
                    moves_list.append(intermediate)
                    intermediate = 0 
            

    
        interlist = []
        for j in range(moves_list[0]):
            if len(stack_dict[str(moves_list[1])]) == 0:
                break
            else:
                
                interlist.insert(0, stack_dict[str(moves_list[1])].pop())
        stack_dict[str(moves_list[2])].extend(interlist)        
                
 
    returnString = ""
    
    for i in stack_dict.keys():
        if len(stack_dict[i]) == 0:
            continue
        else:
            returnString += (stack_dict[i][-1])
    print(returnString)

         