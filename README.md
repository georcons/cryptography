# Криптография

Задача 2.
-----------------------
```
  736
```
Виж /images/problem2.jpeg

Задача 3.
------------------------
Виж /images/problem3.jpeg

Задача 4.
------------------------
```
KEY: QIKLOP
TEXT: QPYANRVBSJNRUVJDETGESTUREGCJXTC

KEY: DKWKNS
TEXT: DNMBOOIDEIMUHTXEFQTGESTUREQKYQP

KEY: AXYWMR
TEXT: GAKPPPFQGULTKGVSGRQTGESTUREYZRM

KEY: BUVYYQ
TEXT: FDNNDQGNDWXSJJYQUSRQDGESTURENSN

KEY: CVSDAC
TEXT: ECQIBEHOABZEIIBLSGSRALGESTUREGO

KEY: QWTAUE
TEXT: QBPLHCVPBYTGUHAOYEGSBIAGESTUREC

KEY: OKUBRR
TEXT: SNOKKPTDCZQTWTZNBREGCJXTGESTURE
```
Виж /src/autokey.py. В този файл е реализиран дешифратор за Автоключ, който пробва всяка възможна позиция на "GESTURE" и проверява дали тя води до еднозначно разшифриране. 

Задача 6.
---------------------------
Линейният регистър е следният:
```
f(b0, b1, b2, b3, b4) = (b4, b1, b2, b3, b3 + b4)
```
В файла /src/registry.c е направена проверка, че той има период 21. Резултатът от тази програма е в /results/problem6.txt.
