# Generated by Django 5.0.6 on 2024-06-06 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_alter_review_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='sale',
            name='total_price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='saleproduct',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='faq',
            name='date_added',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
