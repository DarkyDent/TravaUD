import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
fin = ['Левый мизинец', 'Левый безымянный', 'Левый средний', 'Левый указательный',
                'Левый большой','Правый указательный','Правый средний', 'Правый безымянный','Правый мизинец']
fin_s = ['Левый мизинец', 'Левый безымянный', 'Левый средний', 'Левый указательный','Правый указательный','Правый средний', 'Правый безымянный','Правый мизинец']
fin_lr = ['Левая рука','Правая рука']
bar_width = 0.2

def diogram(q, d, c, qp, dp,  a, scor, texts):
    index = np.arange(len(fin))
    indexs = np.arange(len(fin_s))
    indexlr = np.arange(len(fin_lr))
    plt.figure(figsize=(12, 10))
    
    # Первый график
    plt.subplot(2, 2, 1)
    plt.barh(index + bar_width, q, bar_width, label='ЙЦУКЕН', color='red')
    plt.barh(index, d, bar_width, label='Диктор', color='skyblue')
    plt.barh(index - bar_width, c, bar_width, label='Вызов', color='grey')
    #plt.barh(index - 2*bar_width, z, bar_width, label='Зубачев', color='plum')
    plt.barh(index - 2*bar_width, scor, bar_width, label='Скоропись', color='pink')
    sf = texts[0]
    for i in texts[1:]:
        sf += ', '
        sf += i
    plt.title('Сравнительные гистограммы альтернативных раскладок для ' + sf)
    plt.xlabel("Количество нажатий")
    plt.yticks(index + bar_width / 2, fin[::-1])
    for i in range(len(fin)):
        plt.text(q[i], i + bar_width, f'{(q[i] / a) * 100:.1f}%', ha = 'left', va='center', color='black')
        plt.text(d[i], i, f'{(d[i] / a) * 100:.1f}%', ha = 'left', va='center', color='black')
        plt.text(c[i], i - bar_width, f'{(c[i] / a) * 100:.1f}%', ha = 'left', va='center', color='black')
       #plt.text(z[i], i - 2*bar_width, f'{(z[i] / a) * 100:.1f}%', va='center', color='black')
        plt.text(scor[i], i - 2*bar_width, f'{(scor[i] / a) * 100:.1f}%',ha = 'left', va='center', color='black')
    plt.gca().xaxis.set_major_formatter(ticker.StrMethodFormatter('{x:,.0f}'))
    plt.legend()

    # Второй график
    plt.subplot(2, 2, 2)
    plt.barh(indexs + bar_width, qp, bar_width, label='ЙЦУКЕН', color='red')
    plt.barh(indexs, dp, bar_width, label='Диктор', color='skyblue')
    #plt.barh(indexs - bar_width, cp, bar_width, label='Вызов', color='grey')
    #plt.barh(indexs - 2*bar_width, zp, bar_width, label='Зубачев', color='plum')
    for i in range(len(fin_s)):
        plt.text(qp[i], i + bar_width, f'{(qp[i] / a) * 100:.1f}%', ha = 'left', va='center', color='black')
        plt.text(dp[i], i, f'{(dp[i] / a) * 100:.1f}%', ha = 'left',va='center', color='black')
        #plt.text(cp[i], i - bar_width, f'{(cp[i] / a) * 100:.1f}%', va='center', color='black')
        #plt.text(zp[i], i - 2*bar_width, f'{(zp[i] / a) * 100:.1f}%', va='center', color='black')
    plt.title('Штрафы')
    plt.xlabel("Количество нажатий")
    plt.yticks(indexs + bar_width / 2, fin_s[::-1])
    plt.gca().xaxis.set_major_formatter(ticker.StrMethodFormatter('{x:,.0f}'))
    plt.legend()
    """
    # Третий график
    #qd = [qdl,qdr]
    #dd = [ddl,ddr]
    #qdsum = sum(qd)
    #ddsum = sum(dd)
    #qhs = [qlhs,qrhs]
    #dhs = [dlhs,drhs]
    #qhssum = sum(qhs)
    #dhssum = sum(dhs)
    plt.subplot(2, 2, 3)
    plt.barh(indexlr + bar_width, qd, bar_width, label='Удоб. нажатия ЙЦУКЕН', color='red')
    plt.barh(indexlr, dd, bar_width, label='Удоб. нажатия Диктор', color='blue')
    plt.barh(indexlr - bar_width, dfin, bar_width, label='Кол-во сочетаний Диктор', color='pink')
    plt.barh(indexlr - 2*bar_width, qfin, bar_width, label='Кол-во сочетаний ЙЦУКЕН', color='green')
    #plt.barh(indexlr - bar_width, qhs, bar_width, label='Кол-во нажатий ЙЦУКЕН', color='pink')
    #plt.barh(indexlr - 2*bar_width, dhs, bar_width, label='Кол-во нажатий Диктор', color='green')
    for i in range(len(fin_lr)):
        plt.text(qd[i], i + bar_width, f'{qd[i]}', va='center', color='black')
        plt.text(dd[i], i, f'{dd[i]}', va='center', color='black')
        plt.text(dfin[i], i - bar_width, f'{dfin[i]}', ha = 'left', va='center', color='black')
        plt.text(qfin[i], i - 2*bar_width, f'{qfin[i]}', ha = 'left', va='center', color='black')
    plt.title('Диграммы')
    plt.xlabel('Количество нажатий')
    plt.yticks(indexlr + bar_width / 2, fin_lr)
    plt.gca().xaxis.set_major_formatter(ticker.StrMethodFormatter('{x:,.0f}'))
    plt.legend()
  
    # Четвертый график
    #qtsum = sum(qt)
    #dtsum = sum(dt)
    #qhs = [qlhs,qrhs]
    #dhs = [dlhs,drhs]
    plt.subplot(2, 2, 4)
    plt.barh(indexlr + bar_width, qt, bar_width, label='Удоб. нажатия 3г ЙЦУКЕН', color='red')
    plt.barh(indexlr, dt, bar_width, label='Удоб. нажатия 3г Диктор', color='blue')
    plt.barh(indexlr - bar_width,  qcdft, bar_width, label='Удоб. нажатия 2г ЙЦУКЕН', color='pink')
    plt.barh(indexlr - 2*bar_width, dcdft, bar_width, label='Удоб. нажатия 2г Диктор', color='green')
    #plt.barh(indexlr - 3*bar_width,  qfintr, bar_width, label='Кол-во сочетаний ЙЦУКЕН', color='plum')
    #plt.barh(indexlr - 4*bar_width, dfintr, bar_width, label='Кол-во сочетаний 2г Диктор', color='grey')
    for i in range(len(fin_lr)):
        plt.text(qt[i], i + bar_width, f'{qt[i]}', va='center', color='black')
        plt.text(dt[i], i, f'{dt[i]}', va='center', color='black')
        plt.text( qcdft[i], i - bar_width, f'{ qcdft[i]}', ha = 'left', va='center', color='black')
        plt.text( dcdft[i], i - 2*bar_width, f'{ dcdft[i]}', ha = 'left', va='center', color='black')
        #plt.text( qfintr[i], i - 3*bar_width, f'{ qfintr[i]}', ha = 'left', va='center', color='black')
        #plt.text( dfintr[i], i - 4*bar_width, f'{ dfintr[i]}', ha = 'left', va='center', color='black')
    plt.title('Триграммы и Диграммы')
    plt.xlabel('Количество нажатий')
    plt.yticks(indexlr + bar_width / 2, fin_lr)
    plt.gca().xaxis.set_major_formatter(ticker.StrMethodFormatter('{x:,.0f}'))
    plt.legend()
"""
    plt.tight_layout()
    plt.show()

