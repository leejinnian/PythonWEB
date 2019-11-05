# Generated by Django 2.2.3 on 2019-08-29 01:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
        ('goods', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ordernum', models.CharField(max_length=20)),
                ('createtimes', models.DateTimeField(blank=True, null=True)),
                ('addressid', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='user.Address')),
                ('userid', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='user.User')),
            ],
            options={
                'db_table': 't_order',
            },
        ),
        migrations.CreateModel(
            name='OrederUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.CharField(max_length=100)),
                ('tel', models.CharField(max_length=11)),
                ('address', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='user.Address')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='order.Order')),
                ('user_id', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='user.User')),
            ],
            options={
                'db_table': 't_order_users',
            },
        ),
        migrations.CreateModel(
            name='order_goods',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('goodscount', models.CharField(max_length=5)),
                ('goods_id', models.IntegerField()),
                ('goodsprice', models.FloatField()),
                ('order', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='order.Order')),
            ],
            options={
                'db_table': 't_order_goods',
            },
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('goodsnum', models.CharField(blank=True, default=1, max_length=50)),
                ('goodprice', models.CharField(blank=True, default=1, max_length=40)),
                ('goods', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='goods.Goods')),
                ('user', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='user.User')),
            ],
            options={
                'db_table': 't_cart',
            },
        ),
    ]