# Principles of Programming Languages (IPPL 430 C) Assignment
## Object Oriented Programming  
### Sayantan Chatterjee - IIT 2015 511

<img src="https://img.shields.io/badge/language-Python3-brightgreen.svg"/>
<img src="https://img.shields.io/badge/completion-20%25-yellow.svg"/>
<img src="https://img.shields.io/badge/elementary OS-0.4-red.svg"/>
<img src="https://img.shields.io/badge/VS Code-1.8.1-blue.svg"/>  

### Contents
* [Build Details](#build-details)
* [Testing Instructions](#testing-instructions)
* [Documentation and Class Diagrams](#documentation-and-class-diagrams)
* [Tools Used](#tools-used) 

## Build Details

### Language:

```
 Python 3.5.2
```

### Platform:

```
 VS Code Version 1.8.1
```

### Operating System:

```
 Distributor  :	elementary
 Description  :	elementary OS 0.4 Loki
 Release      :	0.4
 Codename     :	loki
```

## Testing instructions

* Generate random data set (Boys, Girls, Gifts):
```
    python3 test_utility.py
```

* Question x (x ∈ [3, 7] ∪ [9, 10]):
``` 
    python3 question_x.py
```

* Question 8:
``` 
    python3 question_8.py
    OR
    python3 question_8.py any
    OR
    python3 question_8.py every
```
>**NOTE**: Question 8 uses command line arguments for implementing various gift selection mechanisms.
>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;For default mechanism, no argument is required.

* All events will be logged in `eventlog.txt`
* Algorithmic functions are present in `algorithms.py`
* Class definitions for boys, girls and gifts are present in directories `boys`, `girls` and `gifts` respectively
* Class definition for couple is present in `couple.py`
* Class definitions for searching girlfriend names are present in `partners` directory
* Class definitions for gift selectors are present in `selectors` directory
* Data stuctures defined for questions 9 and 10 are present in `top_k.py` and `random_k.py`
* Random generator functions are present in `test_utility.py`
* .csv files `boys.csv`, `girls.csv` and `gifts.csv` will have randomly generated data set

## Documentation and Class Diagrams

* Documentation is available [here](https://ppl-iiita.github.io/ppl-assignment-coderIlluminatus/)

### Command to see documentation offline

``` 
    bash show_doc.sh
```

### Class Diagrams

* All diagrams are already included in html documentation
* Class diagrams are separately present in `/diagrams/*.png`

## Tools Used

* [doxygen](http://www.stack.nl/~dimitri/doxygen/)   :  Generates automatic documentation
* [graphviz](http://www.graphviz.org/)  :  Generates class, inheritance and collaboration diagrams in documentation 
* [pyreverse](https://pypi.python.org/pypi/pyreverse/0.5.1) :  Generates class diagrams separately in .png (component of pylint)