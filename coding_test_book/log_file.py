

def sort(list: list[str]) -> list[str]:
    letters, digits = [], []
    
    # 1. 로그 분류
    for log in list:
        if log.split()[1].isdigit():
            digits.append(log)
        else:
            letters.append(log)    

    # 2. 문자 로그만 정렬
    #                           1차 정렬 기준      2차 정렬 기준
    letters.sort(key=lambda x: (x.split()[1:], x.split()[0]))

    # 3. 문자 로그 + 숫자 로그(원래 순서) 반환
    return letters + digits            


print(sort(["dig1 8 1 5 1", "let1 art can", "dig2 3 6", "let2 own kit dig", "let3 art zero"]))