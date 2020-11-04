# from Backtracking import Backtracking
# from CSPBacktracking import CSPBacktracking
from CSPBacktrackingWithReferences import CSPBacktrackingWithReferences

# back = Backtracking(4)
back = CSPBacktrackingWithReferences(4)

for s in back.back(10):
    print(str(s))