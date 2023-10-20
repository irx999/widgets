
import requests
import os
import re
import time
from concurrent.futures import ThreadPoolExecutor
 
 
class Get_img:
    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'
        }
        self.folder = "壁纸下载/"
        self.path = f"{os.path.split(os.path.realpath(__file__ ))[0]}/{self.folder}"
 
    def get_img_from_url(self, number):
        try:
            #global url
            real_url = url + str(number)
            print(real_url)
            response = requests.get(real_url, headers=self.headers, timeout=500)
            if response.status_code == 200:
                img_url = re.findall(r'data-wallpaper-id="(.*?)"', response.text)
                print(img_url)
                for i in img_url:
                    img_res = 'https://wallhaven.cc/w/' + i
                    response = requests.get(img_res, headers=self.headers, timeout=500)
                    if response.status_code == 200:
                        image_url = re.findall(r'id="wallpaper" src="(.*?)"', response.text)[0]
                        print(image_url)
                        img_response = requests.get(image_url, headers=self.headers, timeout=500)
                        img_name = image_url.split('/')[-1]
                        if not os.path.exists(self.path):
                            os.mkdir(self.path)
                        with open(self.path + img_name, 'wb') as f:
                            f.write(img_response.content)
                            print(img_name + '图片下载成功')
                            time.sleep(1)
                    else:
                        print('图片访问失败' + image_url)
            else:
                print('网页访问失败')
        except Exception as e:
            print(e)    
 
 
if __name__ == '__main__':
    url = 'https://wallhaven.cc/hot?page='
    # get_img = Get_img()
    # executor = ThreadPoolExecutor(max_workers=5)
    # for i in executor.map(get_img.get_img_from_url, range(1, 10)):
    #     print(i)
    for i in range(5,10):
        Get_img().get_img_from_url(i)
        time.sleep(1)
        print('第{}下载完成'.format(i))