class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l=0
        r=len(heights)-1
        max_water=0
        while l<r:
            width=r-l
            h=min(heights[l],heights[r])
            curr_water=h*width
            max_water=max(max_water,curr_water)

            if heights[l]<heights[r]:
                l+=1
            elif heights[l]>heights[r]:
                r-=1
            else:
                l+=1
                r-=1
        return max_water

            

            


            