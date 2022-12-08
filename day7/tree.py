class TreeNode():
    def __init__(self, size=0, parent =None, name= ""):
        self.size = size
        self.children = []
        self.parent = parent
        self.name = name
        
    def addSize(self, val):
        self.size += val
        
    def addChildren(self, nodeList):
        self.children.extend(nodeList)
    
    def addChild(self, node):
        self.children.append(node)
    
    def addParent(self, node):
        self.parent = node
        