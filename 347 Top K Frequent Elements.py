class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        visited = []
        for x in nums:
            if x not in visited:
                visited.append(x)
        freq = []
        for i in visited:
            freq.append(nums.count(i))
        zipped_pairs = zip(freq, visited) #zip(list2, list1)
        z = [x for _, x in sorted(zipped_pairs, reverse = True)]
        
        return z[0:k]        
