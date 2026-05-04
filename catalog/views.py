from django.shortcuts import render


def index(request):
    return render(request, 'catalog/index.html')


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        context = {'name': name}

        return render(request, "catalog/message_received.html", context)

    return render(request, 'catalog/contacts.html')
