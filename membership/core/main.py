import os
import sys
import time
import allure
import pytest

if __name__ == '__main__':
    #print(os.getcwd())
    pytest.main(['-s','-v','-m','not regin','--alluredir=../temps','--clean-alluredir'])
    #pytest.main()
    os.system("allure generate ../temps -o ../report --clean")
    os.system("allure serve ../temps")

