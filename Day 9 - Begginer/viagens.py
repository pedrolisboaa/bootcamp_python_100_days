locais = [
    {
        'pais': 'Brasil',
        'dias': 15,
        'cidade': ['brasilia', 'são paulo', 'rio de janeiro']
    },
    {
        'pais': 'Portugal',
        'dias': 10,
        'cidade': ['porto', 'lisboa', 'cascais']
    },
]


def add_new_country(pais_visitado, dias_visitado, cidade_visitado):
    locais.append(
        {'pais': pais_visitado,
        'dias': dias_visitado,
        'cidade': cidade_visitado
         }
    )


add_new_country('EUA', 2, ['Nova york', 'florida', 'miami'])
print(locais)
