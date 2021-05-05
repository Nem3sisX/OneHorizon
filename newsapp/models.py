from django.db import models

class entertain_news(models.Model):
    News_Name = models.TextField()  
    News_Info=models.TextField()
    News_Content=models.TextField()
    Destination_Image = models.TextField()  
    Date_Published=models.TextField()
    News_Url=models.TextField()
    class Meta:  
        db_table = "entertain"

class business_news(models.Model):
    News_Name = models.TextField()  
    News_Info=models.TextField()
    News_Content=models.TextField()
    Destination_Image = models.TextField()  
    Date_Published=models.TextField()
    News_Url=models.TextField()
    class Meta:  
        db_table = "business"

class general_news(models.Model):
    News_Name = models.TextField()  
    News_Info=models.TextField()
    News_Content=models.TextField()
    Destination_Image = models.TextField()  
    Date_Published=models.TextField()
    News_Url=models.TextField()
    class Meta:  
        db_table = "general"

class sports_news(models.Model):
    News_Name = models.TextField()  
    News_Info=models.TextField()
    News_Content=models.TextField()
    Destination_Image = models.TextField()  
    Date_Published=models.TextField()
    News_Url=models.TextField()
    class Meta:
        db_table = "sports"

class technology_news(models.Model):
    News_Name = models.TextField()  
    News_Info=models.TextField()
    News_Content=models.TextField()
    Destination_Image = models.TextField()  
    Date_Published=models.TextField()
    News_Url=models.TextField()
    class Meta:  
        db_table = "technology"
