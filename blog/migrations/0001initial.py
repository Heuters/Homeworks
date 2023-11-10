from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hashtag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64)),
            ],
            options={
                'verbose_name': 'Хештег)',
                'verbose_name_plural': 'Хештеги',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, null=True, verbose_name='Название книги')),
                ('image', models.ImageField(upload_to='', verbose_name='Загрузите фото')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Дайте описание')),
                ('type_book', models.CharField(choices=[('Фантастика', 'Фанатастика'), ('Художественная', 'Художественная'), ('Хоррор', 'Хоррор'), ('Фентези', 'Фентези')], max_length=100, null=True, verbose_name='выебрите жанр')),
                ('cost', models.PositiveIntegerField(null=True, verbose_name='Укажите цену')),
                ('director', models.CharField(max_length=100, null=True, verbose_name='Укажите имя автора')),
                ('number_of_page', models.IntegerField(null=True, verbose_name='Укажите колличество страниц')),
                ('date_start', models.DateField(null=True, verbose_name='Укажите дату издания')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('hashtags', models.ManyToManyField(to='blog.hashtag')),
            ],
            options={
                'verbose_name': 'Пост',
                'verbose_name_plural': 'Посты',
            },
        ),
    ]