# Generated by Django 3.2.6 on 2021-09-06 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('fname', models.CharField(max_length=50)),
                ('lname', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50, primary_key='True', serialize=False)),
                ('subject', models.CharField(max_length=500)),
            ],
            options={
                'db_table': 'contact',
            },
        ),
        migrations.CreateModel(
            name='Register',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tname', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('pnumbeer', models.CharField(max_length=50)),
                ('tmember', models.CharField(max_length=50)),
                ('sports', models.CharField(max_length=50)),
                ('agroup', models.CharField(max_length=50)),
                ('team', models.CharField(max_length=50)),
                ('Match', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'register',
            },
        ),
    ]
