from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('post_photo', 'user', 'last_name', 'name', 'middle_name')
    list_per_page = 10
    list_display_links = ['name']

    save_on_top = True

    @admin.display(description="Изображение")
    def post_photo(self, profile: Profile):
        if profile.image:
            return mark_safe(f"<img src='{profile.image.url}' width=50>")
        return "Без фото"

    class Meta:
        pass


