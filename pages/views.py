from django.shortcuts import render, redirect
from .models import Content
from .forms import ContentCreateForm
from django.contrib.auth.decorators import user_passes_test
def isAdmin(user):
    return user.is_superuser

def index(request):
    
        contents = Content.objects.filter(category__slug='blog-text').filter(is_active=True)
        return render(request, 'pagess/index.html', {'contents': contents})

@user_passes_test(isAdmin)
def create_blog(request):
    if request.user.is_superuser:
        if request.method == "POST":
            form = ContentCreateForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()          
                return redirect('/')
        else:
            form = ContentCreateForm()
        return render(request, 'pagess/create_blog.html', {'form':form})
    else:
        return redirect('/')
