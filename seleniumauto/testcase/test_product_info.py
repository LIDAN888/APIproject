import pytest

from seleniumauto.page_object.home_page import HomePage


@pytest.mark.run(order=2)
class TestProductInfo:
     def test_add_product(self,open_chrome):
#         '''
#         1.点击上侧菜单栏：产品分类
#         2.点击左侧菜单栏:产品管理
#         3.点击页面：产品信息管理
#         4.添加产品信息
#         '''
        driver=HomePage(open_chrome)
        driver.menu_bar("产品分类")
        driver.menu_bar("产品管理")
        driver.menu_bar("产品信息管理")

