Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 23:11:46) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> complex_one = 1 + 2j
>>> print(complex_one.real)
1.0
>>> print(complex_one.image)
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    print(complex_one.image)
AttributeError: 'complex' object has no attribute 'image'
>>> print(complex_one.image)
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    print(complex_one.image)
AttributeError: 'complex' object has no attribute 'image'
>>> print(complex_one.imag)
2.0
>>> print(bool(None))
False
>>> print(bool('hello'))
True
>>> print(bool(1))
True
>>> print(bool(0))
False
>>> complex_one = 1+2j
>>> complex_two = 6
>>> complex_three = 7j
>>> complex_one = complex(1,2)
>>> print(complex_one)
(1+2j)
>>> 
>>> complex_three = complex(7j)
>>> print(complex_three)
7j
>>> print(bin(decimal))
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    print(bin(decimal))
NameError: name 'decimal' is not defined
>>> print(hex(bin_num))
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    print(hex(bin_num))
NameError: name 'bin_num' is not defined
>>> num_one = 2.0
>>> print(int(num_one))
2
>>> num_two = 5
>>> print(float(num_two))
5.0
>>> print(complex(num_one))
(2+0j)
>>> print(complex(num_two))
(5+0j)
>>> words_one = '10'
>>> print(int(words_one))
10
>>> print(float(words_one))
10.0
>>> print(complex(words_one))
(10+0j)
>>> words = 9
>>> print(float(words))
9.0
>>> word2 = '0b1010'
>>> print(int(word2))
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    print(int(word2))
ValueError: invalid literal for int() with base 10: '0b1010'
>>> word2 = '0b1010'
>>> print(int(word2,base=2))
10
>>> a = 2
>>> b = 8
>>> a+b
10
>>> a*b
16
>>> a / b
0.25
>>> a       **                  b
256
>>> b*     *a
SyntaxError: invalid syntax
>>> B**a
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    B**a
NameError: name 'B' is not defined
>>> b**a
64
>>> b = B
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    b = B
NameError: name 'B' is not defined
>>> c = a+b
>>> printc
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    printc
NameError: name 'printc' is not defined
>>> print(c)
10
>>> a//b
0
>>> a%b
2
>>> a**c
1024
>>> print(10 / 2.0)
5.0
>>> print(10 - (3+5j))
(7-5j)
>>> n, m =1, 2
>>> n*m
2
>>> x = y =z =1
>>> x/y    /z
1.0
>>> num = 3
>>> num +=2
>>> 
>>> print(num +=)
SyntaxError: invalid syntax
>>> num_one = 1
>>> result = num_one + (num_two:=2)
>>> print(result)
3
>>> a==A
Traceback (most recent call last):
  File "<pyshell#64>", line 1, in <module>
    a==A
NameError: name 'A' is not defined
>>>  v=0
 
SyntaxError: unexpected indent
>>> v=9
>>> v!=a
True
>>> v==a
False
>>> v>=a
True
>>> v<=b
False
>>> num+=2
>>> num+=2
>>> num+= 2 ==num=num+2
SyntaxError: invalid syntax
>>> print(num += 2)
SyntaxError: invalid syntax
>>> print(num+=2)
SyntaxError: invalid syntax
>>> print(num = num+2)]
SyntaxError: unmatched ']'
>>> print(num = num+2)
Traceback (most recent call last):
  File "<pyshell#77>", line 1, in <module>
    print(num = num+2)
TypeError: 'num' is an invalid keyword argument for print()
>>> a and b
8
>>> a or b
2
>>> a not b
SyntaxError: invalid syntax
>>> x = 'python'
>>> y = 'p'
>>> print(y in x)
True
>>> print(y not in x)
False
>>> 