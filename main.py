import requests
import sys
import os
import pygame

x = input()
y = input()
z = input()
url = f'https://static-maps.yandex.ru/1.x/?ll={x},{y}&z={z}&l=map'
response = requests.get(url)

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
