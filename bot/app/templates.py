from aiogram import types
from aiogram.utils.markdown import link
from aiogram.utils.emoji import emojize


def quest_data():
    return [
        {
            "task_num": 0,
            "question": "Завдання 1:\nНайпопулярніший вид комічного?",
            "answers": [
                {
                    "text": "Меми",
                    "callback_data": "correct_answer|0",
                    "correct": True
                },
                {
                    "text": "Сатира",
                    "callback_data": "wrong_answer|Неправильно! Спробуй ще раз!",
                    "correct": False
                },
                {
                    "text": "Гумор",
                    "callback_data": "wrong_answer|Неправильно! Спробуй ще раз!",
                    "correct": False
                },
                {
                    "text": "Смішні історії Брюха",
                    "callback_data": "wrong_answer|Неправильно! Спробуй ще раз!",
                    "correct": False
                }
            ],
            "task": f"{link('Локація мемів', 'https://t.me/naukmeme')} підготувала для тебе багато Могилянського та смішного. "
                    "Обов'язково переглянь, який ти мем за гороскопом!\n"
                    "А ми заховали там секретне питання!\n"
                    "Як знайдеш питання, то повертайся сюди та пиши свою відповідь внизу.",
            "ans": ["букиця"]
        },
        {
            "task_num": 1,
            "question": "Завдання 2:\nти маєш дещо в собі\n"
                        "і вона\n"
                        "і він\n\n"

                        "ви особливі. тому ви точно там зустрінетеся. проявите себе."
                        " побачите один одного. почуєте. відчуєте. це почнеться. і це має продовжуватися..\n\n"

                        "що це?",
            "answers": [
                {
                    "text": "Приймальна комісія НаУКМА",
                    "callback_data": "wrong_answer|Неправильно! Спробуй ще раз!",
                    "correct": False
                },
                {
                    "text": "Домашній виступ перед батьками",
                    "callback_data": "wrong_answer|Неправильно! Спробуй ще раз!",
                    "correct": False
                },
                {
                    "text": "Шоу талантів",
                    "callback_data": "correct_answer|1",
                    "correct": True
                },
                {
                    "text": "Творчий вечір на Подолі",
                    "callback_data": "wrong_answer|Неправильно! Спробуй ще раз!",
                    "correct": False
                }
            ],
            "task": "Могилянці мають купу талантів."
                    f" Маленьку частинку з них ти знайдеш на сторінці {link('Карантиннику талантів', '')}.\n"
                    "Серед усіх цих талантів сховане питання, яке відкриє тобі шлях до наступної локації. "
                    "Чекаємо тебе тут із правильною відповіддю! ",
            "ans": ["500", "500 гривень", "п'ятсот", "п'ятсот гривень", "500 грн", "500грн"]
        },
        {
            "task_num": 2,
            "question": "Завдання 3:\nЯк передати привіт людині, яка одночасно дуже поруч і дуже далеко?"
                        " Що потрібно, щоб зустрітись та нічого не забути? Машина часу? Хіба?",
            "answers": [
                {
                    "text": "Лист у майбутнє",
                    "callback_data": "correct_answer|2",
                    "correct": True
                },
                {
                    "text": "Фотографія",
                    "callback_data": "wrong_answer|Неправильно! Спробуй ще раз!",
                    "correct": False
                },
                {
                    "text": "Квиток на потяг",
                    "callback_data": "wrong_answer|Неправильно! Спробуй ще раз!",
                    "correct": False
                },
                {
                    "text": "СМС-ка",
                    "callback_data": "wrong_answer|Неправильно! Спробуй ще раз!",
                    "correct": False
                }
            ],
            "task": f"Так-так, {link('листи у майбутнє!', 'https://docs.google.com/forms/d/e/1FAIpQLSeQd96BhhTFB-nedvErdfQr9Mlz20BZVHPXGYIxb8Mgwll6eA/viewform?usp=sf_link')}\n"
                    "І ти зможеш написати собі такий. А через 4 роки отримати звісточку з минулого.\n"
                    "Традиційно — шукай питання, повертайся з відповіддю!\n"
                    "Підказка: Щоб знайти секретне питання, уважно подивись 'в кінці' локації!",
            "ans": ["28 червня", "двадцять восьме червня", "Двадцять восьме червня", "28-ме червня", "28.06"]
        },
        {
            "task_num": 3,
            "question": "Завдання 4:\nУ викрикувані яких назв змагаються студенти під час могилянських заходів?",
            "answers": [
                {
                    "text": "Спеціальностей",
                    "callback_data": "wrong_answer|Неправильно! Спробуй ще раз!",
                    "correct": False
                },
                {
                    "text": "Факультетів",
                    "callback_data": "correct_answer|3",
                    "correct": True
                },
                {
                    "text": "Планет Сонячної системи",
                    "callback_data": "wrong_answer|Неправильно! Спробуй ще раз!",
                    "correct": False
                },
                {
                    "text": "Кавових напоїв, які рятують під час сесії",
                    "callback_data": "wrong_answer|Неправильно! Спробуй ще раз!",
                    "correct": False
                }
            ],
            "task": f"Розкажи нам про себе, а ми розкажемо тобі, який твій істинний факультет! {link('Клацай сюди', 'http://www.quiz-maker.com/QYS5XZ3UN')}\n "
                    "Як закінчиш — чекаю тебе тут. ",
            "ans": ["шість", "Шість", "6"]
        }
    ]


