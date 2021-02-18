import cv2
import numpy as np

maksimum = 20


class KalmanFilter:
    kf = cv2.KalmanFilter(4, 2)
    kf.measurementMatrix = np.array([[1, 0, 0, 0], [0, 1, 0, 0]], np.float32)
    kf.transitionMatrix = np.array([[1, 0, 1, 0], [0, 1, 0, 1], [0, 0, 1, 0], [0, 0, 0, 1]], np.float32)

    def Paku(self, coordX, coordY, ):
        loeb = np.array([[np.float32(coordX)], [np.float32(coordY)]])
        self.kf.correct(loeb)
        ennustab = self.kf.predict()
        return ennustab


class VideoTuvastus:

    def Tuvastus(self):
        video = cv2.VideoCapture(0)
        if video.isOpened() == False:
            video = cv2.VideoCapture("test.mp4")
            return

        width = int(video.get(3))
        height = int(video.get(4))
        kalman_object = []
        ennustaKords = []
        for i in range(maksimum):
            kalman_object.append(KalmanFilter())
            ennustaKords.append(np.zeros((2, 1), np.float32))

        while video.isOpened():
            ret, frame = video.read()

            if ret == True:
                tuvastusXYZH = self.Tuvastaliikumine(frame)
                cv2.imshow("test", frame)
                for i in range(len(tuvastusXYZH)):
                    if (i > maksimum):
                        break


                    ennustaKords[i] = kalman_object[i].Paku(tuvastusXYZH[i][0], tuvastusXYZH[i][1])
                    frame = self.Tuvastatud(frame, tuvastusXYZH[i][0], tuvastusXYZH[i][1], ennustaKords[i])

                    cv2.imshow("video", frame)
                    if (cv2.waitKey(27)):
                        break

        video.release()
        cv2.destroyAllWindows()

    def Tuvastaliikumine(self, frame):
        gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
        blur = cv2.GaussianBlur(gray, (5, 5), 0)
        _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)
        dilated = cv2.dilate(thresh, None, iterations=3)
        contours, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        # cv2.drawContours(frame1, contours, -1, (0, 255, 0), 2)
        tuvastusXYZH = []
        for c in contours:
            if cv2.contourArea(c) > 1500:
                continue
            rect = cv2.boundingRect(c)
            x, y, w, h = cv2.boundingRect(c)

            kast = x, y, w, h
            print(kast)
            if kast is not None:
                centerCoord = (int((x + w / 2)), int((y + h / 2)))
                tuvastusXYZH.append((x,y,w,h))
                print(tuvastusXYZH)
                return tuvastusXYZH
            print(tuvastusXYZH)
            return tuvastusXYZH

        print(tuvastusXYZH)



    def Tuvastatud(self, frame, tuvastusX, tuvastusY, ennustaKord):
        cv2.rectangle(frame, (int(tuvastusX), int(10)), (int(tuvastusY), int(10)), (0, 255, 0), int(2), 2)
        cv2.line(frame, (int(tuvastusX), int(tuvastusY + 20)), (int(tuvastusX + 50), int(tuvastusY + 20)), [0, 255, 0],
                 2, 8)
        # kalman
        # cv2.rectangle(frame, (ennustaKord[0], ennustaKord[1]),(int(tuvastusW),int(tuvastusH)), 20, [0, 255, 255], 2)
        cv2.rectangle(frame, [(ennustaKord[0], 10), (ennustaKord[1], 10)],(0, 255, 255), 2,2)
        cv2.line(frame, (ennustaKord[0] + 10, ennustaKord[1] - 8), (ennustaKord[0] + 45, ennustaKord[1] - 25),
                 [220, 20, 60], 2, 8)

        return frame


#
# ,tuvastusXYZH[i][2],tuvastusXYZH[i][3]
# tuvastusW,tuvastusH,
# , int(tuvastusW), int(tuvastusH)
def main():
    tuvasta = VideoTuvastus()
    tuvasta.Tuvastus()


if __name__ == "__main__":
    main()

"""
jalgija = cv2.TrackerCSRT_create()

detect=[]
kalman =cv2.KalmanFilter()
cam = cv2.VideoCapture("test.mp4")
while cam.isOpened():
    ret, frame1 = cam.read()
    ret, frame2 = cam.read()

    lugeja = frame1[500: 720,400: 800]
    diff = cv2.absdiff(frame1, frame2)
    gray = cv2.cvtColor(diff, cv2.COLOR_RGB2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)
    dilated = cv2.dilate(thresh, None, iterations=3)
    contours, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# cv2.drawContours(frame1, contours, -1, (0, 255, 0), 2)

    for c in contours:
        if cv2.contourArea(c) < 1500:
            continue

        x, y, w, h = cv2.boundingRect(c)
        box=x,y,w,h
        detect.append(box)


    cv2.imshow("s",frame1)
"""
