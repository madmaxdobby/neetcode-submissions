class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq=defaultdict(int)

        for i in nums:
            if i not in freq.keys():
                freq[i]=0
            freq[i]+=1

        l=sorted(freq.keys(),reverse=True,key=freq.get)
        result=[]
        
        for i in range(k):
            result.append(l[i])
        return result

        
            

            