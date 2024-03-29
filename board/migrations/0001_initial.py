# Generated by Django 2.2.1 on 2019-08-17 18:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='First_Topic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_topic', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Second_Topic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('second_topic', models.CharField(max_length=15)),
                ('first_topic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='second_first_topic', to='board.First_Topic')),
            ],
        ),
        migrations.CreateModel(
            name='Third_Topic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('third_topic', models.CharField(max_length=15)),
                ('views', models.PositiveIntegerField(default=0)),
                ('talk_count', models.PositiveIntegerField(default=0)),
                ('second_topic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='third_second_topic', to='board.Second_Topic')),
            ],
        ),
        migrations.CreateModel(
            name='Board_Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('screenname', models.CharField(max_length=15)),
                ('content', models.TextField(max_length=1000)),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('first_topic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='message_first_topic', to='board.First_Topic')),
                ('second_topic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='message_first_topic', to='board.Second_Topic')),
                ('third_topic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='message_first_topic', to='board.Third_Topic')),
            ],
            options={
                'ordering': ('-pub_date',),
            },
        ),
    ]
