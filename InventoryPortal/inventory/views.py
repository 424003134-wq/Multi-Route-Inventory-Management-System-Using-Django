
from django.shortcuts import render
from django.http import Http404


PRODUCTS = [
    {
        "slug": "laptop",
        "sku": "INV-001",
        "name": "Laptop",
        "category": "Computer",
        "description": "A reliable laptop for school, office work, and everyday computing.",
        "price": 35000,
        "stock": 10,
        "image": "https://images.unsplash.com/photo-1496181133206-80ce9b88a853?auto=format&fit=crop&w=1000&q=85",
        "featured": True,
    },
    {
        "slug": "keyboard",
        "sku": "INV-002",
        "name": "Keyboard",
        "category": "Accessories",
        "description": "A comfortable keyboard for typing, studying, and daily computer use.",
        "price": 1200,
        "stock": 25,
        "image": "https://images.unsplash.com/photo-1587829741301-dc798b83add3?auto=format&fit=crop&w=1000&q=85",
        "featured": True,
    },
    {
        "slug": "mouse",
        "sku": "INV-003",
        "name": "Mouse",
        "category": "Accessories",
        "description": "A practical computer mouse for accurate navigation and everyday use.",
        "price": 650,
        "stock": 30,
        "image": "https://images.unsplash.com/photo-1527864550417-7fd91fc51a46?auto=format&fit=crop&w=1000&q=85",
        "featured": True,
    },
]


def home(request):
    total_stock = sum(product["stock"] for product in PRODUCTS)

    context = {
        "products": PRODUCTS,
        "featured_count": len(PRODUCTS),
        "total_stock": total_stock,
    }
    return render(request, "inventory/home.html", context)


def about(request):
    return render(request, "inventory/about.html")


def product_detail(request, product_name):
    product = next(
        (
            item for item in PRODUCTS
            if item["slug"].lower() == product_name.lower()
            or item["name"].lower() == product_name.lower()
        ),
        None,
    )

    if product is None:
        raise Http404("Product not found")

    return render(
        request,
        "inventory/product_detail.html",
        {"product": product},
    )


def page_not_found(request, exception):
    return render(request, "inventory/404.html", status=404)
