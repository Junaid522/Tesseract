import favicon
import requests

headers = {'User-agent': 'Mozilla/5.0'}

# def write_image_file(i, index):
def write_image_file():
    url = 'https://www.gallaudetathletics.com/landing/index'
    icons = favicon.get(url)
    print(icons)
    for n, i in enumerate(icons):
        response = requests.get(i.url, stream=True, headers=headers)
        print(response.status_code)
        if response.status_code != 200 or i.url.endswith('.com/') or i.url.endswith('.com') or i.url.endswith('.edu/') \
                or i.url.endswith('.edu'):
            continue
        name = i.url.split('/')[-1]
        if name.__contains__('?'):
            name = name.split('?')[0]
        print(name)
        with open('junaid_new/{}_{}.{}'.format('346', '346', name), 'wb') as image:
            for chunk in response.iter_content(1024):
                image.write(chunk)
        break


write_image_file()