import requests

class Request:
    '''
    封装了requests的请求方法，把经过处理的参数放到send_request()方法中去请求
    '''
    def send_request(self,method,url,data,header,**kwargs):
        if method == 'get':
            ret=requests.request(method=method,url=url,params=data)
        elif method == 'post' and header['content-type'] == 'application/x-www-form.urlencoded':
            ret=requests.request(method=method,url=url,data=data,**kwargs)
        elif method == 'post' and header['content-type'] == 'application/json':
            ret=requests.request(method=method,url=url,json=data,**kwargs)
        return ret.json()