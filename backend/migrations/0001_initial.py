# Generated by Django 4.0.6 on 2022-07-17 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Attendes',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('college', models.CharField(max_length=30)),
                ('education', models.CharField(max_length=30)),
                ('phone', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=254)),
                ('address', models.CharField(max_length=30)),
                ('training_location', models.CharField(max_length=30)),
                ('interest', models.TextField()),
                ('basic_skill', models.TextField()),
                ('date', models.DateField()),
                ('time', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Location', models.CharField(max_length=30)),
                ('image', models.ImageField(upload_to='')),
                ('description', models.TextField()),
                ('title', models.CharField(max_length=30)),
                ('date', models.DateField()),
                ('time', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('college', models.CharField(max_length=40)),
                ('education', models.CharField(max_length=40)),
                ('district', models.CharField(max_length=30)),
                ('training_location', models.CharField(choices=[('Kathmandu', 'Kathmandu'), ('Dolakha', 'Dolakha'), ('Lalitpur', 'Lalitpur'), ('Teku', 'Teku'), ('Bhaktapur', 'Bhaktapur'), ('Hetauda', 'Hetauda')], default='Kathmandu', max_length=30)),
                ('age', models.PositiveIntegerField(blank=True, null=True)),
                ('phone', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=254)),
                ('interest', models.CharField(max_length=30)),
                ('basic_skill', models.CharField(max_length=30)),
                ('date', models.DateTimeField()),
                ('time', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Trainer',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=40)),
                ('education', models.CharField(max_length=40)),
                ('organization', models.CharField(max_length=40)),
            ],
        ),
    ]