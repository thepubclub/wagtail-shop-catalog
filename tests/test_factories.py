from .factories import (
    CatalogIndexPageFactory,
    ProductPageFactory,
    ProductVariantPageFactory,
)


class TestCatalogIndexPage:
    def test_catalog_index_page(self):
        catalog_index_page = CatalogIndexPageFactory(
            title="Catalog Index Page",
        )
        assert str(catalog_index_page) == "Catalog Index Page"


class TestProductPage:
    def test_product_page(self):
        product_page = ProductPageFactory(
            title="Product Page",
        )
        assert str(product_page) == "Product Page"


class TestProductVariantPage:
    def test_product_variant_page(self):
        product_variant_page = ProductVariantPageFactory(
            title="Product Variant Page",
        )
        assert str(product_variant_page) == "Product Variant Page"
