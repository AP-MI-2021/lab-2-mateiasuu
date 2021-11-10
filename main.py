def is_superprime(n):
    """
    functia returneaza true daca n este superprim, false in caz contrar
    :return: true or false
    """
    while n > 0:
        for d in range(2, n // 2 + 1):
            if n % d == 0:
                return False
        n = n // 10
    return True


def test_is_superprime():
    """testam functia 'is_superpime' """
    assert is_superprime(237) == False
    assert is_superprime(233) == True
    assert is_superprime(12) == False
    assert is_superprime(113) == True



def get_largest_prime_below(n):
    #returneaza cel mai mare numar prim mai mic decat un numar dat
    cel_mai_mare_div_prim = 0
    for d in range(2,n):
        nrdiv = 0
        for i in range(2,d//2):
            if d % i == 0:
                nrdiv = nrdiv + 1
        if nrdiv == 0:
            cel_mai_mare_div_prim = d
    return cel_mai_mare_div_prim

def test_get_largest_prime_below():
    assert get_largest_prime_below(15) == 13
    assert get_largest_prime_below(25) == 23



def is_palindrome(n):
    inv = 0  # inversul lui n
    x = n  # copie a lui n
    while n:
        inv = inv * 10 + n % 10
        n //= 10
    return inv == x  # returneaza 1 daca n e palindrom sau 0 in caz contrar


def test_is_palindrome():
    assert is_palindrome(121) == True
    assert is_palindrome(12) == False
    assert is_palindrome(11) == True



def main():
    test_is_superprime()
    test_get_largest_prime_below()
    test_is_palindrome()
    while True:
        print("1.verifica daca un nr dat este superprim")
        print("2.calculam cel mai mare numar prim mai mic decat numarul nostru")
        print("3.verifica daca un nr dat este palindrom")
        print("4.iesire")


        optiune = input("alegeti o optiune:")

        if optiune == "1":
            numar1 = int(input("introduceti numar:"))
            print(is_superprime(numar1))
        elif optiune == "2":
            numar2 = int(input("introduceti numar: "))
            print(get_largest_prime_below(numar2))
        elif optiune == "3":
            numar3= int(input("introduceti numar:"))
            print(is_palindrome(numar3))
        elif optiune == "4":
            break

        else:
            print("optiune gresita")


main()