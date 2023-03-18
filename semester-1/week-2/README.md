# Code Summary

## 1

### Topics

- Constants
- Data type casting in python

### Code

``` python
fahrenheit = 100
CONVERSION_FACTOR = (5/9)
BASE = 32

celsius = (CONVERSION_FACTOR)*(fahrenheit - BASE)
celsius = round(celsius, 2)
```

## 2

### Topics

- Changing (hard coding) constants in the code

### Code

``` python
GRASS_CUT_TIME = 2

LENGTH_HOUSE = 60
WIDTH_HOUSE = 45

LENGTH_YARD = 80
WIDTH_YARD = 64

AREA_HOUSE = LENGTH_HOUSE*WIDTH_HOUSE
AREA_YARD = (LENGTH_YARD*WIDTH_YARD) - AREA_HOUSE

required_time = AREA_YARD / GRASS_CUT_TIME
required_time = round(required_time, 2)
```
