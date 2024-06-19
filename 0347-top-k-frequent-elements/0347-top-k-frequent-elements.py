
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Step 1: Count frequencies of each element
        freq_dict = defaultdict(int)
        for num in nums:
            freq_dict[num] += 1
        
        # Step 2: Use a heap to find the top k frequent elements
        # Create a max heap based on frequency by using negative frequencies
        heap = [(-freq, num) for num, freq in freq_dict.items()]
        heapq.heapify(heap)
        
        # Step 3: Extract the top k elements from the heap
        top_k_elements = [heapq.heappop(heap)[1] for _ in range(k)]
        
        return top_k_elements