"""file for main window control"""
from tkinter import Tk, LabelFrame, Label, Button, filedialog, Toplevel
from PIL import Image, ImageTk

from ai_manager import AIManager


class MainWindow:
    """control main_window"""

    def __init__(self):
        self.ai = AIManager()

        self.window = Tk()

        self.filepath = None

        self.__configure_window()
        self.__init_widgets()
        self.__place_widgets()

    def mainloop(self):
        """start mainloop"""
        self.window.mainloop()

    def __init_widgets(self):
        self.income_frame = LabelFrame(text="Обработка", bg="orange", fg="black")

        self.btn_open = Button(
            self.income_frame,
            text="Открыть",
            bg="black",
            fg="orange",
            command=self.__btn_open_handler,
        )

        self.btn_detect = Button(
            self.income_frame,
            text="Обработать",
            bg="black",
            fg="orange",
            command=self.__btn_detect_handler,
        )

        self.label_path = Label(self.income_frame, bg="orange")
        self.label_path.config(text="Img_path:")

    def __place_widgets(self):
        pady = 5

        self.income_frame.pack(pady=pady)
        self.label_path.pack(pady=pady)
        self.btn_open.pack(pady=pady)
        self.btn_detect.pack(pady=pady)

    def __btn_open_handler(self):
        self.filepath = filedialog.askopenfilename()

        if self.filepath == "":
            return

        self.label_path.config(text="Img_path: {}".format(self.filepath))

        self.__open_new_window('ДО')

    def __btn_detect_handler(self):
        try:
            self.ai.detect(self.filepath)
        except ValueError:
            return

        self.__open_new_window('ПОСЛЕ')

    def __open_new_window(self, title):
        new_window = Toplevel(self.window)
        new_window.title(title)

        if title == 'ДО':
            image = Image.open(self.filepath)
        else:
            image = Image.open('image_new.jpg')
        image = ImageTk.PhotoImage(image=image)
        label_img = Label(new_window, image=image)
        label_img.image = image

        label_img.pack()

    def __configure_window(self):
        self.window.title("AI")
        self.window.config(bg="black")