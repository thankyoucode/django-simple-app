from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from django.shortcuts import get_object_or_404, redirect, render

from .forms import ProductForm
from .models import Product


def index(request):
    return render(request, "index.html")


@login_required
def dashboard(request):
    products = Product.objects.filter(user=request.user).order_by("quantity")
    total_products = products.count()
    total_quantity = products.aggregate(Sum("quantity"))["quantity__sum"] or 0
    low_stock = products.filter(quantity__lt=5).count()
    return render(
        request,
        "inventory/dashboard.html",
        {
            "products": products,
            "total_products": total_products,
            "total_quantity": total_quantity,
            "low_stock": low_stock,
        },
    )


@login_required
def add_product(request):
    form = ProductForm(request.POST)
    if form.is_valid():
        product = form.save(commit=False)
        product.user = request.user
        product.save()
        return redirect("dashboard")
    else:
        form = ProductForm()
    return render(request, "inventory/add_product.html", {"form": form})


@login_required
def edit_product(request, product_id):
    product = get_object_or_404(Product, id=product_id, user=request.user)
    if request.method == "POST":
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect("dashboard")
    form = ProductForm(instance=product)
    return render(
        request, "inventory/edit_product.html", {"form": form, "product": product}
    )


@login_required
def delete_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == "POST":
        product.delete()
    return redirect("dashboard")
