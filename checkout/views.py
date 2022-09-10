from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51LgWnFBO1x3Ln70ij2Q9Do4gRZap9EQjvv1VaANb5kvImF8VLzrHWrgweTl7PDUTvG95oYoxQV6v3JHBtplo9TAZ00WSrF8qXw',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
