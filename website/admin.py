from django.contrib import admin
from .models import SiteSettings, Course, News, Event, ContactMessage

admin.site.site_header = "ISDB | Painel administrativo"
admin.site.site_title = "Administração ISDB"
admin.site.index_title = "Gestão do site institucional"

@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    list_display = ("institution_name", "email", "phone", "updated_at")
    def has_add_permission(self, request):
        return not SiteSettings.objects.exists()

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ("title", "degree", "is_published", "updated_at")
    list_filter = ("is_published",)
    search_fields = ("title", "description")
    list_editable = ("is_published",)
    prepopulated_fields = {"slug": ("title",)}

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "published_at", "is_published")
    list_filter = ("category", "is_published")
    search_fields = ("title", "summary", "body")
    list_editable = ("is_published",)
    prepopulated_fields = {"slug": ("title",)}
    date_hierarchy = "published_at"

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ("title", "starts_at", "location", "is_published")
    list_filter = ("is_published",)
    search_fields = ("title", "description", "location")

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "subject", "is_read", "created_at")
    list_filter = ("is_read", "created_at")
    search_fields = ("name", "email", "subject", "message")
    list_editable = ("is_read",)
    readonly_fields = ("name", "email", "subject", "message", "created_at")
