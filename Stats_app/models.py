from django.db import models

from User_IP.models import IPAddress


class HitModel(models.Model):
    movie = models.ForeignKey('Movie_app.Movie',on_delete=models.CASCADE,blank=True,null=True)
    series = models.ForeignKey('Series_app.Series',on_delete=models.CASCADE,blank=True,null=True)
    ip_address = models.ForeignKey(IPAddress,on_delete=models.CASCADE,blank=True,null=True)
    created = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        if self.movie:
            return f'{self.movie}({self.ip_address}) create in :{self.created.ctime()}'
        else:
            return f'{self.series}({self.ip_address}) create in :{self.created.ctime()}'