"""
Calcular la frecuencia con la que aparecen los niveles de intensidad Azul, Verde y Rojo de la imagen tomada en el punto 1.
"""
import cv2
import os
from matplotlib import pyplot

path = os.getcwd()
image_path = "/Images/Part_1_captured_image.png"
path += image_path
image = cv2.imread(path)
check_image_type = str( type(image) )
if check_image_type == "<class 'NoneType'>":
    print("Revise image's path")
    print("Finished execution")
    quit()

def run_program():

    print("\nRunning Part_4.py")
    colours = ('b', 'g', 'r')
    for i, c in enumerate(colours):
        histogram = cv2.calcHist([image], [i], None, [256], [0, 256])
        pyplot.plot(histogram, color = c)
        pyplot.xlim( [0, 256] )
    pyplot.show(block=False)
    pyplot.pause(5)
    pyplot.close("all")
    
if __name__ == "__main__":
    run_program()