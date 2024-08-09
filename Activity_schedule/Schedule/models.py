from django.db import models

# Create your models here.
# Cada evento possui um título, um tipo, uma data ou intervalo de datas, um valor, que também pode ser gratuito, um local, um horário, uma cidade e uma quantidade de vagas, que pode ser ilimitada.

class Activity(models.Model):
    
    TYPE_CHOICES = (
        ('Show', 'Show'),
        ('Apresentação Teatral', 'Apresentação Teatral'),
        ('Orquestra', 'Orquestra'),
        ('Musical', 'Musical'),
        ('Show de comedia', 'Show de comedia'),
        ('Outro', 'Outro'),
    )
    
    event_title = models.CharField('Titulo',max_length=60)
    event_type = models.CharField('Tipo de evento', choices=TYPE_CHOICES)
    event_start_date = models.DateField('Data de Inicio')
    event_end_date = models.DateField('Data de Termino', null=True, blank=True)
    event_time = models.TimeField('Horario do evento')
    event_location = models.CharField('Endereço do evento')
    event_location_city = models.CharField('Cidade do evento')
    event_is_free = models.BooleanField('Entrada gratuita', default=False)
    event_voucher_price = models.DecimalField('Preço do Ingresso', decimal_places=2, default=0.00, max_digits=8)
    event_is_limitless_vacancies = models.BooleanField('Vagas ilimitadas', default=False)
    event_vacancies = models.IntegerField('Vagas', null=True, blank=True)
    
    def __str__(self):
        return self.event_title
    
    def save(self, *args, **kwargs):
        if self.event_is_free:
            self.event_voucher_price = 0
        if self.event_is_limitless_vacancies:
            self.event_vacancies = None
        super().save(*args, **kwargs) 