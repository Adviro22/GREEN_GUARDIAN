# Generated by Django 4.2.6 on 2024-01-05 00:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('upload_file', '0008_alter_registro_cultivo_alter_registro_plaga'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registro',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
