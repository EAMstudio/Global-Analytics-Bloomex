import re

text = """
REF.: N-1   CARD NUMBER : 001 MERCHANT: BLOOMEX
REF.: N-2
REF.: N-3   CARD NUMBER : 003
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
