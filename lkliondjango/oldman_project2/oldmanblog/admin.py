from django.contrib import admin
from .models import Oldman_blog
from .models import Oldman_notice
from .models import Oldman_data
# Register your models here.
admin.site.register(Oldman_blog)
admin.site.register(Oldman_notice)
admin.site.register(Oldman_data)