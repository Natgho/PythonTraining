# -*- coding: utf-8 -*-
#!/usr/bin/python
import sys
ver_2_text = 'Kullandığınız Python sürümü python 3 den küçük ' \
             'olduğundan program doğru çalışmayabilir. Kullandığınız versiyon:'
ver_3_text = 'Programa hoşgeldiniz, python versiyonunuz:'

try:
    vers = sys.version_info.major
    if sys.version_info.major < 3:
        print(ver_2_text, vers)
    else:
        print(ver_3_text, vers)
except AttributeError:
    print(ver_2_text)
