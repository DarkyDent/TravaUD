from tkinter.filedialog import askopenfilename


class Keyboard():
    def __init__(self, name, l1, l2, l3, l4, l5, r2, r3, r4, r5,
                 L1, L2, L3, L4, R2, R3, R4, R5):  # пальцы с левого мизина до правого + для заглавных букв

        self.name = name  # название раскладки для красивого вывода

        self.l1 = l1  # строка символов, нажимаемых этим пальцем, сверху вниз слева направо по клавиатуре
        self.l2 = l2
        self.l3 = l3
        self.l4 = l4
        self.l5 = l5
        self.r2 = r2
        self.r3 = r3
        self.r4 = r4
        self.r5 = r5

        self.L1 = L1  # строка символов, нажимаемых этим пальцем + shift
        self.L2 = L2
        self.L3 = L3
        self.L4 = L4
        self.R2 = R2
        self.R3 = R3
        self.R4 = R4
        self.R5 = R5

        self.fingers = [self.l1, self.l2, self.l3, self.l4, self.l5, self.r2, self.r3, self.r4, self.r5]
        self.FINGERS = [self.L1, self.L2, self.L3, self.L4, self.R2, self.R3, self.R4, self.R5]

        self.text = None

        self.stat = {self.l1: 0,  # статистика нажатий для всех пальцев, не считая энтер
                     self.l2: 0,
                     self.l3: 0,
                     self.l4: 0,
                     self.l5: 0,
                     self.r2: 0,
                     self.r3: 0,
                     self.r4: 0,
                     self.r5: 0,
                     }

        self.STAT = {self.L1: 0,  # строка символов, нажимаемых этим пальцем + shift
                     self.L2: 0,
                     self.L3: 0,
                     self.L4: 0,
                     self.R2: 0,
                     self.R3: 0,
                     self.R4: 0,
                     self.R5: 0
                     }

        self.penalty = {self.l1: 0,  # статистика штрафов для всех пальцев
                        self.l2: 0,
                        self.l3: 0,
                        self.l4: 0,

                        self.r2: 0,
                        self.r3: 0,
                        self.r4: 0,
                        self.r5: 0,
                        }

    def read(self):  # считывает текстовый файл в виде списка строк для дальнейшей работы
        f = open(askopenfilename(), 'r', encoding='utf-8')
        self.text = f.readlines()
        f.close()

    def read(self, filename):
        f = open(filename, "r", encoding="UTF-8")
        self.text = f.readlines()
        f.close()

    def get_stat(self):  # считает количество нажатий для каждого пальца
        fins = self.fingers  # символы без шифта
        FINS = self.FINGERS  # символы с нажатым шифтом

        for i in self.text:
            for j in i:
                for k in fins:  # для каждого пальца, если текущий символ есть в "его" строке, +1 в статистику
                    if j in k:
                        self.stat[k] += 1
                for k in FINS:  # аналогично, но для "шифтовых" символов отдельная статистика
                    if j in k:
                        self.STAT[k] += 1
                        if k in FINS[:4]:
                            self.stat[self.r5] += 1
                        else:
                            self.stat[self.l1] += 1

        q = list(self.stat.values())
        s = list(self.STAT.values())
        for i in range(4):
            q[i] += s[i]
        for i in range(4):
            q[i + 5] += s[i + 4]
        return list(self.stat.values()), s, q

    def hands_stat(self):
        lh = (sum(list(self.stat.values())[:5])
              + sum(list(self.STAT.values())[:4]))
        rh = (sum(list(self.stat.values())[5:])
              + sum(list(self.STAT.values())[4:]))
        return lh, rh

    def get_penalty(self):  # считает количество штрафов для каждого пальца
        """
        Принцип: при создании экземпляра keyboard записываем строкой клавиши, нажимаемые каждым
        пальцем, в определённом порядке - сверху вниз. Таким образом, всегда знаем, где какой символ
        на клавиатуре относительно домашней клавиши, независимо от раскладки. Штраф считается через
        разницу в индексах текущего символа и домашнего символа в строке пальца + поправка на шаг
        влево-вправо.
        """
        fins = self.fingers
        FINS = self.FINGERS

        for i in self.text:
            for j in i:
                for k in fins:
                    if j in k:
                        if k == self.l1:  # левый мизинец - один столбик клавиш + левый верхний угол
                            self.penalty[k] += abs(k.index(j) - 3)
                        elif k == self.l2 or k == self.l3 or k == self.r3 or k == self.r4:  # пальцы с 1 столбцом клавиш
                            self.penalty[k] += abs(k.index(j) - 2)
                        elif k == self.l4 or k == self.r2:  # пальцы с двумя столбиками клавиш, используем деление,
                            # чтобы учесть шаг в сторону от домашнего столбца
                            self.penalty[k] += abs(k.index(j) - 2 - 4 * (k.index(j) // 4)) + (k.index(j) // 4)
                        elif k == self.r5:  # правый мизинец: три столбца и ещё слэш
                            if k.index(j) < 4:
                                self.penalty[k] += abs(k.index(j) - 2)
                            elif k.index(j) < 7:
                                self.penalty[k] += abs(k.index(j) - 2 - 4) + 1
                            elif k.index(j) < 9:
                                self.penalty[k] += 5 - k.index(j) // 4
                            else:
                                self.penalty[k] += 4
                for k in FINS:  # всё то же самое
                    if j in k:
                        if k == self.L1:
                            self.penalty[self.l1] += abs(k.index(j) - 3)
                        elif k == self.L2:
                            self.penalty[self.l2] += abs(k.index(j) - 2)
                        elif k == self.L3:
                            self.penalty[self.l3] += abs(k.index(j) - 2)
                        elif k == self.R3:
                            self.penalty[self.r3] += abs(k.index(j) - 2)
                        elif k == self.R4:
                            self.penalty[self.r4] += abs(k.index(j) - 2)

                        elif k == self.L4:
                            self.penalty[self.l4] += abs(k.index(j) - 2 - 4 * (k.index(j) // 4)) + (k.index(j) // 4)
                        elif k == self.R2:
                            self.penalty[self.r2] += abs(k.index(j) - 2 - 4 * (k.index(j) // 4)) + (k.index(j) // 4)

                        elif k == self.R5:
                            if k.index(j) < 4:
                                self.penalty[self.r5] += abs(k.index(j) - 2)
                            elif k.index(j) < 7:
                                self.penalty[self.r5] += abs(k.index(j) - 2 - 4) + 1
                            elif k.index(j) < 9:
                                self.penalty[self.r5] += 5 - abs(k.index(j) // 4)
                            else:
                                self.penalty[self.r5] += 4
        print(self.name, " всего штрафов: ", sum(list(self.penalty.values())))
        return list(self.penalty.values())  # вывод: список со штрафами (8 штук)

    def grams(self):
        text = self.text
        fins = self.fingers
        FINS = self.FINGERS
        digs = []
        cdigsl = []
        cdigsr = []
        trigs = []
        ctrigsl = []
        ctrigsr = []

        digsl = []
        trigsl = []
        digsr = []
        trigsr = []
        for i in text:
            i = i.replace('\n', '')
            for j in range(len(i)-2):
                digs.append(i[j]+i[j+1])
                trigs.append(i[j]+i[j+1]+i[j+2])
            digs.append(i[-2:])

        for i in digs:
            f1 = None
            f2 = None
            if len(i) >= 2:
                for f in fins[:4]:
                    for F in FINS[:4]:
                        if i[0] in f:
                            f1 = fins.index(f)
                        elif i[0] in F:
                            f1 = FINS.index(F)
                        if i[1] in f:
                            f2 = fins.index(f)
                        elif i[1] in F:
                            f2 = FINS.index(F)
                if f1 is not None and f2 is not None:
                    if f1 < f2:
                        cdigsl.append(i)
                    elif f1 >= f2:
                        digsl.append(i)
                else:
                    f1 = None
                    f2 = None
                    for f in fins[5:]:
                        for F in FINS[4:]:
                            if i[0] in f:
                                f1 = fins.index(f)
                            elif i[0] in F:
                                f1 = FINS.index(F) + 1
                            if i[1] in f:
                                f2 = fins.index(f)
                            elif i[1] in F:
                                f2 = FINS.index(F) + 1
                    if f1 is not None and f2 is not None:
                        if f1 > f2:
                            cdigsr.append(i)
                        elif f1 <= f2:
                            digsr.append(i)
        for i in trigs:
            f1 = None
            f2 = None
            f3 = None
            for f in fins[:4]:
                for F in FINS[:4]:
                    if i[0] in f:
                        f1 = fins.index(f)
                    elif i[0] in F:
                        f1 = FINS.index(F)
                    if i[1] in f:
                        f2 = fins.index(f)
                    elif i[1] in F:
                        f2 = FINS.index(F)
                    if i[2] in f:
                        f3 = fins.index(f)
                    elif i[2] in F:
                        f3 = FINS.index(F)
            if f1 is not None and f2 is not None and f3 is not None:
                if f1 < f2 < f3:
                    ctrigsl.append(i)
                else:
                    trigsl.append(i)
            else:
                f1 = None
                f2 = None
                f3 = None
                for f in fins[5:]:
                    for F in FINS[4:]:
                        if i[0] in f:
                            f1 = fins.index(f)
                        elif i[0] in F:
                            f1 = FINS.index(F) + 1
                        if i[1] in f:
                            f2 = fins.index(f)
                        elif i[1] in F:
                            f2 = FINS.index(F) + 1
                        if i[2] in f:
                            f3 = fins.index(f)
                        elif i[2] in F:
                            f3 = FINS.index(F) + 1
                if f1 is not None and f2 is not None and f3 is not None:
                    if f1 > f2 > f3:
                        ctrigsr.append(i)
                    else:
                        trigsr.append(i)
        return [digsl, digsr, trigsl, trigsr, cdigsl, cdigsr, ctrigsl,
                ctrigsr]

QWERTY = Keyboard('QWERTY', 'ё1йфя', '2цыч', '3увс', '4кам5епи', ' ', '7гоь6нрт', '8шлб', '9щдю', '0зж.-хэ=ъ\\',
                  'Ё!ЙФЯ', '\"ЦЫЧ', '№УВС', ';КАМ%ЕПИ', ':НРТ?ГОЬ', '*ШЛБ', '(ЩДЮ', ')ЗЖ,_ХЭ+Ъ/')
Diktor = Keyboard('Диктор', 'ё1цуф', '2ьиэ', '3яэх', '4,оы5.аю', ' ', '6злб7внм', '8ктп', '9дсг', '0чрж-шй=щ\\',
                  'ЁЪЦУФ', 'ЬЪИЭ', '№ЯЕХ', '%?ОЫ:!АЮ', ';ЗЛБ-ВНМ', '"КТП', '(ДСГ', ')ЧРЖ_ШЙ+Щ/')
Scoropis = Keyboard('Скоропись','*.цуф','ёьиэ','ъяех','?,оы!.аю',' ', '6злб-внм','\'ктп','(дсг',')чрж_шй"щ"','*1ЦУФ','ЁЬИЭ','ЪЯЭХ','4,ОЫ5.АЮ','6ЗЛБ-ВНМ','\'КТП','9ДСГ','0ЧРЖ-ШЙ=Щъ')
Call = Keyboard('Вызов', 'юёвчш', '[ыих', '{оей', '}уак(ь,_', ' ', '=ё./*^нр', ')дтм', '+ясф', ']гбп!жзщцъ',
                 '~%ВЧШ', '7ЫИХ', '5ОЕЙ', '3УАК1<;-', '9Ё:?0ЛНР', '2ДТМ', '4ЯСФ', '6ГДП8ЖЗЩЦ\\')
Zubachev = Keyboard('ZUBACHEW', 'ё1фгш', '2ыиь', '3аею', '4яо.5,уэ', ' ', '6йлб7мтд', '8рсв', '9пнк', '0хзч_цж=щ\'', 'Ё!ФГШ', '"ЫИЪ', '№АЕЮ', ';ЯОЬ%ЪУЭ', ':ЙЛБ?МТД', '*РСВ', '(ПНК', ')ХЗЧ-ЦЖ+Щ/')