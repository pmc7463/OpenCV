title = '서기 1년 1월 1일부터' \
        '오늘 까지'\
        '일수 구하기'
        # 3행에 걸쳐 작성 -> 1개 논리적 명령행
months = [31,28,31,30,31,30,
            31,31,30,31,30,31]

year, month = 2022, 10   # 여러개 변수 한 행에 선언
day = 17; ratio = 365.2425   #2개 논리적 명령행

days = (year - 1) * ratio + \
        sum(months[:month - 1]) + day   #1개 논리적 명령행
        
print(title), print(' - 년:', year), print(' - 월:', month)
print(' - 일:', day); print(' * 일수 총 합:', int(days))