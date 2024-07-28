from typing import List
import collections
import re
class P6_1_Matching_Score:
    '''
    1. Extract information from HTML using Regex.
    2. Calculate matching scores
    '''
    def solution(self, word:str, pages: List[str]):
        url_map = collections.defaultdict(str)
        link_map = collections.defaultdict(int)
        word_map = collections.defaultdict(int)
        linked_page_map = collections.defaultdict(list)

        # 1.
        for i, html in enumerate(pages):
            html = html.lower()
            word = word.lower()

            # 1-1 url
            regex = "<meta property=\"og:url\" content=\"(.*?)\"/"
            matcher = re.compile(regex)
            matches = matcher.findall(html)
            for match in matches:
                url_map[i] = match

            # 1-2 link
            regex = "<a href=\"(.*?)\""
            matcher = re.compile(regex)
            matches = matcher.findall(html)
            link_map[i] = len(matches)
            for match in matches:
                linked_page_map[match].append(i)

            # 1-3 word
            regex = "(?<![a-z])" + re.escape(word) + "(?![a-z])"
            matcher = re.compile(regex)
            matches = matcher.findall(html)
            word_map[i] = len(matches)

        # 2
        max_score = -1
        index = -1
        for i, page in enumerate(pages):
            basic_score = word_map[i]
            link_score = 0
            linked_pages = linked_page_map[url_map[i]]
            for idx in linked_pages:
                link_score += word_map[idx] / link_map[idx]
            total_score = basic_score + link_score

            if total_score > max_score:
                max_score = total_score
                index = i

        return index










