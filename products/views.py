from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Product, Category


def search_products(query):
    """ Utility function to filter products based on a query """
    return Product.objects.filter(
        Q(name__icontains=query) |
        Q(description__icontains=query) |
        Q(category__name__icontains=query)
    )


def fetch_special_products(special):
    """ Utility function to fetch products based on special offers """
    filters = {
        'deal': Q(deal=True),
        'new_arrival': Q(new_arrival=True),
        'clearance': Q(clearance=True),
        'all_specials': Q(deal=True) | Q(new_arrival=True) | Q(clearance=True),
    }
    return Product.objects.filter(filters.get(special, Q()))


def products(request):
    """ A view to show all products, including specials, sorting, and search queries """

    query = request.GET.get('q')
    category = request.GET.get('category')
    special = request.GET.get('special')
    sort = request.GET.get('sort')
    direction = request.GET.get('direction')
    current_sorting = f"{sort}_{direction}" if sort and direction else 'None_None'

    if query:
        products = search_products(query)
        if not products.exists():
            messages.info(request, "No products found for your search.")
    elif special:
        products = fetch_special_products(special)
    elif category:
        products = Product.objects.filter(category__name__iexact=category)
    else:
        products = Product.objects.all()

    # If categories are specified for filtering
    categories = None
    if 'category' in request.GET:
        categories = request.GET['category'].split(',')
        products = products.filter(category__name__in=categories)
        categories = Category.objects.filter(name__in=categories)
    
    # Sorting
    if sort:
        if direction == 'desc':
            sort = f"-{sort}"
        products = products.order_by(sort)

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ A view to show individual product details """

    product = get_object_or_404(Product, pk=product_id)
    return render(request, 'products/product_detail.html', {'product': product})
