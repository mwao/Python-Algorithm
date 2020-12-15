  
import collections
import re
from typing import List


class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        words = [word for word in re.sub(r'[^\w]', ' ', paragraph).lower().split() if word not in banned]

        counts = collections.Counter(words)
        # print(counts) 
        # ㄴ결과 : Counter({'ball': 2, 'bob': 1, 'a': 1, 'the': 1, 'flew': 1, 'far': 1, 'after': 1, 'it': 1, 'was': 1})
        
        # counts.most_common(1) 결과 = [('ball',2)]
        # counts.most_common(1)[0] 결과 = ('ball',2)
        # counts.most_common(1)[0][0] 결과 = 'ball'
    
        # 가장 흔하게 등장하는 단어의 첫 번째 인덱스 리턴
        return counts.most_common(1)[0][0]
