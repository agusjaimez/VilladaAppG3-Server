# Generated by Django 3.1 on 2020-11-24 23:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import multiselectfield.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(max_length=30, unique=True)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254, verbose_name='email address')),
                ('is_padre', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Alumno',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('curso', models.CharField(choices=[('1A', 'Primero A'), ('1B', 'Primero B'), ('1C', 'Primero C'), ('2A', 'Segundo A'), ('2B', 'Segundo B'), ('2C', 'Segundo C'), ('3A', 'Tercero A'), ('3B', 'Tercero B'), ('3C', 'Tercero C'), ('4A', 'Cuarto A'), ('4B', 'Cuarto B'), ('4C', 'Cuarto C'), ('5A', 'Quinto A'), ('5B', 'Quinto B'), ('5C', 'Quinto C'), ('6A', 'Sexto A'), ('6B', 'Sexto B'), ('6C', 'Sexto C'), ('7A', 'Septimo A'), ('7B', 'Septimo B'), ('7C', 'Septimo C')], max_length=2)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('dni', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Comunicado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(blank=True, max_length=500, null=True)),
                ('fecha', models.DateField()),
                ('mensaje', models.TextField()),
                ('curso', multiselectfield.db.fields.MultiSelectField(choices=[('1A', 'Primero A'), ('1B', 'Primero B'), ('1C', 'Primero C'), ('2A', 'Segundo A'), ('2B', 'Segundo B'), ('2C', 'Segundo C'), ('3A', 'Tercero A'), ('3B', 'Tercero B'), ('3C', 'Tercero C'), ('4A', 'Cuarto A'), ('4B', 'Cuarto B'), ('4C', 'Cuarto C'), ('5A', 'Quinto A'), ('5B', 'Quinto B'), ('5C', 'Quinto C'), ('6A', 'Sexto A'), ('6B', 'Sexto B'), ('6C', 'Sexto C'), ('7A', 'Septimo A'), ('7B', 'Septimo B'), ('7C', 'Septimo C')], max_length=62)),
            ],
        ),
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Directivo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=50)),
                ('username', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=30)),
                ('cargo', models.CharField(choices=[('DG', 'Director General'), ('DA', 'Director Academico'), ('VD', 'Vicedirector')], default='VD', max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='PadreTutor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=50)),
                ('delegado', models.BooleanField(default=False)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Preceptor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('dni', models.CharField(max_length=30)),
                ('curso', multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('1A', 'Primero A'), ('1B', 'Primero B'), ('1C', 'Primero C'), ('2A', 'Segundo A'), ('2B', 'Segundo B'), ('2C', 'Segundo C'), ('3A', 'Tercero A'), ('3B', 'Tercero B'), ('3C', 'Tercero C'), ('4A', 'Cuarto A'), ('4B', 'Cuarto B'), ('4C', 'Cuarto C'), ('5A', 'Quinto A'), ('5B', 'Quinto B'), ('5C', 'Quinto C'), ('6A', 'Sexto A'), ('6B', 'Sexto B'), ('6C', 'Sexto C'), ('7A', 'Septimo A'), ('7B', 'Septimo B'), ('7C', 'Septimo C')], max_length=62, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='SolicitudReunion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('motivo', models.TextField()),
                ('padre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.padretutor')),
            ],
        ),
        migrations.CreateModel(
            name='Formulario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.TextField()),
                ('tipo_form', models.CharField(choices=[('F1', 'Formulario 1'), ('F2', 'Formulario 2'), ('F3', 'Formulario 3')], default='F1', max_length=2)),
                ('dias', models.CharField(max_length=45, null=True)),
                ('fecha', models.DateField()),
                ('hora', models.CharField(max_length=45, null=True)),
                ('alumno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.alumno')),
            ],
        ),
        migrations.CreateModel(
            name='ComunicadoRecibido',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recibido', models.BooleanField(default=False)),
                ('comunicado', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.comunicado')),
                ('padre_tutor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.padretutor')),
            ],
        ),
        migrations.AddField(
            model_name='comunicado',
            name='directivo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.directivo'),
        ),
        migrations.AddField(
            model_name='alumno',
            name='tutor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.padretutor'),
        ),
    ]
