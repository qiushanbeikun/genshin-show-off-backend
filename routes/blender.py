import sys
import base64
from PIL import Image, ImageFont, ImageDraw
from io import BytesIO
import json

# to run this file individually, run at the project root folder instead of ./routes

config = json.loads(sys.argv[1])

background = Image.open('./public/images/template_blank1.png').convert('RGBA')
vice_font = ImageFont.truetype('./public/fonts/zh-cn.ttf', 30)
main_prop_font = ImageFont.truetype('./public/fonts/zh-cn.ttf', 28)
main_prop_rate_font = ImageFont.truetype('./public/fonts/zh-cn.ttf', 55)
title_font = ImageFont.truetype('./public/fonts/zh-cn.ttf', 43)


title = config['title']
position = config['position']
main_prop = config['mainProp']
main_prop_rate = config['mainPropRate']
vice_one = config['viceOne']
vice_two = config['viceTwo']
vice_three = config['viceThree']
vice_four = config['viceFour']


match position:
    case '生之花': image_position =  'flower'
    case '死之羽': image_position = 'feather'
    case '时之沙': image_position = 'sand'
    case '空之杯': image_position = 'cup'
    case '理之冠': image_position = 'head'

temp = './public/images/artifacts/data/绝缘之旗印/' + image_position + '.png'

print(temp)

artifact_img = Image.open('./public/images/artifacts/data/绝缘之旗印/' + image_position + '.png').convert('RGBA')

arti_width, arti_height = artifact_img.size
artifact_img = artifact_img.resize((int(arti_width*1.15), int(arti_height*1.15)))


# title = 'whatever123'
#
# position = '时之沙'
# main_prop = '元素充能效率'
# main_prop_rate = '51.8%'
#
# vice_one = '暴击率+1433.1%'
# vice_two = '暴击伤害+22125.8%'
# vice_three = '攻击力+53332.4%'
# vice_four = '生命值+4113.5%'

# title = '大氵逼的帖子'
# position = '时之沙'
# main_prop = '水贴效率'
# main_prop_rate = '114.514%'
#
# vice_one = '回复量+11.4%'
# vice_two = '经验+5'
# vice_three = '色图+14'
# vice_four = '广告麦片数-5'
background.paste(artifact_img, (341, 73), artifact_img)
image = ImageDraw.Draw(background)

image.text((39, 12), title, (255, 255, 255), font=title_font)
image.text((37, 93), position, (255, 255, 255), font=main_prop_font)
image.text((39, 197), main_prop, (194, 175, 168), font=main_prop_font)
image.text((39, 230), main_prop_rate, (255, 255, 255), font=main_prop_rate_font)

image.text((68, 467), vice_one, (73, 82, 103), font=vice_font)
image.text((68, 516), vice_two, (73, 82, 103), font=vice_font)
image.text((68, 565), vice_three, (73, 82, 103), font=vice_font)
image.text((68, 615), vice_four, (73, 82, 103), font=vice_font)
background.save('./output/test_image.png')

buffer = BytesIO()
background.save(buffer, format='PNG')
value = base64.b64encode(buffer.getvalue())

print(value)
# sys.stdout.flush()
