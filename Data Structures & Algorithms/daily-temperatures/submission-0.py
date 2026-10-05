class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        days = [0]
        ans = [0] * len(temperatures)
        

        for i in range(1,len(temperatures)):

           if temperatures[i] <= temperatures[days[-1]]:
                days.append(i)
           else:
                
                while days and temperatures[i] > temperatures[days[-1]]:
                    idx = days[-1]
                    ans[idx] = i - days.pop()
                days.append(i)
        
        return ans


        