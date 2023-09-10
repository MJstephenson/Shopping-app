# Generated by Django 3.2.21 on 2023-09-10 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categories'},
        ),
        migrations.AlterField(
            model_name='product',
            name='alcohol_content',
            field=models.DecimalField(decimal_places=1, help_text='Alcohol content in percentage', max_digits=4),
        ),
        migrations.AlterField(
            model_name='product',
            name='rating',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=6, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='volume',
            field=models.DecimalField(decimal_places=0, help_text='Volume in ml', max_digits=5),
        ),
    ]
