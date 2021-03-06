# Generated by Django 3.1.6 on 2021-08-30 07:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_department'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hod',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('phone', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('address', models.CharField(max_length=30)),
                ('id_hod', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='users.department')),
            ],
        ),
    ]
