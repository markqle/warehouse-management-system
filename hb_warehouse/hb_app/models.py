from django.db import models

# Create your models here.
class brand(models.Model):
    brandId = models.AutoField(primary_key=True)
    brand_name = models.CharField(max_length=100)

    #This is a string representation of the brands
    def __str__(self):
        return (f"brand_id: {self.brandId}, brand name: {self.brand_name}")

class vendor(models.Model):
    vendorId = models.AutoField(primary_key=True)
    vendor_name = models.CharField(max_length=100)
    supply_contact = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.EmailField(max_length=100)
    address = models.CharField(max_length=255)

class customer(models.Model):
    customerId = models.AutoField(primary_key=True)
    customer_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.EmailField(max_length=100)
    address = models.CharField(max_length=255)

class employee(models.Model):
    employeeId = models.AutoField(primary_key=True)
    employee_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=255)
    hire_date = models.DateField()
    role = models.CharField(max_length=50)
    department = models.CharField(max_length=50)

class product(models.Model):
    productId = models.AutoField(primary_key=True)
    vendor = models.ForeignKey(vendor, on_delete=models.CASCADE)
    brand = models.ForeignKey(brand, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    type = models.CharField(max_length=50)
    product_name = models.CharField(max_length=100)

class transaction(models.Model):
    transactionId = models.AutoField(primary_key=True)
    transaction_date = models.DateField()
    customer = models.ForeignKey(customer, on_delete=models.CASCADE)
    employee = models.ForeignKey(employee, on_delete=models.CASCADE)
    isOnline = models.BooleanField()

class inventoryView(models.Model):
    sku = models.CharField(max_length=20, primary_key=True)
    product = models.ForeignKey(product, on_delete=models.CASCADE)
    type = models.CharField(max_length=50)
    gender = models.CharField(max_length=20)
    sizeLabel = models.CharField(max_length=20)
    widthLabel = models.CharField(max_length=20)
    colorName = models.CharField(max_length=30)
    inventoryQuantity = models.IntegerField()
    description = models.TextField()

class transactionItem(models.Model):
    id = models.AutoField(primary_key=True)
    transaction = models.ForeignKey(transaction, on_delete=models.CASCADE)
    sku = models.ForeignKey(inventoryView, on_delete=models.CASCADE)
    orderQuantity = models.IntegerField()
    unitPrice = models.DecimalField(max_digits=10, decimal_places=2)

class payment(models.Model):
    paymentId = models.AutoField(primary_key=True)
    transaction = models.ForeignKey(transaction, on_delete=models.CASCADE)
    paymentMethod = models.CharField(max_length=50)
    amount = models.DecimalField(max_digits=10, decimal_places=2)

class onlineOrder(models.Model):
    transaction = models.OneToOneField(transaction, on_delete=models.CASCADE, primary_key=True)
    carrier = models.CharField(max_length=50)
    trackingNumber = models.CharField(max_length=50)
    shipDate = models.DateField()
    estimateArrival = models.DateField()
    shippingStatus = models.CharField(max_length=50)
    shippingAddress = models.CharField(max_length=255)

class purchaseOrder(models.Model):
    purchaseOrderID = models.AutoField(primary_key=True)
    vendor = models.ForeignKey(vendor, on_delete=models.CASCADE)
    product = models.ForeignKey(product, on_delete=models.CASCADE)
    qtyPo = models.IntegerField()
    orderDate = models.DateField()
    status = models.CharField(max_length=50)
    unitCost = models.DecimalField(max_digits=10, decimal_places=2)
    employee = models.ForeignKey(employee, on_delete=models.CASCADE)

class vendorInvoice(models.Model):
    invoiceId = models.AutoField(primary_key=True)
    vendor = models.ForeignKey(vendor, on_delete=models.CASCADE)
    purchaseOrder = models.ForeignKey(purchaseOrder, on_delete=models.CASCADE)
    paymentStatus = models.CharField(max_length=50)
    paymentDate = models.DateField()
    dueDate = models.DateField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    
