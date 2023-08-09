#User function Template for python3

class Solution:
    
    #Heapify function to maintain heap property.
    def heapify(self,arr, n, i):
        # code here
        largest = i  # Initialize the largest element as the root
        left = 2 * i + 1  # Left child index
        right = 2 * i + 2  # Right child index
    
        # If left child exists and is larger than root
        if left < n and arr[left] > arr[largest]:
            largest = left
    
        # If right child exists and is larger than current largest
        if right < n and arr[right] > arr[largest]:
            largest = right
    
        # If the largest is not the root
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]  # Swap
            self.heapify(arr, n, largest)
        
    #Function to build a Heap from array.
    def buildHeap(self,arr,n):
        # code here
        for i in range(n // 2 - 1, -1, -1):
            self.heapify(arr, n, i)
    
    #Function to sort an array using Heap Sort.    
    def HeapSort(self, arr, n):
        #code here
        n = len(arr)
    
        # Build a max heap
        self.buildHeap(arr, n)
    
        # Extract elements one by one
        for i in range(n - 1, 0, -1):
            arr[i], arr[0] = arr[0], arr[i]  # Swap
            self.heapify(arr, i, 0)









#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

# Contributed by : Mohit Kumara

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        Solution().HeapSort(arr,n)
        print(*arr)

# } Driver Code Ends
