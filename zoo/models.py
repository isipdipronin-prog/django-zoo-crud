from django.db import models

MAX_LENGTH = 255


# 1. Класс животных (справочник)
class AnimalClass(models.Model):
    name = models.CharField(max_length=MAX_LENGTH, verbose_name='Наименование класса')
    description = models.TextField(null=True, blank=True, verbose_name='Описание')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Класс животных'
        verbose_name_plural = 'Классы животных'


# 2. Среда обитания (справочник)
class Habitat(models.Model):
    name = models.CharField(max_length=MAX_LENGTH, verbose_name='Название среды обитания')
    climate = models.CharField(max_length=MAX_LENGTH, verbose_name='Климатическая зона')
    description = models.TextField(null=True, blank=True, verbose_name='Описание')

    def __str__(self):
        return f"{self.name} ({self.climate})"

    class Meta:
        verbose_name = 'Среда обитания'
        verbose_name_plural = 'Среды обитания'


# 3. Тип питания (справочник)
class Diet(models.Model):
    name = models.CharField(max_length=MAX_LENGTH, verbose_name='Тип питания')
    description = models.TextField(null=True, blank=True, verbose_name='Описание рациона')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тип питания'
        verbose_name_plural = 'Типы питания'


# 4. Вольер (CRUD № 1 + Фото № 1)
class Enclosure(models.Model):
    name = models.CharField(max_length=MAX_LENGTH, verbose_name='Название / Номер вольера')
    area = models.FloatField(verbose_name='Площадь (кв. м)')
    capacity = models.PositiveIntegerField(default=5, verbose_name='Вместимость (особей)')
    description = models.TextField(null=True, blank=True, verbose_name='Описание вольера')
    photo = models.ImageField(upload_to='enclosures/%Y/%m/%d', null=True, blank=True, verbose_name='Фото вольера')
    is_open = models.BooleanField(default=True, verbose_name='Открыт для посетителей')
    habitat = models.ForeignKey(Habitat, on_delete=models.PROTECT, verbose_name='Среда обитания')

    def __str__(self):
        return f"{self.name} ({self.habitat.name})"

    class Meta:
        verbose_name = 'Вольер'
        verbose_name_plural = 'Вольеры'


# 5. Сотрудник / Смотритель (CRUD № 2 + Фото № 2)
class Keeper(models.Model):
    full_name = models.CharField(max_length=MAX_LENGTH, verbose_name='ФИО сотрудника')
    position = models.CharField(max_length=MAX_LENGTH, verbose_name='Должность')
    experience_years = models.PositiveIntegerField(default=1, verbose_name='Стаж работы (лет)')
    phone = models.CharField(max_length=50, verbose_name='Телефон')
    photo = models.ImageField(upload_to='keepers/%Y/%m/%d', null=True, blank=True, verbose_name='Фотография')
    bio = models.TextField(null=True, blank=True, verbose_name='О сотруднике')

    def __str__(self):
        return f"{self.full_name} — {self.position}"

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'


# 6. Животное (CRUD № 3 + Фото № 3)
class Animal(models.Model):
    name = models.CharField(max_length=MAX_LENGTH, verbose_name='Кличка')
    species = models.CharField(max_length=MAX_LENGTH, verbose_name='Вид животного')
    age = models.PositiveIntegerField(default=1, verbose_name='Возраст (лет)')
    weight = models.FloatField(verbose_name='Вес (кг)')
    description = models.TextField(null=True, blank=True, verbose_name='Описание')
    photo = models.ImageField(upload_to='animals/%Y/%m/%d', null=True, blank=True, verbose_name='Фото животного')
    arrival_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата поступления в зоопарк')
    is_on_display = models.BooleanField(default=True, verbose_name='В экспозиции')
    animal_class = models.ForeignKey(AnimalClass, on_delete=models.PROTECT, verbose_name='Класс животного')
    enclosure = models.ForeignKey(Enclosure, on_delete=models.PROTECT, verbose_name='Вольер')
    diets = models.ManyToManyField(Diet, verbose_name='Типы питания')
    keepers = models.ManyToManyField(Keeper, verbose_name='Ответственные смотрители')

    def __str__(self):
        return f"{self.name} ({self.species})"

    class Meta:
        verbose_name = 'Животное'
        verbose_name_plural = 'Животные'


# 7. Ветеринарная карта (CRUD № 4, связь OneToOne)
class VetCard(models.Model):
    animal = models.OneToOneField(Animal, on_delete=models.CASCADE, related_name='vet_card', verbose_name='Животное')
    health_status = models.CharField(max_length=MAX_LENGTH, default='Здоров', verbose_name='Состояние здоровья')
    vaccinations = models.TextField(null=True, blank=True, verbose_name='Проведенные прививки')
    allergies = models.TextField(null=True, blank=True, verbose_name='Аллергии и противопоказания')
    last_checkup = models.DateTimeField(auto_now=True, verbose_name='Дата последнего осмотра')

    def __str__(self):
        return f"Веткарта: {self.animal.name} ({self.health_status})"

    class Meta:
        verbose_name = 'Ветеринарная карта'
        verbose_name_plural = 'Ветеринарные карты'


# 8. Расписание кормлений (CRUD № 5)
class FeedingSchedule(models.Model):
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE, verbose_name='Животное')
    keeper = models.ForeignKey(Keeper, on_delete=models.PROTECT, verbose_name='Смотритель')
    feeding_time = models.TimeField(verbose_name='Время кормления')
    food_details = models.CharField(max_length=MAX_LENGTH, verbose_name='Рацион и размер порции')
    notes = models.TextField(null=True, blank=True, verbose_name='Примечания')

    def __str__(self):
        return f"{self.feeding_time} — {self.animal.name} ({self.food_details})"

    class Meta:
        verbose_name = 'Запись кормления'
        verbose_name_plural = 'Расписание кормлений'