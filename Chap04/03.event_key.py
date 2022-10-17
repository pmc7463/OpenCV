import imp
import numpy as np
import cv2

# switch case 문을 사전(dictionary)으로 구현
switch_case = {
    ord('a'): "a키 입력",    #ord()함수 : 문자 -> 아스키코드 변환
    ord('b'): "b키 입력",
    0x41: "A키 입력",
    int('0x42', 16): "B키 입력", #0x42(16진수) -> 10진수 변환
    2424832: "왼쪽 키",
    2490368: "위 키",
    2555904: "오른쪽 키",
    2621440: "아래 키"
}

image = np.ones((200, 300), np.float)   #원소값 1인 행렬 생성
cv2.namedWindow("Keybord Event")        #윈도우 이름
cv2.imshow("Keybord Event", image)

while True: #무한 반복
    key = cv2.waitKeyEx(100)    #100ms 동안 키 이벤트 대기
    if key == 27: break         #ESC 키 누르면 종료
    
    try:
        result = switch_case[key]
        print(result)
    except KeyError:
        result = -1
        
cv2.destroyAllWindows()         #열린 모든 윈도우 제거