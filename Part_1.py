"""
Tomar una Foto con la cámara.
Obtener el valor de los canales BGR del Pixel Central.
Modificar dicho Pixel para que se visualice en color Rojo.
Seleccionar una Región de Interés ROI de 100 pixeles en el eje x por 50 pixeles en el eje y donde el pixel modificado quede centrado.
"""

import cv2
import os


path = os.getcwd()
image_path = "/Images/Part_1_captured_image.png"
path += image_path


def run_program():
    
    print("\nRunning Part_1.py")
    capture = cv2.VideoCapture(0)
    capture_ok, image = capture.read()
    
    if capture_ok:

        cv2.imwrite(path, image)
        image_x_size, image_y_size, image_channels = image.shape
        print("Image size: ( {} , {} )".format(image_x_size, image_y_size) )

        image_half_x_size = int( image_x_size / 2 )
        image_half_y_size = int( image_y_size / 2 )

        print("Pixel @ [{}, {}] turned to red.".format(image_half_y_size, image_half_x_size) )

        image.itemset( (image_half_x_size, image_half_y_size, 0), 0)
        image.itemset( (image_half_x_size, image_half_y_size, 1), 0)
        image.itemset( (image_half_x_size, image_half_y_size, 2), 255)

        cv2.imshow("Pixel at centre turned to red", image)

        ROI_limit_left = image_half_x_size - 50
        ROI_limit_right = image_half_x_size + 50
        ROI_limit_inferior = image_half_y_size - 25
        ROI_limit_superior = image_half_y_size + 25

        image_ROI = image[ ROI_limit_left : ROI_limit_right, ROI_limit_inferior : ROI_limit_superior ]
        cv2.imshow('ROI', image_ROI)

        cv2.waitKey(0)
        cv2.destroyAllWindows()

    else:
        print("Revise camera")

if __name__ == "__main__":
    run_program()