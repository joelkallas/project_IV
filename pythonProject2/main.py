import cv2
import datetime
import imutils
import numpy as np
from classes import KalmanFilter
import threading as thread

"""
todo:
1. vaadta kuidas saada paremini inimest tuvatada ilma mürata x
2. Lisada kalmani filter x
3. ühendada need oma vahel ära  x
4. teha tread kus 2 kaamerat tuvastavad liikumist -- ei võimada arvuti liiga nörk
5. kui üks kaamera tuvastab siis loeb liikumist   
6. kui mõlemad tuvastavad siis see kes enne tuvastab liikumist ja teine kaamera salvestab
pildi mille järel kui 1mene kaamera on vaba uuesti siis tuvastab pilti nii kaua
7. teha juurde läbi front endi avad kuhu kohta saab ruumi siseneda
8. lõpetada loendur  

"""

proto = "SSD_MobileNet_prototxt.txt"
model = "MobileNetSSD_deploy.caffemodel"
modelcvPath = cv2.dnn.readNetFromCaffe(prototxt=proto, caffeModel=model)

tuvastatavad = ["background", "kasutu1", "kasutu2", "kasutu3", "kasutu4",
           "bottle", "kasutu5", "car", "kasutu6", "kasutu7", "kasutu8", "kasutu9",
           "kasutu10", "kasutu11", "kasutu12", "person", "kasutu13", "kasutu14",
           "kasutu15", "kasutu16", "kasutu17"]


# leida aega ainult inimese caffe model
"""
with open('tuba1.txt') as f:
    numbrid = [0]
    lines = f.read().splitlines()
    if lines == None:
        for b in lines:
            b.split(":")
            if b[0] == "tuba 1":
                arv1=b[1]
    f.close()
"""
def kaamera():
    print("Salvestasin koodi Desktop/old/ver_2_3_lp_bck")
def main():
    cap = cv2.VideoCapture("test.mp4")
    fps_alg = datetime.datetime.now()
    fps = 0
    kaadrid = 0
    KF = KalmanFilter(0.1, 1, 1, 1, 0.1, 0.1)

    while True:
        ret, frame = cap.read()
        frame = imutils.resize(frame, width=800, height=600)
        kaadrid = kaadrid + 1

        (H, W) = frame.shape[:2]

        blob = cv2.dnn.blobFromImage(frame, 0.007843, (W, H), 127.5)

        modelcvPath.setInput(blob)
        leid = modelcvPath.forward()

        for i in np.arange(0, leid.shape[2]):
            s = leid[0, 0, i, 2]
            if s > 0.5:
                id = int(leid[0, 0, i, 1])

                if tuvastatavad[id] != "person":
                    continue
                keskpunkt = []
                lahis=[]
                tuvastus = leid[0, 0, i, 3:7] * np.array([W, H, W, H])
                (startX, startY, endX, endY) = tuvastus.astype("int")
                keskpunkt.append((int(startX) + int(endX)) / 2)
                keskpunkt.append(((int(startY) + int(endY)) / 2))
                cv2.rectangle(frame, (startX, startY), (endX, endY), (0, 0, 255), 2)
                if len(keskpunkt) > 0:
                    cv2.circle(frame, (int(keskpunkt[0]), int(keskpunkt[1])), 10, (0, 180, 255), 2)
                    (x, y) = KF.ennusta()
                    cv2.rectangle(frame, (x - 5, y - 5), (x + 5, y + 5), (255, 0, 0), 2)
                    (x1, y1) = KF.uuenda((keskpunkt[0]))
                    cv2.putText(frame, "Kus asub", (x1 + 5, y1 + 4), 0, 0.5, (0, 0, 255), 2)
                    cv2.putText(frame, "Ootatav", (x + 5, y), 0, 0.5, (255, 0, 0), 2)
                    cv2.putText(frame, "Arvatav koht", (int(keskpunkt[0]) + 5, int(keskpunkt[1]) - 5), 0, 0.5,
                                (0, 191, 255), 2)
                    """
                    hetkel laius on 800 ja kõrgus 600 siis saab kergesti jägida kui
                    kesknurk puudutab seda siis sinna läheb, aga probleem, et kuidas läbi front endi seda teha
                    
                    """
                    lahis.append(keskpunkt)
                    if (keskpunkt[0] < 500) and (keskpunkt[1] > 400):
                        print("all vasakus nurgas")
                    if (keskpunkt[0] < 500) and (keskpunkt[1] < 40):
                        print("üleval paremas nurgas")
                    if (keskpunkt[0] < 400) and (keskpunkt[1] > 40):
                        print("üleval keskel")
                    if (keskpunkt[0] < 30) and (keskpunkt[1] > 400):
                        print("all keskel")
                    #for i in lahis:
                      # if (lahis[int(i)][0]-lahis[int(i)+1][0])<30:
                        #   print("liiga lähedal")
        fps_lpp = datetime.datetime.now()
        ajavahe = fps_lpp - fps_alg
        if ajavahe.seconds == 0:
            fps = 0.0
        else:
            fps = (kaadrid / ajavahe.seconds)

        fps_text = "FPS: {:.2f}".format(fps)

        cv2.putText(frame, fps_text, (5, 30), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (0, 255, 0), 1)

        cv2.imshow("Application", frame)
        key = cv2.waitKey(1)
        if key == ord('q'):
            break

    cv2.destroyAllWindows()


if __name__ == '__main__':
    kaamera()
    main()
