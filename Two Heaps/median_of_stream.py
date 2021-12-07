#brute force -- insert_num = O(N) -- inserting in list (insert())takes O(n)
from math import ceil
class MedianOfStream:
    def __init__(self):
        self.stream_list = []
    def insert_num(self, num):
        if len(self.stream_list) == 0 or self.stream_list[len(self.stream_list)-1] <= num:
            self.stream_list.append(num)
        else:
            for i in range(len(self.stream_list)):
                if self.stream_list[i] >= num:
                    self.stream_list.insert(i, num)
            
    def find_median(self):
        if len(self.stream_list)%2 == 1:
            return self.stream_list[int(len(self.stream_list)//2)]
        else:
            return (self.stream_list[int(len(self.stream_list)/2)]+self.stream_list[(int(len(self.stream_list)/2))-1])/2
def main():
    x = MedianOfStream()
    x.insert_num(3)
    print(x.find_median())
    x.insert_num(1)
    print(x.find_median())
    x.insert_num(5)
    print(x.find_median())
    x.insert_num(4)
    print(x.find_median())
main()
#two heaps 
#time: insert_num = O(logN), findMedian = O(1) -- insert in heap takes O(logN), pop is obvi O(1)
#space = O(N)
import heapq
#there is some negative signs going on below -- this is just to convert the default heap of python (min heap) into a max heap by adding a negative in front everytime you insert or pop into/from the max heap
class MedianOfStream:
    def __init__(self):
        self.max_heap = []
        self.min_heap = []
    def insert_num(self, num):
        if not self.max_heap:
            heapq.heappush(self.max_heap, -num)
        elif -self.max_heap[0] > num:
            heapq.heappush(self.max_heap, -num)
        else:
            heapq.heappush(self.min_heap, num)
        if (len(self.max_heap)+len(self.min_heap))%2==0:
            if len(self.max_heap) > len(self.min_heap):
                while len(self.max_heap) != len(self.min_heap):
                    heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))
            elif len(self.min_heap) > len(self.max_heap):
                while len(self.min_heap) != len(self.max_heap):
                    heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))
        else:
            while len(self.max_heap) < len(self.min_heap):
                heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))
                
    def find_median(self):
        if (len(self.max_heap)+len(self.min_heap))%2!=0:
            return -self.max_heap[0]
            
        else:
            return (-self.max_heap[0]+self.min_heap[0])/2
        
        
def main():
    x = MedianOfStream()
    x.insert_num(3)
    print(x.min_heap, x.max_heap)
    print(x.find_median())
    x.insert_num(1)
    print(x.min_heap, x.max_heap)
    print(x.find_median())
    x.insert_num(5)
    print(x.min_heap, x.max_heap)
    print(x.find_median())
    x.insert_num(4)
    print(x.min_heap, x.max_heap)
    print(x.find_median())
main()
