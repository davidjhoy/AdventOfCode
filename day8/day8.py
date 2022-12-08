with open('/Users/davidhoy/desktop/adventDay8.txt', 'r') as file:
    content = file.read()
    oldmatrix = "".join(list(content)).splitlines()
    matrix = [[int(s) for s in xs] for xs in oldmatrix]
    # maxTop = matrix[0][::]
    # visible_trees = (2 * len(matrix[0])) + (2* (len(matrix) - 2))
    
    #i == row
    #j == column 
    
    max_scenc_score = 0
    
  
  
    
    for i in range(len(matrix)):
        ##for each row create a running tally of the max left value 
        # maxLeft = matrix[i][0]
        for j in range(len(matrix[0])):
            # up = left = False
            # down = right = True
            # ##check up ---> use the maxTop array to check for the running tally of the greatest value above the current index
            # if matrix[i][j] > maxTop[j]:
            #     up = True
            #     maxTop[j] = matrix[i][j]
            # ##check right
            # k = j + 1
            # while k < len(matrix[0]):
            #     if matrix[i][k] >= matrix[i][j]:
            #         right = False
            #         break
            #     k += 1
            
            # ##check down
            # l = i + 1
            # while l < len(matrix):
            #     if matrix[l][j] >= matrix[i][j]:
            #         down = False
            #         break
            #     l += 1
        
            # ##check left
            # if matrix[i][j] > maxLeft:
            #     left =  True
            #     maxLeft = matrix[i][j]
            
            # if up or right or down or left:
            #     visible_trees += 1

            #PART TWO 
            
            #Score Up 
            su = 0
            if i > 0:
                t = i - 1 
                while t >= 0:
                    if matrix[i][j] > matrix[t][j]:
                        su += 1
                    else:
                        su += 1
                        break
                    t -= 1
                    
            #Score Right
            sr = 0 
            if j < len(matrix[0])-1:
                u = j + 1
                while u <= len(matrix[0])-1:
                    if matrix[i][j] > matrix[i][u]:
                        sr += 1
                    else:
                        sr +=1 
                        break
                    u += 1
            #Score Down 
            sd = 0 
            if i < len(matrix) -1:
                z = i + 1
                while z <= len(matrix) - 1:
                    if matrix[i][j] > matrix[z][j]:
                        sd += 1
                    else:
                        sd += 1
                        break
                    z += 1
            #Score Left
            sl = 0 
            if j > 0:
                y = j - 1
                while y >=0:
                    if matrix[i][j] > matrix[i][y]:
                        sl += 1
                    else:
                        sl +=1 
                        break
                    y -= 1
            sc = su * sr * sd * sl
            max_scenc_score = max(max_scenc_score, sc)
            
    print(max_scenc_score)
             
