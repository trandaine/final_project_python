import tkinter as tk            #import tkinter library
import font_manager as fonts            #import fonts from font_manager.py
from check_videos import CheckVideos            #import CheckVideos class from check_videos.py
from create_video_list import CreateVideoList
from update_videos import UpdateVideos

def check_videos_clicked():                 #create a function named check_video_clicked
    status_lbl.configure(text="Note: Check Videos button was clicked!")                       #the text change when the button clicked
    CheckVideos(tk.Toplevel(window))            #create an instance of the "CheckVideos" class

def create_video_list_clicked():                                # Create a function
    status_lbl.configure(text="Note: Create Video List button was clicked!")                    # Set the text to the label widget to show the status
    CreateVideoList(tk.Toplevel(window))                            # Create an instance of the "CreateVideoList" class

def update_video_btn_clicked():                                     # Create a function
    status_lbl.configure(text="Note: Update Video button was clicked!")                         # Set the text to the label widget to show the status
    UpdateVideos(tk.Toplevel(window))                                   # Create an instance of the "UpdateVideos" class


window = tk.Tk()                    #create a window
window.geometry("520x150")                  #size of the window
window.title("Video Player")                        #title of the window
fonts.configure()           #call the 'configure' function from font_manager.py

header_lbl = tk.Label(window, text="Select an option by clicking one of the buttons below")         #create a label widget with the text
header_lbl.grid(row=0, column=0, columnspan=3, padx=10, pady=10)            #the label placed in row 0 - column 0, spanning 3 columns and adds padding around it

check_videos_btn = tk.Button(window, text="Check Videos", command=check_videos_clicked)         #create a button "Check Videos" and trigger the check_videos_clicked command when clicked
check_videos_btn.grid(row=1, column=0, padx=10, pady=10)                #the button placed in row 1 - column 0 with 10px weight and height

create_video_list_btn = tk.Button(window, text="Create Video List", command = create_video_list_clicked)             #create a button "Create Video List"
create_video_list_btn.grid(row=1, column=1, padx=10, pady=10)               #the button placed in row 1 - column 1 with 10px weight and height

update_videos_btn = tk.Button(window, text="Update Videos", command = update_video_btn_clicked)                     #create a button "Update Videos:
update_videos_btn.grid(row=1, column=2, padx=10, pady=10)                   #the button placed in row 1 - column 2 with 10px weight and height

status_lbl = tk.Label(window, text="", font=("Helvetica", 10))                         #creates a label widget named "status_lbl" with an initially empty text and a specified font
status_lbl.grid(row=2, column=0, columnspan=3, padx=10, pady=10)                #the empty text label placed in row 2 - column 0, spanning 3 columns with 10px weight and height

window.mainloop()                   #starts the tkinter main event loop, which keeps the GUI application running and responsive to user interactions
