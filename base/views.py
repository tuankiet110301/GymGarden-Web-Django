from django.shortcuts import render
from register.forms import registerForm
from hitcount.views import HitCountDetailView
import datetime
from register.forms import registerForm
# Create your views here.



def faq(request):
    return render(request, 'FAQ.html')


def homepage(request):
    form = registerForm()
    if request.method == 'POST':
        form = registerForm(request.POST)
        if form.is_valid():
            print('Save')
            print(datetime.datetime.now())
            print(form)
            form.save()
    else:
        form = registerForm()
    return render(request, 'index.html', {'form': form})


class Hit_count(HitCountDetailView):
    template_name = 'index.html'
    slug_field = 'slug'
    count_hit = True




def goitap(request):
    if request.method == 'POST':
        form = registerForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            form = registerForm()
        return render(request, 'goitap.html', {'forms': form})
