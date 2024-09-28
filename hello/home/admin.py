from django.contrib import admin
from home.models import Login,user

# Register your models here.
class homelogin(admin.ModelAdmin):
    list_display=('email', 'pas')
admin.site.register(Login)

class userprofile(admin.ModelAdmin):
    list_display=('profile_picture')
admin.site.register(user)

class homehistory(admin.ModelAdmin):
    list_display=('user_email', 'query_text', 'timestamp')
    
