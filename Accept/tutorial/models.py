from django.db import models
from ckeditor.fields import RichTextField


class ReadingEnglish(models.Model):
    title = models.CharField(max_length=255)
    description = RichTextField()

    def __str__(self):
        return self.title


class GrammarEnglish(models.Model):
    title = models.CharField(max_length=255)
    description = RichTextField()

    def __str__(self):
        return self.title


class WritingEnglish(models.Model):
    title = models.CharField(max_length=255)
    guide = RichTextField()

    def __str__(self):
        return self.title


class Pronunciation(models.Model):
    title = models.CharField(max_length=255)
    description = RichTextField()

    def __str__(self):
        return self.title


class Fun(models.Model):
    title = models.CharField(max_length=255)
    description = RichTextField()

    def __str__(self):
        return self.title


class Course(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='tutorial/%y/%m/%d')
    description = RichTextField(null=True, blank=True)

    def __str__(self):
        return self.name
