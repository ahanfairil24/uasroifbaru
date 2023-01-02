from django.shortcuts import render, redirect
from .models import mama
from .forms import mamaform


# Create your views here.

def mamaviews(request):
    mama_form = mamaform(request.POST or None)
    if request.method == 'POST':
        if mama_form.is_valid:
            simpan_data = mama.objects.create(
                asilah = mama_form.cleaned_data.get('asilah'),
                jawaban = mama_form.cleaned_data.get('jawaban'),
                iktirod = mama_form.cleaned_data.get('iktirod'),
                keputusan = mama_form.cleaned_data.get('keputusan'),
            )
            return redirect('mama:mamaList')
    context = {
        'form':mama_form
    }
    return render(request, 'mama.html', context)
