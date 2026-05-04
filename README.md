# YouTube Metrics Report

CLI-инструмент для генерации отчётов по метрикам видео (CSV).

## Установка
```bash
pip install -r requirements.txt
```

## Запуск
python -m app.cli --files stats1.csv stats2.csv --report clickbait

Параметры:

--files — один или несколько CSV-файлов с данными видео.

--report — тип отчёта 