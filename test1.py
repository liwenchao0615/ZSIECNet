'''
Author       : WenChan Li
Date         : 2024-03-19 17:36:40
LastEditors  : WenChan Li
LastEditTime : 2024-03-19 17:36:46
Description  : 
Copyright 2024 OBKoro1, All Rights Reserved. 
2024-03-19 17:36:40
'''

from PIL import Image

# 打开图像文件
image = Image.open('input.jpg')

# 指定新的宽度和高度
new_width = 300
new_height = 200

# 调整图像尺寸
resized_image = image.resize((new_width, new_height))

# 保存调整后的图像
resized_image.save('output.jpg')

# 可选：显示调整后的图像
resized_image.show()
