from PIL import Image

im = Image.open("monkey.jpg")
print(im.format, im.size, im.mode)
x = [0]
y = [0]
x.append(int(im.size[0] / 3))
x.append(int(im.size[0] * 2 / 3))
x.append(im.size[0])
y.append(int(im.size[1] / 3))
y.append(int(im.size[1] * 2 / 3))
y.append(im.size[1])
print(x, y)
for i in range(3):
    for j in range(3):
        box = (x[i], y[j], x[i+1], y[j+1])
        region = im.crop(box)
        name = "%s_%s.jpg" % (i, j)
        region.save(name, "JPEG")