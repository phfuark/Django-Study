from django.db import models

class Pacientes(models.Model):
    choices_queixa = (
        ('TDAH', 'TDAH'),
        ('BORDERLINE', 'BORDERLINE'),
        ('DEPRESSAO', 'DEPRESSÃO')
    )


    nome = models.CharField(max_length=50)
    email = models.EmailField()
    telefone = models.CharField(max_length=12, null=True, blank=True)
    foto = models.ImageField(upload_to='fotos')
    pagamento = models.BooleanField(default=True)
    queixa = models.CharField(max_length=10, choices=choices_queixa)

def __str__(self):
    return self.name
