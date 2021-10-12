# -*- coding: utf-8 -*-
"""
Created on Tue Oct 12 15:43:56 2021

@author: Roberto Rangel
"""
import requests
from bs4 import BeautifulSoup

def get_soup(url: str) -> BeautifulSoup:
    response = requests.get(url)
    return BeautifulSoup(response.content, "html.parser")

def wiki():
    soup = get_soup("https://www.sultanes.com.mx/roster")
    
    fo=open("Integrantes.txt",'w')
    #encontrar la posición de los integrantes
    posicion = soup.find_all("h4")
    #para encontrar los integrantes
    integrantes = soup.find_all("h6", class_="team-meta__name")
    
    #primera posición
    fo.write(posicion[0].getText())
    fo.write("\n")
    #jugadores de la primera pos
    for n in range(13):
        fo.write(integrantes[n].getText())
        fo.write("\n")
    fo.write("\n")
    #segunda posicion
    fo.write(posicion[1].getText())
    fo.write("\n")
    #jugadores de la segunda pos
    for n in range(13,17):
        fo.write(integrantes[n].getText())
        fo.write("\n")
    fo.write("\n")
    #tercera posicion
    fo.write(posicion[2].getText())
    fo.write("\n")
    #jugadores 3ra pos
    for n in range(17,25):
        fo.write(integrantes[n].getText())
        fo.write("\n")
    fo.write("\n")
    
    #cuarta posicion
    fo.write(posicion[3].getText())
    fo.write("\n")
    #jugadores 4ta pos
    for n in range(25,28):
        fo.write(integrantes[n].getText())
        fo.write("\n")
    fo.write("\n")
    #5ta posicion
    fo.write(posicion[4].getText())
    fo.write("\n")
    #jugadores 5ta pos
    for n in range(28,35):
        fo.write(integrantes[n].getText())
        fo.write("\n")
    fo.write("\n")
    fo.close()
    

wiki()