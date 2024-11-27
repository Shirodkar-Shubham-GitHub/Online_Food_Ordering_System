from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseBadRequest
from .models import Item, CartItems, Contact
from django.contrib import messages
from django.views.generic import (
    ListView,
    DeleteView,
)
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.db.models import Sum
from django.db.models import Q
from django.core.paginator import Paginator
import razorpay
from django.conf import settings

class MenuListView(ListView):
    model = Item
    template_name = 'main/home.html'
    context_object_name = 'menu_items'

    def get_queryset(self):
        return Item.objects.all()[:3]
    
def menu(request):
    menu = Item.objects.all()
    
    query= ''
    if 'search' in request.POST:
        query = request.POST.get('searchquery')
        menu = Item.objects.filter(Q(title__icontains=query) | Q(price__icontains=query))

    paginator = Paginator(menu, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {'menu': menu, 'query':query, 'page_obj': page_obj}
    return render(request, 'main/menu.html', context)

def menuDetail(request, slug):
    item = Item.objects.filter(slug=slug).first()
    context = {
        'item' : item,
    }
    return render(request, 'main/dishes.html', context)

@login_required
def add_to_cart(request, slug):
    item = get_object_or_404(Item, slug=slug)
    cart_item = CartItems.objects.create(
        item=item,
        user=request.user,
        ordered=False,
    )
    messages.info(request, "Added to Cart!!Continue Ordering!!")
    return redirect("main:cart")

@login_required
def get_cart_items(request):
    cart_items = CartItems.objects.filter(user=request.user,ordered=False)
    bill = cart_items.aggregate(Sum('item__price'))
    number = cart_items.aggregate(Sum('quantity'))
    plates = cart_items.aggregate(Sum('item__plates'))
    total = bill.get("item__price__sum")
    count = number.get("quantity__sum")
    total_plates = plates.get("item__plates__sum")
    context = {
        'cart_items':cart_items,
        'total': total,
        'count': count,
        'total_plates': total_plates
    }
    return render(request, 'main/cart.html', context)

class CartDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = CartItems
    success_url = '/cart'

    def test_func(self):
        cart = self.get_object()
        if self.request.user == cart.user:
            return True
        return False

@login_required
def order_item(request):
    cart_items = CartItems.objects.filter(user=request.user,ordered=False)
    ordered_date=timezone.now()
    cart_items.update(ordered=True,ordered_date=ordered_date)
    messages.info(request, "Item Ordered")
    return redirect("main:order_details")

@login_required
def order_details(request):
    items = CartItems.objects.filter(user=request.user, ordered=True,status="Active").order_by('-ordered_date')
    cart_items = CartItems.objects.filter(user=request.user, ordered=True,status="Delivered").order_by('-ordered_date')
    bill = items.aggregate(Sum('item__price'))
    number = items.aggregate(Sum('quantity'))
    plates = items.aggregate(Sum('item__plates'))
    total = bill.get("item__price__sum")
    count = number.get("quantity__sum")
    total_plates = plates.get("item__plates__sum")
    context = {
        'items':items,
        'cart_items':cart_items,
        'total': total,
        'count': count,
        'total_plates': total_plates
    }
    return render(request, 'main/order_details.html', context)

def about(request):
    return render(request, 'main/about.html')

def dashboard(request):
    return render(request, 'main/dashboard.html')

def profile(request):
    return render(request, 'main/profile.html')

def contact(request):
    ctx = {'active_link': 'contact'}
    if request.method == "POST":

        name = request.POST["name"]
        email = request.POST["email"]
        phone = request.POST["phone"]
        desc = request.POST["desc"]
        # print(name, email, phone, desc)
        ins = Contact(name=name, email=email, phone=phone, desc=desc)
        ins.save()
    return render(request, 'main/contact.html', ctx)
