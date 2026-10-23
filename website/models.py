from django.db import models
from django.utils import timezone
from django.utils.text import slugify

class SiteSettings(models.Model):
    institution_name = models.CharField("Nome da instituição", max_length=180, default="Instituto Superior Dom Bosco")
    tagline = models.CharField("Frase de destaque", max_length=240, default="Educar para transformar o futuro.")
    about_text = models.TextField("Texto sobre a instituição", blank=True, default="Apresente aqui a história, a missão e os valores oficiais do Instituto Superior Dom Bosco.")
    email = models.EmailField("E-mail oficial", blank=True)
    phone = models.CharField("Telefone oficial", max_length=80, blank=True)
    address = models.CharField("Endereço", max_length=240, blank=True)
    facebook_url = models.URLField("Facebook", blank=True)
    instagram_url = models.URLField("Instagram", blank=True)
    logo = models.ImageField("Logótipo", upload_to="site/", blank=True, null=True)
    hero_image = models.ImageField("Imagem principal", upload_to="site/", blank=True, null=True)
    updated_at = models.DateTimeField("Atualizado em", auto_now=True)

    class Meta:
        verbose_name = "Configuração do site"
        verbose_name_plural = "Configurações do site"

    def __str__(self):
        return self.institution_name

    @classmethod
    def current(cls):
        obj = cls.objects.first()
        if not obj:
            obj = cls.objects.create()
        return obj

class Course(models.Model):
    title = models.CharField("Nome do curso", max_length=180)
    slug = models.SlugField(unique=True, blank=True)
    degree = models.CharField("Grau/nível", max_length=120, blank=True)
    duration = models.CharField("Duração", max_length=100, blank=True)
    description = models.TextField("Descrição")
    admission_requirements = models.TextField("Requisitos de admissão", blank=True)
    image = models.ImageField("Imagem", upload_to="courses/", blank=True, null=True)
    is_published = models.BooleanField("Publicado", default=False)
    created_at = models.DateTimeField("Criado em", auto_now_add=True)
    updated_at = models.DateTimeField("Atualizado em", auto_now=True)

    class Meta:
        ordering = ["title"]
        verbose_name = "Curso"
        verbose_name_plural = "Cursos"

    def save(self, *args, **kwargs):
        if not self.slug:
            base = slugify(self.title) or "curso"
            candidate, n = base, 2
            while Course.objects.filter(slug=candidate).exclude(pk=self.pk).exists():
                candidate, n = f"{base}-{n}", n + 1
            self.slug = candidate
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

class News(models.Model):
    CATEGORY_CHOICES = [
        ("institucional", "Institucional"), ("admissoes", "Admissões"),
        ("academico", "Académico"), ("comunicado", "Comunicado"),
    ]
    title = models.CharField("Título", max_length=220)
    slug = models.SlugField(unique=True, blank=True)
    summary = models.CharField("Resumo", max_length=320)
    body = models.TextField("Conteúdo")
    category = models.CharField("Categoria", max_length=30, choices=CATEGORY_CHOICES, default="institucional")
    image = models.ImageField("Imagem de destaque", upload_to="news/", blank=True, null=True)
    is_published = models.BooleanField("Publicado", default=False)
    published_at = models.DateTimeField("Data de publicação", default=timezone.now)
    created_at = models.DateTimeField("Criado em", auto_now_add=True)

    class Meta:
        ordering = ["-published_at"]
        verbose_name = "Notícia"
        verbose_name_plural = "Notícias"

    def save(self, *args, **kwargs):
        if not self.slug:
            base = slugify(self.title) or "noticia"
            candidate, n = base, 2
            while News.objects.filter(slug=candidate).exclude(pk=self.pk).exists():
                candidate, n = f"{base}-{n}", n + 1
            self.slug = candidate
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

class Event(models.Model):
    title = models.CharField("Nome do evento", max_length=220)
    description = models.TextField("Descrição")
    location = models.CharField("Local", max_length=180, blank=True)
    starts_at = models.DateTimeField("Data e hora")
    image = models.ImageField("Imagem", upload_to="events/", blank=True, null=True)
    is_published = models.BooleanField("Publicado", default=False)

    class Meta:
        ordering = ["starts_at"]
        verbose_name = "Evento"
        verbose_name_plural = "Eventos"

    def __str__(self):
        return self.title

class ContactMessage(models.Model):
    name = models.CharField("Nome", max_length=140)
    email = models.EmailField("E-mail")
    subject = models.CharField("Assunto", max_length=180)
    message = models.TextField("Mensagem")
    is_read = models.BooleanField("Lida", default=False)
    created_at = models.DateTimeField("Recebida em", auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Mensagem de contacto"
        verbose_name_plural = "Mensagens de contacto"

    def __str__(self):
        return f"{self.name} — {self.subject}"
