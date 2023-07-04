# Generated by Django 4.2.1 on 2023-07-03 21:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='categories',
        ),
        migrations.AddField(
            model_name='post',
            name='categories',
            field=models.ForeignKey(default=False, on_delete=django.db.models.deletion.CASCADE, to='app.category'),
        ),
    ]
