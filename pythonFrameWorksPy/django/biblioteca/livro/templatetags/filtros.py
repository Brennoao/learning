from django import template
from datetime import datetime

register = template.Library()

@register.filter
def mostra_duracao(value1, value2):
    if value1 and value2:
        return f"{(value1 - value2).days} Dias"
    else:
        return 'Livro emprestado'