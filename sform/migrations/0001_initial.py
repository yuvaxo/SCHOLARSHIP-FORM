# Generated by Django 5.0.6 on 2024-06-11 05:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('s_code', models.BigIntegerField(primary_key=True, serialize=False)),
                ('s_name', models.CharField(blank=True, max_length=200, null=True)),
                ('sex', models.CharField(blank=True, max_length=1, null=True)),
                ('dob', models.DateField(blank=True, null=True)),
                ('edu_year', models.IntegerField(blank=True, null=True)),
                ('f_m_name', models.CharField(blank=True, max_length=200, null=True)),
                ('community', models.CharField(blank=True, max_length=10, null=True)),
                ('p_income', models.IntegerField(blank=True, null=True)),
                ('ca_name', models.CharField(blank=True, max_length=200, null=True)),
                ('community_attach', models.BinaryField(blank=True, null=True)),
                ('ia_name', models.CharField(blank=True, max_length=200, null=True)),
                ('income_attach', models.BinaryField(blank=True, null=True)),
                ('pass_field', models.CharField(blank=True, db_column='pass', max_length=20, null=True)),
            ],
            options={
                'db_table': 'student',
                'managed': False,
            },
        ),
    ]
