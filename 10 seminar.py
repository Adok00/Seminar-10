# В ячейке ниже представлен код, генерирующий DataFrame, который состоит всего из 1 столбца.
# Ваша задача перевести его в один горячий вид. Можете ли вы это сделать без get_dummies?

# импортировать  панд  как  pd
# импортировать  случайный

lst  = [ 'робот' ] *  10
lst  += [ 'человек' ] *  10
# случайный . перетасовать ( первый )
данные  =  пд . DataFrame ({ 'whoAmI' : lst })

данные . head ()   # Вывод первых 5 строк кадра даты

# Для перевода в один горячий вид без использования функции get_dummies() потребуется создать 2 дополнительные колонки, так как всего 2 значения человек и робот
данные . loc [ data [ 'whoAmI' ] ==  'robot' , 'robot' ] =  '1'   # Создание столбцов robot и заполение строки '1' при выполенении условий
данные . loc [ data [ 'whoAmI' ] ==  'human' , 'human' ] =  '1'   # Аналогично для колонок human (см. выше)
данные . loc [ data [ 'whoAmI' ] ==  'robot' , 'human' ] =  '0'   # Заполение строки '0' в колонке human при выполенении условий
данные . loc [ data [ 'whoAmI' ] ==  'human' , 'robot' ] =  '0'   # Аналогично для колонки robot (см. выше)

# Первый вариант один горячий вид
data [[ 'robot' , 'human' ]]   # Вывод столбцов robot и human (сформированных и заполненных выше)

# Второй вариант один горячий вид
данные . drop ( 'whoAmI' , axis  =  1 )   # drop() возвращает кадр данных удаленного без столбца, (axis = 1 для столбца, 0 - для строки)