# Generated by Django 5.2 on 2025-04-19 00:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='brand',
            fields=[
                ('brandId', models.AutoField(primary_key=True, serialize=False)),
                ('brand_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='customer',
            fields=[
                ('customerId', models.AutoField(primary_key=True, serialize=False)),
                ('customer_name', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=100)),
                ('address', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='employee',
            fields=[
                ('employeeId', models.AutoField(primary_key=True, serialize=False)),
                ('employee_name', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=255)),
                ('hire_date', models.DateField()),
                ('role', models.CharField(max_length=50)),
                ('department', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='transaction',
            fields=[
                ('transactionId', models.AutoField(primary_key=True, serialize=False)),
                ('transaction_date', models.DateField()),
                ('isOnline', models.BooleanField()),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hb_app.customer')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hb_app.employee')),
            ],
        ),
        migrations.CreateModel(
            name='vendor',
            fields=[
                ('vendorId', models.AutoField(primary_key=True, serialize=False)),
                ('vendor_name', models.CharField(max_length=100)),
                ('supply_contact', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=100)),
                ('address', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='onlineOrder',
            fields=[
                ('transaction', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='hb_app.transaction')),
                ('carrier', models.CharField(max_length=50)),
                ('trackingNumber', models.CharField(max_length=50)),
                ('shipDate', models.DateField()),
                ('estimateArrival', models.DateField()),
                ('shippingStatus', models.CharField(max_length=50)),
                ('shippingAddress', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='payment',
            fields=[
                ('paymentId', models.AutoField(primary_key=True, serialize=False)),
                ('paymentMethod', models.CharField(max_length=50)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('transaction', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hb_app.transaction')),
            ],
        ),
        migrations.CreateModel(
            name='product',
            fields=[
                ('productId', models.AutoField(primary_key=True, serialize=False)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('type', models.CharField(max_length=50)),
                ('product_name', models.CharField(max_length=100)),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hb_app.brand')),
                ('vendor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hb_app.vendor')),
            ],
        ),
        migrations.CreateModel(
            name='inventoryView',
            fields=[
                ('sku', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('type', models.CharField(max_length=50)),
                ('gender', models.CharField(max_length=20)),
                ('sizeLabel', models.CharField(max_length=20)),
                ('widthLabel', models.CharField(max_length=20)),
                ('colorName', models.CharField(max_length=30)),
                ('inventoryQuantity', models.IntegerField()),
                ('description', models.TextField()),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hb_app.product')),
            ],
        ),
        migrations.CreateModel(
            name='transactionItem',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('orderQuantity', models.IntegerField()),
                ('unitPrice', models.DecimalField(decimal_places=2, max_digits=10)),
                ('sku', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hb_app.inventoryview')),
                ('transaction', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hb_app.transaction')),
            ],
        ),
        migrations.CreateModel(
            name='purchaseOrder',
            fields=[
                ('purchaseOrderID', models.AutoField(primary_key=True, serialize=False)),
                ('qtyPo', models.IntegerField()),
                ('orderDate', models.DateField()),
                ('status', models.CharField(max_length=50)),
                ('unitCost', models.DecimalField(decimal_places=2, max_digits=10)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hb_app.employee')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hb_app.product')),
                ('vendor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hb_app.vendor')),
            ],
        ),
        migrations.CreateModel(
            name='vendorInvoice',
            fields=[
                ('invoiceId', models.AutoField(primary_key=True, serialize=False)),
                ('paymentStatus', models.CharField(max_length=50)),
                ('paymentDate', models.DateField()),
                ('dueDate', models.DateField()),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('purchaseOrder', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hb_app.purchaseorder')),
                ('vendor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hb_app.vendor')),
            ],
        ),
    ]
