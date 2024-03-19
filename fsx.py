'''
Author       : WenChan Li
Date         : 2024-03-19 18:56:50
LastEditors  : WenChan Li
LastEditTime : 2024-03-19 18:56:56
Description  : 
Copyright 2024 OBKoro1, All Rights Reserved. 
2024-03-19 18:56:50
'''
def preprocess_image(image):
    transform = transforms.Compose([
        transforms.Resize((512, 512)),
        transforms.ToTensor(),
    ])

    image_tensor = transform(image)
    image_tensor = image_tensor.unsqueeze(0)
    return image_tensor
