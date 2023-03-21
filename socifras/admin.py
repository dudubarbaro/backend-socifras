from django.contrib import admin
from .models import Genero, VideoAulas, Artista, Musica
from .models.usuario import Usuario
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _

admin.site.register(Genero)
admin.site.register(VideoAulas)
admin.site.register(Artista)
admin.site.register(Musica)

class UsuarioAdmin(UserAdmin):
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (_("Personal info"), {"fields": ("first_name", "last_name", "email", "cpf", "telefone", "data_nascimento")}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )

admin.site.register(Usuario, UsuarioAdmin)