from django.contrib import admin
from gallery.models import Photography

# Customise Django's admin screen of selection
class ListPhotography(admin.ModelAdmin):
    list_display = ("id", "published", "name", "subtitle")
    list_display_links = ("id", "name")
    search_fields = ("name",)
    list_filter = ("category",)
    list_editable = ("published", )
    list_per_page = 10

admin.site.register(Photography, ListPhotography)
