import cv2
import ffmpeg
import os
#from mss.windows import MSS as mss

def segmentToBraille(imgsegment):
    binaryDigits=""
    for column in [1,0]:
        if imgsegment[3][column] == 255:
            binaryDigits+="1"
        else:
            binaryDigits+="0"
    for column in [1,0]:
        for row in [2,1,0]:
            if imgsegment[row][column] == 255:
                binaryDigits+="1"
            else:
                binaryDigits+="0"
    
    decimalValue=int(binaryDigits, 2)#i found that the python int function takes a parameter for base
    decimalUniValue=10240+decimalValue
    brailleCharacter=chr(decimalUniValue) #this line took an hour to find the fuction for
    if brailleCharacter == "\u2800":
        brailleCharacter="\u2800"
    return brailleCharacter


def threshedToBraille(imgthreshed):
    outstring=""
    maxY=len(imgthreshed)
    maxX=len(imgthreshed[0])
    for y in range(0,maxY-4,4):
        for x in range(0,maxX-2,2):
            cropimg = imgthreshed[y:y+4, x:x+2]
            braille=segmentToBraille(cropimg)
            outstring+=braille
        outstring+="\n"
    return outstring
(
ffmpeg
.input("videoin.mkv")
.filter('fps', fps=30)
.output('frameExtraction/frame-%d.png', 
        start_number=0)
.overwrite_output()
.run()
)#IMPORTANT! ffmpeg wont create folders, they must already exist. 

framecount=len(os.listdir("frameExtraction/"))

with mss() as sct:
    for frame in range(framecount):
        img=cv2.imread("frameExtraction/frame-"+str(frame)+".png")
        greyimg=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        resized=cv2.resize(greyimg, (48,36))
        resized=cv2.bitwise_not(resized)
        ret, imgthreshed = cv2.threshold(resized,127,255,cv2.THRESH_BINARY)
        out=threshedToBraille(imgthreshed)
        #thefile = open("textframes/frame-"+str(frame)+".txt","wb")
        #thefile.write(out.encode("utf-8"))
        #thefile.close()
        print(out)
        #sct.shot(output='scrnshots/scrn-'+str(frame)+'.png')
    
    
    



