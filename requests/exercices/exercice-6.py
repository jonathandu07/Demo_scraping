import requests

img_url = "https://cdn.prod.website-files.com/5fe9ad4805bc9a4cf17e4a6a/60c745e5b87da1fae06a99ca_pont-darc_ardeche.jpg"

img_data = requests.get(img_url).content


with open("img_ardeche.jpg", "wb") as file:
    file.write(img_data)