import pytest
from project import get_answers, get_words, is_valid_word


def main():
    test_get_answers()
    test_get_words()
    test_is_valid_word()

def test_get_answers():
    with open("answers.txt") as answers:
        answers_ = [line for line in answers]
    assert get_answers() == answers_

def test_get_words():
    with open("five-letter-words.txt") as words:
        words_ = [line.strip() for line in words]
    assert get_words() == words_

def test_is_valid_word():
    assert is_valid_word("apple", ["banana","orange"]) == False
    assert is_valid_word("apple", ["banana","orange","apple"]) == True
    assert is_valid_word("Mamour", ["David","Jack","Eliot"]) == False
    assert is_valid_word(None, [True, False, None]) == True



if __name__ == "__main__":
    main()











if __name__ == "__main__":
    main()
