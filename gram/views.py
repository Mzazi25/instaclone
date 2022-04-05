from django.shortcuts import render,redirect
from django.http  import HttpResponse
from .forms import UserForm, CommentForm
from .models import Profile,Image,Comment
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
User = get_user_model()



# Create your views here.
@login_required(login_url='accounts/login/')
def account(request):
    if request.method == 'POST':
        data = request.POST
        image = request.FILES.get('image')

        post = Image.objects.create(
            description = data['description'],
            image = image
        )
        return redirect('account')
    
    all = User.objects.all()
    images=Image.objects.all()

    user = request.user
    return render(request,'account.html', {"images":images,"all":all,"user":user})
@login_required(login_url='accounts/login/')
def home(request):
    if request.method == 'POST':
        data = request.POST            
        profile = Profile.objects.create(
            description = data['description'],
            username = request.username,
        )
        return redirect('home')
    username = request.username
    profile = Profile.objects.filter(username=username).all()
         
    return render(request,'home.html',{"profile":profile})
def search_results(request):

    if 'image' in request.GET and request.GET["image"]:
        search_term = request.GET.get("image")
        searched_category = Image.search_by_title(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"category": searched_category})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})