# Generated by Django 3.0.1 on 2020-02-02 13:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_auto_20200202_1251'),
        ('pxdcast', '0019_auto_20200202_1308'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='podcast',
            name='subscribers',
        ),
        migrations.AddField(
            model_name='podcast',
            name='subscription',
            field=models.ManyToManyField(through='pxdcast.Subscription', to='accounts.Pxdcast'),
        ),
        migrations.AlterField(
            model_name='subscription',
            name='podcast',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subscribers', to='pxdcast.Podcast'),
        ),
    ]