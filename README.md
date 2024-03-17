# Объяснение работы алгоритмов:
##*1* Search_for_a_substring:

Этот код выполняет поиск подстроки needle в строке haystack методом "brute force". Давайте разберем его шаг за шагом:

1. Разберем значения переменных:
needle = "qwer"
haystack = "sdf qwer"
needle - искомая подстрока, haystack - место поиска подстроки (куча сена)

2. for i in range(len(haystack) - len(needle) + 1):

    В данном случае создаётся цикл для диапазона поиска, с помощью операции range(len(haystack) - len(needle) + 1),
    мы сократили количество применения цикла, тоесть расмотрим на уже указанных значениях переменных needle (4 символа) и haystack (8 символов), заметим если из 8 - 4 + 1, то получется 5, это индекс до которого ведется поиск, тоесть это максимально возможное положения подстроки

3. success = True
    
    Это можно назвать флагом, суть которого можете понять по его названию "успешность"

4. for j in range(len(needle)):

    Вложенный цикл суть которого заключен в том, что пока этот цикл не выполнится полностью, мы не пройдем в цикл объявленный ранее, тоесть это объявление вложенного цикла

5. if needle[j] != haystack[i + j]: 
            success = False 
            break 
    
    Проверка на соответсвие, если != то success = False

6. if success: 
        index = i 
        break
    
    Условие каторое срабатывает по окончанию циклов, тоесть за счет предъыдущей операции мы получили значение для флага, за счет чего понимаем была ли обнаружена подстрока, если да, то получаем ответ в виде индекса откуда начинается подстрока

7. else:
    index = -1

    Срабатывает если значение success = False, тоесть условие ранее не сработало, получаем -1, что значит отсутсвие подстроки