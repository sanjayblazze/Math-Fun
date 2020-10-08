# Generated by Django 3.1.1 on 2020-10-08 09:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AllStandard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clsimg', models.ImageField(blank=True, upload_to='classimg/')),
                ('standardname', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Weightage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, upload_to='images/')),
                ('weight', models.TextField(max_length=5000)),
            ],
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tname', models.CharField(max_length=300)),
                ('files', models.FileField(upload_to='pdfs/')),
                ('Topicname', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MathsFun.allstandard')),
            ],
        ),
    ]
