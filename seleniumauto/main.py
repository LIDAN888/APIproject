import os

import pytest

if __name__ == '__main__':
    pytest.main(['-s','-v','--alluredir=../temps','--clean-alluredir'])
    #pytest.main()
    os.system("allure generate ../temps -o ./report --clean")
    os.system("allure serve ../temps")