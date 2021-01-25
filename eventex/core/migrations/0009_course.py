# Generated by Django 3.1.3 on 2021-01-25 21:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_auto_20210125_2125'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('talk_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.talk')),
                ('slots', models.IntegerField()),
            ],
            options={
                'verbose_name': 'Curso',
                'verbose_name_plural': 'Cursos',
            },
            bases=('core.talk',),
        ),
    ]
