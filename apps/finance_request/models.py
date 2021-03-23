from django.db import models
from apps.users.models import User
from django.core.validators import MaxValueValidator, MinValueValidator


class Client(models.Model):
    GOOD = 'gd'
    REGULAR = 'rg'
    BAD = 'bd'
    NULL = 'nl'
    DEBT_SCORE_CHOICES = [
        (GOOD, 'Bueno'),
        (REGULAR, 'Regular'),
        (BAD, 'Malo'),
        (NULL, 'Nulo'),
    ]
    id = models.AutoField(primary_key=True, unique=True)
    first_name = models.CharField('Nombre Completo', max_length=30)
    last_name = models.CharField('Apellidos', max_length=30)
    email = models.EmailField('Correo Electronico', unique=True)
    debt_mount = models.IntegerField(
        'Monto de la deuda',
        default=0,
        validators=[MinValueValidator(0)]
    )
    debt_score = models.CharField(
        'Puntuación de la deuda',
        max_length=2,
        choices=DEBT_SCORE_CHOICES,
        default=NULL
    )
    artificial_indicator = models.IntegerField(
        'Indicador Artificial',
        default=1,
        validators=[MaxValueValidator(10), MinValueValidator(1)]
    )

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'

    REQUIRED_FIELDS = ['__all__']

    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)


class RequestCredit(models.Model):
    id = models.AutoField(primary_key=True)
    client = models.ForeignKey(Client, related_name='requests_credits', on_delete=models.CASCADE)
    request_mount = models.IntegerField(
        'Monto de la solicitud',
        default=1,
        validators=[MaxValueValidator(50000), MinValueValidator(1)]
    )
    is_approved = models.BooleanField('Aprobado?', default=False)

    class Meta:
        verbose_name = 'Solicitud'
        verbose_name_plural = 'Solicitudes'

    REQUIRED_FIELDS = ['__all__']

    def __str__(self):
        return f'Cliente: {self.client.first_name} {self.client.last_name} - Solicitud de: {self.request_mount}'

