"""
En una foto o video mp4 en donde se vea una línea (para seguimiento de robots o de autos), realizar el seguimiento de líneas con la función cv2.HoughLines(), como lo haría un robot móvil.
"""
import cv2
import os
import numpy as np

path = os.getcwd()
video_path = "/Images/video_lineas.avi"
path += video_path


def run_program():
    
    print("\nRunning Part_7.py")
    capture = cv2.VideoCapture(path)
    flag_key_pressed = False

    while ( not flag_key_pressed ):
        
        capture_ok, image = capture.read()
        
        if capture_ok:

            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            edges = cv2.Canny(gray, 50, 150, apertureSize =3)
            lines = cv2.HoughLinesP(edges, 1, np.pi/180, 100, minLineLength=100, maxLineGap=1)
            for line in lines:
                x1, y1, x2, y2 = line[0]
                cv2.line(image, (x1,y1), (x2,y2), (0,255,0), 1, cv2.LINE_AA)

            cv2.imshow("Lines video", image)
            cv2.waitKey(1)
        
        else:
            break

        if cv2.waitKey(1) & 0xFF == 27:
            flag_key_pressed = True

    capture.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    run_program()