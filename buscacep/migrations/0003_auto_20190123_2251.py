# Generated by Django 2.1.5 on 2019-01-24 01:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('buscacep', '0002_endereco_cep'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cidade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=500)),
            ],
        ),
        migrations.AlterField(
            model_name='endereco',
            name='localidade',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='buscacep.Cidade'),
        ),
    ]
