from django.contrib import admin
from .models import Filmo, People


class FilmoAdmin(admin.ModelAdmin):
    list_display = ('moviepartnm', 'peoplecd', 'moviecd')


class PeopleAdmin(admin.ModelAdmin):
    list_display = ('peoplecd', 'peoplenm', 'sex', 'reprolenm')


admin.site.register(Filmo, FilmoAdmin)
admin.site.register(People, PeopleAdmin)
