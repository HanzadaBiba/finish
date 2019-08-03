# Generated by Django 2.2.1 on 2019-05-27 10:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_profile_position'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='departament',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='workers.Departaments', verbose_name='Департамент'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='position',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.Position', verbose_name='Должность'),
        ),
    ]