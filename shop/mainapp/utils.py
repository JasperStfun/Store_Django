from django.db import models


def recalc_cart(cart):
    cart_data = cart.products.aggregate(models.Sum('final_price'), models.Count('id'))
    if cart_data.filter('final_price__sum').first():
        cart.final_price = cart_data['final_price__sum']
    else:
        cart.final_price = 0
    cart.total_products = cart_data['id__count']
    cart.save()
