from django.shortcuts import render, redirect
from .forms import CreateUserForm, LoginForm, CreateRecordForm, UpdateRecordForm
from .forms import CreateOrderForm, UpdateOrderForm
from .forms import CreateProductForm, UpdateProductForm

from django.contrib.auth.models import auth
from django.contrib.auth import authenticate
from django.db.models import Q

from django.contrib.auth.decorators import login_required

from .models import Record, Order, Product

from django.contrib import messages

# - Homepage

def home(request):
    
    return render(request, 'crmapp/index.html')

# - About page

def about(request):
    
    return render(request, 'crmapp/about.html')

# - Terms of Service

def terms_service(request):
    
    return render(request, 'crmapp/terms-service.html')

# - Register a user

def register(request):
    
    form = CreateUserForm()
    
    if request.method == "POST":
        
        form = CreateUserForm(request.POST)

        if form.is_valid():
            
            form.save()
            
            messages.success(request, "Account created successfully")
            
            return redirect("my-login")
    
    context = {'form':form}
    
    return render(request, 'crmapp/register.html', context=context)

# - Login a user

def my_login(request):

    form = LoginForm()
    
    if request.method == "POST":
        
        form = LoginForm(request, data=request.POST)
    
        if form.is_valid():
            
            username = request.POST.get('username')
            password = request.POST.get('password')
            
            user = authenticate(request, username=username, password=password)
    
            if user is not None:
                
                auth.login(request, user)
                
                return redirect("dashboard")
                
    context = {'form':form}
    
    return render(request, 'crmapp/my-login.html', context=context)

# - Dashboard

@login_required(login_url='my-login')
def dashboard(request):
    
    customer_query = request.GET.get('customer_query', '')
    if customer_query:
        my_records = Record.objects.filter(
            user=request.user
        ).filter(
            Q(first_name__icontains=customer_query) | Q(last_name__icontains=customer_query)
        )
    else:
        my_records = Record.objects.filter(user=request.user)

    order_query = request.GET.get('order_query', '')
    if order_query:
        my_orders = Order.objects.filter(
            user=request.user
        ).filter(
            Q(product__name__icontains=order_query) | Q(status__icontains=order_query)
        )
    else:
        my_orders = Order.objects.filter(user=request.user)

    context = {
        'records': my_records,
        'orders': my_orders,
        'customer_query': customer_query,
        'order_query': order_query,
    }
    
    return render(request, 'crmapp/dashboard.html', context=context)

# - Create a record

@login_required(login_url='my-login')
def create_record(request):

    form = CreateRecordForm()
    
    if request.method == "POST":
        
        form = CreateRecordForm(request.POST)
        
        if form.is_valid():
            
            new_record = form.save(commit=False)
            new_record.user = request.user
            new_record.save()
            
            messages.success(request, "Your record was created")
            
            return redirect("dashboard")
    
    context = {'form': form}
    
    return render(request, 'crmapp/create-record.html', context=context)

# - Update a record

@login_required(login_url='my-login')
def update_record(request, pk):
    
    record = Record.objects.get(id=pk)
    
    form = UpdateRecordForm(instance=record)
    
    if request.method == 'POST':
        
        form = UpdateRecordForm(request.POST, instance=record)
        
        if form.is_valid():
            
            form.save()
            
            messages.success(request, "Your record was updated")
            
            return redirect("dashboard")

    context = {'form': form}
    
    return render(request, 'crmapp/update-record.html', context=context)

# - Read / View a singular record

@login_required(login_url='my-login')
def singular_record(request, pk):
    
    record = Record.objects.get(id=pk)
    orders = Order.objects.filter(customer=record)
    
    context = {
        'record': record,
        'orders': orders
    }
    
    return render(request, 'crmapp/view-record.html', context=context)

# - Delete a record

@login_required(login_url='my-login')
def delete_record(request, pk):

    record = Record.objects.get(id=pk)
    
    record.delete()
    
    messages.success(request, "Your record was deleted")
    
    return redirect("dashboard")

# - Products dashboard

@login_required(login_url='my-login')
def products(request):
    
    my_products = Product.objects.filter(user=request.user)
    
    context = {
        'products': my_products
    }

    return render(request, 'crmapp/products.html', context=context)

# - Add a product

@login_required(login_url='my-login')
def add_product(request):

    form = CreateProductForm()
    
    if request.method == "POST":
        
        form = CreateProductForm(request.POST)
        
        if form.is_valid():
            
            product = form.save(commit=False)
            product.user = request.user
            product.save()
            
            messages.success(request, "Your product was created")
            
            return redirect("products")
    
    context = {'form': form}
    
    return render(request, 'crmapp/add-product.html', context=context)

# - Update a product

@login_required(login_url='my-login')
def update_product(request, pk):

    product = Product.objects.get(id=pk)
    
    form = UpdateProductForm(instance=product)
    
    if request.method == 'POST':
        
        form = UpdateProductForm(request.POST, instance=product)
        
        if form.is_valid():
            
            form.save()
            
            messages.success(request, "Your product was updated")
            
            return redirect("products")

    context = {'form': form}
    
    return render(request, 'crmapp/update-product.html', context=context)

# - Read / View a singular product

@login_required(login_url='my-login')
def singular_product(request, pk):
    
    all_products = Product.objects.get(id=pk)
    
    context = {'product': all_products}
    
    return render(request, 'crmapp/view-product.html', context=context)

# - Delete a product

@login_required(login_url='my-login')
def delete_product(request, pk):

    product = Product.objects.get(id=pk)
    
    product.delete()
    
    messages.success(request, "Your product was deleted")
    
    return redirect("products")


# - Create an order

@login_required(login_url='my-login')
def create_order(request):

    form = CreateOrderForm()
    
    if request.method == "POST":
        
        form = CreateOrderForm(request.POST)
        
        if form.is_valid():
            
            order = form.save(commit=False)
            order.user = request.user 
            order.save()
            
            messages.success(request, "Your order was created")
            
            return redirect("dashboard")
    
    context = {'form': form}
    
    return render(request, 'crmapp/create-order.html', context=context)

# - Update an order

@login_required(login_url='my-login')
def update_order(request, pk):

    order = Order.objects.get(id=pk)
    
    form = UpdateOrderForm(instance=order)
    
    if request.method == 'POST':
        
        form = UpdateOrderForm(request.POST, instance=order)
        
        if form.is_valid():
            
            form.save()
            
            messages.success(request, "Your order was updated")
            
            return redirect("dashboard")

    context = {'form': form}
    
    return render(request, 'crmapp/update-order.html', context=context)

# - Read / View a singular order

@login_required(login_url='my-login')
def singular_order(request, pk):
    
    all_orders = Order.objects.get(id=pk)
    
    context = {'order': all_orders}
    
    return render(request, 'crmapp/view-order.html', context=context)

# - Delete an order

@login_required(login_url='my-login')
def delete_order(request, pk):

    order = Order.objects.get(id=pk)
    
    order.delete()
    
    messages.success(request, "Your order was deleted")
    
    return redirect("dashboard")

# - User logout

def user_logout(request):
    
    auth.logout(request)
    
    messages.success(request, "You've been logged out")
    
    return redirect("my-login")