# -*- coding: utf-8 -*-
from janome.tokenizer import Tokenizer
t = Tokenizer()

document = u'これはテストデータです'
tokens = t.tokenize(document)
for token in tokens:
    print(token.surface)