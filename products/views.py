from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Product, Category

# Create your views here.


def products(request):
    """ A view to show special offers """
    
    query = request.GET.get('q')
    category = request.GET.get('category')
    special = request.GET.get('special')

    # If a search query is present, override all other filters
    if query:
        products = Product.objects.filter(
            Q(name__icontains=query) | 
            Q(description__icontains=query) |
            Q(category__name__icontains=query)
        )
        if not products.exists():
            messages.info(request, "No products found for your search.")
    # Handle specials
    elif special == 'deal':
        products = Product.objects.filter(deal=True)
    elif special == 'new_arrival':
        products = Product.objects.filter(new_arrival=True)
    elif special == 'clearance':
        products = Product.objects.filter(clearance=True)
    elif special == 'all_specials':
        products = Product.objects.filter(Q(deal=True) | Q(new_arrival=True) | Q(clearance=True))
    # Handle other categories
    elif category:
        products = Product.objects.filter(category__name__iexact=category)
    else:
        products = Product.objects.all()

    return render(request, 'products/products.html', {'products': products})


def all_products(request):
    """ A view to show all products, including sorting and search queries """

    products = Product.objects.all()
    query = None
    categories = None

    if request.GET:
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('products'))
            
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

            if not products:
                messages.info(request, "No products found matching your search criteria!")

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ A view to show individual product details """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)