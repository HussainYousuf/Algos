from pprint import pprint

# from collections import OrderedDict


def longestPalindrome(s: str) -> str:
    maxString = ''
    for i in range(len(s)):
        left = i-1
        right = i+1
        string = s[i]
        print(left, right, string)
        flag = True
        while(True):
            if(flag and right < len(s) and s[right] == s[i]):
                string += s[right]
                right += 1
            elif(left > -1 and right < len(s) and s[left] == s[right]):
                string = s[left] + string + s[right]
                left -= 1
                right += 1
                flag = False
            else:
                break

        print(string)
        if(len(string) > len(maxString)):
            maxString = string

    print(maxString)
    return maxString



class Solution:
    def convert(self, s: str, numRows: int) -> str:
        distance = numRows + (numRows - 2)
        res=[]
        for i in range(numRows):
            res.append(s[i])
            # print(res)
            j = i + distance
            sub_distance = distance - 2 * i
            k = i + sub_distance
            while (j < len(s) or k < len(s)):
                if(i != 0 and i != numRows - 1): res.append(s[k])
                # print(res)
                res.append(s[j])
                # print(res)
                j += distance
                k += distance
        res="".join(res)
        # print(res)
        return res
                

class Solution:
    def maxArea(self, height: List[int]) -> int:
        self.height = height
        
    def area(left, right):
        width = right - left
        height = min(self.height[left],self.height[right])
        return width * height
    
    def recurse(left, right):
        if(left < right):
            area0 = self.area(left, right)
            area1 = self.recurse(left + 1, right)
            area2 = self.recurse(left, right-1)
            temp = max(area0, area1)
            return max(temp, area2)


longestPalindrome("babad")


from functools import cache

class Solution:
    def maxArea(self, height: List[int]) -> int:
        self.height = height
        self.memo = {}
        maxLeft = None
        maxe = -1
        for i,e in enumerate(height):
            if (e>maxe):
                maxe = e
                maxLeft = i
        maxRight = None
        maxe = -1
        for i,e in enumerate(height):
            if (e>maxe and i != maxLeft):
                maxe = e
                maxRight = i
            
        if(maxLeft > maxRight):
            [maxLeft, maxRight] = [maxRight, maxLeft]
        
        # print(maxLeft, maxRight)
        self.maxLeft = maxLeft
        self.maxRight = maxRight
        
        return self.recurse(0, len(height) -1)
        
    def area(self, left, right):
        width = right - left
        height = min(self.height[left],self.height[right])
        return width * height
    
    # @cache
    def recurse(self, left, right):
        if(left <= self.maxLeft and right >= self.maxRight):
            temp = self.memo.get(str(left)+'_'+str(right))
            if(temp): return temp
            # minHeight = min(self.height[left],self.height[right])
            area0 = self.area(left, right)
            i = 1
            while(left+i-1 < right and self.height[left+i] <= self.height[left]): i+=1
            area1 = self.recurse(left + i, right)
            i = 1
            while(right-i+1 > left and self.height[right-i] <= self.height[right]): i+=1
            area2 = self.recurse(left, right - i)
            temp = max(area0, area1)
            temp = max(temp, area2)
            self.memo[str(left)+'_'+str(right)] = temp
            # print(temp)
            
            return temp
        else:
            return 0 