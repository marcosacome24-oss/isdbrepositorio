from django.contrib import messages
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST
from .models import SiteSettings, Course, News, Event, ContactMessage

def home(request):
    settings = SiteSettings.current()
    courses = Course.objects.filter(is_published=True)[:6]
    news = News.objects.filter(is_published=True, published_at__lte=__import__("django.utils.timezone", fromlist=["now"]).now())[:3]
    events = Event.objects.filter(is_published=True)[:3]
    return render(request, "website/home.html", {"site": settings, "courses": courses, "news": news, "events": events})

def course_list(request):
    items = Course.objects.filter(is_published=True)
    paginator = Paginator(items, 9)
    page = paginator.get_page(request.GET.get("page"))
    return render(request, "website/course_list.html", {"site": SiteSettings.current(), "page": page})

def course_detail(request, slug):
    course = get_object_or_404(Course, slug=slug, is_published=True)
    return render(request, "website/course_detail.html", {"site": SiteSettings.current(), "course": course})

def news_list(request):
    items = News.objects.filter(is_published=True)
    paginator = Paginator(items, 9)
    page = paginator.get_page(request.GET.get("page"))
    return render(request, "website/news_list.html", {"site": SiteSettings.current(), "page": page})

def news_detail(request, slug):
    article = get_object_or_404(News, slug=slug, is_published=True)
    return render(request, "website/news_detail.html", {"site": SiteSettings.current(), "article": article})

@require_POST
def contact(request):
    name = request.POST.get("name", "").strip()
    email = request.POST.get("email", "").strip()
    subject = request.POST.get("subject", "").strip()
    message = request.POST.get("message", "").strip()
    # Honeypot anti-spam field: bots often fill hidden fields.
    if request.POST.get("website", "").strip():
        return redirect("home")
    if not all([name, email, subject, message]) or len(message) > 5000:
        messages.error(request, "Preencha todos os campos corretamente.")
        return redirect("home#contactos")
    ContactMessage.objects.create(name=name, email=email, subject=subject, message=message)
    messages.success(request, "A sua mensagem foi recebida. Obrigado pelo contacto.")
    return redirect("home#contactos")
