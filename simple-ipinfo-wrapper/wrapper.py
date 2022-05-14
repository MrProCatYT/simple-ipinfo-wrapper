import requests

class Wrapper():
    def __init__(self) -> None:
        pass
    def getinfo(self, ip: str = '') -> dict:
        if ip != '': ip += '/'
        try: 
            response = requests.get(f'https://ipinfo.io/{ip}json')
        except: raise
        '''
        Possible keys in the dictionary:
        ip, city, region, country, loc, org, timezone, etc
        (see ipinfo.io for more information)
        '''
        r = response.json()
        if 'error' in r:
            status = r['status']
            message = r['error']['message']
            raise Exception(f'\nStatus: {status}\nMessage: {message}')
        return r


'''
Code example:

wrapper = Wrapper()
print(wrapper.getinfo())
'''
