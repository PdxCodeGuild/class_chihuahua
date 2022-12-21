import num_to_phrase_2;

def test_num_to_phrase_2():
    assert num_to_phrase_2.num_to_phrase(1) == "one"
    assert num_to_phrase_2.num_to_phrase(5) == "five"
    assert num_to_phrase_2.num_to_phrase(10) == "ten"
    assert num_to_phrase_2.num_to_phrase(11) == "eleven"
    assert num_to_phrase_2.num_to_phrase(15) == "fifteen"
    assert num_to_phrase_2.num_to_phrase(19) == "nineteen"
    assert num_to_phrase_2.num_to_phrase(55) == "fifty five"
    assert num_to_phrase_2.num_to_phrase(70) == "seventy"
    assert num_to_phrase_2.num_to_phrase(82) == "eighty two"
    assert num_to_phrase_2.num_to_phrase(99) == "ninety nine"
    assert num_to_phrase_2.num_to_phrase(100) == "one hundred"
    assert num_to_phrase_2.num_to_phrase(101) == "one hundred one"
    assert num_to_phrase_2.num_to_phrase(212) == "two hundred twelve"
    assert num_to_phrase_2.num_to_phrase(650) == "six hundred fifty"
    assert num_to_phrase_2.num_to_phrase(999) == "nine hundred ninety nine"