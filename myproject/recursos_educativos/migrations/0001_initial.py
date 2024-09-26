# Generated by Django 4.2.16 on 2024-09-26 07:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RecursoEducativo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('contenido', models.TextField()),
                ('fecha_publicacion', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Notificacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('metodo_notificacion', models.CharField(max_length=50)),
                ('mensaje', models.TextField()),
                ('recurso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recursos_educativos.recursoeducativo')),
            ],
        ),
    ]
