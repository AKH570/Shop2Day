from django.shortcuts import render,redirect
from .forms import RegistrationForm
from .models import User
from django.contrib import messages,auth
# Create your views here.

def UserRegistraionform(request):
    if request.method == 'POST':
       #print(request.POST)
        form = RegistrationForm(request.POST)
        if form.is_valid():
            # password = form.cleaned_data['password']
            # user = form.save(commit=False)
            # user.set_password(password)
            # user.role = User.CUSTOMER
            # print(user)
            # user.save()
            # print(user)

            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            user = User.objects.create_user(first_name=first_name,last_name=last_name,username=username,email=email,password=password)
            user.save()
            messages.success(request, "Thank you for registration!")
            return redirect('registrationform')
        else:
            pass
    else:
        form=RegistrationForm()
    context={
        'form':form
    }
    return render(request,'Accounts/registrationform.html',context)

def UserLogin(request):
    if request.method =='POST':
        email = request.POST['email']
        password = request.POST['password']

        user = auth.authenticate(email=email,password=password)

        if user is not None:
            auth.login(request,user)
            # messages.success(request,'')
            return redirect('store')
        else:
            messages.error(request,'wrong user and password')
            return redirect('login')
    return render(request,'Accounts/login.html')

def UserLogout(request):
    auth.logout(request)
    return redirect('login')