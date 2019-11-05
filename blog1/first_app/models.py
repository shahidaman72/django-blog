from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class blog(models.Model):
    title=models.CharField(max_length=255)
    pub_date=models.DateTimeField()
    body=models.TextField()
    image=models.ImageField(upload_to='images/')

    hunter=models.ForeignKey(User,on_delete=models.CASCADE)
    def summary(self):
        return self.body[:120]
    def pub_date_pr(self):
        return self.pub_date.strftime('%b %e, %Y')
    def __str__(self):
        return self.title
class index(models.Model):
    title1=models.CharField(max_length=255)
    pub_date1=models.DateTimeField()
    body1=models.TextField()
    image1=models.ImageField(upload_to='images/')

    hunter1=models.ForeignKey(User,on_delete=models.CASCADE)
    def summary1(self):
        return self.body1[:120]
