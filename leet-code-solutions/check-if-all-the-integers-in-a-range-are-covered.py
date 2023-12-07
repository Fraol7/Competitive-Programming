class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
      check = set()
      left_right = {i for i in range(left, right+1)}
      for alist in ranges:
        aset = {i for i in range(alist[0], alist[1]+1)}
        check.update(aset & left_right)
      if check == left_right:
        return True
      else:
        return False