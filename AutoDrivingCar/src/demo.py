import tkinter as tk
from PIL import ImageTk
from PIL import Image

class SimpleApp(object):
    def __init__(self, master, filename, **kwargs):
        self.master = master
        self.filename = filename
        self.canvas = tk.Canvas(master, width=500, height=500)
        self.canvas.pack()

        self.update = self.draw()
        master.after(100, self.update)

    def draw(self):
        image = Image.open(self.filename)
        angle = 0
        count = 0
        t = True
        while t:
            tkimage = ImageTk.PhotoImage(image.rotate(angle))
            canvas_obj = self.canvas.create_image(
                250, 250, image=tkimage)
            self.master.after_idle(self.update)
            yield
            self.canvas.delete(canvas_obj)
            angle += 10
            angle %= 360
            count+= count
            if count is 20: count = False
            print(count)

root = tk.Tk()
app = SimpleApp(root, 'wcar.png')
root.mainloop()
#displayPlantImage = originalPlantImage.subsample(2, 2)
#frame.canvas.create_image(500, 500, anchor=CENTER, image=displayPlantImage)
#frame.frame_loop()