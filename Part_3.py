"""
Realizar la umbralización de la imagen ¨Herramientas¨ cargando valores de umbral y máximo en forma manual para que las herramientas queden negras usando la función “cv2.THRESH_BINARY”.
Realizar la misma operación cargando el valor aportado por “cv2.THRESH_TRIANGLE”, que calcula el valor óptimo de umbralización.
Realizar la Umbralización adaptativa de la imagen “Herramientas”.
"""

import cv2
import os


path = os.getcwd()
image_path = "/Images/herramientas.jpg"
path += image_path
image = cv2.imread(path)
check_image_type = str( type(image) )
if check_image_type == "<class 'NoneType'>":
    print("Revise image's path")
    print("Finished execution")
    quit()

def run_program():

    print("\nRunning Part_3.py")
    image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    user_defined_threshold = 210
    threshold_value, dst = cv2.threshold(image_gray, user_defined_threshold, 255, cv2.THRESH_BINARY)

    cv2.imshow("Manual threshold @ {}".format(threshold_value), dst)
    cv2.waitKey(0)


    threshold_value, dst = cv2.threshold(image_gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_TRIANGLE)
    cv2.imshow("Triangled threshold @ {}".format(threshold_value), dst)
    print("user_defined_threshold: {}. Triangled threshold: {}".format(user_defined_threshold, threshold_value) )
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    run_program()

