from django.contrib import admin
from .forms import registerForm
from .models import register

# Register your models here.


class registerFormAdmin(admin.ModelAdmin):
    list_display = ('name', 'purpose', 'phone', 'time_register')
    list_filter = ("purpose",)
    search_fields = ('name', 'purpose')
    class Meta:
        ordering = ['time_register']


admin.site.register(register, registerFormAdmin)
