import requests
import sys
import os
import pygame

running = True
params = {
    'll': '28.333762,57.819387',
    'z': 17,
    'l': 'map'
}
url = f'https://static-maps.yandex.ru/1.x/'
map_file = "map.png"
pygame.init()
screen = pygame.display.set_mode((600, 450))


def find():
    response = requests.get(url=url, params=params)
    if not response:
        print("Ошибка выполнения запроса:")
        print(url)
        print("Http статус:", response.status_code, "(", response.reason, ")")
        sys.exit(1)
    with open(map_file, "wb") as file:
        file.write(response.content)
    screen.blit(pygame.image.load(map_file), (0, 0))
    pygame.display.flip()


find()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.K_PAGEUP:
            params['z'] = params['z'] + 1
            if params['z'] > 21:
                print('Больше нельзя отдалить')
                params['z'] = 21
            find()
        elif event.type == pygame.K_PAGEDOWN:
            params['z'] = params['z'] - 1
            if params['z'] < 0:
                print('Больше нельзя приблизить')
                params['z'] = 0
            find()
pygame.quit()
