from PIL import Image, ImageTk
import tkinter

class Search_UI():

    def __init__(self):
		# Starts the Search UI, sets title and screen size.
        self.Menu = tkinter.Tk()
        self.Menu.title("Space Mission Search")
        self.Menu.geometry("700x393")


    def searchbar(self):
        # Entry for the search bar where the mission search will be accepted.
        searchbar_entry = tkinter.Entry(self.Menu, font=("Arial", 14), bg = "#181B2C", bd = 0, fg = "grey",
                                        width = 26)
        searchbar_entry.pack()
        searchbar_entry.place(x = 314, y = 34.5)

        # Converts the image to work in tkinter, puts it on a button, then specifies where the button is located.
        searchbutton_img_convert = ImageTk.PhotoImage(Image.open(r'mission_search_photos/searchbutton.jpg'))

        searchbutton = tkinter.Button(self.Menu, width = 33, height = 32, bd = 0,
                                      activebackground = "#0d0f1b",
                                      image = searchbutton_img_convert)
        searchbutton.image = searchbutton_img_convert
        searchbutton.pack()
        searchbutton.place(x=630, y=29)



    def background(self):
        # Converts the image for use with tkinter then displays it with tkinter.
        background_convert = ImageTk.PhotoImage(Image.open(r'mission_search_photos/space_background.jpg'))

        background = tkinter.Label(self.Menu, image = background_convert)
        background.image = background_convert
        background.pack()



def main():
    # Starts the process of all the widgets in the search UI
    menu1 = Search_UI()

    menu1.background()
    menu1.searchbar()
    menu1.Menu.mainloop()


if __name__ == "__main__":
     main()


