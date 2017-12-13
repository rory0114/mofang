import cv2
import numpy as np

def findcolor(H,S,V):
    if S<48:
        c = "w"
    else:
        if  H>130:
            c = "r"
        elif H>75:
            c = "b"
        elif H>38:
            c = "g"
        elif H>22:
            c = "y"
        else:
            if V>200:
                c = "o"
            else:
                c = "r"
    return c


class cubespot(object):
    def __init__(self,x,y,cont,colour="",pos=-1,face=-1,mean=[0,0,0]):
        self.colour=colour
        self.x=x
        self.y=y
        self.cont=cont
        self.pos=pos
        self.face=face
        self.mean=mean
        
def cubeproess(where):
    img1=cv2.imread(where,1)  #读取图像
    img=cv2.resize(img1,(300,500))  #对图像大小进行调整

    img = cv2.GaussianBlur(img,(5,5),0) #进行高斯模糊处理
    #clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) #获得灰度图
    hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)   #获得hsv图
    #gray = clahe.apply(gray)

    cv2.imshow("ff",gray)
    binary = cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_MEAN_C,\
                cv2.THRESH_BINARY,11,2)  #对图像进行而二值处理，采用了平均自适应的算法
    cv2.imshow("fff",binary)
    face,contours, hierarchy = cv2.findContours(binary,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)  #获得轮廓

    def getcol(color):
        return "r"
        
    cube=list()
    select=list()
    for i in range(len(contours)):
        cnt=contours[i]
        x,y,w,h = cv2.boundingRect(cnt)
        area = cv2.contourArea(cnt)
        rect_area = w*h
        extent = float(area)/rect_area
        if area>10 and extent>0.8 and area<10000:
            temp=cubespot(x,y,cnt)
            cube.append(temp)
    if len(cube)==90:
        print("can't find 9 spot")
        exit(0)
    cube=sorted(cube,key=lambda one:(int(one.x/80),one.y))

    for i in range(len(cube)):
        cnt=cube[i].cont
        cv2.drawContours(img,cnt,-1,(0,0,255),thickness=3)
        mask = np.zeros(gray.shape,np.uint8)
        cv2.drawContours(mask,[cnt],0,255,thickness=cv2.FILLED )
        pixelpoints = np.transpose(np.nonzero(mask))
        cv2.imshow("img",img)
        mean_val = cv2.mean(hsv,mask=mask)
        cube[i].pos=i
        cube[i].mean=mean_val
        cube[i].colour=findcolor(mean_val[0],mean_val[1],mean_val[2])

        print(cube[i].colour)
        
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        
    return cube
