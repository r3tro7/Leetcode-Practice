class TimeMap:

    def __init__(self):
        self.maps = dict()

    # add a list to the dictionary value column with timestamp and value
    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.maps:
            self.maps[key] = list()
        self.maps[key].append([timestamp,value])

    # Base case: if the key is not present in the dict, or dict is empty
    # Edge cases: if the timestamp is greater than the last inserted timestamp: return the last inserted timestamp
    #             if the timestamp is smaller than the first inserted ts: return empty
    # logic: if the timestamp is not present in the dict and lies between 2 timestamps
    #     we need to return the value associated with the lower timestamp
    #     for that we use binary search to search for the lower timestamp and return
    def get(self, key: str, timestamp: int) -> str:

        if (key not in self.maps) or (not self.maps):
            return ""
        curr_map = self.maps[key]
        if timestamp > curr_map[-1][0]:
            return curr_map[-1][1]
        elif timestamp < curr_map[0][0]:
            return ""

        low:int = 0
        high:int = len(curr_map)

        while low < high:
            mid:int = low + ((high - low) // 2)

            if curr_map[mid][0] == timestamp:
                return curr_map[mid][1]
            elif(timestamp < curr_map[mid][0]):
                high = mid - 1
            else:
                low = mid
        return curr_map[low][1]




# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)