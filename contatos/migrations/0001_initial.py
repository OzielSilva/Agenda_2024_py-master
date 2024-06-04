# Generated by Django 5.0.4 on 2024-05-31 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contato',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('telefone', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('endereco', models.CharField(max_length=254)),
                ('imagem', models.ImageField(blank=True, upload_to='foto/%Y/%m/%d')),
            ],
        ),
    ]
