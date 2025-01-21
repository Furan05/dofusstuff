from django.db import models

class Character(models.Model):
    CLASSES = [
        ('iop', 'Iop'),
        ('cra', 'Cra'),
        ('feca', 'Feca'),
        ('sacrieur', 'Sacrieur'),
        ('eniripsa', 'Eniripsa'),
        ('sram', 'Sram'),
        ('xelor', 'Xelor'),
        ('ecaflip', 'Ecaflip'),
        ('enutrof', 'Enutrof'),
        ('pandawa', 'Pandawa'),
        ('sadida', 'Sadida'),
        ('osamodas', 'Osamodas'),
        ('roublard', 'Roublard'),
        ('zobal', 'Zobal'),
        ('steamer', 'Steamer'),
        ('eliotrope', 'Eliotrope'),
        ('huppermage', 'Huppermage'),
        ('ouginak', 'Ouginak'),
        ('forgelance', 'Forgelance'),
    ]

    character_class = models.CharField(max_length=20, choices=CLASSES)
    level = models.IntegerField()

class Characteristic(models.Model):
    name = models.CharField(max_length=50)
    identifier = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class BuildRequest(models.Model):
    character = models.ForeignKey(Character, on_delete=models.CASCADE)
    primary_stats = models.ManyToManyField(
        Characteristic,
        related_name='primary_builds'
    )
    secondary_stats = models.ManyToManyField(
        Characteristic,
        related_name='secondary_builds'
    )
    created_at = models.DateTimeField(auto_now_add=True)
