# Generated by Django 4.2.2 on 2023-06-13 21:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_post_imagem_alter_post_titulo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Autor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('texto', models.TextField()),
            ],
        ),
        migrations.RenameField(
            model_name='post',
            old_name='descricao',
            new_name='texto',
        ),
        migrations.RemoveField(
            model_name='post',
            name='autor',
        ),
        migrations.AddField(
            model_name='post',
            name='area',
            field=models.CharField(default=100, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='likes',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='post',
            name='imagem',
            field=models.ImageField(blank=True, null=True, upload_to='blog/'),
        ),
        migrations.AddField(
            model_name='post',
            name='autores',
            field=models.ManyToManyField(to='blog.autor'),
        ),
        migrations.AddField(
            model_name='post',
            name='comentarios',
            field=models.ManyToManyField(to='blog.comentario'),
        ),
    ]
