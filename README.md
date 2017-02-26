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

* Question 1:
``` 
    python3 question_1.py
```

* Question 2:

```
    python3 question_2.py
```
>**NOTE**: Question 2 uses the couples allocated in Question 1, as per given assignment.  
>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Please execute Question 1 before executing Question 2

* All events will be logged in `eventlog.txt`
* Algorithmic functions are present in `algorithms.py`
* Class definitions are present in `boy_uninherited.py`, `girl_uninherited.py`, `gift_uninherited.py` and `couple.py`
* Random generator functions are present in `test_utility.py`
* .csv files `boys.csv`, `girls.csv` and `gifts.csv` will have randomly generated data set

## Documentation and Class Diagrams

* Documentation is available [here](https://ppl-iiita.github.io/ppl-assignment-coderIlluminatus/documentation/html/)

### Command to see documentation offline

``` 
    bash show_doc.sh
```

### Class Diagrams

* All diagrams are already included in html documentation
* Class diagrams are separately present in `/diagrams/*.png`

## Tools Used

* [doxygen](https://www.doxygen.org)   :  Generates automatic documentation
* [graphviz](https://www.graphviz.org)  :  Generates class, inheritance and collaboration diagrams in documentation 
* [pyreverse](https://pypi.python.org/pypi/pyreverse/0.5.1) :  Generates class diagrams separately in .png (component of pylint)