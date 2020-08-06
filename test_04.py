def solve04(str):
    str = str.replace('.','')
    dict = {}
    for index, word in enumerate(str.split(' ')):
        dict[word] = index + 1
    return dict

def test():
    assert solve04("Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can.") == {"Hi":1, "He":2, "Lied":3, "Because":4, "Boron":5, "Could":6, "Not":7, "Oxidize":8, "Fluorine":9, "New":10, "Nations":11, "Might":12, "Also":13, "Sign":14, "Peace":15, "Security":16, "Clause":17, "Arthur":18, "King":19, "Can":20}

