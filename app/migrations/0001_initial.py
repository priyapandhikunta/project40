# Generated by Django 5.0.3 on 2024-06-12 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Sname', models.CharField(max_length=100)),
                ('Slocation', models.CharField(max_length=100)),
                ('Sprincipal', models.CharField(max_length=100)),
            ],
        ),
    ]
