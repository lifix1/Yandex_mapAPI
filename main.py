import requests
import sys
import os
import pygame

running = True
params = {
    'll': '28.333762,57.819387',
    'z': '17',
    'l': 'map'
}
url = f'https://static-maps.yandex.ru/1.x/'
response = requests.get(url=url, params=params)

if not response:
    print("Ошибка выполнения запроса:")
    print(url)
    print("Http статус:", response.status_code, "(", response.reason, ")")
    sys.exit(1)
map_file = "map.png"
with open(map_file, "wb") as file:
    file.write(response.content)
pygame.init()
screen = pygame.display.set_mode((600, 450))
screen.blit(pygame.image.load(map_file), (0, 0))
pygame.display.flip()
while pygame.event.wait().type != pygame.QUIT:
    pass
pygame.quit()
os.remove(map_file)

