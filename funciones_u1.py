# -*- coding: utf-8 -*-
"""Funciones U1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Mx_Jgk2Va1Yp0ZicWdjCkvbKvUfPb_s0

## Funciones de códigos
Alumno y No. de Control: Brandon Erick Alvarado Mejia No.: 2021690025
Docente: Jessica Sarahí Méndez Rincón
Materia: Cómputo en la Nube
Carrera: Ingeniería en Inteligencia Artificial
Grupo: 07-IIA-01
Lugar y fecha de entrega: San Buenaventura, Coahuila a 25 de Septiembre del
2023.
"""

#Brandon Erick Alvarado Mejia
import math
import random

def primo(n):
  if n <= 1:
    return False
  elif n <= 3:
    return True
  elif n%2==0 or n%3==0:
    return False
  i=5
  while i*i <= n:
    if n%i==0 or n%(i+2)==0:
      return False
    i+=6
  return True

def s_primo(n):
  siguiente = n + 1
  while True:
    if primo(siguiente):
      return siguiente
    siguiente += 1

def mediana(n1,n2,n3):
  return sorted([n1,n2,n3])[1]

def contrasena_ran():
  longitud = random.randint(7, 10)
  contrasena = ""
  for i in range(longitud):
      caracter = chr(random.randint(33, 126))
      contrasena += caracter
  return contrasena

def hipotenusa(lado1, lado2):
  hipotenusa = math.sqrt(lado1**2 + lado2**2)
  return hipotenusa