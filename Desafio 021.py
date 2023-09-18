#Faça um programa que leia um arquivo mp3


import pygame
pygame.init()
pygame.mixer.music.load('AD_time.mp3')
pygame.mixer.music.play()
pygame.event.wait()