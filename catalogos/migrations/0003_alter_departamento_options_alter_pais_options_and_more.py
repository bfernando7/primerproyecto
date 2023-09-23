# Generated by Django 4.2.5 on 2023-09-22 04:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalogos', '0002_departamento'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='departamento',
            options={'verbose_name': 'Departamento', 'verbose_name_plural': 'Departamentos'},
        ),
        migrations.AlterModelOptions(
            name='pais',
            options={'verbose_name': 'Pais', 'verbose_name_plural': 'Paises'},
        ),
        migrations.AlterField(
            model_name='departamento',
            name='active',
            field=models.BooleanField(default=True, verbose_name='activo'),
        ),
        migrations.CreateModel(
            name='Municipio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('codigo', models.CharField(blank=True, max_length=4, null=True)),
                ('active', models.BooleanField(default=True, verbose_name='activo')),
                ('departamento', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='catalogos.departamento')),
            ],
            options={
                'verbose_name': 'Municipio',
                'verbose_name_plural': 'Municipios',
            },
        ),
    ]
