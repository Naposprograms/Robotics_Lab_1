"""Dada una imagen de una figura geométrica detectar los vértices de dicha figura mediante el método de Harris Corner y marcarlos en la imagen original.
"""
import cv2
import os
import numpy


path = os.getcwd()
image_path = "/Images/cuadrado.jpg"
path += image_path
image = cv2.imread(path)
check_image_type = str( type(image) )
if check_image_type == "<class 'NoneType'>":
    print("Revise image's path")
    print("Finished execution")
    quit()
    

def run_program():

    print("\nRunning Part_2.py")
    image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    image_gray = numpy.float32(image_gray)

    dst = cv2.cornerHarris(image_gray, 2, 3, 0.04)


    height, width = dst.shape
    color = (0, 255, 0)
    for y in range(0, height):
        for x in range(0, width):
            if dst.item(y, x) >0.01* dst.max():
                cv2.circle(image, (x, y), 3, color, cv2.FILLED, cv2.LINE_AA)

    cv2.imshow('Harris Result', dst)
    cv2.imshow('Harris Corner', image)


    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
if __name__ == "__main__":
    run_program()