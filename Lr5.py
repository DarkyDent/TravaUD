from Keyboard import Keyboard, QWERTY, Diktor
from diogram import lab5

QWERTY.read('1grams-3.txt')
Diktor.read('1grams-3.txt')

lab5(Diktor.grams(), QWERTY.grams())