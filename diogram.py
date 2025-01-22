import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
fin = ['Левый мизинец', 'Левый безымянный', 'Левый средний', 'Левый указательный',
                'Левый большой','Правый указательный','Правый средний', 'Правый безымянный','Правый мизинец']
fin_s = ['Левый мизинец', 'Левый безымянный', 'Левый средний', 'Левый указательный','Правый указательный','Правый средний', 'Правый безымянный','Правый мизинец']
fin_lr = ['Левая рука','Правая рука']
bar_width = 0.15
index = np.arange(len(fin))
indexs = np.arange(len(fin_s))
indexlr = np.arange(len(fin_lr))

def lab12(q, d, a, scor, c, z):
    plt.barh(index + bar_width, q, bar_width, label='ЙЦУКЕН', color='red')
    plt.barh(index, d, bar_width, label='Диктор', color='skyblue')
    plt.barh(index - bar_width, c, bar_width, label='Вызов', color='grey')
    plt.barh(index - 2*bar_width, scor, bar_width, label='Скоропись', color='plum')
    plt.barh(index - 3*bar_width, z, bar_width, label='Зубачев', color='orange')
    plt.title('Сравнительные гистограммы альтернативных раскладок')
    plt.xlabel("Количество нажатий")
    plt.yticks(index + bar_width / 2, fin[::-1])
    for i in range(len(fin)):
        plt.text(q[i], i + bar_width, f'{(q[i] / a) * 100:.1f}%', ha = 'left', va='center', color='black')
        plt.text(d[i], i, f'{(d[i] / a) * 100:.1f}%', ha = 'left', va='center', color='black')
        plt.text(c[i], i - bar_width, f'{(c[i] / a) * 100:.1f}%', ha = 'left', va='center', color='black')
        plt.text(scor[i], i - 2*bar_width, f'{(scor[i] / a) * 100:.1f}%',ha = 'left', va='center', color='black')
        plt.text(z[i], i - 3*bar_width, f'{(z[i] / a) * 100:.1f}%', va='center', color='black')
    plt.gca().xaxis.set_major_formatter(ticker.StrMethodFormatter('{x:,.0f}'))
    plt.legend()
    plt.tight_layout()
    plt.show()


