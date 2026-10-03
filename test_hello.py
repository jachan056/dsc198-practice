from hello import call

def test_call():
    assert call("name") == "name"

test_call()