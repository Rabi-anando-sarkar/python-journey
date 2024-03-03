# Object Types / Data Types 

> Python me koi data type nahi hota 

    For eg : score = 10 

    Behind the scene(memory ke ander) 10 ko bola jaata hai ki uska type number hai na ki ye bola jaata ki score ka type number hai. Score kw data type se koi mtlb nahi na koi lena dena


- Number : 1234, 3.14, 3+4j, 0b111, Decimal(), Fraction()
- String : 'spam', "BOB's", b'a\x01c, u'sp\xc4m'
- List : [1, [2,'rabi'],3.5 ], list(range(10))
- Tuple : (1, (2,'rabi'),3 ), tuple('spam'), namedtuple
- Dictionary : {'food':'spam', "taste":"yum"}, dict(hours=10)

- Set : set('abc'), {'a','b','c'}

- File : open('eggs.txt'), open(r'C:\ham.bin', 'wb')

- Boolean : True,False
- None : None
- Functions, modules, classes
- Advance: Decorators, Generators, Iterators, MetaProgramming

> Mutable

```
- List
- Set
- Dictionary
- Bytearray
- Array
```

> Immutable 

```
- Integers
- Floating - point numbers
- Boolean
- Strings
- Tuples
- Frozen set
- Bytes
```

Jab List banate hai vs jab numbers banate hai differnce hota hai

- jab list banate ho obv uska ref assign hota hai
- to agar change hota hai to waapis se ek new ref create hota hi