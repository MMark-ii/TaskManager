#!/bin/bash

# Обновление пакетов и установка виртуального окружения
sudo apt update
sudo apt install -y python3-venv python3-pip

# Создание виртуального окружения
python3 -m venv .venv

# Активация виртуального окружения
source .venv/bin/activate

# Установка зависимостей
pip install -r ./requirements.txt

# Деактивация виртуального окружения
deactivate

echo "Виртуальная среда и зависимости успешно установлены."
