import os
from requests import get
URL = 'https://api.covid19api.com/summary'
response = get(URL).json()


Countries = response['Countries']


def key_function(Countries):
    return(Countries['NewConfirmed'])


class Covid_19:
    def get_sorted(self):
        Countries.sort(key=key_function, reverse=True)
        for item in Countries:
            print(item['Country'], item['NewConfirmed'], '\n')

    def info(self):
        for item in Countries:
            print(f'{item["Country"]}:\n\tNew Confirmed: {item["NewConfirmed"]}\n\tTotal Confirmed: {item["TotalConfirmed"]}\n\tNew Deaths: {item["NewDeaths"]}\n\tTotal Deaths: {item["TotalDeaths"]}\n\tNew Recovered: {item["NewRecovered"]}\n\tTotal Recovered: {item["TotalRecovered"]}\n')

    def single_info(self):
        find = False
        country = input("Введіть назву країни(ENG): ")

        for item in Countries:
            if item["Country"] == country.capitalize():
                print(f'{item["Country"]}:\n\tNew Confirmed: {item["NewConfirmed"]}\n\tTotal Confirmed: {item["TotalConfirmed"]}\n\tNew Deaths: {item["NewDeaths"]}\n\tTotal Deaths: {item["TotalDeaths"]}\n\tNew Recovered: {item["NewRecovered"]}\n\tTotal Recovered: {item["TotalRecovered"]}\n')
                find = True
                break
        if not find:
            print("Помилка! Невірне ім\'я.")


exit = False
while not exit:
    choise = int(input(
        "Виберіть дію:\n 1. Загальне інфо\n 2. Сортування по новим хворим\n 3. Інфо по країні\n 0. Exit\n: -->> "))
    covid = Covid_19()
    if choise == 1:
        covid.info()

    elif choise == 2:
        covid.get_sorted()

    elif choise == 3:
        covid.single_info()

    elif choise == 0:
        exit = True
        print("Допобачення!")
    else:
        print("Невірний вибір!")
