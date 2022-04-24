import yaml

#读取测试数据
def read_case(filename):
    with open(r'E:\APIproject\membership\db\%s'%filename,'r',encoding='utf-8') as f:
        value=yaml.load(stream=f,Loader=yaml.FullLoader)
        return value
    f.close()

def write_data(filename,data):
    with open(r'E:\APIproject\membership\db\%s'%filename,'a',encoding='utf-8') as f:
        yaml.dump(data,stream=f,allow_unicode=True)
    f.close()

def clear_data(filename):
    with open(r'E:\APIproject\membership\db\%s'%filename,'w',encoding='utf-8') as f:
        f.truncate()
    f.close()
