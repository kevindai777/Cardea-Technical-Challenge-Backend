from django.db import models


class Example(models.Model):
    example = models.TextField()

    def __str__(self):
        return self.example







class Job(models.Model):
    title = models.CharField(max_length=100)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.title



class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.name

class JobCategory(models.Model):
    jobID = models.IntegerField(max_length=100)
    categoryID = models.IntegerField(max_length=100)

    class Meta:
        ordering = ['id']
    
    def __str__(self):
        return self.jobid
