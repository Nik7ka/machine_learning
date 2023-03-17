import requests

params = {'img_url': 'https://www.allaboutbirds.org/news/wp-content/uploads/2020/07/STanager-Shapiro-ML.jpg'}
resp = requests.post('http://localhost:5228/detect', json=params)

print(resp.text)