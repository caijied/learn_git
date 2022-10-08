# Generated by Django 3.2.8 on 2022-10-07 20:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='VPM',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='车队名称')),
                ('sn', models.CharField(blank=True, default='', max_length=32, verbose_name='车队编号')),
                ('add_time', models.DateTimeField(auto_now_add=True, verbose_name='加入时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
            ],
            options={
                'verbose_name': '车队',
                'verbose_name_plural': '车队',
                'ordering': ['-add_time'],
            },
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_leader', models.BooleanField(default=False, verbose_name='是否是领头车')),
                ('name', models.CharField(max_length=32, verbose_name='车辆名称')),
                ('unit_type', models.CharField(max_length=32, verbose_name='车辆型号')),
                ('empty_quality', models.FloatField(default=0, verbose_name='空车质量')),
                ('full_payload_weight', models.FloatField(default=0, verbose_name='满载总重')),
                ('max_speed', models.FloatField(default=0, verbose_name='最高车速（KM/H）')),
                ('min_turning_radius', models.FloatField(default=0, verbose_name='最小转弯半径（M）')),
                ('overall_length', models.FloatField(default=0, verbose_name='全长（mm）')),
                ('overall_width', models.FloatField(default=0, verbose_name='总宽（mm）')),
                ('noload_height', models.FloatField(default=0, verbose_name='空载高度（mm）')),
                ('add_time', models.DateTimeField(auto_now_add=True, verbose_name='加入时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('vpm', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='nav.vpm', verbose_name='车队')),
            ],
            options={
                'verbose_name': '车辆',
                'verbose_name_plural': '车辆',
                'ordering': ['-add_time'],
            },
        ),
    ]
