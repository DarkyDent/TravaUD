from Keyboard import Keyboard
from call import call
from diogram import diogram 
from scoropis import process_file, get_file_path, finger_scoropis

QWERTY = Keyboard('QWERTY', 'ё1йфя', '2цыч', '3увс', '4кам5епи', ' ', '7гоь6нрт', '8шлб', '9щдю', '0зж.-хэ=ъ\\',
                  'Ё!ЙФЯ', '\"ЦЫЧ', '№УВС', ';КАМ%ЕПИ', ':НРТ?ГОЬ', '*ШЛБ', '(ЩДЮ', ')ЗЖ,_ХЭ+Ъ/')
Diktor = Keyboard('Диктор', 'ё1цуф', '2ьиэ', '3яэх', '4,оы5.аю', '6злб7внм', '8ктп', '9дсг', '0чрж-шй=щ\\',
                  'ЁЪЦУФ', 'ЬЪИЭ', '№ЯЕХ', '%?ОЫ:!АЮ', ' ', ';ЗЛБ-ВНМ', '"КТП', '(ДСГ', ')ЧРЖ_ШЙ+Щ/')
Scoropis = Keyboard('Скоропись','*.цуф','ёьиэ','ъяех','?,оы!.аю',' ', '6злб-внм','\'ктп','(дсг',')чрж_шй"щ"','*1ЦУФ','ЁЬИЭ','ЪЯЭХ','4,ОЫ5.АЮ','6ЗЛБ-ВНМ','\'КТП','9ДСГ','0ЧРЖ-ШЙ=Щъ')


n = int(input("Сколько текстов обрабатываем?: "))
texts = []

if n > 0:

    for i in range(n):
        QWERTY.read()
        Diktor.text = QWERTY.text
        Scoropis.text = QWERTY.text
        texts.append(QWERTY.name.split('/')[-1])

        QWERTY.get_stat(True)
        Diktor.get_stat(True)
        Scoropis.get_stat(True)
        QWERTY.get_penalty()
        Diktor.get_penalty()
        Scoropis.get_penalty()
        #QWERTY.comfort_trigrams()
        #QWERTY.comfort_digrams()
        #Diktor.comfort_digrams()

    c = list(call().values())
    s=process_file(finger_scoropis,get_file_path(),1)#вывод кол-ва символов для скорописи в виде списка
    q = QWERTY.get_stat(False)
    d = Diktor.get_stat(False)
    scor = Scoropis.get_stat(False)
    qp = list(QWERTY.penalty.values())
    dp = list(Diktor.penalty.values())
    scorp = list(Scoropis.penalty.values())
    qd = QWERTY.comfort_digrams()
    dd = Diktor.comfort_digrams()
    qt = QWERTY.comfort_trigrams()
    dt = Diktor.comfort_trigrams()
    qcdft =QWERTY.comfort_digrams_fortree()
    dcdft =Diktor.comfort_digrams_fortree()
    """
    qdl = QWERTY.di_stats_l
    qdr = QWERTY.di_stats_r
    ddl = Diktor.di_stats_l
    ddr = Diktor.di_stats_r
    """
    a = sum(q)
    #qlhs = QWERTY.hands_stat()[0]
    #qrhs = QWERTY.hands_stat()[1]
   # dlhs = Diktor.hands_stat()[0]
    #drhs = Diktor.hands_stat()[1]
    diogram(q, d, c, qp, dp, qd, dd, qcdft,dcdft, a, scor, texts, qt, dt)
