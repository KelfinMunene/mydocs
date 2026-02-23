from django.shortcuts import render
from .models import Document
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request, 'home.html')


def document_list(request):
    documents = Document.objects.filter(visibility='public')

    for doc in documents:
        name = doc.file.name.lower()
        doc.is_image = name.endswith(('.png', '.jpg', '.jpeg', '.gif'))
        doc.is_pdf = name.endswith('.pdf')

    return render(request, 'documents.html', {'documents': documents})


@login_required
def private_documents(request):
    documents = Document.objects.filter(
        visibility='private',
        user=request.user
    )
    return render(request, 'private_documents.html', {'documents': documents})
