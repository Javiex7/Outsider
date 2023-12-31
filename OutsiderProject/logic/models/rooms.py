from django.db import models


class RoomModel(models.Model):
    class Meta:
        app_label = "logic"
        verbose_name = "Room"
        verbose_name_plural = "Rooms"

    name = models.CharField(
        max_length=256,
        unique=True,
        verbose_name="Nombre",
        help_text="Nombre de la sala",
    )

    current_connections = models.JSONField(
        verbose_name="Lista de conexiones actuales",
        default=list,
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.name
