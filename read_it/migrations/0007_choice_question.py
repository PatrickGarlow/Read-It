# Generated by Django 3.0.8 on 2020-07-30 20:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('read_it', '0006_auto_20200729_2329'),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(blank=True, null=True)),
                ('status', models.CharField(default='inactive', max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(blank=True, null=True)),
                ('business', models.IntegerField(default=True, null=True)),
                ('childrens', models.IntegerField(default=True, null=True)),
                ('classics', models.IntegerField(default=True, null=True)),
                ('fantasy', models.IntegerField(default=True, null=True)),
                ('history', models.IntegerField(default=True, null=True)),
                ('horror', models.IntegerField(default=True, null=True)),
                ('mystery', models.IntegerField(default=True, null=True)),
                ('nonfiction', models.IntegerField(default=True, null=True)),
                ('romance', models.IntegerField(default=True, null=True)),
                ('sports', models.IntegerField(default=True, null=True)),
                ('science', models.IntegerField(default=True, null=True)),
                ('youngadult', models.IntegerField(default=True, null=True)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='read_it.Question')),
            ],
        ),
    ]