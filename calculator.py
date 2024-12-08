TIPOS_ACEITOS = [int, float]

def verifica_tipo(val:object, tipos:list) -> None:
    """
    Verifica se val é de um dos tipos permitidos
    """
    if type(val) not in tipos:
        raise TypeError(f"{val} não é numérico")    

def soma(x:int|float, y:int|float, *args) -> int|float:
    """
    Soma dois ou mais números
    """
    verifica_tipo(x, TIPOS_ACEITOS)
    verifica_tipo(y, TIPOS_ACEITOS)
    resultado = x + y
    for i in args:
        verifica_tipo(i, TIPOS_ACEITOS)
        resultado += i
    return resultado

def subtrai(x:int|float, y:int|float) -> int|float:
    """
    Subtrai y de x, ambos devem ser números
    """
    verifica_tipo(x, TIPOS_ACEITOS)
    verifica_tipo(y, TIPOS_ACEITOS)
    return x - y

def multiplica(x:int|float, y:int|float, *args) -> int|float:
    """
    Multiplica dois ou mais números
    """
    verifica_tipo(x, TIPOS_ACEITOS)
    verifica_tipo(y, TIPOS_ACEITOS)
    resultado = x * y
    for i in args:
        verifica_tipo(i, TIPOS_ACEITOS)
        resultado *= i
    return resultado

def divide(x:int|float, y:int|float) -> int|float:
    """
    Divide x por y, ambos devem ser números
    """
    verifica_tipo(x, TIPOS_ACEITOS)
    verifica_tipo(y, TIPOS_ACEITOS)
    if y == 0:
        raise ZeroDivisionError(f"Esta tentando dividir {x} por zero")
    return x/y