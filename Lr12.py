from Keyboard import Keyboard, QWERTY, Diktor, Call, Scoropis, Zubachev
from diogram import lab12

QWERTY.read('voina-i-mir.txt')
Diktor.read('voina-i-mir.txt')
Scoropis.read('voina-i-mir.txt')
Call.read('voina-i-mir.txt')
Zubachev.read('voina-i-mir.txt')
a = sum(QWERTY.get_stat()[2])
q = list(QWERTY.stat.values()) #кол-во нажатий йцукен
d = Diktor.get_stat()[0] #кол-во нажатий диктор
scor = Scoropis.get_stat()[0] #кол-во нажатий скоропись
call = Call.get_stat()[0]
z = Zubachev.get_stat()[0]

lab12(q, d, a, scor, call, z)