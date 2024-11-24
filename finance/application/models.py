

# # Create your models here.
# from django.db import models

# # Custom User model (if you're not using Django's built-in User model)
# class User(models.Model):
#     app_label = 'application'
#     name = models.CharField(max_length=100)
#     email = models.EmailField(unique=True)
#     username = models.CharField(max_length=100, unique=True)

#     def __str__(self):
#          return self.username

# # # Transaction model
# class Transaction(models.Model):
#      app_label = 'application'
#      TRANSACTION_TYPES = (
#          ('income', 'Income'),
#          ('expense', 'Expense'),
#      )

#      category = models.CharField(max_length=100)
#      amount = models.DecimalField(max_digits=10, decimal_places=2)
#      date = models.DateField()
#      description = models.TextField(blank=True, null=True)
#      type = models.CharField(max_length=7, choices=TRANSACTION_TYPES)

#      def __str__(self):
#          return f"{self.category} - {self.amount}"
from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    user_name = models.CharField(max_length=100)

    def __str__(self):
        return self.user_name

class Transaction(models.Model):
    TRANSACTION_TYPES = [
        ('Income', 'Income'),
        ('Expense', 'Expense')
    ]
    type = models.CharField(max_length=7, choices=TRANSACTION_TYPES)
    category = models.CharField(max_length=50)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.type}: {self.category} - {self.amount}"


