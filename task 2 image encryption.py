#importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from PIL import Image
import random
#defining class for encyrpting image
def encrypting_image(image_path, output_path):
    image = Image.open("D:\\Users\\zayed\\Downloads\\flower.jpg")
    pixels = image.load("D:\\Users\\zayed\\Downloads\\flower.jpg")
    #Specifying the height and width of image
    width, height = image.size
    for x in range(width):
        for y in range(height):
          # Randomly swap pixel values
                random_x, random_y = random.randint(0, width - 1), random.randint(0, height - 1)
                pixels[x, y], pixels[random_x, random_y] = pixels[random_x, random_y], pixels[x, y]
                image.save("D:\\Cyber\\encyrpted_image.jpg") # Using output_path parameter and save within the function
                return output_path
                # Calling the Function with correct arguements
                encrypting_image("D:\\Users\\zayed\\Downloads\\parrot.jpg", "D:\\Cyber\\encrypted_image.jpg")
                image_path = "input_image.jpg"
                encrypted_path = "encrypted_image.jpg"
                encrypting_image(image_path="D:\\Users\\zayed\\Downloads\\flower.jpg", output_path="D:\\Cyber\\encyrpted_image.jpg")
#defining class for decrypting image
def decrypting_image(image_path, output_path):
    image = Image.open("D:\\Users\\zayed\\Downloads\\flower.jpg")
    pixels = image.load("D:\\Users\\zayed\\Downloads\\flower.jpg")
    #Specifying the height and width of image
    width, height = image.size
    for x in range(width):
        for y in range(height):
          # Randomly swap pixel values
                random_x, random_y = random.randint(0, width - 1), random.randint(0, height - 1)
                pixels[x, y], pixels[random_x, random_y] = pixels[random_x, random_y], pixels[x, y]
                image.save("D:\\Cyber\\decyrpted_image.jpg") # Using output_path parameter and save within the function
                return output_path
                # Calling the Function with correct arguements
                decrypting_image("D:\\Users\\zayed\\Downloads\\flower.jpg", "D:\\Cyber\\decrypted_image.jpg")
                image_path = "input_image.jpg"
                decrypted_path = "decrypted_image.jpg"
                decrypting_image(image_path="D:\\Users\\zayed\\Downloads\\flower.jpg", output_path="D:\\Cyber\\decyrpted_image.jpg")
                encrypt_image("input_image.jpg","encrypted_image.jpg")
                decrypt_image("encrypted_image.jpg","decrypted_image.jpg")