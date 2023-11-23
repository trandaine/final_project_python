import tkinter as tk        #import the necessary modules form Tkinter library
import tkinter.scrolledtext as tkst     #import the necessary modules form Tkinter library
import video_library as lib     #import the module containing function to manage a video library
import font_manager as fonts            #import the module use to configure fonts for the GUI
from PIL import Image, ImageTk          #import the module use to display image in GUI
import os
from idlelib import tooltip

def get_image_path(image_relative_path):
    script_dir = os.path.dirname(os.path.realpath(__file__))
    image_path = os.path.join(script_dir, image_relative_path)
    return image_path

def set_text(text_area, content):   #inserts content into the text_area
    text_area.delete("1.0", tk.END)     #first the exsisting content is deleted
    text_area.insert(1.0, content)      #then the new content is inserted


class CheckVideos():        #define CheckVideos() class to create the main application window and manage the GUI
    def __init__(self, window):             #the constructor of class
        window.geometry("1100x400")          #the dimension for the window
        window.title("Check Videos")            #set the title for the window

        list_videos_btn = tk.Button(window, text="List All Videos", command=self.list_videos_clicked)       #Create a button labeled "List All Videos" and return the list_videos_clicked command
        list_videos_btn.grid(row=0, column=0, padx=10, pady=10)     #the position of the button placed in row 0 and column 0, with 10 pixel horizontally and vertically

        enter_lbl = tk.Label(window, text="Enter Video Number")         #create a labeled "Enter Video Number"
        enter_lbl.grid(row=0, column=1, padx=10, pady=10)               #the position of the button placed in row 0, column 1 with 10 pixel horizontally and vertically

        self.input_txt = tk.Entry(window, width=3)                                                                                           #create a entry allow user input a video number
        self.input_txt.grid(row=0, column=2, padx=10, pady=10)                                                                  #the position of the entry placed in row 0, column 2 with 10 pixel horizontally and vertically

        img_btn_size = (30,30)
        check_image_path = get_image_path("image/check.png")
        check_img = Image.open(check_image_path).resize(img_btn_size)
        check_icon = ImageTk.PhotoImage(check_img)
        self.check_video_btn = tk.Button(window, image=check_icon, command=self.check_video_clicked)  # create a button labeled "Check Video" and return the check_video_clicked command
        self.check_video_btn.place(x=500, y=13)
        tooltip.Hovertip(self.check_video_btn, "Check Video")

        #tạo cái button phụ đi ba, mai tính tiếp
        check_video_btn1 = tk.Button(window, text="Check video", command=self.check_video_clicked)
        check_video_btn1.place(x=560, y=13)

        self.list_txt = tkst.ScrolledText(window, width=48, height=12, wrap="none")                                     #create a scrolled text widget to displaying a list of video, has a width of 48 characterrs and height of 12 lines it doesn't wrap text
        self.list_txt.grid(row=1, column=0, columnspan=3, sticky="W", padx=10, pady=10)                         #the scrolled text widget is placed in row 1, column 0 to 2 and spanning three columns and sticked to the West - left

        self.labelimage = tk.Label(window)              #create a label to display the selected image in library
        self.labelimage.place(x=750, y=70)          #The posistion of the label

        self.video_txt = tk.Text(window, width=24, height=4, wrap="none")                                                  #create a text widget for displaying the detail of selected video. Has a width of 24 characters and height of 4 lines, nor wrapped
        self.video_txt.grid(row=1, column=3, sticky="NW", padx=10, pady=10)                                            #the text located in row 1 - column 3, sticked to North West (top-left) with 10 pixel horizontally and vertically

        self.status_lbl = tk.Label(window, text="", font=("Helvetica", 10))                     #create a label widget to display the status messages
        self.status_lbl.grid(row=2, column=0, columnspan=4, sticky="W", padx=10, pady=10)               #the text located in row 2 - column 0, spanning all four column in the grid layout and stick to the left

        self.list_videos_clicked()              #start the function list_video_clicked() when the CheckVideo window open

    def check_video_clicked(self):                  #define the function check_video_clicked
        key = self.input_txt.get()                      #get the number from the entry
        name = lib.get_name(key)                # Get the name from video_library.py corresponding to the key in the entry
        if name is not None:
            director = lib.get_director(key)        # Get the director from video_library.py corresponding to the key in the entry
            rating = lib.get_rating(key)                # Get the rating from video_library.py corresponding to the key in the entry
            play_count = lib.get_play_count(key)    # Get the play count from video_library.py corresponding to the key in the entry
            video_details = f"{name}\n{director}\nrating: {rating}\nplays: {play_count}"        #set the text to display the searching result
            set_text(self.video_txt, video_details)         #print the text to the text widget video_txt
            video_image = lib.get_image(key)            #Get the key from the entry input
            if video_image:
                image = Image.open(video_image)
                image = image.resize((300,300))
                image = ImageTk.PhotoImage(image)
                self.labelimage.configure(image=image)
                self.labelimage.image = image  # Keep a reference to the image to prevent garbage collection
            else:
                self.labelimage.configure(image="")
        else:
            set_text(self.video_txt, f"Video {key} not found")          #if the key number of the video is not exist in video_library.py, set the error message to the text widget
            self.labelimage.configure(image="")
        self.status_lbl.configure(text="Check Video button was clicked!")           #set the text to the label widget to show the status

    def list_videos_clicked(self):                  #define the function list_videos_clicked
        video_list = lib.list_all()                       #get all the video details in the video_library.py
        set_text(self.list_txt, video_list)          #display the video details in the text widget
        self.status_lbl.configure(text="List Videos button was clicked!")            #set the text to the label widget to show the status

if __name__ == "__main__":  # only runs when this file is run as a standalone
    window = tk.Tk()        # create a TK object
    fonts.configure()       # configure the fonts
    CheckVideos(window)     # open the CheckVideo GUI
    window.mainloop()       # run the window main loop, reacting to button presses, etc
