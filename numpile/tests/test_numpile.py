from numpile.numpile import autojit, engine


@autojit
def add(a, b):
    return a + b


def test_simple_example():
    r = add(2, 3)
    assert r == 5


def test_get_pointer():
    pointer = engine.get_pointer_to_function(add.llfunc)
    assert isinstance(pointer, int)