def start_msg():
    return {
        "text": 'Хей хей хей!\n'
                'Де це ти? У Сансет Веллі? У Ріверсайді? Ні, ти на початку своєї подорожі у світ Могилянки!\n'
                'В цьому квесті тобі доведеться боротися за виживання, шукати скарби та перемагати драконів!'
                ' Іншими словами: будуть неймовірні локації, де ти не лише познайомишся з Могилянкою та могилянцями,'
                ' а ще й отримаєш можливість поповнити свій CAS крутецьким шопером від'
                f' {link("KMA gift shop", "https://instagram.com/kmagiftshop?igshid=g1egl66w3fkw")}.\n'
                'Я — твій помічник в цій пригоді. То що, почнемо?'}


def quest_rules():
    return {
        "text": "Правила дуже прості:\n"
                " 1. Відгадуй загадки, проходь локації та шукай заховані там питання. Вони відкриють шлях до наступного завдання!\n"
                "2. Застряг/ла у квесті? ось не зрозуміло? Пиши @urbi_ca або @AnnTomliak.\n"
                "3. Ти можеш користуватися чит-кодами, питатися у Google або своїх Бадді.\n"
                "Чи ти готова/ий починати?"}


def crslt_info():
    return {
        "text": "За півроку карантину ми забули, які на дотик руки найближчих друзів;"
                " скільки кілометрів займає дорога від рідного міста до Києва;"
                " де можна купити найсмачніший хумус на світі та як прасувати ту саму білу сорочку.\n\n"
                "За півроку карантину нам так не вистачало людей,"
                " які дивуються кольору наших очей. Знайомих людей. Незнайомих людей.\n"
                "Якщо тобі, як і нам, хочеться поділитися найпотаємнішими переживаннями, "
                "описом своїх котів або твором «як я провів це літо», бери участь у «Фреш_крослетерінгу».\n"
                "В комплекті йдуть:\n"
                "  -максимальна відкритість;\n"
                "  -ніякого діджитала — тільки паперові листи;\n"
                "  -лише з власного волевиявлення;\n\n"
                "Пиши. Чекаємо.",
        "photo": types.InputFile('./static/crosslettering.jpg')}


def crslt_description():
    return {
        "text": "Наступним повідомленням відправ всю інфу, за якою можна тебе знайти або надіслати тобі листа: П.І.Б.,"
                " адресу, телефон, поштове відділення, інстаграм. І чекай на магію!\n\n"
                "P.S. Твоя особиста інформація буде знаходитися лише в цьому боті та не потрапить за його межі."
                " Обмін відбуватиметься виключно серед студентів Могилянка."}


def crslt_accepted():
    return {"text": "Твої дані збережено! В 21:00 ти отримаєш контакт людини, якій писатимеш листа"}


def wrong_answer_msg():
    return {"text": "Неправильно! Спробуй ще раз!"}


def second_tips():
    return [
        {"text": "Спитайся у своїх Бадді, може вони допоможуть?"},
        {"text": "Шукай питання у перших постах 'Карантиннику талантів'..."},
        {"text": "Спитай у своїх Бадді, може вони допоможуть?"},
        {"text": "Спитай у своїх Бадді, може вони допоможуть?"}
    ]


