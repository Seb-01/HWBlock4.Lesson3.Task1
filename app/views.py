from django.shortcuts import render
# для работы с DictReader
from csv import DictReader

from collections import OrderedDict

from django.conf import settings


def convert_orderreddict_to_list_of_dict(order_dict: list):
    """
    order_dict: список из OrderedDict
    Вспомогательная функция для преобразования OrderedDict в список dict
    :return:
    """
    # список словарей - значений инфляции по месяцам года
    res_list=[]

    for next_row in order_dict:

        sub_res_list=[]
        # объекты OrderedDict являются списком кортежей, отображающих пары ключ-значение.
        # next_row - объект OrderedDict из одного кортежа ('key','value')
        # список ключей преобразем в кортеж из одного элемента, содержащего строку
        titles=tuple(next_row.keys())[0]
        # список значений преобразем в кортеж из одного элемента, содержащего строку
        values=tuple(next_row.values())[0]

        #разбиваем строки
        titles_list = titles.split(';')
        values_list = values.split(';')

        sub_dict=dict(zip(titles_list,values_list))
        res_list.append(sub_dict)

    return res_list

def inflation_view(request):
    template_name = 'inflation.html'
    data=[]

    # чтение csv-файла и заполнение контекста
    # файл в кодировке utf8
    with open(settings.INFLATION_CSV,encoding='utf8',newline='') as csvfile:
        od = list(DictReader(csvfile))
        data=convert_orderreddict_to_list_of_dict(od)
        total_row=len(data)

    titles=data[0].keys()
    #context = {}

    # return render_to_response('stats.html', context={
    #     'test_conversion': f'{test_rate:.1f}',
    #     'original_conversion': f'{original_rate:.1f}'


    return render(request, 'inflation.html', context = {
        'titles': titles,
        'inflation': data
    })