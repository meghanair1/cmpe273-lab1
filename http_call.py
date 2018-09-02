import requests
import time


for x in range(3):
    response = requests.get('https://webhook.site/#/f8394573-d4cf-4d0e-92d2-72471d6df362/b0498fcd-9ed3-47be-8914-3e7c9566f938/0')
    print(response.headers.get('Date'))
    time.sleep(1)
