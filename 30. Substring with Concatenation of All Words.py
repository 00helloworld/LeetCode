class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        len_word = len(words[0])
        len_words = len(words)
        l = 0
        res = []

        dic = {}
        for w in words:
            if w in dic:
                dic[w] += 1
            else:
                dic[w] = 1

        while l < len(s)-len_word * len_words + 1:
            r = l + len_word * len_words
            tmp = s[l: r]
            i = 0
            current_dic = {}
            while i < len(tmp):
                if tmp[i: i+len_word] not in current_dic:
                    current_dic[tmp[i: i+len_word]] = 1
                else:
                    current_dic[tmp[i: i+len_word]] += 1
                i += len_word

            if current_dic == dic:
                res.append(l)

            l += 1

        return res




        
        # Time Limit Exceeded
        # len_word = len(words[0])
        # len_words = len(words)
        # i = 0
        # j = i + len_word - 1
        # res = []

        # cnt_dic = {}
        # for w in words:
        #     if w in cnt_dic:
        #         cnt_dic[w] += 1
        #     else:
        #         cnt_dic[w] = 1
        # dic = {}

        # cnt = 0
        # while j < len(s):
        #     if s[i+cnt*len_word: j+1] not in words:
        #         i += 1
        #         j = i + len_word - 1
        #         dic = {}
        #         cnt = 0
        #     elif s[i+cnt*len_word:j+1] in dic and dic[s[i+cnt*len_word:j+1]] >= cnt_dic[s[i+cnt*len_word:j+1]]:
        #         i += 1
        #         j = i + len_word - 1
        #         dic = {}
        #         cnt = 0

        #     else:
        #         if s[i+cnt*len_word:j+1] not in dic:
        #             dic[s[i+cnt*len_word:j+1]] = 1
        #         else:
        #             dic[s[i+cnt*len_word:j+1]] += 1
        #         cnt += 1
        #         if cnt == len_words:
        #             res.append(i)
        #             cnt = 0
        #             i += 1
        #             j = i + len_word - 1
        #             dic = {}
        #         else:
        #             j = j + len_word

        # return res
                

s = "wordgoodgoodgoodbestword"
words = ["word","good","best","good"]
so = Solution()
so.findSubstring(s, words)

