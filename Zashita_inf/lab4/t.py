from PIL import Image
import numpy as np
import torch
from einops import repeat
import torchvision.transforms as T

inter_prompts = {
     0: ["stormy sky with sunbeams breaking through", '/content/drive/MyDrive/AI/art1.png'],
    50: ["sky with sun", '/content/drive/MyDrive/AI/art2.png'],
    100: ["dark sky",'/content/drive/MyDrive/AI/art3.png'],
    150: ["stormy sky",'/content/drive/MyDrive/AI/art4.png'],
}


animation_prompts = {
    0: "stormy sky with sunbeams breaking through",
    50: "sky with sun",
    100: "dark sky",
    150: "stormy sky",
    }

print(inter_prompts[0][1])
print(list(animation_prompts.items())[0][0])


W, H = map(lambda x: x - x % 64, (512, 512))
shape = (W, H)
path = 'C:/Users/Олеся/3 course/Zashita_inf/lab4/art1.png'
image = Image.open(path)
image = image.resize(shape, resample=Image.LANCZOS)
image = np.array(image).astype(np.float16) / 255.0
image = image[None].transpose(0, 3, 1, 2)
image = torch.from_numpy(image)
image = 2. * image - 1.
torch.reshape(image, (1, 77, 768))
print(image.shape)

