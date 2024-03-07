def decode_message(encoded_message):
    return ''.join(chr(int(c)) for c in encoded_message.split())
