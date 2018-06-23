#-*- coding:UTF-8 -*-
from PIL import Image

ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")
text = ''
size = len(ascii_char)

im = Image.open('pic1.jpg')
print im.size()
im = im.convert('L')
(width,height) = im.size
im = im.resize((int(width * 0.2),int(height * 0.2)))
im = im.rotate(90)
for i in range(im.size[0]):
    for j in range(im.size[1]):
        grad = im.getpixel((i,j))
        num = int((size * grad) / 256.0)#灰度/256 = num/字符个数（70） 求得num = 字符个数*灰度/256
        text = text + ascii_char[num]
    text = text + '\n'

with open('result.txt','w') as f:
    f.write(text)