
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Step 1: Count the frequency of each element
        count = Counter(nums)
        
        # Step 2: Use the Counter's most_common method to get the k most common elements
        most_common_elements = count.most_common(k)
        
        # Step 3: Extract just the elements (not their counts)
        top_k_elements = [element for element, frequency in most_common_elements]
        
        return top_k_elements