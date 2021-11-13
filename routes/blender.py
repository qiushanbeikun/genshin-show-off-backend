import sys
import base64
from PIL import Image, ImageFont, ImageDraw
from io import BytesIO

# Takes first name and last name via command
# line arguments and then display them
# print("First name: " + sys.argv[1])
# print("Last name: " + sys.argv[2])


background = Image.open('./public/images/erased_template.png')
font = ImageFont.truetype('./public/fonts/zh-cn.ttf', 40)

test_text = '中文字体测试，。 ENGLISH english 1234——+-=，。/；‘<>?:"/..'

image = ImageDraw.Draw(background)
image.text((100, 100), test_text, (255, 255, 255), font=font)
# background.save('../output/test_image.png')

buffer = BytesIO()
background.save(buffer, format='PNG')
value = base64.b64encode(buffer.getvalue())

print(value)













