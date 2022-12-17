from django.contrib import admin
from .models import *

class MyModelAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        print("HELLO",qs)
        print(request.user)
        if request.user.is_superuser:
            return qs
        return qs.filter(author=request.user)
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "author":
            kwargs["queryset"] = User.objects.filter(username=request.user)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


admin.site.register(Cart)
admin.site.register(Product, MyModelAdmin)

# Register your models here.
