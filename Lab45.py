from Keyboard import Keyboard
from diogram import lr45
import codecs

QWERTY = Keyboard('QWERTY', 'ё1йфя', '2цыч', '3увс', '4кам5епи', ' ', '7гоь6нрт', '8шлб', '9щдю', '0зж.-хэ=ъ\\',
                  'Ё!ЙФЯ', '\"ЦЫЧ', '№УВС', ';КАМ%ЕПИ', ':НРТ?ГОЬ', '*ШЛБ', '(ЩДЮ', ')ЗЖ,_ХЭ+Ъ/')
Diktor = Keyboard('Диктор', 'ё1цуф', '2ьиэ', '3яэх', '4,оы5.аю', '6злб7внм', '8ктп', '9дсг', '0чрж-шй=щ\\',
                  'ЁЪЦУФ', 'ЬЪИЭ', '№ЯЕХ', '%?ОЫ:!АЮ', ' ', ';ЗЛБ-ВНМ', '"КТП', '(ДСГ', ')ЧРЖ_ШЙ+Щ/')
Scoropis = Keyboard('Скоропись', '*.цуф', 'ёьиэ', 'ъяех', '?,оы!.аю', ' ', '6злб-внм', '\'ктп', '(дсг', ')чрж_шй"щ"',
                    '*1ЦУФ', 'ЁЬИЭ', 'ЪЯЭХ', '4,ОЫ5.АЮ', '6ЗЛБ-ВНМ', '\'КТП', '9ДСГ', '0ЧРЖ-ШЙ=Щъ')

QWERTY.read()
lr4f = QWERTY.text
QWERTY.read()
lr5f = QWERTY.text

q_massiv_4 = QWERTY.digrams(lr4f)
q_massiv_5 = QWERTY.digrams(lr5f)
d_massiv_4 = Diktor.digrams(lr4f)
d_massiv_5 = Diktor.digrams(lr5f)

lr45(d_massiv_4, q_massiv_4, d_massiv_5, q_massiv_5)
