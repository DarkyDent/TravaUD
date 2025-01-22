from Keyboard import Keyboard, QWERTY, Diktor, Call, Scoropis, Zubachev
from diogram import lab3

QWERTY.read('voina-i-mir.txt')
Diktor.read('voina-i-mir.txt')
Scoropis.read('voina-i-mir.txt')
Call.read('voina-i-mir.txt')
Zubachev.read('voina-i-mir.txt')

lab3(QWERTY.get_penalty(), Diktor.get_penalty(), Call.get_penalty(), Scoropis.get_penalty(), Zubachev.get_penalty())