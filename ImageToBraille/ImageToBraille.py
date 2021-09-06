import cv2


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
    if brailleCharacter == "\u2800": #this is to change the blank character for fonts where it's a different width to the others
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


userin=input("Do you want to use Otsu adaptive thresholding? (y/n) ")
if userin=="y":
    otsu=True
else:
    otsu=False

userin=input("Do you want to resize the image? (y/n) ")
if userin=="y"
    resizeX=int(input("input the width to resize to in pixels "))
    resizeY=int(input("input the height to resize to in pixels "))
else:
    resize=False



img=cv2.imread('img.png')
greyimg=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
if resize == True:
    greyimg=cv2.resize(greyimg, (resizeX,resizeY))

greyimg=cv2.bitwise_not(greyimg)
if otsu == True:
    ret, imgthreshed = cv2.threshold(greyimg,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU) # otsu adaptive thresholding
else:
    ret, imgthreshed = cv2.threshold(greyimg,127,255,cv2.THRESH_BINARY) #binary thresholding

out=threshedToBraille(imgthreshed)
print(out)

thefile = open("img.txt","wb")
thefile.write(out.encode("utf-8"))
thefile.close()
