from exos.exo11 import decode_message

def test_decode_message_hello():
    assert decode_message("72 101 108 108 111") == "Hello"

def test_decode_message_hello_wolrd():
    assert decode_message("72 101 108 108 111 32 87 111 114 108 100") == "Hello World"

def test_decode_message_hello_world_exclamation():
    assert decode_message("72 101 108 108 111 32 87 111 114 108 100 33") == "Hello World!"
