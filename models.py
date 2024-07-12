# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Bank(models.Model):
    acc_no = models.BigIntegerField(primary_key=True)
    s_code = models.ForeignKey('Student', models.DO_NOTHING, db_column='s_code', blank=True, null=True)
    ifsc = models.CharField(max_length=11, blank=True, null=True)
    b_name = models.CharField(max_length=200, blank=True, null=True)
    b_loc = models.CharField(max_length=100, blank=True, null=True)
    b_addr = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bank'
