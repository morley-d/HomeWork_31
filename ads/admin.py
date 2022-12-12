from django.contrib import admin

from ads.models import Category, Ads
from users.models import Location, User

admin.site.register(Category)
admin.site.register(Location)
admin.site.register(User)
admin.site.register(Ads)
