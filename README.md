# Криптография

В това repository са изложени решенията на задачите от домашното по избираемия курс по Криптография към ФМИ за летния семестър 2025 г.

Задача 2.
-----------------------
```
  736
```
Виж /images/problem2.jpg

Задача 3.
------------------------
Виж /images/problem3.jpg

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
f(b0, b1, b2, b3, b4) = (b4, b0, b1, b2, b3 + b4)
```
Във файла /src/registry.c е направена проверка, че той има период 21. Резултатът от тази програма е в /results/problem6.txt.

Задача 7.
------------------------
```
Round 0: A=10, B=1101 (101101)
Round 1: f1(1101)=00; -> next A=1101, next B=10 (110110)
Round 2: f2(0110)=01; -> next A=0110, next B=10 (011010)
Round 3: f3(1010)=00; -> next A=1010, next B=01 (101001)
Round 4: f4(1001)=01; -> next A=1001, next B=11 (100111)

Ciphertext: 100111
```
Горното е резултат от реализацията на задачата в /src/feistel.py.

Задача 8.
-------------------------
Виж /images/problem8.jpg.

Задача 9.
------------------------
```
83
```
Виж реализацията на алгоритъма на Pohlig-Hellman в /src/pohlig-hellman.py.

Задача 12.
------------------------
```
Public key: 86
r = 8
s = 94

Подпис: (r, s) = (8, 94)
Подписът е валиден.
```
Извеждането на ключа и неговата верификация е направена в /src/elgamal.py.

Задача 13.
----------------------------
```
312
```
Тук отново е ползвана имплементацията на алгоритъма на Pohlig-Hellman от /src/pohlig-hellman.py.


Задача 14.
------------------------------
```
(2061, 4715, 3066)
```
Виж /images/problem14.jpg.
