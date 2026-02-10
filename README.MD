### Обновляем список пакетов  
`apt update`
### Обновляем пакеты
`apt upgrade`
### Перезагружаем сервер
reboot
### Устанавливаем необхоидмые пакеты
apt install ffmpeg python3.12-venv
### Копируем репозиторий GigaAM
git clone https://github.com/salute-developers/GigaAM.git
### Переходим в директорию проекта
cd GigaAM/
### Создаем виртуальное окружение для проекта
python3 -m venv gigaam
### Переходим в данное окружение
source  gigaam/bin/activate
### Заменяем setup.py
### Устанавливаем зависимости
pip install -e .
# Выходим из вирутального окружения
deactivate
