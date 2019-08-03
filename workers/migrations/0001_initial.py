# Generated by Django 2.2 on 2019-05-13 06:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название города')),
                ('slug', models.SlugField(max_length=255, verbose_name='Слаг')),
            ],
            options={
                'verbose_name': 'Город',
                'verbose_name_plural': 'Город',
            },
        ),
        migrations.CreateModel(
            name='Departament_block',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
                ('slug', models.SlugField(blank=True, max_length=255, verbose_name='Слаг')),
            ],
            options={
                'verbose_name': 'Отделы подразделение',
                'verbose_name_plural': 'Отделы подразделение',
            },
        ),
        migrations.CreateModel(
            name='Departaments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
                ('slug', models.SlugField(blank=True, max_length=255, verbose_name='Слаг')),
            ],
            options={
                'verbose_name': 'Подразделения',
                'verbose_name_plural': 'Подразделения',
            },
        ),
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название должность')),
                ('slug', models.SlugField(max_length=255, verbose_name='Слаг')),
            ],
            options={
                'verbose_name': 'Должность',
                'verbose_name_plural': 'Должность',
            },
        ),
        migrations.CreateModel(
            name='Units',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
                ('slug', models.SlugField(blank=True, max_length=255, verbose_name='Слаг')),
            ],
            options={
                'verbose_name': 'Структура',
                'verbose_name_plural': 'Структура',
            },
        ),
        migrations.CreateModel(
            name='Workers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=255, verbose_name='Фамилия')),
                ('secondname', models.CharField(max_length=255, verbose_name='Имя')),
                ('lastname', models.CharField(blank=True, max_length=255, verbose_name='Отчество')),
                ('slug', models.SlugField(blank=True, max_length=255, verbose_name='Слаг')),
                ('room', models.CharField(max_length=4, verbose_name='Кабинет')),
                ('ip_number', models.CharField(max_length=16, verbose_name='Ip адрес')),
                ('mobile_phone', models.CharField(blank=True, max_length=12, verbose_name='Телефонный номер')),
                ('phone', models.CharField(blank=True, max_length=12, verbose_name='Городской номер')),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='city_workers', to='workers.City', verbose_name='Город')),
                ('deps', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='workers.Departaments', verbose_name='Подразделение')),
                ('deps_block', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='workers.Departament_block', verbose_name='Отделы подразделение')),
                ('position', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='position_workers', to='workers.Position', verbose_name='Должность')),
            ],
            options={
                'verbose_name': 'Сотрудники',
                'verbose_name_plural': 'Сотрудники',
            },
        ),
        migrations.AddField(
            model_name='departaments',
            name='units',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='workers.Units', verbose_name='Блок'),
        ),
        migrations.AddField(
            model_name='departament_block',
            name='deps',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='workers.Departaments', verbose_name='Подразделение'),
        ),
    ]