# Generated by Django 3.1.2 on 2021-06-22 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apis', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='boleta',
            name='autorizacion_boleta',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='despacho',
            name='autorizacion_despacho',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='producto',
            name='stock',
            field=models.IntegerField(null=True),
        ),
    ]