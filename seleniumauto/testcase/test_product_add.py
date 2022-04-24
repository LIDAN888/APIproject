import pytest

from seleniumauto.page_object.product_add_page import ProductAddPage
from seleniumauto.page_object.proinfo_page import ProinfoPage

@pytest.mark.run(order=4)
class TestProductAdd:
    def test_product_add(self,open_chrome):
        driver=ProinfoPage(open_chrome)
        driver.add_product()
        driver=ProductAddPage(open_chrome)
        driver.add_basic_info("测试",0,1000)
        driver.add_price(10,999,100,889)
        driver.add_kind_info()
