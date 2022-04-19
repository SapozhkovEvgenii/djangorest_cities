from django.contrib import admin
from city.models import City, Continent


class ContinentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('name',)


class CityAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created', 'user')
    list_display_links = ('title',)


admin.site.register(City, CityAdmin)
admin.site.register(Continent, ContinentAdmin)
