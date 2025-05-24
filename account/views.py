from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login , logout, update_session_auth_hash
from account.forms import LoginUserForm, NewUserForm

def user_login(request):
    if request.user.is_authenticated and "next" in request.GET:
        return redirect(request, "account/login.html",{ "error":"Bu sayfayı görüntülemek için admin girişi yapmalısınız"})
    
    if request.method == "POST":
        form = LoginUserForm(request, data= request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')


            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                login(request, user)
                
                nextURL = request.GET.get("next",None)
                if nextURL is None:
                    return redirect("index")
                else:
                    return redirect(nextURL)
            else:
                return render(request, 'account/login.html', {'form': form })
        else:
            return render(request, 'account/login.html', {'form': form })
    else:
        form = LoginUserForm()
        return render(request, 'account/login.html', {'form': form })

def user_register(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)

        if form.is_valid():
            form.save()
            
            username= form.cleaned_data['username']
            password= form.cleaned_data['password1']
            user = authenticate(request, username=username, password=password)
            login(request, user)
            return redirect("index")
        else:
            return render(request, 'account/register.html', {'form': form})
    else:
        form = NewUserForm()
        return render(request, 'account/register.html', {'form': form})
    
def user_logout(request):
    
    logout(request)
    return redirect("index")