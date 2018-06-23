#-*-coding:utf-8-*-
#0000，在邮箱右上角写个数字PIL库有问题，先跳过
from PIL import Image,ImageDraw,ImageFont

def add_num(img):
    draw = ImageDraw.Draw(img)
    myfont = ImageFont.truetype('C:/windows/fonts/Arial.ttf', size=40)
    fillcolor = "#ff0000"
    width, height = img.size
    draw.text((width - 40, 0), '99', font=myfont, fill=fillcolor)
    img.save('result.jpg', 'jpeg')
    return

if __name__ == '__main__':
    f = Image.open('20170915182250.jpg')
    add_num(f)

