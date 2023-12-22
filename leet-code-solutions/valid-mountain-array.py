class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        up = 1
        check = set()
        if len(arr) < 3:
            return False
        elif arr == sorted(arr) or arr == sorted(arr, reverse=True) :
            return False
        for i in range(len(arr)-1):
            if arr[i] == arr[i+1]:
                return False
            if arr[i] < arr[i+1] and up == 0:
                return False
            if arr[i] > arr[i+1]:
                up = 0
        return True
