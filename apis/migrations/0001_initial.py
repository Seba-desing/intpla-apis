# Generated by Django 3.1.2 on 2021-06-16 14:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Boleta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero_de_orden', models.IntegerField()),
                ('valor', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Despacho',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero_de_orden', models.IntegerField()),
                ('direccion', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Marca',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('precio', models.IntegerField()),
                ('description', models.TextField()),
                ('fecha_fabricacion', models.DateTimeField()),
                ('imagen', models.ImageField(null=True, upload_to='productos')),
                ('marca', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='apis.marca')),
            ],
        ),
    ]
