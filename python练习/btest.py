# coding: utf-8
import os
import StringIO
import PIL
from PIL import Image, ImageFont, ImageDraw
import pygame

pygame.init()


def draw_text(msg, image, postion_x=0, postion_y=0, fonts=14, text_color=(0, 0, 0), bg_color=(255, 255, 255), between=-1, enter_len=600):
    """
    :param enter_len:换行长度
    :param msg: 需要绘制的文本
    :param image: 绘制的画纸
    :param postion_x: 绘制距离左边界宽度
    :param postion_y: 绘制距离上边界边界宽度
    :param fonts: 字体大小
    :param text_color: 字体颜色
    :param bg_color: 背景色
    :param between: 默认-1 左对齐，>0按照此宽度居中
    :return: 返回cursor位置
    """
    font = pygame.font.Font(os.path.join("/Users/wangjunfu/Desktop/git_test/python练习", "微软雅黑.ttf"), fonts)

    rtext = font.render(msg, True, text_color, bg_color)

    sio = StringIO.StringIO()
    pygame.image.save(rtext, sio)
    sio.seek(0)

    line = Image.open(sio)
    if between > 0:#居中
        lift = (between-line.size[0])/2
        if lift > 0:
            image.paste(line, (postion_x + lift, postion_y))
            return [postion_x+between, postion_y + line.size[1]]
    else:
        if line.size[0] > enter_len:
            # 字段过长，需要换行
            my_x = postion_x
            my_y = postion_y
            for i in msg:
                lis = draw_text(i, image, postion_x=my_x, postion_y=my_y, fonts=fonts, text_color=text_color, bg_color=bg_color, between=between)
                my_x = lis[0]
                if my_x >= enter_len:
                    my_x = postion_x
                    my_y = lis[1]+16
            return [my_x, lis[1]]
            pass
        image.paste(line, (postion_x, postion_y))
        return [postion_x+line.size[0], postion_y + line.size[1]]


res = {
    'vin_code': u'ASDIEOCKEI3758SKD',
    'brand_name': u'雷克萨斯',
    'family_name': u'雷克萨斯ES系',
    'vehicle_name': u'雷克萨斯 雷克萨斯ES系 三厢 3.0L 自动档  (LEXUS ES300)',
    'displacement': u'2.995',
    'year_pattern': u'',
    'gearbox_type': u'自动档',
    'engine_model': u'丰田1MZ-FE'

}
# im = Image.new("RGB", (300, 50), (255, 255, 255))
im = Image.open('./background.png')
# 绘制vin码
j = 0
for i in res['vin_code']:
    draw_text(u'哈', im, postion_x=12 + j * 36, postion_y=65, fonts=30, text_color=(236, 240, 245),bg_color=(236, 240, 245))
    draw_text(i, im, postion_x=12+j*36, postion_y=65, fonts=30, text_color=(215, 0, 15), bg_color=(236, 240, 245), between=30)
    j += 1
# 绘制其他字段
text = u'品牌：' + res['brand_name']
lis = draw_text(text, im, postion_x=14, postion_y=134, fonts=24)
text = u'车系：' + res['family_name']
lis = draw_text(text, im, postion_x=14, postion_y=lis[1]+8, fonts=24)
text = u'车型：' + res['vehicle_name']
lis = draw_text(text, im, postion_x=14, postion_y=lis[1]+8, fonts=24)
text = u'排量：' + res['displacement']
lis = draw_text(text, im, postion_x=14, postion_y=lis[1]+8, fonts=24)
text = u'年款：' + res['year_pattern']
lis = draw_text(text, im, postion_x=14, postion_y=lis[1]+8, fonts=24)
text = u'变速箱类型：' + res['gearbox_type']
lis = draw_text(text, im, postion_x=14, postion_y=lis[1]+8, fonts=24)
text = u'发动机型号：' + res['engine_model']
lis = draw_text(text, im, postion_x=14, postion_y=lis[1]+8, fonts=24)
im.show()
im.save("./result.png")
