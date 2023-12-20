from django.db import models

# Create your models here.


class Dummy(models.Model):
    dummy = models.CharField(max_length=25)


class Dummy2(models.Model):
    dummy2 = models.CharField(max_length=25)


class Dummy3(models.Model):
    dummy3 = models.CharField(max_length=25)


class PracticeModel(models.Model):
    auto = models.AutoField(primary_key=True)
    big_auto = models.BigAutoField()
    big_int = models.BigIntegerField()
    binary = models.BinaryField()
    bool = models.BooleanField()
    character = models.CharField(max_length=50)
    date = models.DateField()
    date_time = models.DateTimeField(auto_now_add=True)
    decimal = models.DecimalField()
    duration = models.DurationField()
    email = models.EmailField()
    file = models.FileField(upload_to='/files')
    float = models.FloatField()
    dummy_frng = models.ForeignKey(Dummy, related_name='dummies')
    generic_api = models.GenericIPAddressField()
    image_field = models.ImageField(upload_to='/files')
    int_field = models.IntegerField()
    json_field = models.JSONField()
    dummy2 = models.ManyToManyField(Dummy2)
    null_bool = models.NullBooleanField()
    dummy3 = models.OneToOneField(Dummy3)
    pos_big_int = models.PositiveBigIntegerField()
    pos_int = models.PositiveIntegerField()
    pos_smalL_int = models.PositiveSmallIntegerField()
    slug = models.SlugField()
    text = models.TextField()
    time = models.TimeField()
    url = models.URLField()
    uuid = models.UUIDField()
