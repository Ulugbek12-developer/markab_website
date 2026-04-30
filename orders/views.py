from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .models import Order
from phones.models import Phone

class CheckoutView(View):
    def get(self, request, phone_id):
        phone = get_object_or_404(Phone, pk=phone_id)
        return render(request, 'orders/checkout.html', {'phone': phone})

    def post(self, request, phone_id):
        phone = get_object_or_404(Phone, pk=phone_id)
        name = request.POST.get('name')
        user_phone = request.POST.get('phone')
        is_installment = request.POST.get('is_installment') == 'on'
        months = request.POST.get('months')

        Order.objects.create(
            phone=phone,
            customer_name=name,
            customer_phone=user_phone,
            is_installment=is_installment,
            installment_months=int(months) if months else None
        )
        return redirect('orders:success')

class SuccessView(View):
    def get(self, request):
        return render(request, 'orders/success.html')
