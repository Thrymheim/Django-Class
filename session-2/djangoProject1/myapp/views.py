#When we wanna use HTML contact we use render
from django.shortcuts import render

#Simple day for saying our name
def interoduce(request):
    #When we wanna use our contact in the HTML page we use context
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
