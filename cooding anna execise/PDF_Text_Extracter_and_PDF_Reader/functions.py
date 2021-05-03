from tkinter import *
from PIL import Image, ImageTk
import pyttsx3

#------ speech & recognition func ----------
engine=pyttsx3.init()
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
engine.setProperty("rate", 140)
#speack function
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

#place an image on the grid
def display_logo(url, row, column):
    img = Image.open(url)
    #resize image
    img = img.resize((int(img.size[0]/1.5),int(img.size[1]/1.5)))
    img = ImageTk.PhotoImage(img)
    img_label = Label(image=img, bg="white")
    img_label.image = img
    img_label.grid(column=column, row=row, rowspan=2, sticky=NW, padx=20, pady=40)

def display_icon(url, row, column,stick,function):
    icon = Image.open(url)
    #resize image
    icon = icon.resize((20,20))
    icon = ImageTk.PhotoImage(icon)
    icon_label = Button(image=icon,command=function,width=25,height=25)
    icon_label.image = icon
    icon_label.grid(column=column, row=row,sticky=stick)

#place a tebox on the pages
def display_textbox(content, ro, col, root):
    text_box = Text(root, height=10, width=30, padx=10, pady=10)
    text_box.insert(1.0, content)
    text_box.tag_configure("center", justify="center")
    text_box.tag_add("center", 1.0, "end")
    text_box.grid(column=col, row=ro, sticky=SW, padx=25, pady=25)

#Detect Images inside the PDF document
#Thank you sylvain of Stackoverflow
#https://stackoverflow.com/questions/2693820/extract-images-from-pdf-without-resampling-in-python
def extract_images(page):
    images = []
    if '/XObject' in page['/Resources']:
        xObject = page['/Resources']['/XObject'].getObject()

        for obj in xObject:
            if xObject[obj]['/Subtype'] == '/Image':
                size = (xObject[obj]['/Width'], xObject[obj]['/Height'])
                data = xObject[obj].getData()
                mode = ""
                if xObject[obj]['/ColorSpace'] == '/DeviceRGB':
                    mode = "RGB"
                else:
                    mode = "CMYK"
                img = Image.frombytes(mode, size, data)
                images.append(img)
    return images
def image_resizer(img):
    width, height = int(img.size[0]), int(img.size[1])
    if width > height:
        height = int(300/width*height)
        width = 300
    elif height > width:
        width = int(250/height*width)
        height = 250
    else:
        width, height = 250,250
    img = img.resize((width, height))
    return img

def show_images(img):
    img = image_resizer(img)
    img = ImageTk.PhotoImage(img)
    img_label = Label(image=img, bg="white")
    img_label.image = img
    img_label.grid(row=4, column=2, rowspan=2)
    return img_label