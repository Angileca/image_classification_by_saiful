import cv2
from keras.models import load_model
import numpy as np


model= load_model('write here h5 file path')

def test_img_value(number):
    num=int(number[0])
    if num==0:
        deg_nam='Saiful'
    elif num==1:
        deg_nam='Ashrafi'
    else:
        deg_nam='unknown'
    return deg_nam

def classfy(img):
    resize_img=cv2.resize(img, (70,70))
    pir_img=np.array(resize_img).reshape(-1,70,70,3)
    model_path = os.path.join(os.getcwd(), '#here load you model')
    model = load_model(model_path)
    value=model.predict_classes(pir_img)
    dis=test_img_value(value)
    return dis



