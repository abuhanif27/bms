from django.db import models


# Create your models here.
class Books(models.Model):
    class GenreChoice(models.TextChoices):
        FICTION = 'fic', 'Fiction'
        NONFICTION = 'nfic', 'Non-Fiction'
        MYSTERY = 'mys', 'Mystery'
        BIOGRAPHY = 'bio', 'Biography'
        Fantasy = 'fan', 'Fantasy'
        SCIENCE = 'sci', 'Science'
        HISTORY = 'his', 'History'

    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    description = models.TextField()
    genre = models.CharField(max_length=4, choices=GenreChoice)
    published_date = models.DateField()
    added_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"'{self.title}' by {self.author}"
