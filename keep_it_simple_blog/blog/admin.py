from django.contrib import admin
from .models import Post, Categories, Tags, Comments, Replies, Contact, newdef
# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    exclude = ('author',)

    def save_model(self, request, obj, form, change):
        print('This is my reqest.uesr: ', request.user)
        obj.author = request.user
        super(PostAdmin, self).save_model(request, obj, form, change)

#admin.site.register(Post)
admin.site.register(Categories)
admin.site.register(Tags)
admin.site.register(Comments)
admin.site.register(Replies)
admin.site.register(Contact)
admin.site.register(newdef)