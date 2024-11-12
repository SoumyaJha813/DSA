class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        llist = defaultdict(list)
        for s in strs:
            sortedstr = str(sorted(s))
            print(sortedstr)
            llist[sortedstr].append(s)
        return list(llist.values())
