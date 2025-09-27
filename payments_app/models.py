from django.db import models

class Client(models.Model):
    first_name = models.CharField("Имя", max_length=100)	
    last_name = models.CharField("Фамилия", max_length=100)		
    country = models.CharField("Страна", max_length=100)	

    class Meta:
        db_table = "clients"
        verbose_name = "Клиент"
        verbose_name_plural = "Клиенты"

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Payment(models.Model):
    payer =  models.ForeignKey(
        Client, 
        on_delete=models.CASCADE,
        verbose_name="Плательщик",
    )
    amount = models.DecimalField("Сумма", max_digits=10, decimal_places=2)	
    percent	= models.DecimalField("Процент", max_digits=5, decimal_places=2)
    pay_date = models.DateTimeField("Дата платежа")

    class Meta:
        db_table = "payments"
        verbose_name = "Платёж"
        verbose_name_plural = "Платежи"

    def __str__(self):
        return f"Платеж {self.id} от {self.payer}"