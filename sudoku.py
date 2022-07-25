import cv2 
import numpy as np 

img3 = "/Users/jswoo/Desktop/Repository/OpenCV_Sudoku/3.png"
img1 = "/Users/jswoo/Desktop/Repository/OpenCV_Sudoku/1.png"
img2 = "/Users/jswoo/Desktop/Repository/OpenCV_Sudoku/2.png"

def BoxSearch(img):
    img_ori = cv2.imread(img)
    img = img_ori.copy()
    
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    thresh = cv2.adaptiveThreshold(img_gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV,57,7)
 
    contour2, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    cv2.drawContours(img, contour2, -1, (0,255,0), 4)
    '''
    # 컨투어 꼭지점 좌표를 작은 파랑색 점(원)으로 표시 ---⑨
    for i in contour2:
        for j in i:
            cv2.circle(img, tuple(j[0]), 1, (255,0,0), -1) 
    '''
    '''
    edges = cv2.Canny(img_gray, 50, 150, apertureSize = 3)

    vertical_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (1,5))
    thresh1 = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, vertical_kernel, iterations=9)
    horizontal_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5,1))
    thresh2 = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, horizontal_kernel, iterations=9)

   

    ## 선으로 대우를 받고 싶으면 최소길이가 100이어야하고 라인사이 갭은 10이어야한다.
    # p가 붙어서 확률 적으로 무작위로 허프변환 해본다 
    # probabilistic
    lines = cv2.HoughLinesP(edges, 1, np.pi/180, 100, minLineLength=20, maxLineGap=10)
    lines2 = cv2.HoughLinesP(thresh, 1, np.pi/180, 100, minLineLength=40, maxLineGap=10)

    for line in lines2:
        ## 리스트에서 1,2,3,4, 씩 계속 뽑아옴
        x1, y1, x2, y2 = line[0]
        cv2.line(img, (x1,y1), (x2,y2), (0,0,255), 2)
    '''
    cv2.imshow('ori', img)
    #cv2.imshow('vertical', thresh1)
    #cv2.imshow('horizontal', thresh2)
    cv2.imshow('thresh', thresh)
    #cv2.imshow('edges',edges)
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def NumSearch(img):
    pass

def SudokuWarapping(img):
    pass 


BoxSearch(img1)