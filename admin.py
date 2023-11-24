from django.contrib import admin
from .models import *
# Register your models here.


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):    
    list_display = ('user', 'firstname', 'lastname', 'mobile', 'dob','age','gender', 'weight','usertype', 'fitnessgoal', 'sleepinghours', 'diabetes', 'heartdisease', 'allergy' , 'surgery', 'pregnancy' , 'get_injuries_display')
    search_fields = ['firstname', 'lastname', 'mobile','gender','usertype', 'fitnessgoal', 'sleepinghours', 'diabetes', 'heartdisease', 'allergy', 'surgery', 'pregnancy']
    
    def get_injuries_display(self, obj):
        return ', '.join(obj.get_injuries_list())
    
    # def display_injuries(self, obj):
    #     return ", ".join([injury.name for injury in obj.injuries.all()])


# @admin.register(Injured)
# class injuriesAdmin(admin.ModelAdmin): 
#        list_display=('name','discriotion')



@admin.register(Exercise)
class ExerciseAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'duration_minutes', 'calories_burned')
    search_fields = ('name', 'category')
