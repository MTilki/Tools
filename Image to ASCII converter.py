from ctypes import resize
import PIL.Image

#ASCII characters used to make the image
ASCII_CHAR= {"@","#","S","%","?","*","+",";",":",",","."}

def main():
    image=input("Enter the image path:\n")
    try:
        image=PIL.Image.open(path)
    except:
        print(path,"is not a valid path")


def resize_image(image, new_width=100):
    image.size= width,height
    ratio = height / width
    new_hight = int(new_width * ratio)
    resize_image = image_resize((new_width, new_hight))
    return(resize_image)

def grayify(image):
    grayscale_image = inage.convert("L")
    return(grayscale_image)

main()