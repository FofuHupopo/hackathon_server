# Generated by Django 4.1.3 on 2022-12-03 21:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('address', '0002_addressmodel_area_addressmodel_country_and_more'),
        ('account', '0007_remove_childmodel_address_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='BirthCertificateModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('series', models.CharField(max_length=4, verbose_name='Серия')),
                ('number', models.CharField(max_length=6, verbose_name='Номер')),
                ('date_of_issue', models.DateTimeField(verbose_name='Дата выдачи')),
                ('whom_issued', models.TextField(null=True, verbose_name='Кем выдан')),
            ],
            options={
                'verbose_name': 'Свидетельство о рождении',
                'verbose_name_plural': 'Свидетьства о рождении',
                'db_table': 'account__birth_certificate',
            },
        ),
        migrations.CreateModel(
            name='ForeignPassportModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('series', models.TextField(verbose_name='Серия')),
                ('number', models.TextField(verbose_name='Номер')),
                ('date_of_issue', models.DateTimeField(verbose_name='Дата выдачи')),
                ('duration', models.DateTimeField(null=True, verbose_name='Срок действия')),
            ],
            options={
                'verbose_name': 'Паспорт',
                'verbose_name_plural': 'Паспорта',
                'db_table': 'account__foreign_passport',
            },
        ),
        migrations.CreateModel(
            name='RussianPassportModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('series', models.CharField(max_length=4, verbose_name='Серия')),
                ('number', models.CharField(max_length=6, verbose_name='Номер')),
                ('date_of_issue', models.DateTimeField(verbose_name='Дата выдачи')),
                ('whom_issued', models.TextField(null=True, verbose_name='Кем выдан')),
            ],
            options={
                'verbose_name': 'Паспорт',
                'verbose_name_plural': 'Паспорта',
                'db_table': 'account__russian_passport',
            },
        ),
        migrations.RemoveField(
            model_name='representativemodel',
            name='passport',
        ),
        migrations.AddField(
            model_name='childmodel',
            name='citizenship',
            field=models.CharField(choices=[('австралия', 'Австралия'), ('австрия', 'Австрия'), ('азербайджан', 'Азербайджан'), ('албания', 'Албания'), ('алжир', 'Алжир'), ('ангола', 'Ангола'), ('андорра', 'Андорра'), ('антигуа и барбуда', 'Антигуа и Барбуда'), ('аргентина', 'Аргентина'), ('армения', 'Армения'), ('афганистан', 'Афганистан'), ('багамские острова', 'Багамские Острова'), ('бангладеш', 'Бангладеш'), ('барбадос', 'Барбадос'), ('бахрейн', 'Бахрейн'), ('белоруссия', 'Белоруссия'), ('белиз', 'Белиз'), ('бельгия', 'Бельгия'), ('бенин', 'Бенин'), ('болгария', 'Болгария'), ('боливия', 'Боливия'), ('босния и герцеговина', 'Босния и Герцеговина'), ('ботсвана', 'Ботсвана'), ('бразилия', 'Бразилия'), ('бруней', 'Бруней'), ('буркина-фасо', 'Буркина-Фасо'), ('бурунди', 'Бурунди'), ('бутан', 'Бутан'), ('вануату', 'Вануату'), ('великобритания', 'Великобритания'), ('венгрия', 'Венгрия'), ('венесуэла', 'Венесуэла'), ('восточный тимор', 'Восточный Тимор'), ('вьетнам', 'Вьетнам'), ('габон', 'Габон'), ('республика гаити', 'Республика Гаити'), ('гайана', 'Гайана'), ('гамбия', 'Гамбия'), ('гана', 'Гана'), ('гватемала', 'Гватемала'), ('гвинея', 'Гвинея'), ('гвинея-бисау', 'Гвинея-Бисау'), ('германия', 'Германия'), ('гондурас', 'Гондурас'), ('гренада', 'Гренада'), ('греция', 'Греция'), ('грузия', 'Грузия'), ('дания', 'Дания'), ('джибути', 'Джибути'), ('доминика', 'Доминика'), ('доминиканская республика', 'Доминиканская Республика'), ('египет', 'Египет'), ('замбия', 'Замбия'), ('зимбабве', 'Зимбабве'), ('израиль', 'Израиль'), ('индия', 'Индия'), ('индонезия', 'Индонезия'), ('иордания', 'Иордания'), ('ирак', 'Ирак'), ('иран', 'Иран'), ('ирландия', 'Ирландия'), ('исландия', 'Исландия'), ('испания', 'Испания'), ('италия', 'Италия'), ('йемен', 'Йемен'), ('кабо-верде', 'Кабо-Верде'), ('казахстан', 'Казахстан'), ('камбоджа', 'Камбоджа'), ('камерун', 'Камерун'), ('канада', 'Канада'), ('катар', 'Катар'), ('кения', 'Кения'), ('республика кипр', 'Республика Кипр'), ('киргизия', 'Киргизия'), ('кирибати', 'Кирибати'), ('китай', 'Китай'), ('колумбия', 'Колумбия'), ('коморы', 'Коморы'), ('республика конго', 'Республика Конго'), ('демократическая республика конго', 'Демократическая Республика Конго'), ('корейская народно-демократическая республика', 'Корейская Народно-Демократическая Республика'), ('республика корея', 'Республика Корея'), ('коста-рика', 'Коста-Рика'), ('кот-д’ивуар', 'Кот-д’Ивуар'), ('куба', 'Куба'), ('кувейт', 'Кувейт'), ('лаос', 'Лаос'), ('латвия', 'Латвия'), ('лесото', 'Лесото'), ('либерия', 'Либерия'), ('ливан', 'Ливан'), ('ливия', 'Ливия'), ('литва', 'Литва'), ('лихтенштейн', 'Лихтенштейн'), ('люксембург', 'Люксембург'), ('маврикий', 'Маврикий'), ('мавритания', 'Мавритания'), ('мадагаскар', 'Мадагаскар'), ('малави', 'Малави'), ('малайзия', 'Малайзия'), ('мали', 'Мали'), ('мальдивы', 'Мальдивы'), ('мальта', 'Мальта'), ('марокко', 'Марокко'), ('маршалловы острова', 'Маршалловы Острова'), ('мексика', 'Мексика'), ('федеративные штаты микронезии', 'Федеративные Штаты Микронезии'), ('мозамбик', 'Мозамбик'), ('молдавия', 'Молдавия'), ('монако', 'Монако'), ('монголия', 'Монголия'), ('мьянма', 'Мьянма'), ('намибия', 'Намибия'), ('науру', 'Науру'), ('непал', 'Непал'), ('нигер', 'Нигер'), ('нигерия', 'Нигерия'), ('нидерланды', 'Нидерланды'), ('никарагуа', 'Никарагуа'), ('новая зеландия', 'Новая Зеландия'), ('норвегия', 'Норвегия'), ('объединённые арабские эмираты', 'Объединённые Арабские Эмираты'), ('оман', 'Оман'), ('пакистан', 'Пакистан'), ('палау', 'Палау'), ('панама', 'Панама'), ('папуа — новая гвинея', 'Папуа — Новая Гвинея'), ('парагвай', 'Парагвай'), ('перу', 'Перу'), ('польша', 'Польша'), ('португалия', 'Португалия'), ('россия', 'Россия'), ('руанда', 'Руанда'), ('румыния', 'Румыния'), ('сальвадор', 'Сальвадор'), ('самоа', 'Самоа'), ('сан-марино', 'Сан-Марино'), ('сан-томе и принсипи', 'Сан-Томе и Принсипи'), ('саудовская аравия', 'Саудовская Аравия'), ('флаг северной македонии', 'Флаг Северной Македонии'), ('сейшельские острова', 'Сейшельские Острова'), ('сенегал', 'Сенегал'), ('сент-винсент и гренадины', 'Сент-Винсент и Гренадины'), ('сент-китс и невис', 'Сент-Китс и Невис'), ('сент-люсия', 'Сент-Люсия'), ('сербия', 'Сербия'), ('сингапур', 'Сингапур'), ('сирия', 'Сирия'), ('словакия', 'Словакия'), ('словения', 'Словения'), ('соединённые штаты америки', 'Соединённые Штаты Америки'), ('соломоновы острова', 'Соломоновы Острова'), ('сомали', 'Сомали'), ('судан', 'Судан'), ('суринам', 'Суринам'), ('сьерра-леоне', 'Сьерра-Леоне'), ('таджикистан', 'Таджикистан'), ('таиланд', 'Таиланд'), ('танзания', 'Танзания'), ('того', 'Того'), ('тонга', 'Тонга'), ('тринидад и тобаго', 'Тринидад и Тобаго'), ('тувалу', 'Тувалу'), ('тунис', 'Тунис'), ('туркменистан', 'Туркменистан'), ('турция', 'Турция'), ('уганда', 'Уганда'), ('узбекистан', 'Узбекистан'), ('украина', 'Украина'), ('уругвай', 'Уругвай'), ('фиджи', 'Фиджи'), ('филиппины', 'Филиппины'), ('финляндия', 'Финляндия'), ('франция', 'Франция'), ('хорватия', 'Хорватия'), ('центральноафриканская республика', 'Центральноафриканская Республика'), ('чад', 'Чад'), ('черногория', 'Черногория'), ('чехия', 'Чехия'), ('чили', 'Чили'), ('швейцария', 'Швейцария'), ('швеция', 'Швеция'), ('шри-ланка', 'Шри-Ланка'), ('эквадор', 'Эквадор'), ('экваториальная', 'Экваториальная'), ('эритрея', 'Эритрея'), ('эсватини', 'Эсватини'), ('эстония', 'Эстония'), ('эфиопия', 'Эфиопия'), ('южно-африканская республика', 'Южно-Африканская Республика'), ('южный судан', 'Южный Судан'), ('ямайка', 'Ямайка'), ('япония', 'Япония')], default='Россия', max_length=128, verbose_name='Гражданство'),
        ),
        migrations.AddField(
            model_name='childmodel',
            name='document_type',
            field=models.CharField(choices=[('passport', 'Паспорт'), ('birth_certificate', 'Свидетельство о рождении')], default='passport', max_length=64, verbose_name='Тип документа'),
        ),
        migrations.AddField(
            model_name='representativemodel',
            name='citizenship',
            field=models.CharField(choices=[('австралия', 'Австралия'), ('австрия', 'Австрия'), ('азербайджан', 'Азербайджан'), ('албания', 'Албания'), ('алжир', 'Алжир'), ('ангола', 'Ангола'), ('андорра', 'Андорра'), ('антигуа и барбуда', 'Антигуа и Барбуда'), ('аргентина', 'Аргентина'), ('армения', 'Армения'), ('афганистан', 'Афганистан'), ('багамские острова', 'Багамские Острова'), ('бангладеш', 'Бангладеш'), ('барбадос', 'Барбадос'), ('бахрейн', 'Бахрейн'), ('белоруссия', 'Белоруссия'), ('белиз', 'Белиз'), ('бельгия', 'Бельгия'), ('бенин', 'Бенин'), ('болгария', 'Болгария'), ('боливия', 'Боливия'), ('босния и герцеговина', 'Босния и Герцеговина'), ('ботсвана', 'Ботсвана'), ('бразилия', 'Бразилия'), ('бруней', 'Бруней'), ('буркина-фасо', 'Буркина-Фасо'), ('бурунди', 'Бурунди'), ('бутан', 'Бутан'), ('вануату', 'Вануату'), ('великобритания', 'Великобритания'), ('венгрия', 'Венгрия'), ('венесуэла', 'Венесуэла'), ('восточный тимор', 'Восточный Тимор'), ('вьетнам', 'Вьетнам'), ('габон', 'Габон'), ('республика гаити', 'Республика Гаити'), ('гайана', 'Гайана'), ('гамбия', 'Гамбия'), ('гана', 'Гана'), ('гватемала', 'Гватемала'), ('гвинея', 'Гвинея'), ('гвинея-бисау', 'Гвинея-Бисау'), ('германия', 'Германия'), ('гондурас', 'Гондурас'), ('гренада', 'Гренада'), ('греция', 'Греция'), ('грузия', 'Грузия'), ('дания', 'Дания'), ('джибути', 'Джибути'), ('доминика', 'Доминика'), ('доминиканская республика', 'Доминиканская Республика'), ('египет', 'Египет'), ('замбия', 'Замбия'), ('зимбабве', 'Зимбабве'), ('израиль', 'Израиль'), ('индия', 'Индия'), ('индонезия', 'Индонезия'), ('иордания', 'Иордания'), ('ирак', 'Ирак'), ('иран', 'Иран'), ('ирландия', 'Ирландия'), ('исландия', 'Исландия'), ('испания', 'Испания'), ('италия', 'Италия'), ('йемен', 'Йемен'), ('кабо-верде', 'Кабо-Верде'), ('казахстан', 'Казахстан'), ('камбоджа', 'Камбоджа'), ('камерун', 'Камерун'), ('канада', 'Канада'), ('катар', 'Катар'), ('кения', 'Кения'), ('республика кипр', 'Республика Кипр'), ('киргизия', 'Киргизия'), ('кирибати', 'Кирибати'), ('китай', 'Китай'), ('колумбия', 'Колумбия'), ('коморы', 'Коморы'), ('республика конго', 'Республика Конго'), ('демократическая республика конго', 'Демократическая Республика Конго'), ('корейская народно-демократическая республика', 'Корейская Народно-Демократическая Республика'), ('республика корея', 'Республика Корея'), ('коста-рика', 'Коста-Рика'), ('кот-д’ивуар', 'Кот-д’Ивуар'), ('куба', 'Куба'), ('кувейт', 'Кувейт'), ('лаос', 'Лаос'), ('латвия', 'Латвия'), ('лесото', 'Лесото'), ('либерия', 'Либерия'), ('ливан', 'Ливан'), ('ливия', 'Ливия'), ('литва', 'Литва'), ('лихтенштейн', 'Лихтенштейн'), ('люксембург', 'Люксембург'), ('маврикий', 'Маврикий'), ('мавритания', 'Мавритания'), ('мадагаскар', 'Мадагаскар'), ('малави', 'Малави'), ('малайзия', 'Малайзия'), ('мали', 'Мали'), ('мальдивы', 'Мальдивы'), ('мальта', 'Мальта'), ('марокко', 'Марокко'), ('маршалловы острова', 'Маршалловы Острова'), ('мексика', 'Мексика'), ('федеративные штаты микронезии', 'Федеративные Штаты Микронезии'), ('мозамбик', 'Мозамбик'), ('молдавия', 'Молдавия'), ('монако', 'Монако'), ('монголия', 'Монголия'), ('мьянма', 'Мьянма'), ('намибия', 'Намибия'), ('науру', 'Науру'), ('непал', 'Непал'), ('нигер', 'Нигер'), ('нигерия', 'Нигерия'), ('нидерланды', 'Нидерланды'), ('никарагуа', 'Никарагуа'), ('новая зеландия', 'Новая Зеландия'), ('норвегия', 'Норвегия'), ('объединённые арабские эмираты', 'Объединённые Арабские Эмираты'), ('оман', 'Оман'), ('пакистан', 'Пакистан'), ('палау', 'Палау'), ('панама', 'Панама'), ('папуа — новая гвинея', 'Папуа — Новая Гвинея'), ('парагвай', 'Парагвай'), ('перу', 'Перу'), ('польша', 'Польша'), ('португалия', 'Португалия'), ('россия', 'Россия'), ('руанда', 'Руанда'), ('румыния', 'Румыния'), ('сальвадор', 'Сальвадор'), ('самоа', 'Самоа'), ('сан-марино', 'Сан-Марино'), ('сан-томе и принсипи', 'Сан-Томе и Принсипи'), ('саудовская аравия', 'Саудовская Аравия'), ('флаг северной македонии', 'Флаг Северной Македонии'), ('сейшельские острова', 'Сейшельские Острова'), ('сенегал', 'Сенегал'), ('сент-винсент и гренадины', 'Сент-Винсент и Гренадины'), ('сент-китс и невис', 'Сент-Китс и Невис'), ('сент-люсия', 'Сент-Люсия'), ('сербия', 'Сербия'), ('сингапур', 'Сингапур'), ('сирия', 'Сирия'), ('словакия', 'Словакия'), ('словения', 'Словения'), ('соединённые штаты америки', 'Соединённые Штаты Америки'), ('соломоновы острова', 'Соломоновы Острова'), ('сомали', 'Сомали'), ('судан', 'Судан'), ('суринам', 'Суринам'), ('сьерра-леоне', 'Сьерра-Леоне'), ('таджикистан', 'Таджикистан'), ('таиланд', 'Таиланд'), ('танзания', 'Танзания'), ('того', 'Того'), ('тонга', 'Тонга'), ('тринидад и тобаго', 'Тринидад и Тобаго'), ('тувалу', 'Тувалу'), ('тунис', 'Тунис'), ('туркменистан', 'Туркменистан'), ('турция', 'Турция'), ('уганда', 'Уганда'), ('узбекистан', 'Узбекистан'), ('украина', 'Украина'), ('уругвай', 'Уругвай'), ('фиджи', 'Фиджи'), ('филиппины', 'Филиппины'), ('финляндия', 'Финляндия'), ('франция', 'Франция'), ('хорватия', 'Хорватия'), ('центральноафриканская республика', 'Центральноафриканская Республика'), ('чад', 'Чад'), ('черногория', 'Черногория'), ('чехия', 'Чехия'), ('чили', 'Чили'), ('швейцария', 'Швейцария'), ('швеция', 'Швеция'), ('шри-ланка', 'Шри-Ланка'), ('эквадор', 'Эквадор'), ('экваториальная', 'Экваториальная'), ('эритрея', 'Эритрея'), ('эсватини', 'Эсватини'), ('эстония', 'Эстония'), ('эфиопия', 'Эфиопия'), ('южно-африканская республика', 'Южно-Африканская Республика'), ('южный судан', 'Южный Судан'), ('ямайка', 'Ямайка'), ('япония', 'Япония')], default='Россия', max_length=128, verbose_name='Гражданство'),
        ),
        migrations.AddField(
            model_name='representativemodel',
            name='registration_address',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='representative_registration_address', to='address.addressmodel', verbose_name='Адрес регистрации'),
        ),
        migrations.AddField(
            model_name='representativemodel',
            name='residence_address',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='representative_residence_address', to='address.addressmodel', verbose_name='Адрес проживания'),
        ),
        migrations.AlterField(
            model_name='childmodel',
            name='registration_address',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='child_registration_address', to='address.addressmodel', verbose_name='Адрес регистрации'),
        ),
        migrations.AlterField(
            model_name='childmodel',
            name='residence_address',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='child_residence_address', to='address.addressmodel', verbose_name='Адрес проживания'),
        ),
        migrations.DeleteModel(
            name='PassportModel',
        ),
        migrations.AddField(
            model_name='childmodel',
            name='birth_certificate',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='account.birthcertificatemodel', verbose_name='Свидетельство о рождении'),
        ),
        migrations.AddField(
            model_name='childmodel',
            name='foreign_passport',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='account.foreignpassportmodel', verbose_name='Зарубежный паспорт'),
        ),
        migrations.AddField(
            model_name='childmodel',
            name='russian_passport',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='account.russianpassportmodel', verbose_name='Российский паспорт'),
        ),
        migrations.AddField(
            model_name='representativemodel',
            name='foreign_passport',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='account.foreignpassportmodel', verbose_name='Зарубежный паспорт'),
        ),
        migrations.AddField(
            model_name='representativemodel',
            name='russian_passport',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='account.russianpassportmodel', verbose_name='Российский паспорт'),
        ),
    ]
