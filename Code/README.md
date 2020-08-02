По умолчанию предобученные модели берутся из папки ```trained_models```,
поэтому, чтобы запустить предобученную модель на тесте, её нужно положить
в эту папку.
Допустимые названия моделей:
1) BERT_MULTIGRAN_model_sigmoid_ru.pt

В папке ```data_ru``` лежат все размеченные тексты.

В папке ```bert``` должны лежать следующие файлы
(их можно скачать, к примеру, со страницы http://docs.deeppavlov.ai/en/master/features/pretrained_vectors.html,
RuBERT [pytorch]):
1) bert_config.json
2) pytorch_model.bin
3) vocab.txt 

Последовательность действий для запуска приложения из корневой папки:
0. python -m venv myvenv
1. python -m pip install -r requirements.txt 
2. python flask_application.py
3. --> 127.0.0.1:5000
