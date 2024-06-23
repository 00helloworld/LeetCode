class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        if sum(gas) < sum(cost):
            return -1
        
        # O(n**2)
        i = 0
        while i < len(gas):
            new_gas = gas[i:] + gas[:i]
            new_cost = cost[i:] + cost[:i]
            sum_g = 0
            sum_c = 0
            for j in range(len(gas)):
                sum_g += new_gas[j]
                sum_c += new_cost[j]
                if sum_g < sum_c:
                    i = i + j + 1
                    break
                if j == len(gas) - 1:
                    return i


gas = [1,2,3,4,5]
cost = [3,4,5,1,2]

s = Solution()
print(s.canCompleteCircuit(gas, cost))