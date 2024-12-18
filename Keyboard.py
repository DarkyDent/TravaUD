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

    def get_stat(self, flag):  # считает количество нажатий для каждого пальца
        if flag:
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
            return list(self.stat.values()), list(self.STAT.values())  # вывод: два списка со статистикой,
            # без шифта и с
        else:
            q = list(self.stat.values())
            s = list(self.STAT.values())
            for i in range(4):
                q[i] += s[i]
            for i in range(4):
                q[i + 5] += s[i + 4]
            return q  # вывод: список с единой статистикой

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
        return list(self.penalty.values())  # вывод: список со штрафами (8 штук)

    def comfort_digrams(self):
        fins = self.fingers
        FINS = self.FINGERS
        di_stats_l=0
        di_stats_r=0
        prevf = self.r2
        contf = self.r2
        for i in self.text:
            for j in i:
                for k in fins[:5]:
                    if j in k:
                        prevf=contf
                        contf=k
                        if fins.index(prevf)<=fins.index(contf):
                            di_stats_l+=1
                            break
                for k in fins[5:]:
                    if j in k:
                        prevf=contf
                        contf=k
                        if fins.index(prevf)>=fins.index(contf):
                            di_stats_r+=1
                            break
        return di_stats_l,di_stats_r



"""
мысли на будущее: сбор статистики в реальном времени + время + бэкспас
"""
