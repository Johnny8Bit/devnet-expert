from program import one, two, three


def test_one():

    test = one()

    assert test == 13


def test_two():

    test = two(3, 3)

    assert test == 9


def test_three():

    test = three()

    assert test["band_6ghz"]["clients"]
