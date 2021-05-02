"""
Tomar una foto con la cámara, seleccionar un objeto a identificar en la imagen, hacer un recorte y guardar como patrón. Identificar ese patrón en la imagen original recuadrándola e indicando su posición. El patrón debe ser encontrada en una posición definida por el desarrollador. Si se carga una nueva imagen con el mismo patrón pero en otra posición debe avisarnos patrón desfasado.
"""

import cv2
import os
import sys


path = os.getcwd()
image_path = "/Images/Part_6_captured_image.png"
path += image_path

try:
    mode = str(sys.argv[1])
    
    if (mode != "Select_Template" and mode != "Match_Template"):
        raise ArgumentError

except IndexError:
    print("Script requires one argument (mode)")

except ArgumentError:
    print("Script argument should be Select_Template or Match_Template")


def run_program():
    
    print("\nRunning Part_6.py, mode: {}".format(mode))
    
    if (mode == "Select_Template"):
        
        capture = cv2.VideoCapture(0)
        capture_ok, image = capture.read()
        
        if capture_ok:
            #cv2.imwrite(path, image)
            cv2.imshow("Draw rectangle to select the pattern template", image)
            
        else:
            print("Revise camera")



if __name__ == "__main__":
    run_program()