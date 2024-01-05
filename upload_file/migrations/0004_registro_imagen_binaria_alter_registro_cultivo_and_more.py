# Generated by Django 4.2.6 on 2024-01-04 04:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('upload_file', '0003_registro_cultivo'),
    ]

    operations = [
        migrations.AddField(
            model_name='registro',
            name='imagen_binaria',
            field=models.BinaryField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='registro',
            name='cultivo',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='registro',
            name='plaga',
            field=models.IntegerField(default=0),
        ),
    ]