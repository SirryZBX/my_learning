# -*- coding: UTF-8 -*-
# envo1 python3.9
"""
@Author:大王
@File:city_functions.py
@CreateTime:2022/4/18 20:30
"""


def get_city_country(city, country, population=''):
    if population:
        city_info = f"{city}, {country}-population={population}"
        return city_info.title()
    else:
        city_info = f"{city}, {country}"
        return city_info.title()


if __name__ == '__main__':
    while True:
        your_city = input("Your city name is: ")
        if your_city == 'q':
            break
        your_country = input("Your country name is: ")
        if your_country == 'q':
            break
        city_centre = get_city_country(your_city, your_country)
        print(f"\tYour city centre is {city_centre}")

