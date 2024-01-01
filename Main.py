import json
from Encoder import encode
from Decoder import decode

vocab = json.loads(open("vocab.json", "r").read())

y = encode("Why are you like this", vocab)
print(y)
print(decode(y, vocab))
