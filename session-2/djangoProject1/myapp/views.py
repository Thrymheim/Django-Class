from django.shortcuts import render

def interoduce(request):
    context = {
        'name':'maziyar',
    }
    return render(request, 'name.html', context)

def about(request):
    context = {
        'name':'maziyar',
        'last_name':'kolagar',
        'age':'20',
    }
    return render(request, 'about.html', context)