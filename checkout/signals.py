from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from.models import OrderLineItem


@receiver(post_save, sender=OrderLineItem)
def update_total_on_save(sender, instance, created, **kwargs):
    """Update order total on lineitem or creates a new one"""
    instance.order.grand_total_update()


@receiver(post_delete, sender=OrderLineItem)
def update_total_on_delete(sender, instance, **kwargs):
    """Update order total on lineitem when item is deleted"""
    instance.order.grand_total_update()
