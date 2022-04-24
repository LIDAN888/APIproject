import re

from membership.common import read_testcase


def ProcessData(obj):
    '''
    1.处理从yaml文件中读取的数据，把相关字段提取出来
    :param obj: 参数化的参数名称，是通过yaml读取的测试数据
    :return:
    '''
    print('\n', obj['name'])
    method = obj['method'].lower()
    url = obj['url']
    header = obj['header']
    data = obj['data']
    validata = obj['Validata']
    return method,url,header,data,validata

def ExtractData(data):
    '''
    把从结果提取的关联参数关联到下一个请求的参数中
    data:请求参数中的data,是字典类型
    :return:
    '''
    new_data=data.copy()
    while True:
        search_extract = re.search("'\$.*?'", str(new_data).replace(' ', '')) #正则表达式提取请求参数中的关联参数
        if search_extract:#如果有关联参数就处理，没有直接返回data
            extract_word = eval(search_extract.group())#把正则表达式匹配到的值取出来，并且进行eval()处理字符串
            extract_word = extract_word.strip('$')#去除关联符号
            extracr_data = read_testcase.read_case('extract_data.yaml')#wewmcwenbcbcmdbmcbncdcb n extract_word in key:
            data[extract_word]= extracr_data[extract_word]
            new_data.pop(extract_word) #删除data中的第一个关联数据，再去寻找下一个
        else:
            return data



# a={'uuid':'$uuid','token':'1233'}
# print(ExtractData(a))




