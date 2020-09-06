import random
import tkinter as tk
from PIL import Image, ImageTk
from bs4 import BeautifulSoup
import requests

food_names = ["カレー", "餃子", "ハンバーガー", "海鮮丼", "唐揚げ", "キムチ鍋", "肉じゃが", 
              "パスタ", "ラーメン", "サラダ", "チャーハン", "焼肉"]

file_photo = [
    "/Users/yamanakakouhei/Desktop/food/menu/curry.jpg",
    "/Users/yamanakakouhei/Desktop/food/menu/gyouza.jpg",
    "/Users/yamanakakouhei/Desktop/food/menu/hamburger.jpg",
    "/Users/yamanakakouhei/Desktop/food/menu/kaisenndonn.jpg",
    "/Users/yamanakakouhei/Desktop/food/menu/karaage.jpg",
    "/Users/yamanakakouhei/Desktop/food/menu/nabe.jpg",
    "/Users/yamanakakouhei/Desktop/food/menu/nikujaga.jpg",
    "/Users/yamanakakouhei/Desktop/food/menu/pasta.jpg",
    "/Users/yamanakakouhei/Desktop/food/menu/rahmen.jpg",
    "/Users/yamanakakouhei/Desktop/food/menu/sarada.jpg",
    "/Users/yamanakakouhei/Desktop/food/menu/tyahann.jpg",
    "/Users/yamanakakouhei/Desktop/food/menu/yakiniku.jpg"
]

def screenletter():
    randomResult = random.choice(food_names)
    label.configure(text = randomResult, font = ("", 50))
    button.configure(text = "お腹いっぱい", font = ("", 30), command = title)
    canvas.itemconfig(canvasImage, image = filelist[food_names.index(randomResult)])

def title():
    label.configure(text = "お腹すいたな〜", font = ("", 50))
    button.configure(text = "メニュー", font = ("", 30), command = screenletter)
    canvas.itemconfig(canvasImage, image = cooking)

screen = tk.Tk()
screen.title("料理")
screen.geometry("800x800")

canvas = tk.Canvas(bg = "white", width = 800, height = 800)
canvas.place(x = 0, y = 0)

button = tk.Button(text = "メニュー", font = ("", 30), command = screenletter) 
button.pack(fill = "none", pady = 30, side = "bottom")
button.pack()

label = tk.Label(text = "お腹すいたな〜", font = ("", 50))
label.pack(fill = "none", side = "bottom")
label.pack()


def openresize(sozai):
    food_img = Image.open(sozai)
    menu_img = ImageTk.PhotoImage(food_img.resize(size = (780, 600)))
    return menu_img

cooking = openresize("/Users/yamanakakouhei/Desktop/food/cooking.jpg")
canvasImage = canvas.create_image(10, 0, image = cooking, anchor = tk.NW)

filelist = []

for name in file_photo:
    obj = openresize(name)
    filelist.append(obj)

screen.mainloop()