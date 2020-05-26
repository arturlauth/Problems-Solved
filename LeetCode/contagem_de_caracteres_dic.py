def contar_caracteres(s):
    """ Função que conta os caracteres de uma string

    Ex:

    >>> contar_caracteres('artur')

    {'a': 1, 'r': 2, 't': 1, 'u': 1}


    :param s: string a ser contada
    :return:
    """
    dict = {}

    for caracter in s:
        dict[caracter] = dict.get(caracter, 0) + 1

    return dict

if __name__ == '__main__':
    print(contar_caracteres('renzo'))
    print(contar_caracteres('artur'))