def lr45(d_massiv_4, q_massiv_4, d_massiv_5, q_massiv_5):
    d_cdigsl_4 = d_massiv_4[4]  # уд. сочет лев рука диктор лр4
    d_cdigsr_4 = d_massiv_4[5]  # уд. сочет прав рука диктор лр4
    d_allcdigsl_4 = d_massiv_4[0]
    d_allcdigsr_4 = d_massiv_4[1]  # все сочет прав рука диктор лр4

    q_cdigsl_4 = q_massiv_4[4]  # уд. сочет лев рука qwerty лр4
    q_cdigsr_4 = q_massiv_4[5]  # уд. сочет прав рука qwerty лр4
    q_allcdigsl_4 = q_massiv_4[0]  # все сочет лев рука qwerty лр4
    q_allcdigsr_4 = q_massiv_4[1]  # все сочет прав рука qwerty лр4

    d_cdigsl_5 = d_massiv_5[4]  # уд. сочет лев рука диктор лр5 дигр
    d_cdigsr_5 = d_massiv_5[5]  # уд. сочет прав рука диктор лр5 дигр
    d_ctrigsl_5 = d_massiv_5[6]  # уд. сочет лев рука диктор лр5 тригр
    d_ctrigsr_5 = d_massiv_5[7]  # уд. сочет прав рука диктор лр5 тригр

    q_cdigsl_5 = d_massiv_5[4]  # уд. сочет лев рука qwerty лр5 дигр
    q_cdigsr_5 = d_massiv_5[5]  # уд. сочет прав рука qwerty лр5 дигр
    q_ctrigsl_5 = d_massiv_5[6]  # уд. сочет лев рука qwerty лр5 тригр
    q_ctrigsr_5 = d_massiv_5[7]  # уд. сочет прав рука qwerty лр5 тригр

    indexlr = np.arange(len(fin_lr))
    plt.figure(figsize=(12, 10))
    
    #LR4
    qd4 = [q_cdigsl_4,q_cdigsr_4]
    dd4 = [d_cdigsl_4,d_cdigsr_4]
    qdall4 = [q_allcdigsl_4,q_allcdigsr_4]
    ddall4 = [d_allcdigsl_4,d_allcdigsr_4]
    plt.subplot(2, 2, 1)
    plt.barh(indexlr + bar_width, qd4, bar_width, label='ЙЦУКЕН удоб. сочетания', color='red')
    plt.barh(indexlr, dd4, bar_width, label='Диктор удоб. сочетания', color='blue')
    plt.barh(indexlr - bar_width, qdall4, bar_width, label='ЙЦУКЕН кол-во сочетаний', color='red')
    plt.barh(indexlr - 2*bar_width, ddall4, bar_width, label='Диктор кол-во сочетаний', color='blue')
    for i in range(len(fin_lr)):
        plt.text(qd4[i], i + bar_width, f'{qd4[i]}', va='center', color='black')
        plt.text(dd4[i], i, f'{dd4[i]}', va='center', color='black')
        plt.text(qdall4[i], i - bar_width, f'{qdall4[i]}', ha = 'left', va='center', color='black')
        plt.text(ddall4[i], i - 2*bar_width, f'{ddall4[i]}', ha = 'left', va='center', color='black')
    plt.title('Диграммы')
    plt.xlabel('Количество нажатий')
    plt.yticks(indexlr + bar_width / 2, fin_lr)
    plt.gca().xaxis.set_major_formatter(ticker.StrMethodFormatter('{x:,.0f}'))
    plt.legend()   
    
    
    #LR5
    plt.subplot(2, 2, 2)
    qd5 = [q_cdigsl_5,q_cdigsr_5] 
    dd5 = [d_cdigsl_5,d_cdigsr_5]
    qt5 = [q_ctrigsl_5,q_ctrigsr_5]
    dt5 = [d_ctrigsl_5,d_ctrigsr_5]
    plt.barh(indexlr + bar_width, qt5, bar_width, label='ЙЦУКЕН 3 удоб. сочетания', color='red')
    plt.barh(indexlr, dt5, bar_width, label='Диктор 3 удоб. сочетания', color='blue')
    plt.barh(indexlr - bar_width,  qd5, bar_width, label='ЙЦУКЕН 2 удоб. сочетания', color='red')
    plt.barh(indexlr - 2*bar_width, dd5, bar_width, label='Диктор 2 удоб. сочетания', color='blue')
    for i in range(len(fin_lr)):
        plt.text(qt5[i], i + bar_width, f'{qt5[i]}', va='center', color='black')
        plt.text(dt5[i], i, f'{dt5[i]}', va='center', color='black')
        plt.text( qd5[i], i - bar_width, f'{ qd5[i]}', ha = 'left', va='center', color='black')
        plt.text( dd5[i], i - 2*bar_width, f'{ dd5[i]}', ha = 'left', va='center', color='black')
    plt.title('Триграммы и Диграммы')
    plt.xlabel('Количество нажатий')
    plt.yticks(indexlr + bar_width / 2, fin_lr)
    plt.gca().xaxis.set_major_formatter(ticker.StrMethodFormatter('{x:,.0f}'))
    plt.legend()

    plt.tight_layout()
    plt.show()