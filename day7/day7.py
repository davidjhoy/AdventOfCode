from tree import TreeNode

with open('/Users/davidhoy/desktop/adventDay7.txt', 'r') as file:
    content = file.read()
    
    ##Short for Terminal Actions
    TA = "".join(list(content)).splitlines()
    n = len(TA)
    
    ##Let's skip the first action and just manually create a parent dir with name = "/"
    i = 1
    dummy = TreeNode()
    current = TreeNode(name="/")
    
    ###This will be used when we iterate over the tree later
    dummy.addChild(current)
    
    ####Create the Tree
    while i < n:
        
        ###ls actions finished
        if TA[i][2] == "l":
            ##add to children of the current node
            i += 1
            child_list = []
            ##Iterate until we reach another terminal $ input
            while i < n:
                if TA[i][0] != "$":
        
                    ## if it is a dir 
                    if TA[i][0:3] == "dir" and len(current.children) == 0:
                        node_name = TA[i][4:]
                        child_list.append(TreeNode(parent = current, name = node_name))
                    
                    ## if it is a file
                    elif len(current.children) == 0:
                        size = ""
                        ###while loop to find all digits
                        j = 0
                        while j < len(TA[i]):
                            if TA[i][j].isnumeric():
                                size += TA[i][j]
                            else:
                                break
                            j += 1
                        current.addSize(int(size))
                        
                    i += 1
                else:
                    break
            if len(child_list) > 0:
                current.addChildren(child_list)
                
        ##cd .. 
        elif TA[i][5] == ".":
           
            ###change current to the current's parent
            current = current.parent
            i += 1
            
        # cd <child name> 
        else:
            ###Move to the specified node in the current's children
            
            cd_name = TA[i][5:]
            for child in current.children:
                if child.name == cd_name:
                    current = child
                    break 
            i += 1
        

    
    ###Iterate through and find the dirs with values <= 100000
    sum = 0
    def dfs(root):
        if len(root.children) == 0:
            return
        for child in root.children:
            dfs(child)
            root.addSize(child.size)
                
    def bfs(root):
        global sum
        q = []
        q.append(root)
    
        while len(q) > 0:
            curr = q.pop(0)
            if curr.size <= 100000:
                sum += curr.size
            for child in curr.children:
                q.append(child)
        
    dfs(dummy.children[0])
    # bfs(dummy.children[0])
    # print(sum)
    
    
    ###Part II
    minVal = 70000000
    totalSize = dummy.children[0].size
    currentDifference = 70000000 - totalSize
    sizeNeeded = 30000000-currentDifference
    
    def bfsMinSearch(root):
        global minVal
        global sizeNeeded
        q = []
        q.append(root)
    
        while len(q) > 0:
            curr = q.pop(0)
            if curr.size <= minVal and curr.size >= sizeNeeded:
                minVal = curr.size
            for child in curr.children:
                q.append(child)
    
    bfsMinSearch(dummy.children[0])    
    

   
    print(minVal)
    

    
