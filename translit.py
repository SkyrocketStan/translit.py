"""
Заменяет буквы русского алфавита буквами английского алфавита по правилам, установленным приказом
Федеральной миграционной службы от 26 марта 2014 г. N 211 "Об утверждении Административного
регламента предоставления Федеральной миграционной службой государственной услуги по оформлению и
выдаче паспортов гражданина Российской Федерации, удостоверяющих личность гражданина Российской
Федерации за пределами территории Российской Федерации, содержащих электронный носитель информации".
(Приложение N 6)

Таблица транслитерации имени и фамилии для загранпаспорта
а - a
б - b
в - v
г - g
д - d
е - e
ё - e
ж - zh
з - z
и - i
й - i
к - k
л - l
м - m
н - n
о - o
п - p
р - r
с - s
т - t
у - u
ф - f
х - kh
ц - ts
ч - ch
ш - sh
щ - shch
ы - y
ъ - ie
э - e
ю - yu
я - ya

От себя: Добавлен мягкий знак, так как его изначально не было.
"""

TRANSLIT_DICTONARY = {
    "а" : "a", "б" : "b", "в" : "v", "г" : "g", "д" : "d", "е" : "e", "ё" : "e",
    "ж" : "zh", "з" : "z", "и" : "i", "й" : "i", "к" : "k", "л" : "l", "м" : "m",
    "н" : "n", "о" : "o", "п" : "p", "р" : "r", "с" : "s", "т" : "t", "у" : "u",
    "ф" : "f", "х" : "kh", "ц" : "ts", "ч" : "ch", "ш" : "sh", "щ" : "shch",
    "ы" : "y", "ъ" : "", "э" : "e", "ю" : "yu", "я" : "ya", "ь" : ""}

def translit(string):
    """Gets str translit it and returns str"""
    for key in TRANSLIT_DICTONARY:
        string = string.lower().replace(key, TRANSLIT_DICTONARY[key])
    return string
