# ipinfo-simple-wrapper
Simple wrapper for ipinfo.io
## Installation
To install, you'll need python 3 and pip.

```pip install ipinfo-simple-wrapper```
## Code example
This code will print info about the ip

```python
from ipinfo-simple-wrapper Wrapper

wrapper = Wrapper()
ip = input('Enter your ip: ') # Ex.: 127.0.0.1
print(wrapper.getinfo(ip))
```
