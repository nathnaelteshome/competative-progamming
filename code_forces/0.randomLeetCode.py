# User function Template for python3


class Solution:
    # Heapify function to maintain heap property.
    def heapify(self, arr, n, i):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n and arr[i] < arr[left]:
            largest = left
        if right < n and arr[largest] < arr[right]:
            largest = right

        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            self.heapify(arr, n, largest)
            # code here

    # Function to build a Heap from array.
    def buildHeap(self, arr, n):
        for i in range(n, -1, -1):
            self.heapify(arr, n, i)
        # code here

    # Function to sort an array using Heap Sort.
    def HeapSort(self, arr, n):
        self.buildHeap(arr, n)

        for i in range(n - 1, 0, -1):
            arr[i], arr[0] = arr[0], arr[i]
            self.heapify(arr, i, 0)


soln = Solution()
print(soln.HeapSort([4, 1, 3, 9, 7], 5))
