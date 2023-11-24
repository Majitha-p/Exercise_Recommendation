from django.db import models
from django.db import models
from django.contrib.auth.models import User 
from datetime import datetime

# Create your models here.

class Injury(models.Model):
    type = models.CharField(max_length=20)

    def __str__(self):
        return self.type

class Profile(models.Model):
    GENDER_CHOICES = (
        ('male', 'Male'),
        ('female', 'Female'),        
    )
    USER_TYPES = (
        ('beginner', 'beginner'),
        ('intermediate', 'intermediate'),
        ('advanced', 'advanced'),
    )

    FITNESS_GOALS = (
        ('weightloss', 'Wwightloss'),
        ('musclebuilding', 'musclebuilding'),
        ('fitness', 'fitness'),
    )

    SLEEPING_HOURS_CHOICES = (
        ('morethan6', 'More than 6 hours'),
        ('lessthan6', 'Less than 6 hours'),
    )

    USER_SURGERY_CHOICES = (
        ('Nosurgery', 'No surgery'),
        ('minorsurgery', 'Minor Sugery'),
        ('majorsurgery2to4', 'Major Surgery (2-4 months ago)' ),
        ('majorsurgery6' , 'Major Surgery (6 months ago)' ),
    )

    

    INJURY_CHOICES = (
        ('head', 'head'),
        ('hand', 'hand'),
        ('stomach', 'stomach'),
        ('leg', 'leg'),
    )

    PREGNANCY_STATUS_CHOICES = (
        ('nopregnant', 'No'),
        ('pregnant', 'Pregnant'),
        ('postpregnancy', 'Post pregnancy'),
    )
    

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    mobile = models.CharField(max_length=15)
    gender = models.CharField(max_length=20, choices=GENDER_CHOICES, default='male')
    dob = models.DateField()
    age = models.IntegerField(default=0)
    weight = models.DecimalField(max_digits=5, decimal_places=2)       
    usertype = models.CharField(max_length=20, choices=USER_TYPES, default='beginner')
    fitnessgoal = models.CharField(max_length=20, choices=FITNESS_GOALS,  default='weightloss' )
    sleepinghours = models.CharField(max_length=20, choices=SLEEPING_HOURS_CHOICES , default='morethan6')
    diabetes = models.BooleanField()
    heartdisease = models.BooleanField()
    allergy = models.BooleanField()
    surgery = models.CharField(max_length=20, choices=USER_SURGERY_CHOICES,null=True,blank=True)
    injuries = models.ManyToManyField('Injury', choices=INJURY_CHOICES,  blank=True)
    pregnancy = models.CharField(max_length=20, choices=PREGNANCY_STATUS_CHOICES,null=True,blank=True)
    def get_injuries_list(self):
        return list(self.injuries.all().values_list('type', flat=True))
    def save(self, *args, **kwargs):
        # Calculate age from date of birth
        if self.dob:
            today = datetime.today()
            age = today.year - self.dob.year - ((today.month, today.day) < (self.dob.month, self.dob.day))
            self.age = age
        super().save(*args, **kwargs)
# class Injured(models.Model):
#     name = models.CharField(max_length=50)

   
    # def __str__(self):        
    #     return self.name
    


class Exercise(models.Model):
    
    name = models.CharField(max_length=255)
    description = models.TextField()
    category = models.CharField(max_length=50)
    duration_minutes = models.PositiveIntegerField()
    calories_burned = models.PositiveIntegerField()

    def __str__(self):
        return self.name
  
