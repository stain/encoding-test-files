#!/usr/bin/env python

import codecs

# 
tests = [
          u'premi\u00e8re is first',  # latin1, cp865
          u'\u041a\u0438\u0440\u0438\u043b\u043b\u0438\u0446\u0430 is Cyrillic', # koi8
          u'\U00010400 am Deseret'  # only in utf8/utf16
        ]

encodings = ["ascii", "utf8", "utf16", "cp865", "latin1", "koi8_r"]

for codec in encodings:
    f = codecs.open("%s.txt" % codec, "w", codec, "replace")
    f.write("\n".join(tests))
    f.write("\n")
    f.close()

