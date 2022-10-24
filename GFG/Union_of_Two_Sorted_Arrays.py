class Solution:
    
    #Function to return a list containing the union of the two arrays.
    def mergeArrays(self,a,b,n,m):
        '''
        :param a: given sorted array a
        :param n: size of sorted array a
        :param b: given sorted array b
        :param m: size of sorted array b
        :return:  The union of both arrays as a list
        '''
        # code here 
        first = 0
        second = 0
        final = []
        # final.append(min(a[first],b[second]))
        if(a[first] < b[second]):
            final.append(a[first])
            first+=1
        else:
            final.append(b[second])
            second+=1
        
        while((first<n) and (second<m)):
            if((a[first] == b[second])):
                if((a[first]!=final[-1])):
                    final.append(a[first])
                first+=1
                second+=1
            elif((a[first] < b[second])):
                if((a[first]!=final[-1])):
                    final.append(a[first])
                first+=1
            else:
                if(b[second] != final[-1]):
                    final.append(b[second])
                second+=1
                
        while(first<n):
            if(a[first] != final[-1]):
                final.append(a[first])
            first+=1
            
        while(second<m):
            if(b[second] != final[-1]):
                final.append(b[second])
            second+=1
        
        return final