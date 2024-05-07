class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        dic = {}
        grouped_list = []
        for word in strs:
            nw_word = "".join(sorted(word))

            if nw_word not in dic:
                dic[nw_word] = [word]
            else:
                dic[nw_word].append(word)
        
        for value in dic.values():
            grouped_list.append(value)

        return grouped_list        
        