def congratulations_msgs():
    return [
        {"text": "Молодець! Лови наступну загадку!"},
        {"text": "Ти неперевершена/ий!"},
        {"text": "Далі складніше! Лови наступну загадку!"},
        {"text": "Ти вже майже на фініші! Залишився останній крок."}
    ]


def finish_gratz():
    return {"text": f"Пам-парам-пам, вітаємо з фінішем!{emojize(':confetti_ball:')}\n"
                    "Сподіваюся, ти отримав максимум задоволення від цього квесту та зміг"
                    " з легкістю знайти усі відповіді. Тепер ти більше знаєш про могилянську спільноту та про себе."
                    " А також маєш можливість виграти в розіграші подарунків від KMA gift shop!"
                    "Проте це ще не все!"
                    "Ти можеш ще раз повернутися на будь-’яку з локацій, а також – побувати на деяких нових."
                    " Тому зверни особливу увагу на “Ігри у Діскорді” та “Фреш-крослетерінг” –"
                    " там тебе точно чекає щось цікаве!"}


def help_msg():
    return {"text": "Виникли питання щодо бота? Пиши @dima_zhornyk\n"
                    "Застряг/ла у квесті? Щось не зрозуміло? Пиши @urbi_ca або @AnnTomliak\n"
                    "Будь-які інші питання: @marinmor"}


def already_completed_msg():
    return {"text": "Ти вже завершив квест, тому не можеш проходити його знову(\n"
                    "Але тобі завжди доступні всі локації за командою /info"}


def info_msg():
    return {"text": "Ось список доступних локацій:\n"
                    "/crosslettering - написати парперового листа\n"
                    "/games - ігри в діскорді\n"
                    "/letter_in_future - лист в майбутнє\n"
                    "/quarantynnyk - карантинник\n"
                    "/memes - мем-локація\n"
                    "/faculty_test - який ти факультет"}


def games_msg():
    return {"text": "Games description and links",
            "photo": types.InputFile('./static/discord.jpg')}


def letter_in_future_msg():
    return {
        "text": "Чи пам‘ятаєш ти якими були твої мрії у дванадцять? Або про що ти думав у п‘ятнадцять?"
                " А чи запам’ятаєш ти, що відбувається у твоїй голові зараз?"
                "Ми гарантуємо, що так! Напиши листа самому собі у майбутнє,"
                " де можеш написати все, що завгодно: свої думки, почуття, мрії,"
                " або навіть запитання до самого себе. 20го, на спешл фреш фесті,"
                f" заповнюй формочку {link('тут', 'https://docs.google.com/forms/d/e/1FAIpQLSeQd96BhhTFB-nedvErdfQr9Mlz20BZVHPXGYIxb8Mgwll6eA/viewform?usp=sf_link')}, а ми потурбуємося про те,"
                " щоб через чотири роки звісточка з минулого успішно дісталася до тебе",
        "photo": types.InputFile('./static/mails_in_future.jpg')}


def faculty_test_msg():
    return {
        "text": "Ти вже знаєш який твій факультет в Гогвардсі, яка ти принцеса Дісней та ким був/була у минулому житті,"
                " але досі не знаеш який ти факультет в могилянці?\n"
                f"Тоді хучшіш проходь наш {link('тест', 'http://www.quiz-maker.com/QYS5XZ3UN')}! "
                "Судячи з того яку каву ти п‘єш, чим займаєшся у вільний час та які "
                "меми полюбляєш ми визначимо чи правильний ти зробив вибір при вступі",
        "photo": types.InputFile('./static/tests.jpg')
    }


def quarantynnyk_msg():
    return {
        "text": "karantynnyk description"
    }


def memes_msg():
    return {
        "text": "memes description",
        "photo": types.InputFile('./static/memes.jpg')
    }


def forbid_msg():
    return {
        "text": "Привіт!\n"
                "Ми ще поки готуємо взлом пентагону, виносимо геймерські столи і запускаємо ігри.\n"
                "Повертайся сюди 20.09.2020 о 17:00!",
        "photo": "types.InputFile('./static/ff_image.JPG')"
    }
