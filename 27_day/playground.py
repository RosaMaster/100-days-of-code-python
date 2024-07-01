def add(*args):
    sum = 0
    soma = [(sum += n) for n in args]
    return soma

add(3, 5, 6)