def lab3(qp, dp, cp, sp, zp):
    plt.figure(figsize=(10,5))
    plt.barh(indexs + bar_width, qp, bar_width, label='ЙЦУКЕН', color='red')
    plt.barh(indexs, dp, bar_width, label='Диктор', color='skyblue')
    plt.barh(indexs - bar_width, cp, bar_width, label='Вызов', color='grey')
    plt.barh(indexs - 2*bar_width, sp, bar_width, label='Скоропись', color='plum')
    #plt.barh(indexs - 3*bar_width, zp, bar_width, label='Зубачев', color='orange')
    for i in range(len(fin_s)):
        plt.text(qp[i], i + bar_width, f'{qp[i]}', va='center', color='black')
        plt.text(dp[i], i, f'{dp[i]}',va='center', color='black')
        plt.text(cp[i], i - bar_width, f'{(cp[i])}', ha = 'left', va='center', color='black')
        plt.text(sp[i], i - 2*bar_width, f'{(sp[i])}', va='center', color='black')
        #plt.text(zp[i], i - 3*bar_width, f'{(zp[i])}', va='center', color='black')
    plt.title('Штрафы')
    plt.xlabel("Количество нажатий")
    plt.yticks(indexs + bar_width / 2, fin_s)
    plt.gca().xaxis.set_major_formatter(ticker.StrMethodFormatter('{x:,.0f}'))
    plt.legend(title= 'ЙЦУКЕН всего штрафов: 2778937\n'+ 'Диктор всего штрафов: 1969311\n'+ 'Вызов всего штрафов: 2037175\n'+ 'Скоропись всего штрафов: 2238191', bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.tight_layout()
    plt.show()


def lab4(d_massiv_4, q_massiv_4):
    d_cdigsl_4 = d_massiv_4[4]  # уд. сочет лев рука диктор лр4 дигр
    d_cdigsr_4 = d_massiv_4[5]  # уд. сочет прав рука диктор лр4 дигр
    d_allcdigsl_4 = d_massiv_4[0] # все сочет лев рука диктор лр4 дигр 
    d_allcdigsr_4 = d_massiv_4[1]  # все сочет прав рука диктор лр4 дигр

    q_cdigsl_4 = q_massiv_4[4]  # уд. сочет лев рука qwerty лр4 дигр 
    q_cdigsr_4 = q_massiv_4[5]  # уд. сочет прав рука qwerty лр4 дигр 
    q_allcdigsl_4 = q_massiv_4[0]  # все сочет лев рука qwerty лр4 дигр 
    q_allcdigsr_4 = q_massiv_4[1]  # все сочет прав рука qwerty лр4 дигр

    qd4 = [len(q_cdigsl_4),len(q_cdigsr_4)] #уд. сочетания йцукен
    dd4 = [len(d_cdigsl_4),len(d_cdigsr_4)] #уд. сочетания диктор
    qdall4 = [len(q_allcdigsl_4)+len(q_cdigsl_4),len(q_allcdigsr_4)+len(q_cdigsr_4)] #все сочетания йцукен
    ddall4 = [len(d_allcdigsl_4)+len(d_cdigsl_4),len(d_allcdigsr_4)+len(d_cdigsr_4)] #все сочетания диктор
    plt.barh(indexlr + bar_width, qd4, bar_width, label='ЙЦУКЕН удоб. сочетания', color='red')
    plt.barh(indexlr, qdall4, bar_width, label='ЙЦУКЕН кол-во сочетаний', color='salmon')
    plt.barh(indexlr- bar_width, dd4, bar_width, label='Диктор удоб. сочетания', color='navy')
    plt.barh(indexlr - 2*bar_width, ddall4, bar_width, label='Диктор кол-во сочетаний', color='blue')
    for i in range(len(fin_lr)):
        plt.text(qd4[i], i + bar_width, f'{qd4[i]}', va='center', color='black')
        plt.text(qdall4[i], i, f'{qdall4[i]}', va='center', color='black')
        plt.text(dd4[i], i - bar_width, f'{dd4[i]}', va='center', color='black')
        plt.text(ddall4[i], i - 2*bar_width, f'{ddall4[i]}', va='center', color='black')
    plt.title('Диграммы')
    plt.xlabel('Количество диграмм')
    plt.yticks(indexlr + bar_width / 2, fin_lr)
    plt.gca().xaxis.set_major_formatter(ticker.StrMethodFormatter('{x:,.0f}'))
    plt.legend()
    plt.tight_layout()
    plt.show()
   

def lab5(d_massiv_5, q_massiv_5):
    q_cdigsl_5 = q_massiv_5[4]  # уд. сочет лев рука qwerty лр5 дигр
    q_cdigsr_5 = q_massiv_5[5]  # уд. сочет прав рука qwerty лр5 дигр
    d_cdigsl_5 = d_massiv_5[4]  # уд. сочет лев рука диктор лр5 дигр
    d_cdigsr_5 = d_massiv_5[5]  # уд. сочет прав рука диктор лр5 дигр
    
    q_allcdigsl_5 = q_massiv_5[0]  # все сочет лев рука qwerty лр5 дигр
    q_allcdigsr_5 = q_massiv_5[1]  # все сочет прав рука qwerty лр5 дигр
    d_allcdigsl_5 = d_massiv_5[0]  # все сочет лев рука диктор лр5 дигр
    d_allcdigsr_5 = d_massiv_5[1]  # все сочет прав рука диктор лр5 дигр

    qdall5 = [len(q_allcdigsl_5)+len(q_cdigsl_5), len(q_allcdigsr_5)+len(q_cdigsr_5)] #все сочетания йцукен дигр
    ddall5 = [len(d_allcdigsl_5)+len(d_cdigsl_5),len(d_allcdigsr_5)+len(d_cdigsr_5)] #все сочетания диктор дигр
    
    q_ctrigsl_5 = q_massiv_5[6]  # уд. сочет лев рука qwerty лр5 тригр
    q_ctrigsr_5 = q_massiv_5[7]  # уд. сочет прав рука qwerty лр5 тригр
    d_ctrigsl_5 = d_massiv_5[6]  # уд. сочет лев рука диктор лр5 тригр
    d_ctrigsr_5 = d_massiv_5[7]  # уд. сочет прав рука диктор лр5 тригр

    q_allctrigsl_5 = q_massiv_5[2]  # все сочет лев рука qwerty лр5 тригр
    q_allctrigsr_5 = q_massiv_5[3]  # все сочет прав рука qwerty лр5 тригр
    d_allctrigsl_5 = d_massiv_5[2]  # все сочет лев рука диктор лр5 тригр
    d_allctrigsr_5 = d_massiv_5[3]  # все сочет прав рука диктор лр5 тригр

    qtall5 = [len(q_allctrigsl_5)+len(q_ctrigsl_5),len(q_allctrigsr_5)+len(q_ctrigsr_5)] #все сочетания йцукен тригр
    dtall5 = [len(d_allctrigsl_5)+len(d_ctrigsl_5),len(d_allctrigsr_5)+len(d_ctrigsr_5)] #все сочетания диктор тригр
    
    qd5 = [len(q_cdigsl_5),len(q_cdigsr_5)] #уд. диграммы йцукен
    dd5 = [len(d_cdigsl_5),len(d_cdigsr_5)] #уд. диграммы диктор
    qt5 = [len(q_ctrigsl_5),len(q_ctrigsr_5)] #уд. триграммы йцукен
    dt5 = [len(d_ctrigsl_5),len(d_ctrigsr_5)] #уд. триграммы диктор
    plt.figure(figsize=(12, 10))
    #Диграммы
    plt.subplot(2, 2, 1)
    plt.barh(indexlr + bar_width, qd5, bar_width, label='ЙЦУКЕН удоб. сочетания', color='red')
    plt.barh(indexlr, qdall5, bar_width, label='ЙЦУКЕН кол-во сочетаний', color='salmon')
    plt.barh(indexlr - bar_width, dd5, bar_width, label='Диктор удоб. сочетания', color='navy')
    plt.barh(indexlr - 2*bar_width, ddall5, bar_width, label='Диктор кол-во сочетаний', color='blue')
    for i in range(len(fin_lr)):
        plt.text(qd5[i], i + bar_width, f'{qd5[i]}', va='center', color='black')
        plt.text(qdall5[i], i, f'{qdall5[i]}', va='center', color='black')
        plt.text(dd5[i], i - bar_width, f'{dd5[i]}', va='center', color='black')
        plt.text(ddall5[i], i - 2*bar_width, f'{ddall5[i]}', va='center', color='black')
    plt.title('Диграммы')
    plt.xlabel('Количество сочетаний')
    plt.yticks(indexlr + bar_width / 2, fin_lr)
    plt.gca().xaxis.set_major_formatter(ticker.StrMethodFormatter('{x:,.0f}'))
    plt.legend()
    
    #Триграммы
    plt.subplot(2, 2, 2)
    plt.barh(indexlr + bar_width, qt5, bar_width, label='ЙЦУКЕН удоб. сочетания', color='red')
    plt.barh(indexlr, qtall5, bar_width, label='ЙЦУКЕН кол-во сочетаний', color='salmon')
    plt.barh(indexlr- bar_width, dt5, bar_width, label='Диктор удоб. сочетания', color='navy')
    plt.barh(indexlr - 2*bar_width, dtall5, bar_width, label='Диктор кол-во сочетаний', color='blue')
    for i in range(len(fin_lr)):
        plt.text(qt5[i], i + bar_width, f'{qt5[i]}', va='center', color='black')
        plt.text(qtall5[i], i, f'{qtall5[i]}', va='center', color='black')
        plt.text(dt5[i], i - bar_width, f'{dt5[i]}', va='center', color='black')
        plt.text(dtall5[i], i - 2*bar_width, f'{dtall5[i]}', va='center', color='black')
    plt.title('Триграммы')
    plt.xlabel('Количество сочетаний')
    plt.yticks(indexlr + bar_width / 2, fin_lr)
    plt.gca().xaxis.set_major_formatter(ticker.StrMethodFormatter('{x:,.0f}'))
    plt.legend()
    plt.tight_layout()
    plt.show()