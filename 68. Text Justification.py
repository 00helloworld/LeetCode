class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        res = []
        line = ''

        sum_width = 0
        start = 0
        end = 0

        while end <= len(words):
            if sum_width+end-start-1 > maxWidth:
                spaces_per_interval = (maxWidth - (sum_width-len(words[end-1]))) // (end - start - 2) if (end - start - 2)>0 else (maxWidth - (sum_width-len(words[end-1])))
                complement = (maxWidth - (sum_width-len(words[end-1]))) % (end - start - 2) if (end - start - 2)>0 else (maxWidth - (sum_width-len(words[end-1])))
                for i in range(start, end-1):
                    line = line + words[i] + spaces_per_interval*' '
                    if complement > 0:
                        line += ' '
                        complement -= 1
                if end-1-start == 1:
                    line = line.strip()
                    line = line + ' '*(maxWidth-len(line))
                    res.append(line)
                else:
                    res.append(line.strip())
                
                line = ''
                sum_width = 0
                end -= 1
                start = end
            else:
                if end == len(words):
                    line = ' '.join(words[start:])
                    line = line + ' '*(maxWidth-len(line))
                    res.append(line)
                    break
                sum_width += len(words[end])
                end += 1

        return res


words = ["What","must","be","acknowledgment","shall","be"]
maxWidth = 16
s = Solution()
s.fullJustify(words, maxWidth)