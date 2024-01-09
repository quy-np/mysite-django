from django.db import models

class User(models.Model):
    id = models.BigAutoField(primary_key=True)
    email = models.EmailField(unique=True, null=True)
    username = models.CharField(max_length=255, unique=True, null=True)
    password = models.CharField(max_length=255, null=True)
    first_name = models.CharField(max_length=255, null=True)
    last_name = models.CharField(max_length=255, null=True)
    first_name_kana = models.CharField(max_length=255, null=True)
    last_name_kana = models.CharField(max_length=255, null=True)
    address1 = models.CharField(max_length=255, null=True)
    address2 = models.CharField(max_length=255, null=True)
    address3 = models.CharField(max_length=255, null=True)
    address4 = models.CharField(max_length=255, null=True)
    address = models.CharField(max_length=255, null=True)
    tel = models.CharField(max_length=25, null=True)
    created_at = models.DateTimeField(null=True)
    updated_at = models.DateTimeField(null=True)
    deleted_at = models.DateTimeField(null=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['email'], name='unique_email'),
            models.UniqueConstraint(fields=['username'], name='unique_username'),
        ]

class UserConfiguration(models.Model):
    id = models.BigAutoField(primary_key=True)
    data_json = models.JSONField(null=True)
    created_at = models.DateTimeField(null=True)
    updated_at = models.DateTimeField(null=True)
    deleted_at = models.DateTimeField(null=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['id'], name='unique_id'),
        ]
