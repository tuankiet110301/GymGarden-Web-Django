from django.contrib import admin
from .models import Post, PostImage
from django.core.exceptions import PermissionDenied
from django_summernote.admin import SummernoteModelAdmin

class PostImageAdmin(admin.ModelAdmin):
    pass


class PostImageInline(admin.StackedInline):
    model = PostImage
    max_num = 4
    extra = 0

class PostAdmin(SummernoteModelAdmin):
    list_display = ('title', 'slug', 'status', 'created_on', 'image', 'views')
    list_filter = ("status",)
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}
    inlines = [PostImageInline]
    summernote_fields = ('content',)


def users_list_view(request):
    if not request.user.has_perm('auth.view_user'):
        raise PermissionDenied()

admin.site.register(Post, PostAdmin)
admin.site.register(PostImage, PostImageAdmin)
