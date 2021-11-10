import cv2
vidcap = cv2.VideoCapture('D:\\Video\\101121_0.avi')

while(vidcap.isOpened()):
    success,image = vidcap.read()
    print(success)

    count = 0
    while success:
        cv2.imwrite("D:\\Videos\\101121_0\\frame%d.png" % count, image)     # save frame as JPEG file      
        success,image = vidcap.read()
        print('Read a new frame: ', success)
        count += 1
