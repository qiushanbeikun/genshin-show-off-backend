import sys
import base64
from PIL import Image, ImageFont, ImageDraw
from io import BytesIO

# Takes first name and last name via command
# line arguments and then display them
# print("First name: " + sys.argv[1])
# print("Last name: " + sys.argv[2])


background = Image.open('./public/images/template_blank.png')
vice_font = ImageFont.truetype('./public/fonts/zh-cn.ttf', 30)
main_prop_font = ImageFont.truetype('./public/fonts/zh-cn.ttf', 28)
main_prop_rate_font = ImageFont.truetype('./public/fonts/zh-cn.ttf', 55)
title_font = ImageFont.truetype('./public/fonts/zh-cn.ttf', 43)


test_text = '中文字体测试，。 ENGLISH english 1234——+-=，。/；‘<>?:"/..'

# position = '时之沙'
# main_prop = '元素充能效率'
# main_prop_rate = '51.8%'
#
# vice_one = '暴击率+1433.1%'
# vice_two = '暴击伤害+22125.8%'
# vice_three = '攻击力+53332.4%'
# vice_four = '生命值+4113.5%'

title = '大氵逼的帖子'
position = '时之沙'
main_prop = '水贴效率'
main_prop_rate = '114.514%'

vice_one = '回复量+11.4%'
vice_two = '经验+5'
vice_three = '色图+14'
vice_four = '广告麦片数-5'

image = ImageDraw.Draw(background)
image.text((39, 13), title, (255, 255, 255), font=title_font)
image.text((37, 93), position, (255, 255, 255), font=main_prop_font)
image.text((39, 197), main_prop, (194, 175, 168), font=main_prop_font)
image.text((39, 230), main_prop_rate, (255, 255, 255), font=main_prop_rate_font)


image.text((68, 467), vice_one, (73, 82, 103), font=vice_font)
image.text((68, 516), vice_two, (73, 82, 103), font=vice_font)
image.text((68, 565), vice_three, (73, 82, 103), font=vice_font)
image.text((68, 615), vice_four, (73, 82, 103), font=vice_font)
# background.save('../output/test_image.png')

buffer = BytesIO()
background.save(buffer, format='PNG')
value = base64.b64encode(buffer.getvalue())

print(value)













