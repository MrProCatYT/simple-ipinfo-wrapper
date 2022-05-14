# simple-ipinfo-wrapper
Simple wrapper for ipinfo.io
## Installation
To install, you'll need python 3 and pip.

```pip install simple-ipinfo-wrapper```
## Code example
This code will print info about the ip

```python
from simple-ipinfo-wrapper Wrapper

wrapper = Wrapper()
ip = input('Enter your ip: ') # Ex.: 127.0.0.1
print(wrapper.getinfo(ip))
```
