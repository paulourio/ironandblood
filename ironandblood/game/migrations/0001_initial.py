# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-31 15:18
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
                ('wood1', models.IntegerField(default=0, verbose_name='Wood I')),
                ('wood2', models.IntegerField(default=0, verbose_name='Wood II')),
                ('wood3', models.IntegerField(default=0, verbose_name='Wood III')),
                ('stone1', models.IntegerField(default=0, verbose_name='Stone I')),
                ('stone2', models.IntegerField(default=0, verbose_name='Stone II')),
                ('gems', models.IntegerField(default=0, verbose_name='Gems')),
                ('spices', models.IntegerField(default=0, verbose_name='Spices')),
                ('coffee', models.IntegerField(default=0, verbose_name='Coffee')),
                ('yerba_mate', models.IntegerField(default=0, verbose_name='Yerba mate')),
                ('alcohol', models.IntegerField(default=0, verbose_name='Alcohol')),
                ('salt', models.IntegerField(default=0, verbose_name='Salt')),
                ('opium', models.IntegerField(default=0, verbose_name='Opium')),
                ('tea', models.IntegerField(default=0, verbose_name='Tea')),
                ('pearls', models.IntegerField(default=0, verbose_name='Pearls')),
                ('perfumery', models.IntegerField(default=0, verbose_name='Perfumery')),
                ('textilesI', models.IntegerField(default=0, verbose_name='Textiles I')),
                ('textilesII', models.IntegerField(default=0, verbose_name='Textiles II')),
                ('craft', models.IntegerField(default=0, verbose_name='Craft')),
                ('ore', models.IntegerField(default=0, verbose_name='Ore')),
                ('coal', models.IntegerField(default=0, verbose_name='Coal')),
                ('metal1', models.IntegerField(default=0, verbose_name='Metal')),
                ('metal2', models.IntegerField(default=0, verbose_name='Precious Metal')),
                ('currency', models.IntegerField(default=0, verbose_name='Currency')),
                ('food', models.IntegerField(default=0, verbose_name='Food')),
                ('fibre', models.IntegerField(default=0, verbose_name='Fibre')),
                ('guano', models.IntegerField(default=0, verbose_name='Guano')),
                ('saltpetre', models.IntegerField(default=0, verbose_name='Saltpetre')),
                ('sulfur', models.IntegerField(default=0, verbose_name='Sulfur')),
                ('gunpowder', models.IntegerField(default=0, verbose_name='Gunpowder')),
                ('maturity_date', models.IntegerField(default=0)),
                ('bond_age', models.IntegerField(default=0)),
                ('state', models.CharField(choices=[('W', 'Pending'), ('P', 'Paid'), ('F', 'Forgiven')], default='W', max_length=1)),
                ('creditor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='creditor', to=settings.AUTH_USER_MODEL)),
                ('issuer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='issuer', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
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
                ('wood1', models.IntegerField(default=0, verbose_name='Wood I')),
                ('wood2', models.IntegerField(default=0, verbose_name='Wood II')),
                ('wood3', models.IntegerField(default=0, verbose_name='Wood III')),
                ('stone1', models.IntegerField(default=0, verbose_name='Stone I')),
                ('stone2', models.IntegerField(default=0, verbose_name='Stone II')),
                ('gems', models.IntegerField(default=0, verbose_name='Gems')),
                ('spices', models.IntegerField(default=0, verbose_name='Spices')),
                ('coffee', models.IntegerField(default=0, verbose_name='Coffee')),
                ('yerba_mate', models.IntegerField(default=0, verbose_name='Yerba mate')),
                ('alcohol', models.IntegerField(default=0, verbose_name='Alcohol')),
                ('salt', models.IntegerField(default=0, verbose_name='Salt')),
                ('opium', models.IntegerField(default=0, verbose_name='Opium')),
                ('tea', models.IntegerField(default=0, verbose_name='Tea')),
                ('pearls', models.IntegerField(default=0, verbose_name='Pearls')),
                ('perfumery', models.IntegerField(default=0, verbose_name='Perfumery')),
                ('textilesI', models.IntegerField(default=0, verbose_name='Textiles I')),
                ('textilesII', models.IntegerField(default=0, verbose_name='Textiles II')),
                ('craft', models.IntegerField(default=0, verbose_name='Craft')),
                ('ore', models.IntegerField(default=0, verbose_name='Ore')),
                ('coal', models.IntegerField(default=0, verbose_name='Coal')),
                ('metal1', models.IntegerField(default=0, verbose_name='Metal')),
                ('metal2', models.IntegerField(default=0, verbose_name='Precious Metal')),
                ('currency', models.IntegerField(default=0, verbose_name='Currency')),
                ('food', models.IntegerField(default=0, verbose_name='Food')),
                ('fibre', models.IntegerField(default=0, verbose_name='Fibre')),
                ('guano', models.IntegerField(default=0, verbose_name='Guano')),
                ('saltpetre', models.IntegerField(default=0, verbose_name='Saltpetre')),
                ('sulfur', models.IntegerField(default=0, verbose_name='Sulfur')),
                ('gunpowder', models.IntegerField(default=0, verbose_name='Gunpowder')),
                ('state', models.CharField(choices=[('W', 'Waiting'), ('A', 'Accepted'), ('R', 'Rejected')], default='W', max_length=1)),
                ('offeree', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='offeree', to=settings.AUTH_USER_MODEL)),
                ('offeror', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='offeror', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wood1', models.IntegerField(default=0, verbose_name='Wood I')),
                ('wood2', models.IntegerField(default=0, verbose_name='Wood II')),
                ('wood3', models.IntegerField(default=0, verbose_name='Wood III')),
                ('stone1', models.IntegerField(default=0, verbose_name='Stone I')),
                ('stone2', models.IntegerField(default=0, verbose_name='Stone II')),
                ('gems', models.IntegerField(default=0, verbose_name='Gems')),
                ('spices', models.IntegerField(default=0, verbose_name='Spices')),
                ('coffee', models.IntegerField(default=0, verbose_name='Coffee')),
                ('yerba_mate', models.IntegerField(default=0, verbose_name='Yerba mate')),
                ('alcohol', models.IntegerField(default=0, verbose_name='Alcohol')),
                ('salt', models.IntegerField(default=0, verbose_name='Salt')),
                ('opium', models.IntegerField(default=0, verbose_name='Opium')),
                ('tea', models.IntegerField(default=0, verbose_name='Tea')),
                ('pearls', models.IntegerField(default=0, verbose_name='Pearls')),
                ('perfumery', models.IntegerField(default=0, verbose_name='Perfumery')),
                ('textilesI', models.IntegerField(default=0, verbose_name='Textiles I')),
                ('textilesII', models.IntegerField(default=0, verbose_name='Textiles II')),
                ('craft', models.IntegerField(default=0, verbose_name='Craft')),
                ('ore', models.IntegerField(default=0, verbose_name='Ore')),
                ('coal', models.IntegerField(default=0, verbose_name='Coal')),
                ('metal1', models.IntegerField(default=0, verbose_name='Metal')),
                ('metal2', models.IntegerField(default=0, verbose_name='Precious Metal')),
                ('currency', models.IntegerField(default=0, verbose_name='Currency')),
                ('food', models.IntegerField(default=0, verbose_name='Food')),
                ('fibre', models.IntegerField(default=0, verbose_name='Fibre')),
                ('guano', models.IntegerField(default=0, verbose_name='Guano')),
                ('saltpetre', models.IntegerField(default=0, verbose_name='Saltpetre')),
                ('sulfur', models.IntegerField(default=0, verbose_name='Sulfur')),
                ('gunpowder', models.IntegerField(default=0, verbose_name='Gunpowder')),
                ('delinquency', models.IntegerField(default=0, help_text='Number of delinquent bonds as creditor. The rate of delinquency (delinquent bonds over total paid bonds) affects the credit quality of the player.', verbose_name='Delinquent bonds')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
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
            model_name='charter',
            name='territory',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='game.Territory'),
        ),
    ]
