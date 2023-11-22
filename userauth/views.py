from django.shortcuts import render, redirect
from userauth.forms import UserRegisterForm
from django.contrib.auth import login, authenticate, get_user_model
from django.contrib import messages
from .forms import EmailForm
from .forms import ProfileForm

def register_view(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            new_user = form.save()

            # Authenticate the user only if registration is successful
            email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password1")
            User = get_user_model()
            new_user = authenticate(request, username=email, password=password)

            if new_user is not None:
                login(request, new_user)
                messages.success(request, f"Hey {email}, Your account was created successfully")
                return redirect("app:home")
            else:
                messages.error(request, "Failed to authenticate user.")
    else:
        form = UserRegisterForm()

    context = {
        'form': form
    }

    # Clear messages after they have been displayed
    storage = messages.get_messages(request)
    storage.used = True

    return render(request, "userauth/sign-up.html", context)


def subscribe(request):
    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirect to the home page
            return redirect('app:home')
    else:
        form = EmailForm()

    return render(request, 'app/home.html', {'form': form})



def login_view(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            user = authenticate(request, username=email, password=None)
            if user is not None:
                login(request, user)
                messages.success(request, f"Welcome, {email}! You are now logged in.")
                return redirect('app:home')  # Redirect to the home page after successful login
            else:
                messages.error(request, f"No account found with email {email}. Please register.")
                pass
    else:
        form = ProfileForm()

    context = {'form': form}
    return render(request, 'app/profile.html', context)
