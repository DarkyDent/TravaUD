import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
fin = ['Левый мизинец', 'Левый безымянный', 'Левый средний', 'Левый указательный',
                'Левый большой','Правый указательный','Правый средний', 'Правый безымянный','Правый мизинец']
fin_s = ['Левый мизинец', 'Левый безымянный', 'Левый средний', 'Левый указательный','Правый указательный','Правый средний', 'Правый безымянный','Правый мизинец']
fin_lr = ['Левая рука','Правая рука']
bar_width = 0.2

def diogram(q, d, c, qp, dp, qdl, qdr, ddl, ddr, qlhs, qrhs, dlhs, drhs, a):
    index = np.arange(len(fin))
    indexs = np.arange(len(fin_s))
    indexlr = np.arange(len(fin_lr))
    plt.figure(figsize=(10, 8))
    
    # Первый график
    plt.subplot(2, 2, 1)
    plt.barh(index + bar_width, q, bar_width, label='ЙЦУКЕН', color='red')
    plt.barh(index, d, bar_width, label='Диктор', color='skyblue')
    plt.barh(index - bar_width, c, bar_width, label='Вызов', color='grey')
    #plt.barh(index - 2*bar_width, z, bar_width, label='Зубачев', color='plum')
    plt.title('Сравнительные гистограммы альтернативных раскладок для текста')
    plt.xlabel("Количество нажатий")
    plt.yticks(index + bar_width / 2, fin[::-1])
    for i in range(len(fin)):
        plt.text(q[i], i + bar_width, f'{(q[i] / a) * 100:.1f}%', va='center', color='black')
        plt.text(d[i], i, f'{(d[i] / a) * 100:.1f}%', va='center', color='black')
        plt.text(c[i], i - bar_width, f'{(c[i] / a) * 100:.1f}%', va='center', color='black')
       # plt.text(z[i], i - 2*bar_width, f'{(z[i] / a) * 100:.1f}%', va='center', color='black')
    plt.gca().xaxis.set_major_formatter(ticker.StrMethodFormatter('{x:,.0f}'))
    plt.legend()

    # Второй график
    plt.subplot(2, 2, 2)
    plt.barh(indexs + bar_width, qp, bar_width, label='ЙЦУКЕН', color='red')
    plt.barh(indexs, dp, bar_width, label='Диктор', color='skyblue')
    #plt.barh(indexs - bar_width, cp, bar_width, label='Вызов', color='grey')
    #plt.barh(indexs - 2*bar_width, zp, bar_width, label='Зубачев', color='plum')
    for i in range(len(fin_s)):
        plt.text(qp[i], i + bar_width, f'{(qp[i] / a) * 100:.1f}%', va='center', color='black')
        plt.text(dp[i], i, f'{(dp[i] / a) * 100:.1f}%', va='center', color='black')
        #plt.text(cp[i], i - bar_width, f'{(cp[i] / a) * 100:.1f}%', va='center', color='black')
        #plt.text(zp[i], i - 2*bar_width, f'{(zp[i] / a) * 100:.1f}%', va='center', color='black')
    plt.title('Штрафы')
    plt.xlabel("Количество нажатий")
    plt.yticks(indexs + bar_width / 2, fin_s[::-1])
    plt.gca().xaxis.set_major_formatter(ticker.StrMethodFormatter('{x:,.0f}'))
    plt.legend()
    
    # Третий график
    qd = [qdl,qdr]
    dd = [ddl,ddr]
    qdsum = sum(qd)
    ddsum = sum(dd)
    plt.subplot(2, 2, 3)
    plt.barh(indexlr + bar_width, qd, bar_width, label='ЙЦУКЕН', color='red')
    plt.barh(indexlr, dd, bar_width, label='Диктор', color='skyblue')
    for i in range(len(fin_lr)):
        plt.text(qd[i], i + bar_width, f'{(qd[i] / qdsum) * 100:.1f}%', va='center', color='black')
        plt.text(dd[i], i, f'{(dd[i] / ddsum) * 100:.1f}%', va='center', color='black')
    plt.title('Диграммы')
    plt.xlabel('Количество нажатий')
    plt.yticks(indexlr + bar_width / 2, fin_lr[::-1])
    plt.gca().xaxis.set_major_formatter(ticker.StrMethodFormatter('{x:,.0f}'))
    plt.legend()
  
    
    # Четвертый график
    plt.subplot(2, 2, 4)
    qhs = [qlhs,qrhs]
    dhs = [dlhs,drhs]
    qhssum = sum(qhs)
    dhssum = sum(dhs)
    plt.barh(indexlr + bar_width, qhs, bar_width, label='ЙЦУКЕН', color='red')
    plt.barh(indexlr, dhs, bar_width, label='Диктор', color='skyblue')
    for i in range(len(fin_lr)):
        plt.text(qhs[i], i + bar_width, f'{(qhs[i] / qhssum) * 100:.1f}%', va='center', color='black')
        plt.text(dhs[i], i, f'{(dhs[i] / dhssum) * 100:.1f}%', va='center', color='black')
    plt.title('Нажатия по рукам')
    plt.xlabel('Количество нажатий')
    plt.yticks(indexlr + bar_width / 2, fin_lr[::-1])
    plt.gca().xaxis.set_major_formatter(ticker.StrMethodFormatter('{x:,.0f}'))
    plt.legend()
  
    plt.tight_layout()
    plt.show()