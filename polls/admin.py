from django.contrib import admin

from .models import Candidates, Votes

# Register your models here.
admin.site.register(Candidates)
admin.site.register(Votes)