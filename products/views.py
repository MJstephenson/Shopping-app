from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower

from .models import Product, Category
from .forms import ProductForm

# Create your views here.

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


def all_products(request):
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

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)


def add_product(request):
    """ Add a product to the store """
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to add product. Please ensure the form is valid.')
    else:
        form = ProductForm()
        
    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


def edit_product(request, product_id):
    """ Edit a product in the store """
    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to update product. Please ensure the form is valid.')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


def delete_product(request, product_id):
    """ Delete a product from the store """
    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Product deleted!')
    return redirect(reverse('products'))