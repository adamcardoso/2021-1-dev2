# Generated by Django 3.2 on 2021-05-29 18:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('socialnetworks', '0001_initial'),
        ('clients', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='client',
            options={'ordering': ['id'], 'verbose_name': 'Cliente', 'verbose_name_plural': 'Clientes'},
        ),
        migrations.AddField(
            model_name='client',
            name='address',
            field=models.CharField(default=1, max_length=200, verbose_name='Endereco'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='client',
            name='cell_phone',
            field=models.CharField(default=1, max_length=20, verbose_name='Telefone celular'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='client',
            name='email',
            field=models.EmailField(default=1, max_length=254, verbose_name='E-mail'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='client',
            name='gender',
            field=models.CharField(choices=[('M', 'Masculino'), ('F', 'Feminino'), ('O', 'Outro')], default=1, max_length=1, verbose_name='Genero'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='client',
            name='last_name',
            field=models.CharField(default=1, max_length=100, verbose_name='Sobrenome'),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='ClientSocialnetwork',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clients.client')),
                ('socialnetwork', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='socialnetworks.socialnetwork')),
            ],
            options={
                'verbose_name': 'Item de Redes Social',
                'verbose_name_plural': 'Itens de Rede Social',
                'ordering': ['id'],
            },
        ),
        migrations.AddField(
            model_name='client',
            name='client_socialnetwork',
            field=models.ManyToManyField(blank=True, through='clients.ClientSocialnetwork', to='socialnetworks.Socialnetwork'),
        ),
    ]