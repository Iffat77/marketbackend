# Generated by Django 4.1.7 on 2023-04-12 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='category',
            field=models.CharField(choices=[('electronics', 'Electronics'), ('books', 'Books'), ('clothing', 'Clothing'), ('home', 'Home'), ('collectibles', 'Collectibles'), ('sporting_goods', 'Sporting Goods')], default='electronics', max_length=20),
        ),
    ]
