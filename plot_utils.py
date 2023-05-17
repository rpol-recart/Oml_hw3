import matplotlib.pyplot as plt 
import random


def two_col_plot(X, class0_idx, class1_idx):
    '''
    Функция рисует 10 графиков в 5 рядах и 2 столбца. На чётных графиках класс 1, на нечётных - класс 0. 
    Каждый график отображает случайный сэмпл из соответствующего класса.

    Параметры:
    X : numpy.ndarray
        Матрица признаков размера (n_samples, n_features)
    class0_idx : numpy.ndarray 
        Индексы сэмплов класса 0 
    class1_idx : numpy.ndarray 
        Индексы сэмплов класса 1 

    Возвращаемое значение:
    None
    '''

    fig, axes = plt.subplots(nrows=5, ncols=2, figsize=(12, 7))
    for i, ax in enumerate(axes.flat):
        if (i+1) % 2 == 0:
            n = random.choice(class1_idx)
        else:
            n = random.choice(class0_idx)

        ax.plot(X[n, :])

        if i == 0:
            ax.set_title(f'Класс 0')
        if i == 1:
            ax.set_title(f'Класс 1')
        ax.set_xlabel('Измерение')
        ax.set_ylabel('Значение ЭЭГ')

    plt.tight_layout()
    plt.show()