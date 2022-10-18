import cv2
import numpy as np
import pandas as pd
import argparse
# Creating a parser to accept image path as input from command line
ap = argparse.ArgumentParser()
ap.add_argument('- i', '--image', required = True, help = "Image Path")
args = vars(ap.parse_args())
img_path = args['image']
# Reading the images with opencv
img = cv2.imread(img_path)
# Declaring global variables(will be used later on)
clicked = False
r = g = b = xpos = ypos = 0
# Reading csv file with pandas and giving names to each colum
index = ["color", "color_name", "hex", "R", "G", "B"]
csv = pd.read_csv('colors.csv', names = index, header = None)