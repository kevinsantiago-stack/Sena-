from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from .models import Perfil, Post

User = get_user_model()

@receiver(post_save, sender=User)
def crear_perfil(sender, instance, created, **kwargs):
    if created:
        from .models import Perfil as PerfilModel
        PerfilModel.objects.create(usuario=instance)
