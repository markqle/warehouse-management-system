from django.contrib import admin
from .models import brand, vendor, customer, employee, product, transaction, inventoryView, transactionItem, payment, onlineOrder, purchaseOrder, vendorInvoice
# Register your models here.

admin.site.register(brand)
