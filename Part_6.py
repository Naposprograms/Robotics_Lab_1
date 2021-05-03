"""
Tomar una foto con la cámara, seleccionar un objeto a identificar en la imagen, hacer un recorte y guardar como patrón.
Identificar ese patrón en la imagen original recuadrándola e indicando su posición.
El patrón debe ser encontrada en una posición definida por el desarrollador.
Si se carga una nueva imagen con el mismo patrón pero en otra posición debe avisarnos patrón desfasado.
"""

import cv2
import os
import sys


try:
    mode = str(sys.argv[1])
    if (mode != "Select_Template" and mode != "Match_Template"):
        print("Script argument should be Select_Template or Match_Template")
        quit()

except IndexError:
    print("Script requires one argument (mode)")
    quit()


path = os.getcwd()
image_path = "/Images/Part_6_captured_image.png"
template_path = "/Images/Part_6_template_image.png"
full_image_path = path + image_path
full_template_path = path + template_path

pointer_start = None
pointer_end = None
flag_selected_area = False
start = False

def on_mouse(event, x, y, flags, source_image):
    
    global start, flag_selected_area, pointer_start, pointer_end
    
    if event == cv2.EVENT_LBUTTONDOWN:
        pointer_start = (x, y)
        start = True
    
    elif start and event == cv2.EVENT_LBUTTONUP:
        pointer_end = (x, y)
        
        ROI_limit_left = pointer_start[0]
        ROI_limit_right = pointer_end[0]
        ROI_limit_inferior = pointer_start[1]
        ROI_limit_superior = pointer_end[1]

        template_image = source_image[ ROI_limit_left : ROI_limit_right, ROI_limit_inferior : ROI_limit_superior ]
        cv2.imwrite(full_template_path, template_image)

        source_image = cv2.rectangle(source_image, pointer_start, (x, y), (0, 255, 0), 3, cv2.LINE_AA)
        start = False
        flag_selected_area = True
    

def run_program():
    
    print("\nRunning Part_6.py, mode: {}".format(mode))
    global flag_selected_area
    if (mode == "Select_Template"):
        title = "Draw rectangle to select the pattern template"
        capture = cv2.VideoCapture(0)
        capture_ok, image = capture.read()
        
        if capture_ok:
        
            cv2.namedWindow(title)
            cv2.setMouseCallback(title, on_mouse, image)
            while (not flag_selected_area):
            
                cv2.imshow(title, image)
                if cv2.waitKey(1) & 0xFF == 27:
                    flag_selected_area = True
            
            cv2.imshow("Selected pattern template", image)
            cv2.waitKey(0)

        else:
            print("Revise camera")

    if (mode == "Match_Template"):
        template_image = cv2.imread(full_template_path)
        check_image_type = str( type(template_image) )
        if check_image_type == "<class 'NoneType'>":
            print("Revise image's path: {}".format(full_template_path))
            print("Be sure to select a template before trying to find a match")
            quit()


if __name__ == "__main__":

    run_program()