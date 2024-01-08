"""Этот код предназначен для извлечения информации из текста банковских отчетов по чарджбэкам. Входной текст содержит
различные записи с информацией о транзакциях, включая номер карты, ссылки (REF), и название продавца (MERCHANT).

Код использует регулярные выражения для извлечения этих данных из текста. Затем он формирует список кортежей с
извлеченной информацией. В данном случае, код выводит результат в виде списка кортежей, каждый из которых
представляет собой информацию о транзакции (номер ссылки, номер карты и название продавца), если эта информация
присутствует в записи.

Этот инструмент может быть полезен для автоматического анализа и сортировки данных в банковских отчетах по
чарджбэкам, что упрощает обработку финансовых операций."""


import re

text = """
REF.: N-1   CARD NUMBER : 001 MERCHANT: BLOOMEX
REF.: N-2
REF.: N-3   CARD NUMBER : 004
REF.: N-4   MERCHANT: BLOOMEX
REF.: N-5   CARD NUMBER : 005 MERCHANT: BLOOMEX
"""


def extract_info(input_text):
    pattern = re.compile(r'REF\.: (N-\d+)(?:\s+CARD NUMBER : (\d+))?(?:\s+MERCHANT: (\w+))?')
    matches = pattern.findall(input_text)

    result = []
    for match in matches:
        result.append(tuple(part.strip() if part else None for part in match))

    return result


output = extract_info(text)
print(output)
