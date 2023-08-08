# Python - Everything is object
This project introduces a new concept: everything in __Python__ is a __object__.

## General
In this project, we were able to:
* Know what is an object
* distinguish between a class and an object or instance
* distinguish between immutable object and mutable object
* Know what is a reference and what is assignement
* Know what is an alias

## Tasks
0. Who am I?
* What function would you use to get the type of an object?

* Write the name of the function in the file, without `()`.

1. Where are you?
* How do you get the variable identifier (which is the memory address in the CPython implementation)?

* Write the name of the function in the file, without `()`.

2. Right count
* In the following code, do `a` and `b` point to the same object? Answer with `Yes` or `No`.
```
>>> a = 89
>>> b = 100
```
3. Right count =
* In the following code, do `a` and `b` point to the same object? Answer with `Yes` or `No`.
```
>>> a = 89
>>> b = 89
```
4. Right count =
* In the following code, do `a` and `b` point to the same object? Answer with `Yes` or `No`.
```
>>> a = 89
>>> b = a
```

5. Right count =+
* In the following code, do `a` and `b` point to the same object? Answer with `Yes` or `No`.
```
>>> a = 89
>>> b = a + 1
```

6. Is equal
* What do these 3 lines print?
```
>>> s1 = "Best School"
>>> s2 = s1
>>> print(s1 == s2)
```

7. Is the same
* What do these 3 lines print?
```
>>> s1 = "Best"
>>> s2 = s1
>>> print(s1 is s2)
```
8. Is really equal
* What do these 3 lines print?
```
>>> s1 = "Best School"
>>> s2 = "Best School"
>>> print(s1 == s2)
```
