class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        newlist = defaultdict(list)
        for string in strs:
            sorted1 = sorted(string)
            newlist[tuple(sorted1)].append(string)
        return newlist.values()