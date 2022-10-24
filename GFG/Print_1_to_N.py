class Solution:    
    #Complete this function
    def recApproach(self,num,N):
        if(num > N):
            return
        print(num,end = " ")
        num += 1
        self.recApproach(num,N)
    
    def printNos(self,N):
        #Your code here
        self.recApproach(1,N)