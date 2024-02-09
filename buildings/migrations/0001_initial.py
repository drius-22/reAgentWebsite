# Generated by Django 4.2.10 on 2024-02-09 06:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='city',
            fields=[
                ('name', models.CharField(max_length=50, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='country',
            fields=[
                ('name', models.CharField(max_length=50, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='buildings.city')),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='buildings.country')),
            ],
        ),
        migrations.CreateModel(
            name='property',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=250)),
                ('status', models.CharField(choices=[('complete', 'Complete'), ('incomplete', 'Incomplete'), ('depricated', 'Depricated')], default='incomplete', max_length=10)),
                ('date_posted', models.DateTimeField(auto_now_add=True)),
                ('category', models.CharField(choices=[('departamento', 'Departamento'), ('casa', 'Casa'), ('terreno', 'Terreno')], default='casa', max_length=15)),
                ('type', models.CharField(choices=[('venta', 'Venta'), ('renta', 'Renta')], default='venta', max_length=8)),
                ('n_bathrooms', models.IntegerField(blank=True, null=True)),
                ('n_bedrooms', models.IntegerField(blank=True, null=True)),
                ('n_garages', models.IntegerField(blank=True, null=True)),
                ('size', models.IntegerField(blank=True, null=True)),
                ('address', models.CharField(max_length=250, null=True)),
                ('area', models.CharField(max_length=250, null=True)),
                ('postal_code', models.CharField(max_length=250, null=True)),
                ('features', models.CharField(blank=True, max_length=500, null=True)),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=12)),
                ('description', models.TextField(blank=True, null=True)),
                ('virtualtour_link', models.CharField(blank=True, default='', max_length=500, null=True)),
                ('location', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='buildings.location')),
            ],
        ),
        migrations.CreateModel(
            name='province',
            fields=[
                ('name', models.CharField(max_length=50, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='property_images',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='uploads/')),
                ('property_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='buildings.property')),
            ],
        ),
        migrations.AddField(
            model_name='location',
            name='province',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='buildings.province'),
        ),
    ]
