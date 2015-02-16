# SortedSafeConfigParser
A Python module to get "sorted" ini file output.  
Sections and options in output ini file are sorted in sorted() order.  
Except write(), same as SafeConfigParser.  


## Installation
```
git clone https://github.com/narikin/SortedSafeConfigParser.git
python setup.py install
```


## Get Started
Usage is almost same as SafeConfigParser.  
Specify argument "sort=True" in order to sort output ini file.  

```python
from SortedSafeConfigParser import SortedSafeConfigParser


if __name__ == '__main__':
    config = SortedSafeConfigParser.SortedSafeConfigParser()
    config.read('./sample.ini')

    with open('./result.ini', 'w') as f:
        config.write(f)               # not sorted
        config.write(f, sort=True)    # sorted
        config.write(f, sort=False)   # not sorted
```
