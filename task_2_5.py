
#import random - создание массива цен

#i = 0
#prices = []
#while i <= 19:
#    price = round(random.random() * 1000 / 10, 2)
#    prices.insert(i,price)
#    i += 1
#print(prices)

prices = [64.45, 4.6, 59.64, 7.16, 80.13, 49.64, 30.69, 54.52, 30.94, 64.74, 75.26, 34.46, 0.65, 19.0, 51.18, 2.73, 77.7, 49.75, 35.64, 67.07]
#эти цены я "зафиксировал" после отработки рандома
print(id(prices))

def sorting_prices():
    prices_print_list = []
    i = 0
    for price in prices:
        price_rub = price // 1
        price_rub = int(price_rub)
        cent = round(price - price_rub,2) * 100
        cent = int(cent)
        prices_print_list.append(f' {price_rub} руб. {cent:02d} коп.')
        prices_print = ', '.join(prices_print_list)
    return(prices_print)

def sorting_prices_ascend():
    prices_ascend = list(reversed(prices))
    prices_print_list = []
    i = 0
    for price in prices_ascend: #по хорошему весь этот блок я хотел как-то в одну функцию свернуть, так как смысл один и тот же, но знаний пока не хватило.
        price_rub = price // 1
        price_rub = int(price_rub)
        cent = round(price - price_rub,2) * 100
        cent = int(cent)
        prices_print_list.append(f' {price_rub} руб. {cent:02d} коп.')
        prices_print = ', '.join(prices_print_list)
    return(prices_print)

def sorting_prices_ascend_filter():
    prices_ascend = list(reversed(prices))
    prices_ascend = prices_ascend[4::-1] #по сути, именно эта часть возвращает список из пяти товаров, дальше уже приведение к одному формату
    prices_print_list = []
    i = 0
    for price in prices_ascend:
        price_rub = price // 1
        price_rub = int(price_rub)
        cent = round(price - price_rub,2) * 100
        cent = int(cent)
        prices_print_list.append(f' {price_rub} руб. {cent:02d} коп.')
        prices_print = ', '.join(prices_print_list)
    return(prices_print)

print("Список цен в читаемом виде: ",sorting_prices())
prices.sort()
print("Сортировка по возрастанию: ",sorting_prices())
print(id(prices))
print("Сортировка по убыванию: ", sorting_prices_ascend())
print("Цены пяти самых дорогих товаров: ", sorting_prices_ascend_filter())