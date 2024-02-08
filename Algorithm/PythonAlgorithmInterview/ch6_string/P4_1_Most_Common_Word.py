import re
import collections
from collections import Counter


class P4_1_Most_Common_Word:
    def mostCommonWord(self, paragraph: str, banned: list[str]) -> str:
        # 1. data cleansing and change to list
        paragraph_list = re.sub("\\W", " ", paragraph).lower().split()

        # 2. remove banned words in list
        not_banned_paragraph = [word for word in paragraph_list if word not in banned]

        # 3. create count dictionary
        count_dict = Counter(not_banned_paragraph)

        # 4. extract the most common word and return
        return count_dict.most_common(1)[0][0]


    def mostCommonWord2(self, paragraph: str, banned: list[str]) -> str:
        paragraph_list = re.sub("\\W", " ", paragraph).lower().split()

        not_banned_paragraph = [word for word in paragraph_list if word not in banned]

        counts = collections.defaultdict(int)

        for word in not_banned_paragraph:
            counts[word] += 1

        return max(counts, key=counts.get)
