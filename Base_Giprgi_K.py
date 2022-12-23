from math import modf

def reverse_dictionary(dic):
    k = [key for key in dic.keys()]
    v = [value for value in dic.values()]
    rev = {}
    for i, new_key in enumerate(v):
        rev[new_key] = k[i]
    return rev

chiffres = {
    0: '0',
    1: '1',
    2: '2',
    3: '3',
    4: '4',
    5: '5',
    6: '6',
    7: '7',
    8: '8',
    9: '9',
    10: 'a',
    11: 'b',
    12: 'c',
    13: 'd',
    14: 'e',
    15: 'f',
}

base_suffix = {
    2: '0b',
    16: '0x',
}

chiffres_rev = reverse_dictionary(chiffres)

def int_base(num, base):
    """Retuns a string of num in base 'baze' """
    restes = ''
    while True:
        r, num = num % base, num // base
        R = chiffres[r]
        restes = str(R) + restes
        if not num:
            break
    restes = base_suffix[base] + restes
    return restes

# La précision est la puissance négative de la base 
# maximale éloignant le résultat de la réalité
def fractionnal_to_base(num, base=2, precision=None):
    """Same but for floats strictly inferior to 1"""
    restes = ''
    while True:
        num *= base
        partie_entiere = modf(num)[1]
        if num >= 1:
            restes += chiffres[partie_entiere]
            num -= partie_entiere
        else:
            restes += '0'
        if num == 0 and precision == None:
            break
        elif precision != None:
            if num < base ** (-precision):
                break
    if len(restes) == 0:
        restes = '0'
    restes = '0.' + restes
    return restes

def base_10_to_n(num, base, precision=None):
    whole = int_base(num=modf(num)[1], base=base)
    fractional = fractionnal_to_base(num=num - modf(num)[1], base=base, precision=precision)
    return whole + ',' + fractional[2:]

# Testing
truthy = [(hex(i) == int_base(i, 16)) for i in range(1000)]
print(truthy.count(False))   # False si le test réussit
def verify_2(string):
    """Prend la chaine littérale de num en base 2 et renvoie 
    le nombre équivalent en base 10"""
    l = [int(i) for i in string[2:]]
    num = 0
    for i, value in enumerate(l):
        num += int(value) * (2 ** (-i - 1))
    return num

f = fractionnal_to_base
truthy = [verify_2(f(i / 1000)) == (i / 1000) for i in range(1000)]
print(truthy.count(False))

def verify_16(string):
    """Prend la chaine littérale de num en base 16 et renvoie
     le nombre équivalent en base 10"""
    l = [chiffres_rev[i] for i in string[2:]]
    num = 0
    for i, value in enumerate(l):
        num += chiffres_rev[chiffres[value]] * (16 ** (-i - 1))
    return num

truthy = [[round(verify_16(f(i / 1000, base=16, precision=8)), 4) == i / 1000 for i in range(1000)]]
print(truthy.count(False))   # Si tout marche bien imprime 0

print(int_base(num=500, base=2))
print(base_10_to_n(num=500.25, base=2))
print(base_10_to_n(num=500.45, base=16, precision=5))
print(int_base(num=500, base=16))
