from django.db import models

class Data(models.Model):
    login = models.CharField("Логин", max_length=50)
    password = models.CharField("Пароль", max_length=50)
    name = models.CharField("Имя", max_length=50, null=True)
    surname = models.CharField("Фамилия", max_length=50, null=True)
    class Meta:
        verbose_name = "User"
        verbose_name_plural = "User"
        def __str__(self):
            return self.title

class Files(models.Model):
    audio = models.FileField(upload_to="files_to/", blank=False, null=True)
    class Meta:
        verbose_name = "File"
        verbose_name_plural = "Files"
        def __str__(self):
            return self.title

class Images(models.Model):
    images = models.ImageField(upload_to="files_to/images/", blank=False, null=True)
    class Meta:
        verbose_name = "Image"
        verbose_name_plural = "Images"
        def __str__(self):
            return self.title

class Questions(models.Model):
    question = models.TextField("Вопрос", max_length=255, null=True)
    answer = models.TextField("Ответ", max_length=255,  null=True)
    answerwrong1 = models.TextField("Неправильный ответ 1", max_length=255,  null=True)
    answerwrong2 = models.TextField("Неправильный ответ 2", max_length=255,  null=True)
    class Meta:
        verbose_name = "Question"
        verbose_name_plural = "Questions"
        def __str__(self):
            return self.title

# Create your models here.
