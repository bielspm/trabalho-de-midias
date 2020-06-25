from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from django.http import HttpResponseNotAllowed
from app.forms import UploadForm
from app.models import Upload, Midia, Arquivo
from uploader import settings
from django.contrib import messages

def home(request):
    return render(request, 'app/base.html')

def store(request):
    if request.method == "GET":
        return render(request, "app/create_upload.html")
    else:
        upload_form = UploadForm(request.POST, request.FILES)
        upload_form.emprestado = False
        if request.POST['emprestado']:
            upload_form.emprestado = True
        if request.FILES:
            upload_form.size = request.FILES['arquivo'].size
            upload_form.old_name = request.FILES['arquivo'].name

        if upload_form.is_valid():
            upload_form.save()
            messages.success(request, "O registro foi criado com sucesso!!")
            return redirect('store')
        else:
            messages.error(request, "Há um erro no formulario")
            return redirect('store')
            

def edit(request, upload_id):
    if request.method == "GET":
        upload = get_object_or_404(Upload, id=upload_id)
        upload_form = UploadForm(instance=upload)
        context = {
            'upload' : upload,
            'form' : upload_form
        }
        return render(request, "app/edit_upload.html", context)
    else:
        upload_form = UploadForm(request.POST)
        if upload_form.is_valid():
            upload_form.save()
            messages.success(request, "O registro foi atualizado com sucesso!!")
            return redirect('show', upload_id=upload_id)
        else:
            messages.error(request, "Algo deu errado!!")
            return redirect('show', upload_id=upload_id)

def delete(request, upload_id):
    upload = get_object_or_404(Upload, id=upload_id)
    try:
        upload.delete()
    except Exception as err:
        messages.error(request, "Algo deu errado!!")
        return redirect('index')
    else:
        messages.success(request, "Registro excluido com sucesso!!")
        return redirect('index')


def show(request, upload_id):
    if request.method == "GET":
        upload = get_object_or_404(Upload, id=upload_id)
        return render(request, "app/upload.html", {'upload':upload})


def index(request):
    if request.method == "GET":
        if not request.GET:
            uploads = Upload.objects.all()
            tipo_midias = Midia.objects.all()
            tipo_arquivos = Arquivo.objects.all()
            context = {
                'uploads' : uploads,
                'tipo_midias' : tipo_midias,
                'tipo_arquivos' : tipo_arquivos
            }
        else:
            if request.GET['tipo_midia']:
                pass
            if request.GET['tipo_arquivo']:
                pass
        return render(request, 'app/list_upload.html', context)