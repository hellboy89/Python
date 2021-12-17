# Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.
import pygame

file = 'sweet.mp3'
pygame.init()
pygame.mixer.music.load(file)
pygame.mixer.music.play()
pygame.event.wait()

while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(10)
