from seleniumauto.page_object.proinfo_page import ProinfoPage


class TestProductAdd:
    def test_product_add(self,open_chrome):
        driver=ProinfoPage(open_chrome)