from django.test import TestCase

from tests.factories import (
    CatalogIndexPageFactory,
    ProductPageFactory,
    ProductVariantPageFactory,
)


class TestCatalogIndexPage(TestCase):
    def setUp(self):
        self.catalog_index_page = CatalogIndexPageFactory()

    def test_catalog_index_page(self):
        self.assertEqual(self.catalog_index_page.get_children().count(), 0)


class TestProductPage(TestCase):
    def setUp(self):
        self.product_page = ProductPageFactory()

    def test_product_page(self):
        self.assertEqual(self.product_page.get_children().count(), 0)


class TestProductVariantPage(TestCase):
    def setUp(self):
        self.product_variant_page = ProductVariantPageFactory()

    def test_product_variant_page(self):
        self.assertEqual(self.product_variant_page.get_children().count(), 0)
