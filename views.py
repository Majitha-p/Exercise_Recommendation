from django.shortcuts import render ,redirect
from django.contrib.auth.models import User
from django.contrib import auth
# from . import models
# Create your views here.
def index(request):
    return render(request, 'index.html')

def signup(request):
    message=""
    if request.method == 'POST':
        # Handle signup form submission
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        if username and email and password:

        
        # Create user (you may want to add additional checks/validation)
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()
            message="sign up success"

            return redirect('login')
        else:
            message="sign up failed"
        # Redirect to login page
    else:
        
        return render(request, 'signup.html',{"message":message,"name":"akhil"})


def login(request):
    print(request.user.id)
    if request.method == 'POST':
        # Handle login form submission
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        
        if user is not None:
            auth.login(request, user)
            
            # Redirect to some page after successful login
            return redirect('register')
        else:
            # Handle invalid login
            return render(request, 'login.html', {'error': 'Invalid credentials'})
    else:
        return render(request, 'login.html')


from django.http import HttpResponse
from .models import Profile 
from django.contrib.auth.decorators import login_required
from .models import Injury
from datetime import datetime

@login_required  # To ensure users are logged in to access this view
def register(request):
    if request.method == 'POST':
        # Extract form data from POST request
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        mobile = request.POST.get('mobile')
        gender = request.POST.get('gender')  
        dob = request.POST.get('dob')
        weight = request.POST.get('weight')
        usertype = request.POST.get('usertype')
        fitnessgoal = request.POST.get('fitnessgoal')
        sleepinghours = request.POST.get('sleepinghours')
        diabetes = request.POST.get('diabetes' , False) == 'True'
        heartdisease = request.POST.get('heartdisease' , False) == 'True'
        allergy = request.POST.get('allergy' , False) == 'True'
        surgery = request.POST.get('surgery' )
        pregnancy = request.POST.get('pregnancy')
        selected_injuries = request.POST.getlist('injuries[]')

        dob_date = datetime.strptime(dob, '%Y-%m-%d')
        today = datetime.today()
        age = today.year - dob_date.year - ((today.month, today.day) < (dob_date.month, dob_date.day))

        # Check if a profile already exists for the user
        existing_profile = Profile.objects.filter(user=request.user).exists()
        if existing_profile:
            # User already has a profile, handle this case (e.g., redirect with a message)
            return render(request, 'register.html', {'message': 'You already have a profile.'})
        
        # Create a new profile for the logged-in user
        
        my_user_profile = Profile.objects.create(
            user_id=request.user.id,
            firstname=firstname,
            lastname=lastname,
            mobile=mobile,
            gender = gender, 
            dob=dob_date,
            age=age,
            weight=weight,
            usertype=usertype,
            fitnessgoal=fitnessgoal,
            sleepinghours=sleepinghours,
            diabetes=diabetes,
            heartdisease=heartdisease,
            allergy=allergy,
            surgery=surgery,
            # injuries=inj,
            pregnancy=pregnancy
        )
        for injury_type in selected_injuries:
            injury, _ = Injury.objects.get_or_create(type=injury_type)
            my_user_profile.injuries.add(injury)
            
        #  get_or_create   
        my_user_profile.save()
        return redirect('rec')

    return render(request, 'register.html')

# def rec(request):
    
#     return render(request,'rec.html')
from .models import Exercise

def rec(request):
    # Get user attributes from the submitted form
    dob = request.POST.get('dob')
    weight = request.POST.get('weight')
    usertype = request.POST.get('usertype')
    fitnessgoal = request.POST.get('fitnessgoal')
    sleepinghours = request.POST.get('sleepinghours')
    diabetes = request.POST.get('diabetes' , False) == 'True'
    heartdisease = request.POST.get('heartdisease' , False) == 'True'
    allergy = request.POST.get('allergy' , False) == 'True'
    # injuries_id = request.POST.getlist('injuries')
    surgery = request.POST.get('surgery' )
    pregnancy = request.POST.get('pregnancy')
    selected_injuries = request.POST.getlist('injuries[]')

    # Example: Filtering exercises based on user attributes
    # Modify this based on your actual logic and fitness recommendations
    if fitnessgoal == 'weightloss':
        # Recommend exercises for weight loss (adjust criteria as needed)
        recommended_workouts = Exercise.objects.filter(category__icontains='cardio')

    elif fitnessgoal == 'musclebuilding':
        # Recommend exercises for muscle building (adjust criteria as needed)
        recommended_workouts = Exercise.objects.filter(category__icontains='strength')

    elif fitnessgoal == 'fitness':
        # Recommend general fitness exercises (adjust criteria as needed)
        recommended_workouts = Exercise.objects.all()

    # Pass recommended workouts to the template
    context = {
        'recommended_workouts': rec,
        # You can pass other relevant data to the template here
    }

    return render(request, 'rec.html', context)
