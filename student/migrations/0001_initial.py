# Generated by Django 3.2.9 on 2021-11-30 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_no', models.IntegerField(max_length=3)),
                ('student_name', models.CharField(max_length=30)),
                ('student_DOB', models.DateField(blank=True, null=True)),
                ('student_DOJ', models.DateField(blank=True, null=True)),
            ],
        ),
    ]
