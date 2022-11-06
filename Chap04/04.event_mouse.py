import numpy as np
import cv2

def onMouse(event, x, y, flags, param):     #콜백 함수 - 이벤트 내용 출력
    if event == cv2.EVENT_LBUTTONDOWN:
        print("마우스 왼쪽 버튼 누르기")
    elif event == cv2.EVENT_RBUTTONDOWN:
        print("마우스 오르쪽 버튼 누르기")
    elif event == cv2.EVENT_RBUTTONUP:
        print("마우스 오르쪽 버튼 떼기")
    elif event == cv2.EVENT_LBUTTONDBLCLK:
        print("마우스 왼쪽 버튼 더블클릭")
        
image = np.full((200, 300), 0, np.uint8)    # 초기 영상 생성
image1 = np.full((200, 300), 255, np.uint8)

title1, title2 = "Mouse Event1", "Mouse Event2"
cv2.imshow(title1, image)
cv2.imshow(title2, image1)

cv2.setMouseCallback(title1, onMouse)   # 마우스 콜백 함수
cv2.waitKey(0)  #키 이벤트 대기
cv2.destroyAllWindows()     # 열린 모든 윈도우 제거