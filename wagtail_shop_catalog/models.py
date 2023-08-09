from wagtail.models import Page


class WagtailShopCatalogBasePage(Page):
    class Meta:
        abstract = True


class CatalogIndexPage(WagtailShopCatalogBasePage):
    template = 'wagtail_shop_catalog/catalog_index_page.html'


class WagtailShopProductBasePage(Page):
    class Meta:
        abstract = True


class ProductPage(WagtailShopProductBasePage):
    template = 'wagtail_shop_catalog/product_page.html'


class WagtailShopProductVariantBasePage(Page):
    class Meta:
        abstract = True


class ProductVariantPage(WagtailShopProductVariantBasePage):
    template = 'wagtail_shop_catalog/product_variant_page.html'
