import cv2 as cv
import os

def video_to_img(videopath):
    cap = cv.VideoCapture(videopath)
    i=0
    while(cap.isOpened()):
        ret, frame = cap.read()
        if ret == False:
            break
        path = os.path.join('Converted_img', 'frame' +  f'{i:03}' +'.jpg')
        cv.imwrite(path, frame)
        i+=1
        
    cap.release()
    cv.destroyAllWindows()


def img_to_video(imgpath):
    dirs = os.listdir(imgpath)
    all_img = []
    for dir in dirs:
        dir = os.path.join(imgpath, dir)
        img = cv.imread(dir)
        all_img.append(img)
        h, w, l = img.shape
        size = (w, h)

    
    video = cv.VideoWriter('outputVideo.mp4', cv.VideoWriter_fourcc(*'MP4V'), 20, size)
    for i in range(len(all_img)):
        video.write(all_img[i])
    
    cv.destroyAllWindows()
    video.release()
    pass

# video_to_img('pnla1.mp4')
img_to_video('Converted_img')
