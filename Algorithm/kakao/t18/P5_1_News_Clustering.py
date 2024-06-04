import collections
import re


class P5_1_News_Clustering:
    def solution(self, str1, str2):
        # Create pairs with each two characters
        str1lst = [
            str1[i: i + 2].lower()
            for i in range(len(str1) - 1)
            if re.findall('[a-z]{2}', str1[i: i + 2].lower())
        ]

        str2lst = [
            str2[i: i + 2].lower()
            for i in range(len(str2) - 1)
            if re.findall('[a-z]{2}', str2[i: i + 2].lower())
        ]


        # Calculate sum and intersection
        intersection = sum((collections.Counter(str1lst) & collections.Counter(str2lst)).values())
        union = sum((collections.Counter(str1lst) | collections.Counter(str2lst)).values())

        # Calculate Jaccard Similarity
        jaccard_sim = 1 if union == 0 else intersection / union
        return int(jaccard_sim * 65536)
