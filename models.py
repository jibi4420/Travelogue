from django.db import models

# Tour Package Model
class TourPackage(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    duration = models.IntegerField(help_text="Duration in days")
    image = models.ImageField(upload_to='tour_images/', null=True, blank=True)

    def __str__(self):
        return self.name

# Booking Model
class Booking(models.Model):
    PACKAGE_CHOICES = [
        ('family', 'Family Tour'),
        ('international', 'International Tour'),
        ('universal', 'Universal Tour'),
    ]

    TOUR_CHOICES = [
        ('kodaikanal', 'Kodaikanal'),
        ('goa', 'Goa'),
        ('brazil', 'Brazil'),
    ]

    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('cancelled', 'Cancelled'),
    ]

    package = models.CharField(max_length=20, choices=PACKAGE_CHOICES)
    tour = models.CharField(max_length=20, choices=TOUR_CHOICES)
    date = models.DateField()
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.tour}"

# Payment Model
class Payment(models.Model):
    booking = models.OneToOneField(Booking, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    card_number = models.CharField(max_length=16)
    expiry_date = models.CharField(max_length=7)
    cvv = models.CharField(max_length=4)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    paid_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Payment for {self.booking.name}"

# Refund Model
class Refund(models.Model):
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=255)
    email = models.EmailField()
    reason = models.TextField()
    refund_method = models.CharField(max_length=20, choices=[
        ('credit-card', 'Credit Card'),
        ('paypal', 'PayPal'),
        ('bank-transfer', 'Bank Transfer'),
    ])
    requested_at = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    def __str__(self):
        return f"Refund Request by {self.full_name}"


# Create your models here.
