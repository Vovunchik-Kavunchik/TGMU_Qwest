import cv2
from PIL import Image
while True:
    try:
        x=input ("введите название изображения ")
        im = Image.open("Images/"+x+".jpg")
        im.show()
        print(im.format, im.size, im.mode)
        break
    except Exception as e:
        print("Попробуй снова ошибка ", e)

while True:
    try:
        a = input("как редактируем изображение? Отзеркалить по горизонтали(1), инвертировать(2), черно-белое(3), спецэффект(4) ")
        if a == "1":
            pixels = list(im.getdata())
            w, h = im.size
            rows = [pixels[i * w: (i + 1) * w] for i in range(h)]
            flipped_rows = [row[::-1] for row in rows]
            new_pixels = [pix for row in flipped_rows for pix in row]
            new_img = Image.new(im.mode, (w, h))
            new_img.putdata(new_pixels)
            new_img.show()
            im = new_img
            break
        elif a == "2":
            r, g, b = im.split()
            im = Image.merge("RGB", (b, g, r))
            im.show()
            break
        elif a=="3":
            im = im.convert("L")
            im.show()
            break
        elif a=="4":
            im = im.point(lambda i: i * 5)
            im.show()
            break
        else:
            print("1,2,3 или 4!!!")
    except Exception as e:
        print("Попробуй снова ошибка ", e)
while True:
        #for x in range(0:im.size):
        y=input ('введи новое имя файла ')
        try:
            im.save("Images/red.img/" + y + ".jpg")
            break
        except Exception as d:
            print("Попробуй снова ошибка ", d)


