import sys

import heapq

n = int(sys.stdin.readline())

heap = []

for _ in range(n):
    x = int(sys.stdin.readline())
    if x == 0:
        if len(heap) == 0 :
            print(0)
        else :

            reverse_sign = lambda x : x * -1
            max_heap = list(map(reverse_sign, heap))
            heapq.heapify(max_heap)
            max_heap = list(map(reverse_sign, max_heap))
            
            print(heapq.heappop(heap))

    else :
        heapq.heappush(heap, x)
        
