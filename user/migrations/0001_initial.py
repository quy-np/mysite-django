# Generated by Django 5.0.1 on 2024-01-09 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('email', models.EmailField(max_length=254, null=True, unique=True)),
                ('username', models.CharField(max_length=255, null=True, unique=True)),
                ('password', models.CharField(max_length=255, null=True)),
                ('first_name', models.CharField(max_length=255, null=True)),
                ('last_name', models.CharField(max_length=255, null=True)),
                ('first_name_kana', models.CharField(max_length=255, null=True)),
                ('last_name_kana', models.CharField(max_length=255, null=True)),
                ('address1', models.CharField(max_length=255, null=True)),
                ('address2', models.CharField(max_length=255, null=True)),
                ('address3', models.CharField(max_length=255, null=True)),
                ('address4', models.CharField(max_length=255, null=True)),
                ('address', models.CharField(max_length=255, null=True)),
                ('tel', models.CharField(max_length=25, null=True)),
                ('created_at', models.DateTimeField(null=True)),
                ('updated_at', models.DateTimeField(null=True)),
                ('deleted_at', models.DateTimeField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserConfiguration',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('data_json', models.JSONField(null=True)),
                ('created_at', models.DateTimeField(null=True)),
                ('updated_at', models.DateTimeField(null=True)),
                ('deleted_at', models.DateTimeField(null=True)),
            ],
        ),
        migrations.AddConstraint(
            model_name='user',
            constraint=models.UniqueConstraint(fields=('email',), name='unique_email'),
        ),
        migrations.AddConstraint(
            model_name='user',
            constraint=models.UniqueConstraint(fields=('username',), name='unique_username'),
        ),
        migrations.AddConstraint(
            model_name='userconfiguration',
            constraint=models.UniqueConstraint(fields=('id',), name='unique_id'),
        ),
    ]