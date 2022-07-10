import cv2 
import numpy as np 

img3 = "/Users/jswoo/Desktop/Repository/OpenCV_Sudoku/3.png"
img1 = "/Users/jswoo/Desktop/Repository/OpenCV_Sudoku/1.png"
img2 = "/Users/jswoo/Desktop/Repository/OpenCV_Sudoku/2.png"

def BoxSearch(img):
    img = cv2.imread(img)

    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(img_gray, 50, 150, apertureSize = 3)
    ## 선으로 대우를 받고 싶으면 최소길이가 100이어야하고 라인사이 갭은 10이어야한다.
    # p가 붙어서 확률 적으로 무작위로 허프변환 해본다 
    # probabilistic
    lines = cv2.HoughLinesP(edges, 1, np.pi/180, 100, minLineLength=20, maxLineGap=10)

    for line in lines:
        ## 리스트에서 1,2,3,4, 씩 계속 뽑아옴
        x1, y1, x2, y2 = line[0]
        cv2.line(img, (x1,y1), (x2,y2), (0,0,255), 2)

    cv2.imshow('test',img)
    cv2.imshow('edges',edges)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def NumSearch(img):
    pass

def SudokuWarapping(img):
    pass 


BoxSearch(img1)