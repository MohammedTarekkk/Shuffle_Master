import wx
import random
import os

## Define the list of names and corresponding photos
# names = ["Ali", "Mina", "Tarek", "Menna", "Youmna", "Beshoy", "Haidy", "Mayar", "Moemen", "Sherif"]
# photos = ["1.png", "2.jpg", "3.jpg", "4.png", "5.png", "6.png", "7.jpg", "8.png", "9.jpg", "10.jpg"]


# Define the GUI class
class MainFrame(wx.Frame):

    def __init__(self, *args, **kw):
        super(MainFrame, self).__init__(*args, **kw)
        self.data_file = "people_data.txt"
         # Set the application icon
         # Load the data from the file and populate the self.people list
        self.load_data()
        icon = wx.Icon("logo.png", wx.BITMAP_TYPE_PNG)
        self.SetIcon(icon)

        # self.SetSize((1200, 800))
        self.Maximize()  # Set the frame to fullscreen
        self.bSizerMain = wx.BoxSizer(wx.VERTICAL)

        # Add the image at the top left
        image = wx.Image("logo.png", wx.BITMAP_TYPE_PNG)
        image = image.Scale(100, 50, wx.IMAGE_QUALITY_HIGH)
        bitmap = wx.Bitmap(image)
        static_bitmap = wx.StaticBitmap(self, wx.ID_ANY, bitmap)
        self.bSizerMain.Add(static_bitmap, 0, wx.ALIGN_RIGHT | wx.ALL, 5)
        # self.bSizerMain.AddStretchSpacer(2)  
        # Create a StaticBoxSizer with title
        box_sizer = wx.StaticBoxSizer(wx.VERTICAL, self)
        

        # Create a wx.StaticText object with the desired font for the label
        label = wx.StaticText(self, label='SYS STANDUP MEETING ')
        font = wx.Font(wx.FontInfo(20))  # Create a font object with 20-point size
        label.SetFont(font)  # Set the font for the label
        # label.SetSize(1000, 100)

        # Add the label to the StaticBoxSizer
        box_sizer.Add(label, 0, wx.CENTER)

        # Create a ScrolledWindow to hold the images
        # scroll_window = wx.ScrolledWindow(self)
        # scroll_sizer = wx.BoxSizer(wx.HORIZONTAL)

        # Create a FlexGridSizer to hold the photos and names
        self.grid_sizer = wx.FlexGridSizer(rows=6, cols=8, vgap=10, hgap=10)
        # self.grid_sizer.AddGrowableCol(7, 2)  # Make the fourth column growable with proportion 2

        # Create a list of tuples containing the name and photo for each person
        # self.people = list(zip(names, photos))
        # Shuffle the list of people
        random.shuffle(self.people)

        for index, (name, photo) in enumerate(self.people):
            # Load the photo using wx.Image
            image = wx.Image(photo)
            # Scale the image to the desired size using wx.Image.Scale
            image = image.Scale(200, 200, wx.IMAGE_QUALITY_HIGH)
    
            # Convert the image to wx.Bitmap
            bitmap = wx.Bitmap(image)

            # Create a wx.StaticBitmap object and add it to the grid sizer using the scaled bitmap
            static_bitmap = wx.StaticBitmap(self, wx.ID_ANY, bitmap)
            self.grid_sizer.Add(static_bitmap, 0, wx.ALL | wx.CENTER, 5)
            

            # Create a label with the index and name
            label_text = f"{index + 1}. {name}"  # Add the index to the label text
            label = wx.StaticText(self, label=label_text)
            self.grid_sizer.Add(label, 0, wx.ALL | wx.CENTER, 5)
        

      

        # Create a box sizer to hold the buttons
        button_sizer = wx.BoxSizer(wx.HORIZONTAL)

        # Create a button to shuffle the names and photos
        shuffle_button = wx.Button(self, label="Shuffle")
        shuffle_button.SetBackgroundColour(wx.Colour(173, 216, 230))  # Set background color to white
        shuffle_button.SetForegroundColour(wx.Colour(0, 0, 0))  # Set foreground color to black
        shuffle_button_font = wx.Font(10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL)  # Define font for the button
        shuffle_button.SetFont(shuffle_button_font)  # Set the font for the button
        shuffle_button.SetMinSize((100, 40))
        button_sizer.Add(shuffle_button, 0, wx.EXPAND | wx.ALL, 5)
        # Set the tooltip for the shuffle_button
        shuffle_button.SetToolTip("Click to shuffle names and photos")
        
        # Bind the button to the shuffle_names_and_photos() method
        shuffle_button.Bind(wx.EVT_BUTTON, self.shuffle_names_and_photos)

        # Create a button to add a person and their photo to the list
        add_button = wx.Button(self, label="Add ")
        add_button.SetBackgroundColour(wx.Colour(144, 238, 144))  # Set background color to white
        add_button.SetForegroundColour(wx.Colour(0, 0, 0))  # Set foreground color to black
        add_button_font = wx.Font(10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL)  # Define font for the button
        add_button.SetFont(add_button_font)  # Set the font for the button
        # add_button.SetWindowStyleFlag(wx.BU_EXACTFIT)
        

        # Set the border size to add padding inside the button
        # add_button.SetBorder(5)
        button_sizer.Add(add_button, 0, wx.EXPAND | wx.ALL, 5)

        # Set the tooltip for the add_button
        add_button.SetToolTip("Click to Add a person and his/her photo")
        # Bind the button to the add_person_and_photo() method
        add_button.Bind(wx.EVT_BUTTON, self.add_person_and_photo)
        

        # Create a button to delete a person and their photo from the list
        delete_button = wx.Button(self, label="Delete ")
        delete_button.SetBackgroundColour(wx.Colour(255, 153, 153))  # Set background color to white
        delete_button.SetForegroundColour(wx.Colour(0, 0, 0))  # Set foreground color to black
        delete_button_font = wx.Font(10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL)  # Define font for the button
        delete_button.SetFont(delete_button_font)  # Set the font for the button
        button_sizer.Add(delete_button, 0, wx.EXPAND | wx.ALL, 5)
         # Set the tooltip for the add_button
        delete_button.SetToolTip("Click to delete a person and his/her photo")
        # Bind the button to the delete_person_and_photo() method
        delete_button.Bind(wx.EVT_BUTTON, self.delete_person_and_photo)


        # self.left_sizer = wx.BoxSizer(wx.VERTICAL) 
        # self.bSizerMain.Add(self.left_sizer)

        # Add self.grid_sizer to the left sizer
        # self.left_sizer.Add(self.grid_sizer, 1, wx.EXPAND | wx.ALL, 5)

        # self.right_sizer = wx.BoxSizer(wx.VERTICAL)
        # self.bSizerMain.Add(self.right_sizer)

        # if self.grid_sizer.CalcMin().height > self.GetSize().height:
    
        #     # Create scrolled window and set sizer
        #     scrolled_window = wx.ScrolledWindow(self)  
        #     scrolled_window.SetSizer(self.grid_sizer)  
            
        #     # Fit scrolled window and set scroll rate
        #     scrolled_window.FitInside()  
        #     scrolled_window.SetScrollRate(0, 20)

        #     self.right_sizer.Add(scrolled_window, 1, wx.EXPAND)
        # self.SetSizerAndFit(self.bSizerMain) 

        # Add a stretch spacer before and after the StaticBoxSizer to center it vertically
        self.bSizerMain.AddStretchSpacer()
        # Add box_sizer to bSizerMain
        self.bSizerMain.Add(box_sizer, 1, wx.CENTER | wx.ALL, 5)
        self.bSizerMain.AddStretchSpacer()

        # Add the grid_sizer sizer to the bSizerMain
        self.bSizerMain.Add(self.grid_sizer, 1, wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)
        # self.bSizerMain.Add(self.grid_sizer, 1, wx.EXPAND | wx.ALL, 5)

        
        # Add the button sizer to the bSizerMain
        self.bSizerMain.Add(button_sizer, 0, wx.ALIGN_RIGHT, 5)
        
        

        # Set the sizer for the frame
        self.SetSizer(self.bSizerMain)

        # Set the background color for the frame
        # self.SetBackgroundColour(wx.Colour(128, 128, 128))
        
    def load_data(self):
        self.people = []  # Initialize an empty list
        with open(self.data_file, "r") as file:
            for line in file:
                name, photo_name = line.strip().split(",")
                self.people.append((name, photo_name))

    def shuffle_names_and_photos(self, event):
        # Shuffle the list of people
        random.shuffle(self.people)

        # Update the labels and photos in the grid sizer
        for index, (name, photo) in enumerate(self.people):
            # Load the photo using wx.Image
            image = wx.Image(photo)
            # Scale the image to the desired size using wx.Image.Scale
            image = image.Scale(200, 200, wx.IMAGE_QUALITY_HIGH)
            # Convert the image to wx.Bitmap
            bitmap = wx.Bitmap(image)

            # Calculate the index of the label and static bitmap widgets in the grid sizer
            label_index = index * 2 + 1
            static_bitmap_index = index * 2

            # Update the corresponding wx.StaticBitmap object in the grid sizer with the new bitmap
            static_bitmap_item = self.grid_sizer.GetItem(static_bitmap_index)
            static_bitmap_widget = static_bitmap_item.GetWindow()
            static_bitmap_widget.SetBitmap(bitmap)

            # Update the corresponding wx.StaticText object in the grid sizer with the updated index and name
            label_item = self.grid_sizer.GetItem(label_index)
            label_widget = label_item.GetWindow()
            label_text = f"{index + 1}. {name}"
            label_widget.SetLabel(label_text)

        # Update the layout of the frame
        self.Layout()

    def add_person_and_photo(self, event):
        dlg = wx.FileDialog(self, "Choose a photo file", wildcard="Image files (*.png;*.jpg)|*.png;*.jpg")

      
        if dlg.ShowModal() == wx.ID_OK:
        
            photo_path = dlg.GetPath()
            photo_name = os.path.basename(photo_path)
            name = wx.GetTextFromUser("Enter the person's name")

            # Add the new person and photo to the list
            self.people.append((name, photo_name))
            # Load the photo using wx.Image
            image = wx.Image(photo_path)
            # Scale the image to the desired size using wx.Image.Scale
            image = image.Scale(200, 200, wx.IMAGE_QUALITY_HIGH)
            # Convert the image to wx.Bitmap
            bitmap = wx.Bitmap(image)

            # Calculate the index for the new person
            new_index = len(self.people)

            
            # Create a wx.StaticBitmap object and add it to the grid sizer using the scaled bitmap
            static_bitmap = wx.StaticBitmap(self, wx.ID_ANY, bitmap)
            self.grid_sizer.Add(static_bitmap, 0, wx.ALL | wx.CENTER, 5)
           
            # Create a wx.StaticText object with the label containing the new index and name
            label_text = f"{new_index}. {name}"
            label = wx.StaticText(self, label=label_text)
            self.grid_sizer.Add(label, 0, wx.ALL | wx.CENTER, 5)
            # Refresh the sizer to update the layout
            self.grid_sizer.Layout()


            # Save the updated data to the file
            self.save_data()

        dlg.Destroy()

    def save_data(self):
        with open(self.data_file, "w") as file:
            for name, photo_name in self.people:
                file.write(f"{name},{photo_name}\n")
    
    def delete_person_and_photo(self, event):
        # Create a dialog with a single choice list of names
        names = [name for name, photo in self.people]
        dlg = wx.SingleChoiceDialog(self, 'Select a name to delete', 'Delete Person', names)

        # Show the dialog and get the user's selection
        if dlg.ShowModal() == wx.ID_OK:
            selected_name = dlg.GetStringSelection()

            # Find the index of the selected name
            selected_index = names.index(selected_name)

            # Remove the corresponding name and photo from the people list
            deleted_person = self.people.pop(selected_index)

            # Update the indices of the remaining items in the list
            for index, (name, photo) in enumerate(self.people):
                label_text = f"{index + 1}. {name}"
                self.grid_sizer.GetItem(index * 2 + 1).GetWindow().SetLabel(label_text)

            # Clear the grid sizer and remove all children
            self.grid_sizer.Clear(True)

            # Iterate over the updated self.people list and add the photos and labels back to the grid sizer
            for index, (name, photo) in enumerate(self.people):
                # Load the photo using wx.Image
                image = wx.Image(photo)
                # Scale the image to the desired size using wx.Image.Scale
                image = image.Scale(200, 200, wx.IMAGE_QUALITY_HIGH)
                # Convert the image to wx.Bitmap
                bitmap = wx.Bitmap(image)
                # Create a wx.StaticBitmap object and add it to the grid sizer using the scaled bitmap
                static_bitmap = wx.StaticBitmap(self, wx.ID_ANY, bitmap)
                self.grid_sizer.Add(static_bitmap, 0, wx.ALL | wx.CENTER, 5)

                # Create a label with the index and name
                label_text = f"{index + 1}. {name}"  # Add the index to the label text
                label = wx.StaticText(self, label=label_text)
                self.grid_sizer.Add(label, 0, wx.ALL | wx.CENTER, 5)

            # Refresh the layout of the grid sizer
            self.grid_sizer.Layout()

            # Refresh the frame to reflect the changes
            self.Refresh()

            # Update the people_data.txt file
            self.update_data_file()
        
    def update_data_file(self):
            with open(self.data_file, "w") as file:
                for name, photo in self.people:
                    file.write(f"{name},{photo}\n")
    




# Create the app and frame
app = wx.App()
frame = MainFrame(None, title="ShuffleMaster")
# Show the frame
frame.Show()
# Run the app
app.MainLoop()

   
    