
import re
with open('/Users/davidhoy/Desktop/adventDay2.txt', 'r') as txt:
    content = txt.read()
    original_list = "".join(list(content)).splitlines()
    
        
    
    movesDict = {
        "A": {"X": 3, "Y": 4, "Z": 8},
        "B": {"X": 1, "Y": 5, "Z": 9 },
        "C": {"X": 2, "Y": 6, "Z": 7 }
    }

    returnSum = 0
    
    for i, val in enumerate(original_list):
        
        returnSum += movesDict[val[0]][val[2]]

    print(returnSum)
    
    
