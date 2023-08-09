from django.test import TestCase
from tests.factories import CatalogIndexPageFactory, ProductPageFactory, ProductVariantPageFactory


class TestCatalogIndexPage(TestCase):
    def setUp(self):
        self.catalog_index_page = CatalogIndexPageFactory()

    def test_catalog_index_page(self):
        self.assertEqual(self.catalog_index_page.get_children().count(), 0)
