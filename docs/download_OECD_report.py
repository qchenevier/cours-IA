import io
import requests

from PIL import Image

#%% en français (pdf non structuré)
base_url = "https://asset.keepeek-cache.com/medias/domain21/_pdf/media4955/755926-pb4yl95li6/large/"
images = []

for i in range(181):
    print(i)
    image_data = requests.get(f"{base_url}/{i}.jpg").content
    image = Image.open(io.BytesIO(image_data)).convert('RGB')
    images.append(image)

filename = "./OECD - L'intelligence Artificielle dans la Société.pdf"
images[0].save(filename, save_all=True, append_images=images[1:])

#%% en anglais (pdf structuré)
url = "https://ec.europa.eu/jrc/communities/sites/jrccties/files/eedfee77-en.pdf"

filename = "./OECD - Artificial Intelligence in Society.pdf"
filedata = requests.get(url).content

open(filename, "wb").write(filedata)
