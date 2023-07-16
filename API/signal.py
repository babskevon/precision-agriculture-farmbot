from django.db.models.signals import post_save
from django.dispatch import receiver
from API.models import FileUpdate

@receiver(post_save, sender=FileUpdate)
def update_status(sender, created, instance, *args, **kwargs):
    if created:
        FileUpdate.objects.exclude(id=instance.id).update(current_update=False)