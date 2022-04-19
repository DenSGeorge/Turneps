import numpy as np
def min_predict(number: int = 1) -> int:

    min = 1
    max = 101
    number = np.random.randint(min, max)

    count = 0

    while True:
        count+=1
  
        mid = round((min+max) / 2)
        if mid > number:
            max = mid
    
        elif mid < number:
            min = mid
        else:
            # print(f"Компьютер угадал число за {count} попыток. Это число {number}")
            return count
            break #конец игры выход из цикла
    
# print(f'Количество попыток: {min_predict()}')

def score_game(min_predict) -> int:
  
    count_ls = [] # список для сохранения количества попыток
    np.random.seed(1) # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000)) # загадали список чисел

    for number in random_array:
        count_ls.append(min_predict(number))

        score = int(np.mean(count_ls)) # находим среднее количество попыток

        print(f'Ваш алгоритм угадывает число в среднем за: {score} попыток')    
        return(score)
    
# RUN
if __name__ == '__main__':
    score_game(min_predict)

