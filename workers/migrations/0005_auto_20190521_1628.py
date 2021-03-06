# Generated by Django 2.2 on 2019-05-21 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workers', '0004_workers_status'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='workers',
            options={'ordering': ['-id'], 'verbose_name': 'Сотрудники', 'verbose_name_plural': 'Сотрудники'},
        ),
        migrations.AddField(
            model_name='workers',
            name='date_in',
            field=models.DateField(blank=True, null=True, verbose_name='Дата приезда'),
        ),
        migrations.AddField(
            model_name='workers',
            name='date_out',
            field=models.DateField(blank=True, null=True, verbose_name='Дата отьезда'),
        ),
    ]
