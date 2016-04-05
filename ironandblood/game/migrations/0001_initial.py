# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-05 23:40
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Bond',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('maturity', models.IntegerField(default=0)),
                ('state', models.CharField(choices=[('W', 'Pending'), ('P', 'Paid'), ('F', 'Forgiven')], default='W', max_length=1)),
                ('borrower', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('holder', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Charter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.IntegerField(default=10, verbose_name='Land area percentage')),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Exchange',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('offeror_as_bond', models.BooleanField(default=False)),
                ('offeror_as_bond_maturity', models.IntegerField(default=0)),
                ('offeree_as_bond', models.BooleanField(default=False)),
                ('offeree_as_bond_maturity', models.IntegerField(default=0)),
                ('state', models.CharField(choices=[('U', 'Unknown'), ('W', 'Waiting'), ('A', 'Accepted'), ('R', 'Rejected'), ('C', 'Canceled')], default='U', max_length=1)),
                ('offer_date', models.DateTimeField(blank=True, null=True)),
                ('answer_date', models.DateTimeField(blank=True, null=True)),
                ('offeree', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('offeree_bond', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='game.Bond')),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('delinquency', models.IntegerField(default=0, help_text='Number of delinquent bonds as creditor. The rate of delinquency (delinquent bonds over total paid bonds) affects the credit quality of the player.', verbose_name='Delinquent bonds')),
            ],
        ),
        migrations.CreateModel(
            name='Resources',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('currency', models.IntegerField(default=0, verbose_name='Currency')),
                ('manufactured', models.IntegerField(default=0, verbose_name='Manufactured Goods')),
                ('agricultural', models.IntegerField(default=0, verbose_name='Agricultural Goods')),
            ],
        ),
        migrations.CreateModel(
            name='Territory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('land_area', models.IntegerField(default=100, verbose_name='Land area')),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='player',
            name='resources',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='game.Resources'),
        ),
        migrations.AddField(
            model_name='player',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='player', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='exchange',
            name='offeree_resources',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='game.Resources'),
        ),
        migrations.AddField(
            model_name='exchange',
            name='offeree_territory',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='game.Territory'),
        ),
        migrations.AddField(
            model_name='exchange',
            name='offeror',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='exchange',
            name='offeror_bond',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='game.Bond'),
        ),
        migrations.AddField(
            model_name='exchange',
            name='offeror_resources',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='game.Resources'),
        ),
        migrations.AddField(
            model_name='exchange',
            name='offeror_territory',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='game.Territory'),
        ),
        migrations.AddField(
            model_name='charter',
            name='territory',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='game.Territory'),
        ),
        migrations.AddField(
            model_name='bond',
            name='resources',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='game.Resources'),
        ),
        migrations.AddField(
            model_name='bond',
            name='territory',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='game.Territory'),
        ),
    ]
