from django.db import models


from django.contrib.auth.models import User
# Create your models here.
# Train model
class Train(models.Model):                   
    name = models.CharField(max_length=100)
    number = models.CharField(max_length=100)
    source = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    departure_time = models.TimeField(max_length=100)
    arrival_time = models.TimeField(max_length=100)
    status = models.CharField(max_length=100)
    
    def __str__(self):
        return "%s Train" % self.name

    def get_absolute_url(self):
        return reverse('home-book', kwargs={'pk':self.pk})
    

# class Seat(models.Model):
#     seat_id = models.CharField(max_length=100)
#     train = models.ForeignKey(Train,on_delete =models.CASCADE)
#     status = models.CharField(max_length=100)
#     date = models.DateField()
  
#     def __str__(self):
#         return "%s's " % self.train.name + self.seat_id

#ticket model
class Ticket(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    pnr = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    train = models.ForeignKey(Train,on_delete=models.CASCADE)
    passenger_name = models.CharField(max_length=100)
    age = models.CharField(max_length=100)
    date = models.DateField()
    
    def __str__(self):
        return "%s " % self.passenger_name + self.pnr
