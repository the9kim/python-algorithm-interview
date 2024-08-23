import collections
import re
from typing import List


class P6_1_Matching_Score:
    '''
    1. Parse html pages
    2. Calculate the optimal matching score
    '''

    def solution(self, word: str, pages: List[str]):

        n = len(pages)

        urls = []
        basic_scores = []
        links = collections.defaultdict(list)
        matching_scores = []

        word = word.lower()
        word_pattern = re.compile(r'(?<![a-zA-Z])' + re.escape(word) + r'(?![a-zA-Z])')
        url_pattern = re.compile(r'<meta property="og:url" content="(.*?)"/>')
        link_pattern = re.compile(r'<a href="(.*?)">')

        for i, page in enumerate(pages):
            page = page.lower()

            # URL
            url = re.search(url_pattern, page)
            urls.append(url.group(1) if url else '')

            # Word
            basic_scores.append(len(re.findall(word_pattern, page)))

            # Link
            links[i].extend(re.findall(link_pattern, page))

        for i in range(n):
            score = basic_scores[i]

            for j in range(n):

                if i != j and urls[i] in links[j]:
                    score += basic_scores[j] / len(links[j])

            matching_scores.append(score)

        return matching_scores.index(max(matching_scores))
