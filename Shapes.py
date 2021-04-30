from tkinter import *
import time

tk = Tk()

canvas = Canvas(tk, height=500, width = 500)
canvas.pack()

class Sq:
    def __init__(self, x, y, x2, y2, color, canvas):
        self.x,self.y,self.x2,self.y2,self.color,self.canvas = (x,y,x2,y2,color,canvas)
        self.id = self.canvas.create_rectangle(self.x, self.y, self.x2, self.y2, fill=self.color)
        self.canvas.update()

    def move(self, x, y):
        self.canvas.move(self.id, x, y)

    def delete(self):
        self.canvas.delete(self.id)

    def drag(self, x, y):
        px = self.canvas.coords(self.id)[0]
        py = self.canvas.coords(self.id)[1]
        while px != x or py != y:
            if x > px:
                self.canvas.move(self.id, 1, 0)
                time.sleep(0.01)
                self.canvas.update()
                px = self.canvas.coords(self.id)[0]
                py = self.canvas.coords(self.id)[1]
            else:
                self.canvas.move(self.id, -1, 0)
                time.sleep(0.01)
                self.canvas.update()
                px = self.canvas.coords(self.id)[0]
                py = self.canvas.coords(self.id)[1]
            if y > py:
                self.canvas.move(self.id, 0, 1)
                time.sleep(0.01)
                self.canvas.update()
                px = self.canvas.coords(self.id)[0]
                py = self.canvas.coords(self.id)[1]
            else:
                self.canvas.move(self.id, 0, -1)
                time.sleep(0.01)
                self.canvas.update()
                px = self.canvas.coords(self.id)[0]
                py = self.canvas.coords(self.id)[1]
                
        px = str(self.canvas.coords(self.id)[0])
        py = str(self.canvas.coords(self.id)[1])
        print("x = " + px + ", y = " + py)
            
            
