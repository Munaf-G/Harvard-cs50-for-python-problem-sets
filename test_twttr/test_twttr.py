from twttr import shorten

def main():

    test_upper_lower_cases()
    test_numbers()
    test_punctuation()

def test_upper_lower_cases():

    assert shorten('hello') == 'hll'
    assert shorten('HELLO')  == 'HLL'
    assert shorten('hello, WORLD')  == 'hll, WRLD'

def test_numbers():
    assert shorten('1234') == '1234'
def test_punctuation():
    assert shorten(',._-') == ',._-'

if __name__ == "__main__":
    main()
