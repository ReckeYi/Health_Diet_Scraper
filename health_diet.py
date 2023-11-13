import csv
import random
from time import sleep

import requests
from bs4 import BeautifulSoup
import json

url = 'https://health-diet.ru/table_calorie/?utm_source=leftMenu&utm_medium=table_calorie'

'''To show that you are not a bot'''
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
    'accept': '*/*'}

"""--------------RUN FIRST, ONCE AND COMMENT IT--------------"""
'''creates variable for GET method result'''
req = requests.get(url, headers=headers)

'''Saves received object to src variable and calls .text method'''
src = req.text

'''Saves received page to .html file'''
with open('index.html', 'w', encoding="utf8") as file:
    file.write(src)
print('Category page "index.html" was saved')
print('Now comment lines  17-27')


"""--------------RUN SECOND, ONCE AND COMMENT IT--------------"""
# '''Opens saved .html file and saves page code to variable src'''
# with open('index.html', encoding="utf8") as file:
#     src = file.read()
#
# '''Creating BS object with src variable and lxml parser'''
# soup = BeautifulSoup(src, 'lxml')
#
# '''Gets all links by class_'''
# all_products_hrefs = soup.find_all(class_='mzr-tc-group-item-href')
#
# '''Creates dictionary with category titles as keys and links as values'''
# all_categories_dict = {}
# for i in all_products_hrefs:
#     i_text = i.text
#     i_href = 'https://health-diet.ru' + i.get('href')
#
#     all_categories_dict[i_text] = i_href
#
# '''Saves dictionary with categories to .json file'''
# with open('all_categories_dict.json', 'w', encoding="utf8")  as file:
#     json.dump(all_categories_dict, file, indent=4, ensure_ascii=False)
#
# print('File "all_categories_dict.json" was created')
# print('Now comment lines  31-54')


"""--------------RUN THIRD, AS MANY TIMES AS YOU CAN, BUT ONCE IS ENOUGH--------------"""
# '''Creating a dictionary with categories'''
# with open('all_categories_dict.json', encoding="utf8") as file:
#     all_categories = json.load(file)
#
# '''Creates variable for total number of category pages'''
# iteration_count = int(len(all_categories)) - 1
# count = 0
# print(f'Total iterations: {iteration_count}')
#
#
# '''Cycle for visiting each category page and collecting all products data'''
# for category_name, category_href in all_categories.items():
#
#     '''Replaces all delimiters with underscore'''
#     rep = [",", " ", "-", "'", "__"]
#     for i in rep:
#         if i in category_name:
#             category_name = category_name.replace(i, '_')
#
#     '''Gets single category page'''
#     req = requests.get(url=category_href, headers=headers)
#     src = req.text
#
#     '''Saves single category page as .html file to /data '''
#     with open(f'data/{count}_{category_name}.html', 'w', encoding="utf8") as file:
#         file.write(src)
#
#     '''Opens single category .html file and saves it to variable'''
#     with open(f'data/{count}_{category_name}.html', encoding="utf8") as file:
#         src = file.read()
#
#     '''Creates BS object'''
#     soup = BeautifulSoup(src, 'lxml')
#
#     '''Handles possible errors'''
#     alert_block = soup.find(class_='uk-alert-danger')
#     if alert_block is not None:
#         continue
#
#     '''Collects table headings'''
#     table_head = soup.find(class_='mzr-tc-group-table').find('tr').find_all('th')
#     product = table_head[0].text
#     calories = table_head[1].text
#     proteins = table_head[2].text
#     fats = table_head[3].text
#     carbohydrates = table_head[4].text
#
#     '''Saves collected headings'''
#     with open(f'data/{count}_{category_name}.csv', 'w', encoding="utf8") as file:
#         writer = csv.writer(file)
#         writer.writerow(
#             (
#                 product,
#                 calories,
#                 proteins,
#                 fats,
#                 carbohydrates
#             )
#         )
#
#     '''Collects products data'''
#     product_data = soup.find(class_='mzr-tc-group-table').find('tbody').find_all('tr')
#
#     '''Getting all 'td' tags with required data from each 'tr' '''
#     product_info = []
#     for i in product_data:
#         product_tds = i.find_all('td')
#
#         title = product_tds[0].text
#         calories = product_tds[1].text
#         proteins = product_tds[2].text
#         fats = product_tds[3].text
#         carbohydrates = product_tds[4].text
#
#         '''Creates dictionary for .json files'''
#         product_info.append(
#             {
#                 'Title': title,
#                 'Calories': calories,
#                 'Proteins': proteins,
#                 'Fats': fats,
#                 'Carbohydrates': carbohydrates
#             }
#
#         )
#         '''Adds collected from 'td' tags data to .csv files'''
#         with open(f'data/{count}_{category_name}.csv', 'a', encoding="utf8") as file:
#             writer = csv.writer(file)
#             writer.writerow(
#                 (
#                     title,
#                     calories,
#                     proteins,
#                     fats,
#                     carbohydrates
#                 )
#             )
#
#     '''Adds product_info to .json files'''
#     with open(f'data/{count}_{category_name}.json', 'a', encoding="utf8") as file:
#         json.dump(product_info, file, indent=4, ensure_ascii=False)
#
#     count += 1
#     print(f'Iteration #{count}. {category_name} written down...')
#     iteration_count = iteration_count - 1
#
#     if iteration_count == 0:
#         print('Done')
#         break
#
#     print(f'Iterations left: {iteration_count}')
#     sleep(random.randrange(2, 4))
