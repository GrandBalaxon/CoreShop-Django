from django.shortcuts import render

from catalog.models import ContactInfo


def index(request):
    return render(request, 'catalog/index.html')


def contacts(request):
    contact_info = ContactInfo.objects.get(id=1)
    context = {'contact_info': contact_info}

    if request.method == 'POST':
        name = request.POST.get('name')
        context['name'] = name

        return render(request, "catalog/message_received.html", context)

    return render(request, 'catalog/contacts.html', context)
