# Generated by Django 5.1.7 on 2025-03-22 14:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finished_goods', '0006_remove_boxorder_delivery_date_boxorder_profit_margin_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='BoxSpecification',
        ),
        migrations.DeleteModel(
            name='BoxTemplate',
        ),
        migrations.RemoveField(
            model_name='manufacturingcost',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='manufacturingcost',
            name='machine_cost',
        ),
        migrations.RemoveField(
            model_name='manufacturingcost',
            name='overhead_cost',
        ),
        migrations.RemoveField(
            model_name='manufacturingcost',
            name='updated_at',
        ),
        migrations.RemoveField(
            model_name='materialrequirement',
            name='calculated_at',
        ),
        migrations.RemoveField(
            model_name='materialrequirement',
            name='flute_paper_weight',
        ),
        migrations.RemoveField(
            model_name='materialrequirement',
            name='middle_paper_weight',
        ),
        migrations.AlterField(
            model_name='boxdetails',
            name='box_name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='boxdetails',
            name='breadth',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='boxdetails',
            name='flute_type',
            field=models.CharField(choices=[('A', 'A Flute'), ('B', 'B Flute'), ('C', 'C Flute'), ('E', 'E Flute'), ('F', 'F Flute'), ('BC', 'BC Flute')], max_length=2),
        ),
        migrations.AlterField(
            model_name='boxdetails',
            name='height',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='boxdetails',
            name='length',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='boxdetails',
            name='order_quantity',
            field=models.IntegerField(default=1000),
        ),
        migrations.AlterField(
            model_name='boxdetails',
            name='print_color',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='boxorder',
            name='updated_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='boxpaperrequirements',
            name='bottom_paper_bf',
            field=models.DecimalField(decimal_places=2, max_digits=6),
        ),
        migrations.AlterField(
            model_name='boxpaperrequirements',
            name='bottom_paper_gsm',
            field=models.DecimalField(decimal_places=2, max_digits=6),
        ),
        migrations.AlterField(
            model_name='boxpaperrequirements',
            name='box',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='paper_requirements', to='finished_goods.boxdetails'),
        ),
        migrations.AlterField(
            model_name='boxpaperrequirements',
            name='flute_paper1_bf',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True),
        ),
        migrations.AlterField(
            model_name='boxpaperrequirements',
            name='flute_paper1_gsm',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True),
        ),
        migrations.AlterField(
            model_name='boxpaperrequirements',
            name='flute_paper2_bf',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True),
        ),
        migrations.AlterField(
            model_name='boxpaperrequirements',
            name='flute_paper2_gsm',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True),
        ),
        migrations.AlterField(
            model_name='boxpaperrequirements',
            name='flute_paper_bf',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True),
        ),
        migrations.AlterField(
            model_name='boxpaperrequirements',
            name='flute_paper_gsm',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True),
        ),
        migrations.AlterField(
            model_name='boxpaperrequirements',
            name='middle_paper_bf',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True),
        ),
        migrations.AlterField(
            model_name='boxpaperrequirements',
            name='middle_paper_gsm',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True),
        ),
        migrations.AlterField(
            model_name='boxpaperrequirements',
            name='top_paper_bf',
            field=models.DecimalField(decimal_places=2, max_digits=6),
        ),
        migrations.AlterField(
            model_name='boxpaperrequirements',
            name='top_paper_gsm',
            field=models.DecimalField(decimal_places=2, max_digits=6),
        ),
        migrations.AlterField(
            model_name='manufacturingcost',
            name='box_order',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='manufacturing_cost', to='finished_goods.boxorder'),
        ),
        migrations.AlterField(
            model_name='manufacturingcost',
            name='labor_cost',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='materialrequirement',
            name='box_order',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='material_requirement', to='finished_goods.boxorder'),
        ),
        migrations.AlterField(
            model_name='materialrequirement',
            name='gum_cost',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='materialrequirement',
            name='paper_cost',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]
