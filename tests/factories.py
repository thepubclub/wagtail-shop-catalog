import wagtail_factories

from wagtail_shop_catalog import models


class CatalogIndexPageFactory(wagtail_factories.PageFactory):
    class Meta:
        model = models.CatalogIndexPage


class ProductPageFactory(wagtail_factories.PageFactory):
    class Meta:
        model = models.ProductPage


class ProductVariantPageFactory(wagtail_factories.PageFactory):
    class Meta:
        model = models.ProductVariantPage
