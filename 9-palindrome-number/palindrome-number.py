class Solution:
    def isPalindrome(self, x: int) -> bool:
        temp=x
        sum=0
        if(x<0):
            return False
        while(x>0):
            dig=x%10
            sum=(sum*10)+dig
            x=x//10
        return sum==temp