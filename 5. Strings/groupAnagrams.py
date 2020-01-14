class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        idx = [i for i in range(len(strs))]
        tpls = zip(["".join(sorted(x)) for x in strs], idx)

        tpls_sorted = sorted(list(tpls))
        
        out = []
        group = []
        last = ""
        for i in tpls_sorted:
            if last != i[0] and group != []:
                out.append(group)
                group = []
                group.append(strs[i[1]])
            else:
                group.append(strs[i[1]])
            last = i[0]
        out.append(group)
        
        return out
        
        # Easier solution from "discussions":
        # d = {}
        # for w in strs:
        #   key = tuple(sorted(w))
        #   d[key] = d.get(key, []) + [w]
        # return d.values()
