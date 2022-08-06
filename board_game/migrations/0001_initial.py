# Generated by Django 4.0.6 on 2022-08-02 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('loc_x', models.IntegerField()),
                ('loc_w', models.IntegerField()),
                ('loc_d', models.IntegerField()),
                ('user', models.CharField(max_length=255, unique=True)),
                ('win', models.BooleanField(default=False)),
                ('loss', models.BooleanField(default=False)),
            ],
        ),
    ]