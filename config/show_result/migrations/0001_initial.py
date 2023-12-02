# Generated by Django 4.2.7 on 2023-12-02 02:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Marca',
            fields=[
                ('idmarca', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre')),
            ],
            options={
                'verbose_name_plural': 'Marcas',
                'db_table': 'Marca',
                'ordering': ['idmarca'],
            },
        ),
        migrations.CreateModel(
            name='PeriodoTiempo',
            fields=[
                ('idperiodo_tiempo', models.IntegerField(primary_key=True, serialize=False)),
                ('descripcion', models.CharField(max_length=100, verbose_name='Descripción')),
            ],
            options={
                'verbose_name_plural': 'Periodos Tiempo',
                'db_table': 'Periodo_Tiempo',
                'ordering': ['idperiodo_tiempo'],
            },
        ),
        migrations.CreateModel(
            name='Plaga',
            fields=[
                ('idplaga', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre')),
                ('descripcion', models.CharField(max_length=100, verbose_name='Descripción')),
            ],
            options={
                'verbose_name_plural': 'Plagas',
                'db_table': 'Plaga',
                'ordering': ['idplaga'],
            },
        ),
        migrations.CreateModel(
            name='Planta',
            fields=[
                ('idplanta', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre')),
                ('descripcion', models.CharField(max_length=100, verbose_name='Descripción')),
            ],
            options={
                'verbose_name_plural': 'Plantas',
                'db_table': 'Planta',
                'ordering': ['idplanta'],
            },
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('idproducto', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre')),
                ('descripcion', models.CharField(max_length=100, verbose_name='Descripción')),
                ('idmarca', models.IntegerField(verbose_name='ID Marca')),
            ],
            options={
                'verbose_name_plural': 'Productos',
                'db_table': 'Producto',
                'ordering': ['idproducto'],
            },
        ),
        migrations.CreateModel(
            name='TipoPlanta',
            fields=[
                ('idtipo_planta', models.IntegerField(primary_key=True, serialize=False)),
                ('descripcion', models.CharField(max_length=100, verbose_name='Descripción')),
            ],
            options={
                'verbose_name_plural': 'Tipos Plantas',
                'db_table': 'Tipo_Planta',
                'ordering': ['idtipo_planta'],
            },
        ),
        migrations.CreateModel(
            name='Resultado',
            fields=[
                ('idresultado', models.IntegerField(primary_key=True, serialize=False)),
                ('fecha_hora', models.DateField(verbose_name='Fecha y Hora')),
                ('idregistro', models.IntegerField(verbose_name='ID Registro')),
                ('idplaga', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='show_result.plaga', verbose_name='Plaga')),
                ('idplanta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='show_result.planta', verbose_name='Planta')),
            ],
            options={
                'verbose_name_plural': 'Resultados',
                'db_table': 'Resultado',
                'ordering': ['idresultado'],
            },
        ),
        migrations.AddField(
            model_name='planta',
            name='idtipo_planta',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='show_result.tipoplanta', verbose_name='Tipo de Planta'),
        ),
        migrations.CreateModel(
            name='DetalleResultado',
            fields=[
                ('id_detalle_result', models.IntegerField(primary_key=True, serialize=False)),
                ('idperiodo_tiempo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='show_result.periodotiempo', verbose_name='Periodo Tiempo')),
                ('idproducto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='show_result.producto', verbose_name='Producto')),
                ('idresultado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='show_result.resultado', verbose_name='Resultado')),
            ],
            options={
                'verbose_name_plural': 'Detalles Resultados',
                'db_table': 'Detalle_Resultado',
                'ordering': ['id_detalle_result'],
            },
        ),
    ]
