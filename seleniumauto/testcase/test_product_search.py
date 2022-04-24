from seleniumauto.page_object.home_page import HomePage
from seleniumauto.page_object.proinfo_page import ProinfoPage
import pytest

@pytest.mark.run(order=3)
class TestProductSearch:
    def test_product_search(self,open_chrome):
        driver=ProinfoPage(open_chrome)
        driver.search_product("1","test computer","2017-04-01","2018-12-12")
        driver.clear_search(open_chrome)