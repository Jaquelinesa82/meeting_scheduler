from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Room(models.Model):
    name = models.CharField(max_length=100)
    capacity = models.PositiveIntegerField()
    resources = models.TextField(blank=True)
    created_at = models.DateTimeField(default=timezone.now, verbose_name='Criado em')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Atualizado em')
    
    def __str__(self):
        return self.name


class Reservation(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='reservations')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reservations')
    title = models.CharField(max_length=100)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    purpose = models.CharField(max_length=255)
    created_at = models.DateTimeField(default=timezone.now, verbose_name='Criado em')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Atualizado em')
    
    def __str__(self):
        return f"{self.room.name} reservado por {self.user.username} de {self.start_time} a {self.end_time}"