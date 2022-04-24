import sys
import base64
from PIL import Image, ImageFont, ImageDraw
from io import BytesIO
import json

config = json.loads(sys.argv[1])

background = Image.open('./public/images/all_empty_template.png').convert('RGBA')
vice_font = ImageFont.truetype('./public/fonts/zh-cn.ttf', 30)
main_prop_font = ImageFont.truetype('./public/fonts/zh-cn.ttf', 28)
main_prop_rate_font = ImageFont.truetype('./public/fonts/zh-cn.ttf', 55)
title_font = ImageFont.truetype('./public/fonts/zh-cn.ttf', 43)

image = ImageDraw.Draw(background)

image.text((39, 12), config['title'], (255, 255, 255), font=title_font)
image.text((37, 93), config['position'], (255, 255, 255), font=main_prop_font)
image.text((39, 197), config['main_prop'], (194, 175, 168), font=main_prop_font)
image.text((39, 230), config['main_prop_val'], (255, 255, 255), font=main_prop_rate_font)

image.text((68, 467), config['vice_prop1'], (73, 82, 103), font=vice_font)
image.text((68, 516), config['vice_prop2'], (73, 82, 103), font=vice_font)
image.text((68, 565), config['vice_prop3'], (73, 82, 103), font=vice_font)
image.text((68, 615), config['vice_prop4'], (73, 82, 103), font=vice_font)


image.text((39, 673), config['desc_title'], (122, 188, 122), font=vice_font)
image.text((68, 730), config['desc'], (73, 82, 103), font=vice_font)
image.text((39, 1035), config['owner'], (73, 82, 103), font=vice_font)

background.save('./output/test_image.png')

buffer = BytesIO()
background.save(buffer, format='PNG')
value = base64.b64encode(buffer.getvalue())

print(value)