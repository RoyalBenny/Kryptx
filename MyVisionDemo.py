import os, io
from google.cloud import vision
from google.cloud.vision import types
import numpy as np
import pandas as pd

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'ServiceAccountToken.json'

client = vision.ImageAnnotatorClient()

image_name = 'abc.jpeg'
folder_path = r'D:\SiH-Frame-Project\MyVisionDemo\Images'

with io.open(os.path.join(folder_path, image_name), 'rb') as image_file:
    content = image_file.read()

image = types.Image(content=content)
# respose = client.text_detection(image=image)
# texts = respose.text_annotations
#
# df = pd.DataFrame(["locale", "description"])
# i=1
# for text in texts:
#     df = df.append(dict(
#         locale=i,
#         description=text.description
#     ), ignore_index=True)
#     i=i+1
# print(df)
features = client._get_all_features()