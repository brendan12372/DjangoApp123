# Generated by Django 3.2.11 on 2022-07-02 17:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('image', models.ImageField(upload_to='')),
                ('price', models.FloatField()),
                ('link', models.CharField(max_length=50)),
                ('discription', models.TextField(max_length=2000)),
            ],
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('pub_date', models.DateField()),
                ('subtitle', models.CharField(max_length=30)),
                ('image', models.ImageField(upload_to='')),
                ('text1', models.TextField(max_length=2000)),
                ('text2', models.TextField(max_length=2000)),
                ('text3', models.TextField(max_length=2000)),
                ('text4', models.TextField(max_length=2000)),
                ('products', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='tracker.product')),
            ],
        ),
    ]