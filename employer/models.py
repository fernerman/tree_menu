from django.db import models
from django.utils import timezone
from django.db import models
from mptt.models import MPTTModel
from mptt.fields import TreeForeignKey


class Employer(MPTTModel):
    f_name = models.CharField(max_length=15, verbose_name="Имя")
    m_name = models.CharField(max_length=20, verbose_name="Фамилия")
    l_name = models.CharField(max_length=15, verbose_name="Отчество")
    position = models.CharField(max_length=100, verbose_name="Должность")
    date_employment = models.DateField(default=timezone.now, verbose_name="Дата приема на работу")
    salary = models.DecimalField(max_digits=6, decimal_places=0, verbose_name="Размер заработной платы")
    parent = TreeForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='children',
        verbose_name='Начальник',
        default=None

    )

    class Meta:
        verbose_name = 'Начальник'
        verbose_name_plural = 'Начальники'

    class MPTTMeta:
        order_insertion_by = ['position']

    def __str__(self):  # С помощью функции меняем то, как будет представлена запись в модели.
        return self.position  # Указываем, что она будет идентифицироваться с помощью своего заголовка.
