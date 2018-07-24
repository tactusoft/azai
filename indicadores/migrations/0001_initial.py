# Generated by Django 2.0.7 on 2018-07-24 16:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dominio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
                ('descripcion', models.CharField(max_length=1000)),
                ('valor', models.CharField(max_length=1000)),
                ('grupo', models.CharField(max_length=255)),
                ('estado', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Indicador',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_indicador', models.CharField(max_length=255)),
                ('descripcion_indicador', models.CharField(max_length=1000)),
                ('estado', models.IntegerField()),
                ('dominio', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='indicadores.Dominio')),
            ],
        ),
        migrations.CreateModel(
            name='TipoIndicador',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
                ('descripcion', models.CharField(max_length=1000)),
                ('estado', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='indicador',
            name='tipo_indicador',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='indicadores.TipoIndicador'),
        ),
    ]
