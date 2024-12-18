from Keyboard import Keyboard
from call import call
from diogram import diogram 

QWERTY = Keyboard('QWERTY', 'ё1йфя', '2цыч', '3увс', '4кам5епи', ' ', '7гоь6нрт', '8шлб', '9щдю', '0зж.-хэ=ъ\\',
                  'Ё!ЙФЯ', '\"ЦЫЧ', '№УВС', ';КАМ%ЕПИ', ':НРТ?ГОЬ', '*ШЛБ', '(ЩДЮ', ')ЗЖ,_ХЭ+Ъ/')
Diktor = Keyboard('Диктор', 'ё1цуф', '2ьиэ', '3яэх', '4,оы5.аю', '6злб7внм', '8ктп', '9дсг', '0чрж-шй=щ\\',
                  'ЁЪЦУФ', 'ЬЪИЭ', '№ЯЕХ', '%?ОЫ:!АЮ', ' ', ';ЗЛБ-ВНМ', '"КТП', '(ДСГ', ')ЧРЖ_ШЙ+Щ/')


n = int(input("Сколько текстов обрабатываем?: "))

for i in range(n):
    QWERTY.read()
    Diktor.text = QWERTY.text

    QWERTY.get_stat(True)
    Diktor.get_stat(True)
    QWERTY.get_penalty()
    Diktor.get_penalty()
    QWERTY.comfort_digrams()
    Diktor.comfort_digrams()

c = list(call().values())

q = QWERTY.get_stat(False)
d = Diktor.get_stat(False)
qp = list(QWERTY.penalty.values())
dp = list(Diktor.penalty.values())

qdl, qdr = QWERTY.comfort_digrams()
ddl, ddr = Diktor.comfort_digrams()
a = sum(q)
qlhs = QWERTY.hands_stat()[0]
qrhs = QWERTY.hands_stat()[1]
dlhs = Diktor.hands_stat()[0]
drhs = Diktor.hands_stat()[1]
diogram(q, d, c, qp, dp, qdl, qdr, ddl, ddr, qlhs, qrhs, dlhs, drhs,a)