from django.db import models
from django import forms
from django.core.files import File
from urllib import request
import os
from django.utils import timezone

# Create your models here.

Meal = [
        'Breakfast',
        'Lunch',
        'Dinner',
        'Snack',
        ]

class Recipe(models.Model):
    RecipeId = models.AutoField(primary_key=True)
    RecipeName = models.CharField(max_length=100)
    RecipeMeal = models.CharField(max_length=30)
    RecipeDateAdded = models.DateField(default=timezone.now())
    RecipeDateUpdated = models.DateField(default=timezone.now())
    RecipePhoto_name = models.CharField(max_length=100)
    RecipePhoto_file = models.ImageField(upload_to='images')
    RecipePhoto_url = models.URLField()
    
    def get_remote_image(self):
        if self.RecipePhoto_url and not self.RecipePhoto_file:
            result =  request.urlretrieve(self.RecipePhoto_url)
            self.RecipePhoto_file.save(
                os.path.basename(self.RecipePhoto_url),
                File(open(result[0], 'rb'))
            )
            self.save()

        
    # ModelChoiceField(queryset=..., to_field_name='Meal', empty_label=None)
    # def select_RecipeMeal(self, type, index, subindex=None, attrs=None):
        
        # RecipeMeal = super().select_RecipeMeal(type,index, subindex, attrs)
        # if value:
        #     R
    
# class MealModelChoiceField(forms.ModelChoiceField):
#     def label_from_instance(self, obj):
#         return obj.name   

class Member(models.Model):
    MemberId = models.AutoField(primary_key=True)
    MemberFName = models.CharField(max_length=30)
    MemberLName = models.CharField(max_length=30)
    MemberDateAdded = models.DateField(default=timezone.now())
    MemberRecipes = models.CharField(max_length=100)
    MemberPhoto_name = models.CharField(max_length=100)
    MemberPhoto_file = models.ImageField(upload_to='images')
    MemberPhoto_url = models.URLField()
    
    def get_remote_image(self):
        if self.MemberPhoto_url and not self.MemberPhoto_file:
            result =  request.urlretrieve(self.MemberPhoto_url)
            self.MemberPhoto_file.save(
                os.path.basename(self.MemberPhoto_url),
                File(open(result[0], 'rb'))
            )
            self.save()