from django.db import models
from uploader.settings import BASE_DIR

class Arquivo(models.Model):

    tipos_de_arquivo = (
        ('livro', 'Livro'),
        ('cd', 'CD'),
        ('vinil', 'Vinil'),
        ('mp3', 'MP3'),
        ('mp4', 'MP4'),
        ('filme', 'Filme'),
        ('dvd', 'DVD'),
        ('blu-ray', 'Blu-Ray')
    )
    tipo = models.CharField("tipo do arquivo", max_length=50, choices=tipos_de_arquivo)

    def __str__(self):
        return self.tipo
    
    class Meta:
        ordering = ['tipo']


class Midia(models.Model):
    
    tipos_de_midia = (
        ('fisica', 'Fisica'),
        ('digital', 'Digital')
    )

    tipo = models.CharField("tipo da midia", max_length=50, choices=tipos_de_midia)

    def __str__(self):
        return self.tipo


class Upload(models.Model):
    nome = models.CharField(max_length=50)
    descricao = models.CharField(max_length=50, null=True, blank=True)
    arquivo = models.FileField(upload_to=BASE_DIR + '/app/static/files', max_length=100, blank=True, null=True)
    created_at = models.DateTimeField( auto_now=False, auto_now_add=True)
    emprestado = models.BooleanField(null=True, blank=True)
    emprestado_name = models.CharField(null=True, blank=True, max_length=50)
    emprestado_email = models.EmailField(max_length=254,blank=True, null=True)
    edited_at = models.DateTimeField(auto_now=True, auto_now_add=False)
    size = models.FloatField(null=True, blank=True)
    old_name = models.CharField(max_length=150, null=True, blank=True)
    tipo_de_midia = models.ForeignKey(Midia, verbose_name="tipo de midia", on_delete=models.CASCADE)
    tipo_de_arquivo = models.ForeignKey(Arquivo, verbose_name="tipo de arquivo", on_delete=models.CASCADE)

    def __str__(self):
        return self.nome
    
    class Meta:
        ordering = ['created_at']