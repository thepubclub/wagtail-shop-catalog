# Wagtail Shop Catalog

This is a Wagtail Shop Catalog app. It is a simple catalog app that allows you to add products to your Wagtail site.

It's part of the [Wagtail Shop](https://github.com/thepubclub/wagtail-shop) project.

## Installation

Install using pip:

```bash
pip install wagtail-shop-catalog
```

Add `wagtail_shop_catalog` to your `INSTALLED_APPS`:

```python
INSTALLED_APPS = [
    # ...
    'wagtail_shop_catalog',
    # ...
]
```

Add `wagtail_shop_catalog.urls` to your `urlpatterns`:

```python
urlpatterns = [
    # ...
    path('catalog/', include('wagtail_shop_catalog.urls')),
    # ...
]
```

Run migrations:

```bash
python manage.py migrate
```

## Usage

### Adding products

...
