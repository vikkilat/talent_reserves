# Generated by Django 4.2.7 on 2024-01-09 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Ваше имя')),
                ('email', models.EmailField(max_length=254, verbose_name='Ваш e-mail')),
                ('subject', models.CharField(max_length=50, verbose_name='Тема сообщения (кратко)')),
                ('message', models.TextField(verbose_name='Ваше сообщение')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]