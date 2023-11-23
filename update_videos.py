import tkinter as tk                                        # Import the necessary modules form Tkinter library
import tkinter.scrolledtext as tkst                 #Import the necessary modules form Tkinter library
import  video_library as lib                                # Import the module containing function to manage a video library
import font_manager as fonts                            # Import the module use to configure fonts for the GUI


def set_text(text_area, content):   #inserts content into the text_area
    text_area.delete("1.0", tk.END)     #first the exsisting content is deleted
    text_area.insert(1.0, content)      #then the new content is inserted

class UpdateVideos():                   # Define UpdateVideos() class to create the main application window and manage the GUI
    def __init__(self, window):             # The constructor of class
        
        window.geometry("1200x450")         # The dimension of the window
        window.title('Update Videos')           # Set the title of the window

        self.list_videos_btn = tk.Button(window, text="Update All Videos", command=self.list_videos_btn_clicked)                                # Create a button labeled "Update All Videos" and return the list_videos_clicked command
        self.list_videos_btn.grid(row=0, column=0, padx=10, pady=10)                                                                                                     # The position of the button placed in row 0 and column 0, with 10 pixel horizontally and vertically

        label_1 = tk.Label(window, text="Enter the video number that you want to modify")                                                                       # Create a labeled "Enter the video number that you want to modify"
        label_1.grid(row=0, column=1, padx=10, pady=10)                                                                                                                         # The position of the button placed in row 0 and column 1, with 10 pixel horizontally and vertically

        self.enter_number_txt = tk.Entry(window, width=2)                                                                                                                           # Create a entry allow user input a video number
        self.enter_number_txt.grid(row=0, column=2, padx=10, pady=10)                                                                                                   # The position of the button placed in row 0 and column 2, with 10 pixel horizontally and vertically

        self.list1_txt = tk.Text(window, width=30, height=5, state="disabled")                                                                                              # Create an display to display the selected video
        self.list1_txt.place(x=510, y=90)                                                                                                                                                        # The text widget located at 510 pixel horizontal and 90 pixel vertical on the window

        self.list_txt  = tkst.ScrolledText(window, width=48, height=14, wrap="none")                                                                                    # Create a scrolled text widget to displaying a list of video, has a width of 48 characterrs and height of 14 lines it doesn't wrap text
        self.list_txt.grid(row=1, column=0, columnspan=3, sticky="W", padx=10, pady=10)                                                                         # The scrolled text widget is placed in row 1, column 0 to 2 and spanning three columns and sticked to the West - left

        self.check_videos_btn = tk.Button(window, text="Check selected video", command=self.check_video_clicked)                                # Create a button labeled "Check selected video" and return the check_video_clicked command
        self.check_videos_btn.grid(row=0, column=3, padx=10, pady=10)                                                                                                       # The position of the button placed in row 0, column 3 with 10 pixel horizontally and vertically

        self.list2_txt = tk.Text(window, width=30, height=5, state="disabled")                                                                                                  # Create a text widget to display the selected video
        self.list2_txt.place(x=820, y=90)                                                                                                                                                            # The position of the text widget located at 820 pixel horizontal and 90 pixel vertical on the window

        label_2 = tk.Label(window, text="Preview:")                                                                                                                                          # Create a label widget
        label_2.place(x=820, y=60)                                                                                                                                                                    # The position of the label widget located at 820 pixel horizontal and 60 pixel vertical on the window

        label_3 = tk.Label(window, text="Rating:")                                                                                                                                              # Create a label widget
        label_3.place(x=505, y=200)                                                                                                                                                                    # The position of the label widget located at 505 pixel horizontal and 200 pixel vertical on the window

        self.apply_btn = tk.Button(window, text="Apply", command=self.update_rating)                                                                                    # Create a button labeled "Apply" and return the update_rating command
        self.apply_btn.place(x=830,y=346)                                                                                                                                                           # The position of the button widget located at 830 pixel horizontal and 346 pixel vertical on the window

        cancel_btn = tk.Button(window, text="Cancel", command=exit)                                                                                                             # Create a button labeled "Cancel" and return the exit command
        cancel_btn.grid(row=3, column=5, padx=10, pady=10)                                                                                                                          # The position of the button placed in row 3, column 5 with 10 pixel horizontally and vertically

        self.status_lbl = tk.Label(window, text="", font=("Helvetica", 10))                                                                                                             #create a label widget to display the status messages
        self.status_lbl.place(x=10, y=347)                                                                                                                                                              # The position of the label widget located at 10 pixel horizontal and 347 pixel vertical on the window

        self.enter_number_entry = tk.Entry(window, width=2)                                                                                                                             # Create a entry allow user input a video number
        self.enter_number_entry.place(x=572, y=205)                                                                                                                                         # The position of the label widget located at 572 pixel horizontal and 205 pixel vertical on the window

    def check_video_clicked(self):                                                                                              # Define a function
        key = self.enter_number_txt.get()                                                                                      # Get the number from entry
        name = lib.get_name(key)                                                                                                # Get the name from video_library.py corresponding to the key in the entry
        if name is not None:
            self.list1_txt["state"] = "normal"                                                                                      # Set the text widget status to normal
            director = lib.get_director(key)                                                                                        # Get the director from video_library.py corresponding to the key in the entry
            rating = lib.get_rating(key)                                                                                                # Get the rating from video_library.py corresponding to the key in the entry
            play_count = lib.get_play_count(key)                                                                                # Get the play count from video_library.py corresponding to the key in the entry
            video_details = f"{name}\n{director}\nrating: {rating}\nplays: {play_count}"                        # Set the text to display the searching result
            set_text(self.list1_txt, video_details)                                                                                     # Print the text to the text widget
            self.list1_txt["state"] = "disabled"                                                                                            # Set the text widget status to disable to prevent user editing content
        else:
            set_text(self.status_lbl.configure(text=f"Video {key} not found"))                                              # Set the text to the label widget to show the status if the number from the entry is not available
        self.status_lbl.configure(text="Check Video button was clicked!")                                                 # Set the text to the label widget to show the status

    def list_videos_btn_clicked(self):                                                                      # Define a function
        video_list = lib.list_all()                                                                                 # List all the videos in video_library
        set_text(self.list_txt, video_list)                                                                     # Print all the videos to list widget
        self.status_lbl.configure(text="List Videos button was clicked!")                    # Set the text to the label widget to show the status

    def update_rating(self):                                                                                            # Define a function
        key = self.enter_number_txt.get()                                                                         # Get the number from entry
        update = int(self.enter_number_entry.get())                                                         # Get the number from entry
        lib.set_rating(key, update)                                                                                     # Set the rating by using the function in library_item
        name = lib.get_name(key)                                                                                    # Get the name from video_library.py corresponding to the key in the entry
        self.list2_txt["state"] = "normal"                                                                              # Set the text widget status to normal
        director = lib.get_director(key)                                                                                # Get the director from video_library.py corresponding to the key in the entry
        rating = lib.get_rating(key)                                                                                     # Get the rating from video_library.py corresponding to the key in the entry
        play_count = lib.get_play_count(key)                                                                    # Get the play count from video_library.py corresponding to the key in the entry
        video_details = f"{name}\n{director}\nrating: {rating}\nplays: {play_count}"            # Set the text to display the searching result
        set_text(self.list2_txt, video_details)                                                                     # Display the text to the text widget
        self.list2_txt["state"] = "disabled"                                                                            # Set the text widget status to disable to prevent user editing content
        self.status_lbl.configure(text="Rating has changed successfully!")                          # Set the text to the label widget to show the status



if __name__ == "__main__":                       # Only runs when this file is run as a standalone
    window = tk.Tk()                                      # Create a TK object
    fonts.configure()                                      # Configure the fonts
    UpdateVideos(window)                            # Open the CheckVideo GUI
    window.mainloop()                                   # Run the window main loop, reacting to button presses, etc