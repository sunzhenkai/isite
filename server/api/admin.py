from django.contrib import admin

# Register your models here.
from api.models import *

admin.site.register(Article)
admin.site.register(ArticleCategory)
