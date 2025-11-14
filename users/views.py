from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.utils.http import url_has_allowed_host_and_scheme


def user(request):
    return render(request, "index.html")


def login_user(request):
    next_url = request.GET.get("next") or request.POST.get("next")
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Validate the next URL to prevent open redirect vulnerabilities
            if next_url and url_has_allowed_host_and_scheme(
                next_url, allowed_hosts=request.get_host()
            ):
                return redirect(next_url)
            else:
                return redirect("/inventory")
        else:
            # Handle invalid login
            return render(
                request,
                "login.html",
                {"error": "Invalid credentials", "next": next_url},
            )
    return render(request, "login.html", {"next": next_url})


def logout_user(request):
    logout(request)
    return redirect("login")


def register_user(request):
    storage = messages.get_messages(request)
    storage.used = True
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")

        # --- simple validations ---
        if not username or not password1:
            messages.error(request, "Username and password are required.")
            return redirect("register")

        if password1 != password2:
            messages.error(request, "Passwords do not match.")
            return redirect("register")

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already taken.")
            return redirect("register")

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already in use.")
            return redirect("register")

        user = User.objects.create_user(
            username=username,
            password=password1,
            email=email,
        )

        login(request, user)
        return redirect("dashboard")

    return render(request, "register.html")
