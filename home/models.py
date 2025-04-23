# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Category(models.Model):

    #__Category_FIELDS__
    name = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(max_length=255, null=True, blank=True)

    #__Category_FIELDS__END

    class Meta:
        verbose_name        = _("Category")
        verbose_name_plural = _("Category")


class Product(models.Model):

    #__Product_FIELDS__
    description = models.TextField(max_length=255, null=True, blank=True)
    market_price = models.IntegerField(null=True, blank=True)
    selling_price = models.IntegerField(null=True, blank=True)
    transpot_cost = models.IntegerField(null=True, blank=True)
    stock = models.IntegerField(null=True, blank=True)
    category_name = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_at = models.DateTimeField(blank=True, null=True, default=timezone.now)
    discount = models.IntegerField(null=True, blank=True)

    #__Product_FIELDS__END

    class Meta:
        verbose_name        = _("Product")
        verbose_name_plural = _("Product")


class Orders(models.Model):

    #__Orders_FIELDS__
    order_product_name = models.ForeignKey(product, on_delete=models.CASCADE)
    order_date = models.DateTimeField(blank=True, null=True, default=timezone.now)
    qty = models.IntegerField(null=True, blank=True)
    status = models.BooleanField()

    #__Orders_FIELDS__END

    class Meta:
        verbose_name        = _("Orders")
        verbose_name_plural = _("Orders")



#__MODELS__END
