# Generated by Django 2.0.2 on 2018-03-20 22:06

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SignUp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rin', models.IntegerField(null=True)),
                ('password', models.CharField(max_length=20, null=True)),
                ('email', models.EmailField(max_length=254, null=True)),
                ('name', models.CharField(max_length=120, null=True)),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True)),
                ('fax_number', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]