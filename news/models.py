from django.db import models

class Categories(models.Model):
    name = models.CharField("Nom", max_length=200)
    content = models.TextField("Description")
    CHOICES = (
        ('NEWS', 'News'),
        ('PAGE', 'Page'),
        ('CATFORUM', 'Catégorie Forum'),
    )
    type = models.CharField(max_length=100, choices=CHOICES, default="NEWS")
    created_at = models.DateTimeField()
    
    class Meta:
        db_table = 'categories'
    
    def __str__(self):
        return self.name

class News(models.Model):
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField("date de publication")
    updated_at = models.DateTimeField("Date de modification")
    
    class Meta:
        db_table = 'news'
    
    def __str__(self):
        return self.name
    
