from bank import value

def main():
    test_value1()
    test_value2()
    test_value3()


def test_value1():
    assert value("hello") == 0
    assert value("HELLO") == 0
    assert value("hello") == 0

def test_value2():
    assert value("hi") == 20
    assert value("halakah") == 20
    assert value("HIlo") == 20

def test_value3():
    assert value("cs50") == 100
    assert value("50") == 100
    assert value("what the hell?") == 100

if __name__ == "__main__":
    main()
