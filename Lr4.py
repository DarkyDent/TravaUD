from Keyboard import Keyboard, QWERTY, Diktor
from diogram import lab4

QWERTY.read('digrmas.txt')
Diktor.read('digrmas.txt')

lab4(Diktor.grams(), QWERTY.grams())