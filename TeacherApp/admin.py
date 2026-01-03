from django.contrib import admin

# Register your models here.
from .models import herotext,contentcolumn,Certification,contentbody,ContactMessage,footer,comparison,whyus

from django.contrib import admin

admin.site.site_header = "CERT King Admin Panel"
admin.site.site_title = "CERT KingAdmin"
admin.site.index_title = "Welcome to CERT King Dashboard"


@admin.register(herotext)
class heroAdmin(admin.ModelAdmin):
    list_display = ('id', 'toptext', 'hero_title', 'hero_description')
@admin.register(contentcolumn)
class contentAdmin(admin.ModelAdmin):
    list_display = ('title','description','image', 'is_active')
@admin.register(Certification)
class CertificationAdmin(admin.ModelAdmin):
    list_display = ('description', 'is_active')
@admin.register(contentbody)
class bodyAdmin(admin.ModelAdmin):
    list_display = ('title','description','image', 'is_active')




@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'created_at')
    search_fields = ('name', 'email', 'phone')
    readonly_fields = ('created_at',)

@admin.register(footer)
class footerAdmin(admin.ModelAdmin):
    list_display = ('title','description','image', 'is_active')
@admin.register(whyus)
class whyusadmin(admin.ModelAdmin):
    list_display = ('title','description','images', 'is_active')

@admin.register(comparison)
class comparisonadmin(admin.ModelAdmin):
    list_display= ('labels', 'others', 'teacher', 'is_active')