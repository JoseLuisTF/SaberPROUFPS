# Generated by Django 3.2.3 on 2021-06-07 05:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('bancopreguntas', '0001_initial'),
        ('usuario', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Matricula',
            fields=[
                ('id_matricula', models.AutoField(primary_key=True, serialize=False)),
                ('hora_inicio', models.DateTimeField()),
                ('activa', models.BooleanField(default=False)),
                ('estudiante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuario.estudiante')),
            ],
        ),
        migrations.CreateModel(
            name='Respuesta',
            fields=[
                ('id_respuesta', models.AutoField(primary_key=True, serialize=False)),
                ('respuesta', models.CharField(max_length=80)),
                ('matricula', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='prueba.matricula')),
                ('pregunta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bancopreguntas.pregunta')),
            ],
        ),
        migrations.CreateModel(
            name='Prueba',
            fields=[
                ('id_prueba', models.AutoField(primary_key=True, serialize=False)),
                ('hora_inicio', models.DateTimeField()),
                ('realizada', models.BooleanField(default=False)),
                ('programa_academico', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuario.programaacademico')),
            ],
        ),
        migrations.CreateModel(
            name='Nota',
            fields=[
                ('id_nota', models.AutoField(primary_key=True, serialize=False)),
                ('correcta', models.IntegerField()),
                ('cantidad', models.IntegerField()),
                ('matricula', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='prueba.matricula')),
            ],
        ),
        migrations.AddField(
            model_name='matricula',
            name='prueba',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='prueba.prueba'),
        ),
        migrations.CreateModel(
            name='Cuadernillo',
            fields=[
                ('id_cuadernillo', models.AutoField(primary_key=True, serialize=False)),
                ('pregunta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bancopreguntas.pregunta')),
                ('prueba', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='prueba.prueba')),
            ],
        ),
    ]