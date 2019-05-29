# Generated by Django 2.2 on 2019-05-29 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plans', '0004_create_user_plans'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='is_recurring',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AddField(
            model_name='pricing',
            name='visible',
            field=models.BooleanField(db_index=True, default=True, help_text='Is visible in current offer', verbose_name='visible'),
        ),
        migrations.AlterField(
            model_name='plan',
            name='available',
            field=models.BooleanField(db_index=True, default=False, help_text='Is still available for purchase', verbose_name='Plan Available'),
        ),
        migrations.AlterField(
            model_name='plan',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Plan Name'),
        ),
        migrations.AlterField(
            model_name='plan',
            name='order',
            field=models.PositiveIntegerField(db_index=True, editable=False, verbose_name='order'),
        ),
        migrations.AlterField(
            model_name='plan',
            name='visible',
            field=models.BooleanField(db_index=True, default=True, help_text='Is visible in current offer', verbose_name='Plan Visible'),
        ),
        migrations.AlterField(
            model_name='quota',
            name='order',
            field=models.PositiveIntegerField(db_index=True, editable=False, verbose_name='order'),
        ),
    ]
