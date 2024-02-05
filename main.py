import requests
import sys
import os
import pygame

running = True
types = ['map', 'sat', 'sat,skl']
ind = 0
params = {
    'll': '28.333762,57.819387',
    'z': 17,
    'l': types[ind]
}
url = f'https://static-maps.yandex.ru/1.x/'
map_file = "map.png"

x, y = map(float, params['ll'].split(','))
pygame.init()
screen = pygame.display.set_mode((600, 450))


def calc_step(z):
    return (1 - z / 21) * 4


def find(x, y):
    params['ll'] = f'{x},{y}'
    response = requests.get(url=url, params=params)
    if response.status_code == 200:
        with open(map_file, "wb") as file:
            file.write(response.content)
        screen.blit(pygame.image.load(map_file), (0, 0))
        pygame.display.flip()


find(x, y)

while running:
    for event in pygame.event.get():
        step = calc_step(params['z'])
        x, y = map(float, params['ll'].split(','))
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_PAGEUP:
            params['z'] = params['z'] + 1
            if params['z'] > 21:
                print('Больше нельзя приблизить')
                params['z'] = 21
            find(x, y)
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_PAGEDOWN:
            params['z'] = params['z'] - 1
            if params['z'] < 0:
                print('Больше нельзя отдалить')
                params['z'] = 0
            find(x, y)
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
            y += step if y + step <= 90 else 0
            find(x, y)
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
            y -= step if y - step >= -90 else 0
            find(x, y)
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
            x -= step if x - step >= -180 else x
            find(x, y)
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            x += step if x + step <= 180 else x
            find(x, y)
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_q:
            if ind + 1 > 2:
                ind = 0
            else:
                ind += 1
            find(x, y)
pygame.quit()
