from django.db import models

import os

# Create your models here.
class Landing(models.Model):
  title = models.CharField(max_length=150)
  content = models.TextField()

  def __str__(self):
    return self.title

class Skill(models.Model):
  skill = models.CharField(max_length=150)
  percent = models.PositiveSmallIntegerField()
  knowledge = models.TextField(blank=True)

  def __str__(self):
    return self.skill

class Card(models.Model):
  imagenProject = models.ImageField(upload_to='project_images/', blank=True, null=True)
  titleProject = models.CharField(max_length=150)
  contentProject = models.TextField()
  pdfProject = models.FileField(upload_to='project_pdfs/', blank=True, null=True)

  def __str__(self):
    return self.titleProject
