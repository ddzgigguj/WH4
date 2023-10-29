from django.db import models

class Manga_shops(models.Model):
    GENRE = (
        ('Хоррор', 'Хоррор'),
        ('Комедия','Комедия'),
        ('Фантастика','Фантастика'),
        ('Драмма','Драмма'),
        ('Боевые искусства','Боевые искусства')
    )
    title = models.CharField('Укажите название манги', max_length=100)
    description = models.TextField('Укаэите описание манги')
    image = models.ImageField('Загрузите фото', upload_to='manga/')
    genre = models.CharField('Укажите жанр', max_length=100, choices=GENRE)
    author = models.CharField('Укажите автора', max_length=100)
    cost = models.PositiveIntegerField('Укажите цену')
    year = models.DateTimeField('Укажите дату выпуска манги', null=True)

    def __str__(self):
        return f'{self.title}.{self.genre}'