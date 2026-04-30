# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.contrib.auth.models import User
from django.db import models


class Application(models.Model):
    pk_application = models.AutoField(primary_key=True)
    adress_end = models.CharField(max_length=255)
    date_time = models.DateTimeField()
    adress_start = models.CharField(max_length=255)
    weight = models.FloatField()
    fk_userapp = models.ForeignKey('Userapp', models.DO_NOTHING, db_column='fk_userapp')
    fk_type_carge = models.ForeignKey('TypeCarge', models.DO_NOTHING, db_column='fk_type_carge')

    class Meta:
        managed = False
        db_table = 'application'


class TypeCarge(models.Model):
    pk_type_carge = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'type_carge'


class Userapp(models.Model):
    pk_userapp = models.AutoField(primary_key=True)
    middlename = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=20)
    fk_user = models.ForeignKey(User, models.CASCADE, db_column='fk_user')

    class Meta:
        managed = False
        db_table = 'userapp'
