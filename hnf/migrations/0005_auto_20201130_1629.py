# Generated by Django 3.1.3 on 2020-11-30 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hnf', '0004_auto_20190401_1213'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='asset',
            options={'verbose_name': '资产表', 'verbose_name_plural': '资产表'},
        ),
        migrations.AlterModelOptions(
            name='userinfo',
            options={'verbose_name': '用户表', 'verbose_name_plural': '用户表'},
        ),
        migrations.AlterField(
            model_name='asset',
            name='brand',
            field=models.CharField(max_length=32, verbose_name='品牌'),
        ),
        migrations.AlterField(
            model_name='asset',
            name='leader',
            field=models.CharField(max_length=32, verbose_name='领用人'),
        ),
        migrations.AlterField(
            model_name='asset',
            name='leader_time',
            field=models.DateTimeField(max_length=32, verbose_name='领用时间'),
        ),
        migrations.AlterField(
            model_name='asset',
            name='model',
            field=models.CharField(max_length=32, verbose_name='型号'),
        ),
        migrations.AlterField(
            model_name='asset',
            name='number',
            field=models.CharField(max_length=32, verbose_name='编号'),
        ),
        migrations.AlterField(
            model_name='asset',
            name='other',
            field=models.CharField(max_length=128, null=True, verbose_name='备注'),
        ),
        migrations.AlterField(
            model_name='asset',
            name='return_time',
            field=models.DateTimeField(max_length=32, null=True, verbose_name='归还时间'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='department',
            field=models.CharField(max_length=32, verbose_name='部门'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='password',
            field=models.CharField(max_length=32, verbose_name='密码'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='username',
            field=models.CharField(max_length=32, verbose_name='用户名'),
        ),
    ]
