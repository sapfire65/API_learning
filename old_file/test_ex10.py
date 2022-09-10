import pytest

def test_ex10():
    print('Введите фразу менее 15 символов')
    phrase = input("Set a phrase: ")
    assert len(phrase) <= 15, print("введено более 15 символов!")
    print('спасибо')















