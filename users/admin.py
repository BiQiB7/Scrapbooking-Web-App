from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

# Models
from django.contrib.auth.models import User
from users.models import Profile

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('pk','user','profile_pic','bio')
    list_display_links = ('pk','user')
    list_editable = ('bio','profile_pic')

    search_fields = (
        'user__email',
        'user__username',
        'user__first_name',
        'user__family_name',
    )

    list_filter = (
        'user__is_active',
        'user__is_staff',
        'created',
        'modified',
    )
    fieldsets = (
        (
            'Profile',
            { 'fields': (('user', 'profile_pic'),)}
        ),
        (
            'Extra info',
            {
                'fields': (
                    ('bio'),
                )
            }
        ),
        (
            'Metadata',
            {
                'fields': (('created', 'modified'),)
            }
        ),
    )
    readonly_fields = ('created', 'modified')

# Para que ambos admins se vean en uno solo se hace de la sgte forma


class ProfileInline(admin.StackedInline):
        """Profile in-line admin for users."""
        model = Profile
        can_delete = False
        verbose_name_plural = 'profiles'


class UserAdmin(BaseUserAdmin):
    """Add profile admin to base user admin."""
    inlines = (ProfileInline, )
    list_display = (
        'username',
        'first_name',
        'last_name',
        'is_active',
        'is_staff',
    )

admin.site.unregister(User)
# admin.site.register(Modelo,Clase)
admin.site.register(User, UserAdmin)