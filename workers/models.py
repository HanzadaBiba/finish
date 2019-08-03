from django.db import models
from django.urls import reverse
# Create your models here.
from django.db import models
from django.utils import timezone
from django.utils.text import slugify as django_slugify

alphabet = {'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ё': 'yo', 'ж': 'zh', 'з': 'z', 'и': 'i',
            'й': 'j', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p', 'р': 'r', 'с': 's', 'т': 't',
            'у': 'u', 'ф': 'f', 'х': 'kh', 'ц': 'ts', 'ч': 'ch', 'ш': 'sh', 'щ': 'shch', 'ы': 'i', 'э': 'e', 'ю': 'yu',
            'я': 'ya'}


def slugify(s):
    return django_slugify(''.join(alphabet.get(w, w) for w in s.lower()))
class Units(models.Model):
    name=models.CharField(max_length=255,verbose_name='Название')
    slug=models.SlugField(max_length=255,verbose_name='Слаг',blank=True)
    def __str__(self):
        return self.name
    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if not self.slug:
            self.slug=slugify((self.name))
        super(Units, self).save()
    def get_absolute_url(self):
        return reverse('unit_detail',args=[self.slug])
    class Meta:
        verbose_name_plural='Структура'
        verbose_name='Структура'
class Departaments(models.Model):
    name=models.CharField(max_length=255,verbose_name='Название')
    slug=models.SlugField(max_length=255,verbose_name='Слаг',blank=True)
    units=models.ForeignKey(Units,on_delete=models.CASCADE,verbose_name='Блок')
    def __str__(self):
        return '{} {}'.format(self.name,self.units.name)
    def get_absolute_url(self):
        return reverse('departament_detail',args=[self.slug])
    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if not self.slug:
            self.slug=slugify('{}-{}'.format(self.units.id,self.name))
        super(Departaments, self).save()
    class Meta:
        ordering=['id']
        verbose_name='Подразделения'
        verbose_name_plural='Подразделения'
class Departament_block(models.Model):
    name=models.CharField(max_length=255,verbose_name='Название')
    slug = models.SlugField(max_length=255, verbose_name='Слаг',blank=True)
    deps = models.ForeignKey(Departaments, on_delete=models.CASCADE, verbose_name='Подразделение')
    def __str__(self):
        return '{} {}'.format(self.deps,self.name)
    def get_absolute_url(self):
        return reverse('departament_block_detail',args=[self.slug])
    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if not self.slug:
            self.slug=slugify('{}_{}_{}'.format(self.deps.units.id,self.deps.id,self.name))
        super(Departament_block, self).save()
    class Meta:
        verbose_name='Отделы подразделение'
        verbose_name_plural='Отделы подразделение'


class Position(models.Model):
    name=models.CharField(max_length=255,verbose_name='Название должность')
    slug = models.SlugField(max_length=255, verbose_name='Слаг')
    def __str__(self):
        return self.name
    class Meta:
        verbose_name='Должность'
        verbose_name_plural='Должность'
class City(models.Model):
    name=models.CharField(max_length=255,verbose_name='Название города')
    slug = models.SlugField(max_length=255, verbose_name='Слаг')
    def __str__(self):
        return self.name
    class Meta:
        verbose_name='Город'
        verbose_name_plural='Город'




class Workers(models.Model):
    choices_status=(('На работе' ,'На работе'),
                    ('Отпуск','Отпуск'),
                    ('Командировка','Командировка'),
                    ('Больничная','Больничная'))
    fullname=models.CharField(max_length=255,verbose_name='Фио')
    slug=models.SlugField(max_length=255,verbose_name='Слаг',blank=True)
    deps=models.ForeignKey(Departaments,on_delete=models.CASCADE,verbose_name='Подразделение',blank=True,null=True)
    deps_block=models.ForeignKey(Departament_block,on_delete=models.CASCADE,verbose_name='Отделы подразделение',blank=True,null=True)
    position=models.ForeignKey(Position,on_delete=models.CASCADE,related_name='position_workers',verbose_name='Должность')
    room=models.CharField(max_length=4,verbose_name='Кабинет',blank=True)
    ip_number=models.CharField(max_length=16,verbose_name='Ip адрес',blank=True)
    city=models.ForeignKey(City,on_delete=models.CASCADE,verbose_name='Город',related_name='city_workers')
    mobile_phone=models.CharField(max_length=12,verbose_name='Телефонный номер',blank=True)
    phone=models.CharField(max_length=12,verbose_name='Телефонный номер',blank=True)
    status=models.CharField(max_length=15,verbose_name='Статус',choices=choices_status,default='На работе')
    date_out = models.DateField(verbose_name='Дата начала', blank=True,null=True)
    date_in = models.DateField(verbose_name='Дата окончания', blank=True,null=True)

    def __str__(self):
        return '{}'.format(self.fullname)
    def full_name(self):
        return '{}'.format(self.fullname)

    def get_absolute_url(self):
        return reverse('home:worker_detail', args=[self.slug])

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if not self.slug:
            self.slug = slugify('{}'.format(self.full_name()))
        super(Workers, self).save()
    class Meta:
        verbose_name='Сотрудники'
        verbose_name_plural='Сотрудники'
        ordering=['id']
