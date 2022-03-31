from django.shortcuts import render,redirect
from django.http  import HttpResponse
from .forms import UserForm, CommentForm
from .models import Profile,Image, Like,Comment
from django.contrib.auth import get_user_model
User = get_user_model()


# Create your views here.

def home(request):
    if request.method == 'POST':
        data = request.POST
        image = request.FILES.get('image')

        post = Image.objects.create(
            description = data['description'],
            image = image,
            user = request.user
        )
        return redirect('home')
    
    all = User.objects.all()
    images=Image.objects.all()

    user = request.user
    return render(request,'profile/home.html', {"images":images,"all":all,"user":user})