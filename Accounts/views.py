from django.shortcuts import render,redirect
from .forms import RegistrationForm
from .models import User
from django.contrib import messages,auth
from django.utils.http import urlsafe_base64_decode
from django.contrib.auth.tokens import default_token_generator
from .utils import mailresetpassword
# Create your views here.

def UserRegistraionform(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            # checkbox = request.POST('chkbox')

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
            return redirect('index')
        else:
            messages.error(request,'wrong user and password')
            return redirect('login')
    return render(request,'Accounts/login.html')

def UserLogout(request):
    auth.logout(request)
    return redirect('login')

def forgetPassword(request):
    if request.method == 'POST':
        reqemail = request.POST['email']

        if User.objects.filter(email=reqemail).exists():
            user = User.objects.get(email=reqemail)
            print(f'user mail:{user}')
        #send verification email
            
            mailresetpassword(request,user)
            messages.success(request,'Please check your gmail for reset password')
            return redirect('login')
        else:
            messages.error(request,'You did not have email address')
            return redirect('registrationform')
    return render(request,'Accounts/forgotpassword.html')

def resetPasswordValidate(request,uidb64,token):
    #decode the resetpassword link
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = User._default_manager.get(pk=uid)
    except(TypeError,ValueError,OverflowError,User.DoesNotExist):
        user = None
    if user is not None and default_token_generator.check_token(user,token):
        request.session['uid'] = uid
        messages.info(request,'Please reset your password')
        return redirect('resetpassword')
def resetPassword(request):
    if request.method == 'POST':
        password = request.POST['password']
        confirmpassword = request.POST['cpassword']

        if password == confirmpassword:
            # check the user from session
            uid = request.session.get('uid')
            user = User.objects.get(pk=uid)
            user.set_password(password)
            user.is_active=True
            user.save()
            messages.success(request,'Password reset done!')
            return redirect('login')
        else:
            messages.error(request,'password did not match')
            return redirect('resetpassword')
    return render(request,'Accounts/resetpassword.html')
