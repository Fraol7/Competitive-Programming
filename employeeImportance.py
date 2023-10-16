"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List["Employee"], id: int) -> int:
        employee_dict = {employee.id: employee for employee in employees}
        def dfs(empl_id):
            employee = employee_dict[empl_id]
            totalImprt = employee.importance
            for subordinate_id in employee.subordinates:
                totalImprt += dfs(subordinate_id)
            return totalImprt
        ans = dfs(id)
        return ans
