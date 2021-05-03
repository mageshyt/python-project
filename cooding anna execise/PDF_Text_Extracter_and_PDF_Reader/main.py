from tkinter import *
import tkinter
from typing import Counter
import PyPDF2
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfile
from functions import display_logo, display_textbox, extract_images,display_icon,image_resizer,show_images,speak


root = Tk()
root.geometry('+%d+%d'%(350,10)) 
#header area - logo & browse button
header = Frame(root, width=800, height=175, bg="white")
header.grid(columnspan=3, rowspan=2, row=0)
 #main content area - text and image extraction
main_content = Frame(root, width=800, height=250, bg="#20bebe")
main_content.grid(columnspan=3, rowspan=2, row=4)
#variable
page_contents=[]
all_images=[]
img_idex=[0]
displayed_img=[]
#button Fuction

#Copy Fucntion

def Copy_text(content):
    root.clipboard_clear()
    root.clipboard_append(content[-1])

#Save All Images

def Save_All(images):
    image_counter=1 #for saving all image in pdf 
    for i in images:
        if i.mode != "RGB":
            i=i.convert("RGB")
        i.save(f'img{image_counter}.png',format="png")
        image_counter+=1

#save Img

def Save_img(image):
    if image.mode != "RGB":
            image=image.convert("RGB")
    image.save(f'img.png',format="png")

#Right Arrow
def right_arrow(all_images, selected_img, what_text):
    #restrict button actions to the number of avialable images
    if img_idex[-1] < len(all_images) -1:
        #change to the following index
        new_idx = img_idex[-1] + 1
        img_idex.pop()
        img_idex.append(new_idx)
        #remove displayed image if exists
        if displayed_img:
            displayed_img[-1].grid_forget()
            displayed_img.pop()
        #create a new image in the new index & display it
        new_img = all_images[img_idex[-1]]
        selected_img = show_images(new_img)
        displayed_img.append(selected_img)
        #update the new index on the interface
        what_text.set("image " + str(img_idex[-1] + 1) + " out of " + str(len(all_images)))

#left arrow
def left_arrow(all_images, selected_img, what_text):
    if img_idex[-1] >= 1:
        #change to the previous index
        new_idx = img_idex[-1] - 1
        img_idex.pop()
        img_idex.append(new_idx)
        #remove displayed image if exists
        if displayed_img:
            displayed_img[-1].grid_forget()
            displayed_img.pop()
        #create a new image in the new index & display it
        new_img = all_images[img_idex[-1]]    
        selected_img = show_images(new_img)  #New image will be displayed
        displayed_img.append(selected_img)
        #update the new index on the interface
        what_text.set("image " + str(img_idex[-1] + 1) + " out of " + str(len(all_images)))


#Read function
def Read_Text(page_content):
    speak(page_content)

#Main function
def open_file():
    for i in img_idex:
        img_idex.pop()
    img_idex.append(0)
    browse_text.set("loading...")
    file = askopenfile(parent=root, mode='rb', filetypes=[("Pdf file", "*.pdf")])
    if file:
        read_pdf = PyPDF2.PdfFileReader(file)
        #page selected
        page = read_pdf.getPage(0)
        page_content = page.extractText()
        
        page_content = page_content.replace('\u2122', "'")
        
        page_contents.append(page_content)
        
        #clear the content of for next pdf
        if page_contents:
            for i in page_contents:
                page_contents.pop()

        #clear the image list from the previous PDF file
        for i in range(0, len(all_images)):
            all_images.pop()

        #hide the displayed image from the previous PDF file and remove it
        if displayed_img:
            displayed_img[-1].grid_forget()
            displayed_img.pop()
        
        #extract text
        page_contents.append(page_content)

        #extract images
        images = extract_images(page)
        for img in images:
            all_images.append(img)
        
        #Displaying image
        current_img=show_images(images[img_idex[-1]])
        displayed_img.append(current_img)
        

        #show text box on row 2 col 0
        display_textbox(page_content, 4, 0, root)

        #reset the button text back to Browse
        browse_text.set("Browse")
            #Save img
        save_img = Frame(root, width=800, height=60, bg="#c8c8c8")
        save_img.grid(columnspan=3, rowspan=1, row=3)

        # image info
        what_text = StringVar()
        _image = Label(root, textvariable=what_text, font=("shanti", 10))
        what_text.set("image " + str(img_idex[-1] + 1) + " out of " + str(len(all_images)))
        _image.grid(row=2, column=1)

        #arrow
        
        #left_arrow
        display_icon('arrow_l.png', 2, 0, E, lambda:left_arrow(all_images, current_img, what_text))
       
        #right arrow    
        display_icon('arrow_r.png', 2, 2, W, lambda:right_arrow(all_images, current_img, what_text))
                # Buttons ----->copy,save,read
        Copy_Btn=Button(root,text="Copy Text",command=lambda:Copy_text(page_contents),font=("shanti",10),height=1,width=15,bg='#eee')
        SaveAll_btn=Button(root,text="Save all thing",command=lambda:Save_All(all_images),font=("shanti",10),height=1,width=15)
        save_btn=Button(root,text="Save",command=lambda:Save_img(all_images[img_idex[-1]]),font=("shanti",10),height=1,width=15)
        read_btn=Button(root,text="Read the text",command=lambda:Read_Text(page_contents[-1]),font=("shanti",10),height=1,width=15)

        #placing Buttons
        Copy_Btn.grid(row=3,column=0)
        SaveAll_btn.grid(row=3,column=1)
        save_btn.grid(row=3,column=2)
        read_btn.grid(row=5,column=1)

display_logo('logo.png', 0, 0)

#instructions
instructions = Label(root, text="Select a PDF file", font=("Raleway", 10), bg="white")
instructions.grid(column=2, row=0, sticky=SE, padx=75, pady=5)

#browse button
browse_text = StringVar()
browse_btn = Button(root, textvariable=browse_text, command=lambda:open_file(), font=("Raleway",12), bg="#20bebe", fg="white", height=1, width=15)
browse_text.set("Browse")
browse_btn.grid(column=2, row=1, sticky=NE, padx=50)

root.mainloop()
