from django.db import models

class Client(models.Model):
    client_id = models.CharField(max_length=150, unique=True)
    name = models.CharField('Имя', max_length=150)
    surname = models.CharField('Фамилия', max_length=150)
    number = models.CharField('Телефон', max_length=150)
    birth = models.DateField('Дата рождения')
    email = models.CharField('email', max_length=150)

    def __str__(self):
        return f'Клиент {self.surname} {self.name}'

    def get_absolute_url(self):
        return f'/bonus/client/{self.id}'

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'

class BonusCard(models.Model):
    owner = models.OneToOneField(Client, on_delete=models.CASCADE, related_name='bonus_cards')
    card_number = models.CharField('Номер карты', max_length=30, unique=True)
    bonus = models.PositiveIntegerField('Количество бонусов')
    expiration_date = models.DateField('Действительна до')

    def __str__(self):
        return f'Бонусная карта клиента {self.owner.name} {self.owner.surname}'

    def get_absolute_url(self):
        return f'/bonus/{self.id}'

    class Meta:
        verbose_name = 'Бонусная карта'
        verbose_name_plural = 'Бонусные карты'
