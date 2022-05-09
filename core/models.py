from django.db import models

# Create your models here.

class Vehicle(models.Model):

    brand = models.CharField('Marca', max_length=30, blank=False)
    vehicle = models.CharField('Modelo', max_length=40, blank=False)
    color = models.CharField('Cor', max_length=20, blank=False)
    plate = models.CharField('Placa', max_length=10, blank=False)
    date_create = models.DateField('Data de Cadastro', blank=False)

    class Meta:
        verbose_name = 'Veículo'
        verbose_name_plural = 'Veículos'
        ordering = ['-date_create']

    def __str__(self):
        return self.brand

    
class Supply(models.Model):

    STATUS_CHOICES = (

        ('sim', 'Sim'),
        ('não', 'Não'),
    )
    
    amount_ofag_liters = models.FloatField('Quant de litros', blank=False)
    milee = models.FloatField('Kilometragem', blank=False)
    supply_value = models.DecimalField('Valor do abastecimento', decimal_places=2, max_digits=9, blank=False)
    payment = models.CharField('Pagamento', choices=STATUS_CHOICES, max_length=3)
    driver_name = models.CharField('Nome do motorista', max_length=50, blank=False)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE, verbose_name='Veículo')
    mark_supply = models.CharField('Marca', max_length=50, blank=False)
    date_supply = models.DateField('Data de abastecimento', blank=False)

    class Meta:
        verbose_name = 'Abastecimento'
        verbose_name_plural = 'Abastecimentos'
        ordering = ['-date_supply']

    def __str__(self):
        return self.mark_supply

class Provider(models.Model):

    provide_name = models.CharField('Nome', max_length=100, blank=False)
    address = models.CharField('Endereço', max_length=100, blank=False)
    number = models.IntegerField('Número', blank=False)
    district = models.CharField('Bairro', max_length=100, blank=False)
    city = models.CharField('Cidade', max_length=50, blank=False)
    phone_number = models.CharField('Telefone', max_length=15, blank=False)
    email = models.EmailField('E-mail', blank=False)
    date_create = models.DateField('Data de Cadastro', blank=False)
    class Meta:
        verbose_name = 'Fornecedor'
        verbose_name_plural = 'Fornecedores'
        ordering = ['-date_create']

    def __str__(self):
        return self.provide_name


class Maintenance(models.Model):

    departure_date = models.DateField('Data de saída', blank=False)
    service = models.CharField('Serviço', max_length=200, blank=False)
    delivery_date = models.DateField('Data de entrega', blank=False)
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE, verbose_name='Fornecedor')
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE, verbose_name='Veículo')
    mark_main = models.CharField('Marca', max_length=50, blank=False)
    value = models.DecimalField('Valor', decimal_places=2, max_digits=9, blank=False)
    next_service = models.DateField('Próximo serviço', blank=False)

    class Meta:
        verbose_name = 'Manutenção'
        verbose_name_plural = 'Manutenções'
        ordering = ['-departure_date']

    def __str__(self):
        return self.service

class Traffic(models.Model):

    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE, verbose_name='Veículo')
    mark_traffic = models.CharField('Marca', max_length=50, blank=False)
    departure_date = models.DateField('Data de saída' , blank=False)
    departure_time = models.TimeField('Hora da saída', blank=False)
    km_of_exit = models.IntegerField('Km de saída', blank=False)
    destiny = models.CharField('Destino', max_length=100, blank=False)
    arrival_date = models.DateField('Data de chegada', blank=False)
    arrival_time = models.TimeField('Hora de chegada', blank=False)
    arrival_kml = models.IntegerField('Km de chegada', blank=False)
    service_purpose = models.CharField('Finalidade do serviço', max_length=200, blank=False)
    difference = models.IntegerField('Diferença', blank=False)
    drivers_name = models.CharField('Nome do motorista', max_length=100, blank=False)
    asked_by = models.CharField('Solicitado por', max_length=100, blank=False)

    class Meta:
        verbose_name = 'Controle de tráfego'
        verbose_name_plural = 'Controles de tráfegos'
        ordering = ['vehicle']

    def __str__(self):
        return self.service_purpose

    def diferenca(self):
        return self.arrival_kml - self.km_of_exit
