def count(self,arr, n, x):
		# code here
		first = self.findOcc(arr, x, n,True)
		if first != -1:
            last = self.findOcc(arr, x, n,False)
            return last-first+1
        return 0
		
	def findOcc(self, nums, target, arr_len,find_start_index):
        ans = -1
        start = 0
        end = arr_len - 1
        while(start <= end):
            mid = start + ((end - start)//2)
            if(target > nums[mid]):
                start = mid + 1
            elif(target < nums[mid]):
                end = mid - 1
            else:
                ans = mid
                if(find_start_index):
                    end = mid - 1
                else:
                    start = mid + 1
        return ans