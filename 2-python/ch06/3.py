class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letters, digits=[],[]
        for log in logs:
            # isdigit() 숫자인지 판별
            if log.split()[1].isdigit():
                digits.append(log)
            else:
                letters.append(log)
        # lambda 식으로 후순위로 sort 가능 
        letters.sort(key=lambda x:(x.split()[1:],x.split()[0]))
        return letters+digits 
