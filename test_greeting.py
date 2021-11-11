import pytest

from hello_packaging import greeting


@pytest.mark.parametrize('argument, printed_value',
                         [(None, "Hello from a package!"),
                          ("person's name", "Hello to person's name from a package!"),
                          ])
def test_greeting(capsys, argument, printed_value):
    assert greeting(argument) is None
    assert printed_value in capsys.readouterr().out
