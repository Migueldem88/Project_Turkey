# Generated by Django 4.1.3 on 2022-12-10 21:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SearchAPI', '0004_alter_producttable_column3'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producttable',
            name='column2',
            field=models.IntegerField(blank=True, null=True, verbose_name='Unnamed: 0.1'),
        ),
        migrations.AlterField(
            model_name='producttable',
            name='column3',
            field=models.IntegerField(blank=True, null=True, verbose_name='Unnamed: 0'),
        ),
        migrations.AlterField(
            model_name='producttable',
            name='pcode',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
