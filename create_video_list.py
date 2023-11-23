import tkinter as tk                                            #import the necessary modules form Tkinter library
import tkinter.scrolledtext as tkst                      #import the necessary modules form Tkinter library
import video_library as lib                                 #import the module containing function to manage a video library
import font_manager as fonts                            #import the module use to configure fonts for the GUI

def set_text(text_area, content):   #inserts content into the text_area
    text_area.delete("1.0", tk.END)     #first the exsisting content is deleted
    text_area.insert(1.0, content)      #then the new content is inserted

class CreateVideoList():                        #define CheckVideos() class to create the main application window and manage the GUI
    def __init__(self, window):                 #the constructor of class
        window.geometry("1000x450")         #the dimension of the window
        window.title("Create Video List")       #set the title for the window

        self.video_list = []                            #create a memory list
        self.video_key_list = []                       #create a memory list
        self.updated_videos = []                  # Create a memory list

        list_videos_btn = tk.Button(window, text="List All Videos", command=self.list_videos_btn_clicked)                       #create a button labeled "list all videos" and return the list_video_btn_clicked command
        list_videos_btn.grid(row=0, column=0, padx=10, pady=10)                                                                                     #the position of the button placed in row 0 and column 0, with 10 pixel horizontally and vertically

        label_1 = tk.Label(window, text="Enter the video number that you want to add")                                  #create a labeled "Enter the video number that you want to add"
        label_1.grid(row=0, column=1, padx=10, pady=10)                                                                               #the position of the button placed in row 0 and column 1, with 10 pixel horizontally and vertically

        self.enter_number_txt = tk.Entry(window, width=3)                                                                               #create a entry allow user input a video number
        self.enter_number_txt.grid(row=0, column=2, padx=10, pady=10)                                                       #the position of the entry placed in row 0 and column 2, with 10 pixel horizontally and vertically

        add_video_button = tk.Button(window, text="Add", command=self.add_video_clicked)                                #create a button labeled "Add" and return the add_video_clicked command
        add_video_button.grid(row=0, column=3, padx=10, pady=10)                                                                        #the position of the button placed in row 0, column 3 with 10 pixel horizontally and vertically

        self.list_txt = tkst.ScrolledText(window, width=48, height=12, wrap="none")                                         #create a scrolled text widget to displaying a list of video, has a width of 48 characterrs and height of 12 lines it doesn't wrap text
        self.list_txt.grid(row=1, column=0, columnspan=3, sticky="W", padx=10, pady=10)                             #the scrolled text widget is placed in row 1, column 0 to 2 and spanning three columns and sticked to the West - left

        label_2 = tk.Label(window, text=">>>")                                                                                                  #create a label widget
        label_2.place(x=460, y=170)                                                                                                                  #the label widget located at 460 pixel horizontal and 170 vertical on the window.

        self.list1_txt = tk.Text(window, width=50, height=12, state="disabled")                         #create an display to display the selected video
        self.list1_txt.place(x=510, y=73)                                                                                       #the text widget located at 510 pixel horizontal and 73 pixel vertical on the window

        self.status_lbl = tk.Label(window, text="", font=("Helvetica", 10))                                                         #create a label widget to display the status messages
        self.status_lbl.grid(row=3, column=0, columnspan=4, sticky="W", padx=10, pady=10)                   #the text located in row 3 - column 0, spanning all four column in the grid layout and stick to the left

        self.play_video_btn = tk.Button(window, text="Create and Play", command=self.play_video_btn_clicked)                #create a button labeled "Create and Play" and return the play_video_btn_clicked command
        self.play_video_btn.grid(row=4, column=2, padx=10, pady=10)                                                                                     #the position of the button placed in row 4, column 2 with 10 pixel horizontally and vertically

        clear_videos_btn = tk.Button(window, text="Clear", command=self.clear_video_btn_clicked)                            #create a button labeled "Clear" and return the clear_video_btn_clicked command
        clear_videos_btn.grid(row=4, column=3, padx=10, pady=10)                                                                            #the position of the button placed in row 4, column 3 with 10 pixel horizontally and vertically

        cancel_btn = tk.Button(window, text="Cancel", command=exit)                         #create a button labeled "Cancel" and return the exit command
        cancel_btn.grid(row=4, column=4, padx=10, pady=10)                                      #the position of the button placed in row 4, column 4 with 10 pixel horizontally and vertically

    def list_videos_btn_clicked(self):                                                                      #define a function
        video_list = lib.list_all()                                                                                  # Call your list_all function to get a list of all videos
        set_text(self.list_txt, video_list)                                                                      #print the list to the text widget list_txt
        self.status_lbl.configure(text="List Videos button was clicked!")                   #set the text to the label widget to show the status

    def add_video_clicked(self):                                #define the function add_video_clicked
        key = self.enter_number_txt.get()                   #get the number from entry
        name = lib.get_name(key)                                #get the name from video_library.py corresponding to the key in the entry
        if name is not None:
            director = lib.get_director(key)                                #get the director from video_library.py corresponding to the key in the entry
            rating = lib.get_rating(key)                                     #get the rating from video_library.py corresponding to the key in the entry
            play_count = lib.get_play_count(key)                    #get the play count from video_library.py corresponding to the key in the entry
            video_details = f"{name}, {director}, rating: {rating}, plays: {play_count}"                        #set the text to display the searching result
            self.video_list.append(video_details)                                   #add the video_details to the video_list memory
            self.video_key_list.append(key)                                            #add the key to the video_key_list memory
            self.update_video_list()                                                        # Call the function to update the displayed list
            self.status_lbl.configure(text=f"Video {key} added to the list successful")                     #set the text to the label widget to show the status
        else:
            self.status_lbl.configure(text=f"Video {key} not found")                                    #set the text to the label widget to show the status if the number from the entry is not available
        self.update_video_list()                                # Call the function update_video_list

    def update_video_list(self):                                        # Define the function
        self.list1_txt["state"] = "normal"                              # Set the text widget status to normal
        self.list1_txt.delete("1.0", tk.END)                          # Delete the previous content
        contents = ""                                                           # Store the formatted text
        for video in self.video_list:                                      # For each video in video_list
            contents += video + "\n"                                      # Appear the video content for display on the new line
        self.list1_txt.insert(1.0, contents)                            # insert the new contents
        self.list1_txt["state"] = "disabled"                             # Set the text widget status to disable to prevent user editing content

    def clear_video_btn_clicked(self):                              # Define the function clear_video_btn_clicked
        self.video_list.clear()                                               # Clear the video_list memory
        self.video_key_list.clear()                                        # Clear the video_key_list memory
        self.update_video_list()                                            # Call the function update_video_list
        self.status_lbl.configure(text="Clear button was clicked!")             # Set the text to the label widget to show the status


    def play_video_btn_clicked(self):                       # Define the function
        for key in self.video_key_list:                         # For every key in video_key_list
            lib.increment_play_count(key)                   # Increment the play count for each video
            name = lib.get_name(key)                        # Get the name from video_library.py corresponding to the key in the entry
            director = lib.get_director(key)                    # Get the director from video_library.py corresponding to the key in the entry
            rating = lib.get_rating(key)                         # Get the rating from video_library.py corresponding to the key in the entry
            play_count = lib.get_play_count(key)        # Get the play count from video_library.py corresponding to the key in the entry
            video_details = f"{name}, {director}, rating: {rating}, plays: {play_count}"                # Set the text to display the searching result
            self.updated_videos.append(video_details)                                   # Add the video_details to the memory
        self.video_list = self.updated_videos                                                   # Update the video list with the updated play counts
        self.update_video_list()                                                                        # Update the displayed list with the updated videos
        self.status_lbl.configure(text="Create and Play button was clicked!")                   # Set the text to the label widget to show the status


if __name__ == "__main__":              # Only runs when this file is run as a standalone
    window = tk.Tk()                            # Create a TK object
    fonts.configure()                           # Configure the fonts
    CreateVideoList(window)                 # Open the CheckVideo GUI
    window.mainloop()                       # Run the window main loop, reacting to button presses, etc
