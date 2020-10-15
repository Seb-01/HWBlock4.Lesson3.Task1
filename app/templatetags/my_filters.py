from django.template import library

register = library.Library()

@register.filter
def get_float(value: str):
    """
    Преобразует строку в число сплавающей точкой
    :param value:
    :return:
    """
    return float(value)

#register.filter('get_float',get_float)