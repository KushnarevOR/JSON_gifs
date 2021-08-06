from PIL import Image, ImageDraw, ImageTk
import tkinter as tk
import numpy as np
import json
import time

start_time = time.time()

print("Введите полное имя файла:")
path = input()

with open(path) as read_file:
    data = json.load(read_file)

all_images = []

for i in range(data['frames']):
    rgb = np.array(data["data"][i])
    r = np.reshape(rgb[:, 0], (data['height'], data['width']))
    g = np.reshape(rgb[:, 1], (data['height'], data['width']))
    b = np.reshape(rgb[:, 2], (data['height'], data['width']))

    rgb = np.dstack((r, g, b))
    image = Image.fromarray(rgb.astype(np.uint8))
    all_images.append(image)

#images = []
#for i in range(data['frames']):
#    images.append(imageio.imread('img{}.png'.format(i)))
#imageio.mimsave('movie.gif', images)

root = tk.Tk()

img = all_images[0]
imgTK = ImageTk.PhotoImage(image = img)
panel = tk.Label(root, image = imgTK)
panel.pack(side="bottom", fill="both", expand="yes")

def draw():
    while True:
        animation_start = time.time()
        for i in range(0, data['frames']):
            img = ImageTk.PhotoImage(image = all_images[i])
            panel.configure(image=img)
            panel.image = img
            time.sleep(0.05)
            root.update()
        T2 = time.time() - animation_start
        time.sleep(0.1)
        S = T1 + T2 - 0.03 * (data['frames'] - 1)
        print('time: {: .2f}'.format(S))

T1 = time.time() - start_time

draw()
root.mainloop()