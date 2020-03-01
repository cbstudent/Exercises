"""
# Employee info
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        # It's the unique id of each node.
        # unique id of this employee
        self.id = id
        # the importance value of this employee
        self.importance = importance
        # the id of direct subordinates
        self.subordinates = subordinates
"""
class Solution:
        
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        
        edict = {}
        for e in employees:
            edict[e.id] = e
        
        #DFS
        importancesum = 0
        return self.dfs(edict[id], edict, importancesum)

               
    def dfs(self, curr, edict, importancesum):
        importancesum += curr.importance

        for i in curr.subordinates:
            importancesum = self.dfs(edict[i], edict, importancesum)
            
        return importancesum
