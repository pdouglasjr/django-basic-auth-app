# Generated by Django 5.1.3 on 2024-11-22 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_rename_is_saff_customuser_is_staff'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customuser',
            options={'verbose_name': 'User'},
        ),
        migrations.AlterField(
            model_name='customuser',
            name='username',
            field=models.CharField(),
        ),
    ]
