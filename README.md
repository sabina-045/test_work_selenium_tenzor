# test_work_selenium_tenzor

*Инструкция для Windows:*

**Скачиваем проект:**

* git clone git@github.com:sabina-045/test_work_selenium_tenzor.git

**Устанавливаем и активируем виртуальное окружение**
* python -m venv venv
* source venv/Scripts/activate

**Устанавливаем зависимости:**
* pip install -r requirements.txt --upgrade pip

**Ставим приложение allure:**
* скачиваем и устанавливаем OpenJDK 17
  - ```https://learn.microsoft.com/en-us/java/openjdk/download```

* устанавливаем Scoop:
  - открываем power shell и вводим:
    - Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
    - Invoke-RestMethod -Uri https://get.scoop.sh | Invoke-Expression

* устанавливаем allure:
  - scoop install allure

**Запускаем тесты:**
python -m pytest --alluredir allure-results

**Генерируем отчет:**
allure serve allure-results
