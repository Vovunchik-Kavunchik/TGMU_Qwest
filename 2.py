import cv2
from PIL import Image
while True:
    try:
        x=input ("введите название изображения")
        im = Image.open("Images/"+x+".jpg")
        im.show()
        break
    except Exception as e:
        print("Попробуй снова ошибка ", e)
while True:
        #for x in range(0:im.size):
        y=input ('введи новое имя файла')
        try:
            im.save("Images/" + y + ".jpg")
            im.show()
            break
        except Exception as d:
            print("Попробуй снова ошибка ", d)


