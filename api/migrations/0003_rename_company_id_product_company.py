# Generated by Django 4.1.2 on 2022-10-30 09:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_rename_company_product_company_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='company_id',
            new_name='company',
        ),
    ]