# from keras.applications.resnet50 import ResNet50
from keras.applications.xception import Xception
from keras.preprocessing import image
from keras.applications.xception import preprocess_input, decode_predictions
from keras.utils.vis_utils import plot_model
import numpy as np
# import matplotlib.pyplot as plt

# model = ResNet50(weights='imagenet')
model = Xception()
print(model.summary())
# plot_model(model, to_file='xception.png')
model = Xception(weights='imagenet')
img_path = 'elephant.jpg'
# img_path = 'parrot.jpg'
img = image.load_img(img_path, target_size=(299, 299))
x = image.img_to_array(img)
# plt.imshow(x / 255.)
# plt.show()
x = np.expand_dims(x, axis=0)
x = preprocess_input(x)

preds = model.predict(x)
# decode the results into a list of tuples (class, description, probability)
# (one such list for each sample in the batch)
print('Predicted:', decode_predictions(preds, top=8)[0])
# img.show()
for pred in decode_predictions(preds, top=8)[0]:
    print(pred)
