# Generated by Django 3.1.2 on 2021-06-22 15:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('apis', '0002_auto_20210622_1014'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='producto',
            name='stock',
        ),
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stock', models.IntegerField()),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='apis.producto')),
            ],
        ),
    ]