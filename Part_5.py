"""
Seguir un objeto de color verde con la cámara con un enmarcado que delimite el objeto a medida que se está moviendo.
"""
import cv2
import numpy as np

def run_program():
    
    print("\nRunning Part_5.py")
    flag_key_pressed = False
    upper_hsv_range = np.array([80, 255, 255])
    lower_hsv_range = np.array([40, 70, 50])
    capture = cv2.VideoCapture(0)

    while (not flag_key_pressed):
        capture_ok, frame = capture.read()
        if capture_ok:
            hsv = cv2.cvtColor(frame, cv2.COLOR_RGB2HSV)
            mask = cv2.inRange(hsv, lower_hsv_range, upper_hsv_range)
            contours, hierarchy = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
            cv2.drawContours(frame, contours, -1, (0, 0, 255), 2, cv2.LINE_AA)
            cv2.imshow("Contours of green objects - Press ESC to exit.", frame)
                
        if cv2.waitKey(1) & 0xFF == 27:
            flag_key_pressed = True

    capture.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    run_program()