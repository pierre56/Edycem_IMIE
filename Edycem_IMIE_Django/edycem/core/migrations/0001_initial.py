# Generated by Django 2.2.3 on 2019-07-08 07:59

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('user_name', models.CharField(max_length=255, unique=True)),
                ('_password', models.CharField(blank=True, max_length=255)),
                ('email', models.EmailField(max_length=255)),
                ('user_type', models.PositiveSmallIntegerField(choices=[(1, 'Employé'), (2, 'Manager')], default=1)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
                ('progress', models.PositiveSmallIntegerField(blank=True, choices=[(0, 'en attente'), (1, 'en cours'), (2, 'terminé')], default=0)),
                ('priority', models.PositiveSmallIntegerField(blank=True, choices=[(0, 'faible'), (1, 'normal'), (2, 'urgent')], default=1)),
                ('manager', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CodirValidation',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('is_positive', models.BooleanField(default=False)),
                ('holding_validation', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Contract',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('licence_name', models.CharField(max_length=255)),
                ('company_name', models.CharField(max_length=255)),
                ('agreement_product', models.CharField(max_length=255)),
                ('agreement_supply', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Insurance',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('company_name', models.CharField(max_length=255)),
                ('normalisation', models.CharField(max_length=255)),
                ('is_validated', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Partner',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('financial_search', models.BooleanField(default=False)),
                ('object_of_partnership', models.TextField()),
                ('technique', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Patent',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('inventor_name', models.CharField(max_length=255)),
                ('INPI_number', models.CharField(max_length=255)),
                ('ownership_rights', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='SectionFinance',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('is_etude', models.BooleanField(default=False)),
                ('office_name', models.CharField(max_length=255)),
                ('roi', models.FloatField(blank=True, null=True)),
                ('example', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='SectionProject',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('year', models.IntegerField(blank=True, choices=[(1984, 1984), (1985, 1985), (1986, 1986), (1987, 1987), (1988, 1988), (1989, 1989), (1990, 1990), (1991, 1991), (1992, 1992), (1993, 1993), (1994, 1994), (1995, 1995), (1996, 1996), (1997, 1997), (1998, 1998), (1999, 1999), (2000, 2000), (2001, 2001), (2002, 2002), (2003, 2003), (2004, 2004), (2005, 2005), (2006, 2006), (2007, 2007), (2008, 2008), (2009, 2009), (2010, 2010), (2011, 2011), (2012, 2012), (2013, 2013), (2014, 2014), (2015, 2015), (2016, 2016), (2017, 2017), (2018, 2018), (2019, 2019)], null=True)),
                ('priority', models.PositiveSmallIntegerField(blank=True, choices=[(0, 'faible'), (1, 'normal'), (2, 'urgent')], default=1)),
                ('site', models.CharField(max_length=255)),
                ('deadline', models.DateTimeField()),
                ('goal', models.TextField()),
                ('is_chaire', models.BooleanField(default=False)),
                ('document', models.FileField(upload_to=None)),
            ],
        ),
        migrations.CreateModel(
            name='task',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
                ('progress', models.PositiveSmallIntegerField(blank=True, choices=[(0, 'en attente'), (1, 'en cours'), (2, 'terminé')], default=0)),
                ('manager', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('societe', models.CharField(max_length=255)),
                ('nom', models.CharField(max_length=255)),
                ('confidentialite', models.IntegerField()),
                ('activity', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='core.Activity')),
                ('codir_validation', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='core.CodirValidation')),
                ('contract', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='core.Contract')),
                ('insurance', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='core.Insurance')),
                ('partner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='core.Partner')),
                ('patent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='core.Patent')),
                ('section_project', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='core.SectionProject')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PrivacyAgreement',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('contract_name', models.CharField(max_length=255)),
                ('project_sponsor_company_name', models.CharField(max_length=255)),
                ('project_sponsor_name', models.CharField(max_length=255)),
                ('patent_name', models.CharField(max_length=255)),
                ('contract', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='core.Contract')),
            ],
        ),
    ]
