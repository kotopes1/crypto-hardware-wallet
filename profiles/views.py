"""
Django views for User Profile management.
This module contains views for managing user profiles, including rendering the
user profile template, updating user profile information, and displaying
error messages.
Imports:
    render, get_object_or_404 : Django's render and get_object_or_404 shortcuts
    messages : Django's messages framework for handling messages
    login_required : Django's login_required decorator
    for handling authentication
    UserProfile : UserProfile model for user profile management
    UserProfileForm : Form for updating user profile information
"""

from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import UserProfile
from .forms import UserProfileForm

from checkout.models import Order


@login_required
def profile(request):
    """ Display the user's profile. """
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')
        else:
            messages.error(request,
                           ('Update failed. Please ensure '
                            'the form is valid.'))
    else:
        form = UserProfileForm(instance=profile)
    orders = profile.orders.all()

    template = 'profiles/profile.html'
    context = {
        'form': form,
        'orders': orders,
        'on_profile_page': True
    }

    return render(request, template, context)


def order_history(request, order_number):
    """
Retrieves the order history for a given user.
Retrieves the order history for the user specified by the user_id parameter.
The order history includes information such as the order date, total cost, and
items included in the order.
    """
    order = get_object_or_404(Order, order_number=order_number)

    messages.info(request, (
        f'This is a past confirmation for order number {order_number}. '
        'A confirmation email was sent on the order date.'
    ))

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'from_profile': True,
    }

    return render(request, template, context)
