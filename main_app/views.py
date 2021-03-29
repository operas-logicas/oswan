from django.contrib.auth import authenticate, get_user_model, login, logout
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import Motorcycle, Favorite
from .forms import AddMotorcycle, LoginForm

# Create your views here.
def index(request):
    motorcycles = Motorcycle.objects.all()
    favs_int = []
    likes = 0
    if request.user.is_authenticated:
        favorite = Favorite.objects.get(user=request.user)
        if favorite is not None:
            favs = favorite.favs.split()
            favs_int = list(map(int, favs))
            likes = favorite.likes
    form = AddMotorcycle()
    return render(request, 'index.html', {'motorcycles': motorcycles, 'form': form, 'favs': favs_int, 'likes': likes})

def like_motorcycle(request):
    motorcycle_id = request.POST.get('motorcycle_id', None)
    favs = []
    likes = 0
    if motorcycle_id:
        motorcycle = Motorcycle.objects.get(id=int(motorcycle_id))
        if motorcycle is not None:
            favorite = Favorite.objects.get(user=request.user)
            if favorite is not None:
                favs = favorite.favs.split()
                if motorcycle_id in favs:
                    # Exists already so remove from favorites
                    favs.remove(motorcycle_id)
                    favorite.favs = ' '.join(favs)
                    likes = favorite.likes - 1
                    favorite.likes = likes
                    favorite.save()
                    return HttpResponse('remove')
                else:
                    # Otherwise new so add to favorites
                    favs.append(motorcycle_id)
                    favorite.favs = ' '.join(favs)
                    likes = favorite.likes + 1
                    favorite.likes = likes
                    favorite.save()
                    return HttpResponse('add')

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            u = form.cleaned_data['username']
            p = form.cleaned_data['password']
            user = authenticate(username=u, password=p)
            if user is not None:
                if user.is_active:
                    # Authentication successful so login
                    login(request,user)
                    return HttpResponseRedirect('/')
        # Invalid username and password
        messages.error(request, 'Invalid username and/or password')
        return HttpResponseRedirect('/login/')
    else:
        # Display login form if GET request
        form = LoginForm()
        return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')

def post_motorcycle(request):
    form = AddMotorcycle(request.POST, request.FILES)
    if form.is_valid():
        motorcycle = form.save(commit=False)
        motorcycle.user = request.user
        motorcycle.save()
    return HttpResponseRedirect('/')

def product_details(request, motorcycle_id):
    motorcycle = Motorcycle.objects.get(id=motorcycle_id)
    favs_int = []
    likes = 0
    if request.user.is_authenticated:
        favorite = Favorite.objects.get(user=request.user)
        if favorite is not None:
            favs = favorite.favs.split()
            favs_int = list(map(int, favs))
            likes = favorite.likes
    return render(request, 'product-details.html', {'motorcycle': motorcycle, 'favs': favs_int, 'likes': likes})

def profile(request, username):
    User = get_user_model()
    user = User.objects.get(username=username)
    motorcycles = Motorcycle.objects.filter(user=user)
    favs_int = []
    likes = 0
    if request.user.is_authenticated:
        favorite = Favorite.objects.get(user=request.user)
        if favorite is not None:
            favs = favorite.favs.split()
            favs_int = list(map(int, favs))
            likes = favorite.likes
    return render(request, 'profile.html', {'username': username, 'motorcycles': motorcycles, 'favs': favs_int, 'likes': likes})
