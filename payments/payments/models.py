from django.db import models

class Services(models.Model): 
    TYPE_CHOICE = [
        ('MR', 'Mobile Recharge'),
        ('DR', 'DTH Recharge'),
        ('IP', 'Insurance Payment')
    ]
    MODE_CHOICE = [
        ('U', 'UPI'),
        ('IB', 'Internet Banking'),
        ('CP', 'Card')
    ]

    type = models.CharField(max_length=2, choices=TYPE_CHOICE)
    mode = models.CharField(max_length=2 ,choices=MODE_CHOICE)
    company = models.CharField(max_length=100)

    def __str__(self): 
        return self.type



class ServiceUser(models.Model):
    GENDER_CHOICE = [
        ('M', 'MALE'),
        ('F', 'FEMALE'),
        ('N', 'NOT PREFER')
    ]
    name = models.CharField(max_length=30)
    email = models.EmailField()
    age = models.IntegerField()
    gender = models.CharField(max_length=1 ,choices=GENDER_CHOICE)
    service = models.ManyToManyField(Services, related_name="service")

    def __str__(self): 
        return self.name

class Subscription(models.Model): 
    user = models.ForeignKey(ServiceUser, on_delete=models.CASCADE)
    services = models.ForeignKey(Services, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=7, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)