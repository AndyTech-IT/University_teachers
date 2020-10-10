from django.db import models

class Post(models.Model) :
    name = models.CharField('Должность', max_length=70)
    hourly_rate = models.IntegerField('Почасовая ставка')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Должность'
        verbose_name_plural = 'Должности'
    pass

class Teacher(models.Model) :
    post = models.ForeignKey(Post, on_delete=models.DO_NOTHING, verbose_name="Должность")
    fio = models.CharField('ФИО', max_length=70)
    phone = models.CharField('Телефон', max_length=11)
    home_address = models.CharField('Адресс', max_length=70)
    characteristic = models.TextField('Характеристика')

    def __str__(self):
        return self.post.name+' '+self.fio

    class Meta:
        verbose_name = 'Преподаватель'
        verbose_name_plural = 'Преподаватели'
    pass

class Thing(models.Model) :
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, verbose_name="Учитель")
    work_place = models.CharField('Место работы', max_length=70)
    name = models.CharField('Предмет', max_length=70)
    hours = models.IntegerField('Суммарные часы')

    def __str__(self):
        return self.teacher.post.name + ' ' + self.teacher.fio + '(' + self.name + ')'

    class Meta:
        verbose_name = 'Предмет'
        verbose_name_plural = 'Предметы'
    pass

