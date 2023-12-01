import re

rfi_pattern = re.compile(
    r"NAB RFI REF\.: (\S+)(?:.*?CARD NUMBER : (\S+))?(?:.*?MERCHANT: (.*?)\s*)?",
#   r"NAB RFI REF\.: (\S+).*?CARD NUMBER : (\S+).*?MERCHANT: (.*?)\s*",
#   r"NAB RFI REF\.: (\S+)(?:.*CARD NUMBER : (\S+))?(?:.*MERCHANT: (.*?)\s*)?",
#   r"NAB RFI REF\.: (\S+)(?:.*?CARD NUMBER : (\S+))?(?:.*?MERCHANT: (.*?)\s*)?", #it works
#   r"NAB RFI REF\.: (\S+)(?:.*CARD NUMBER : (\S+))?(?:.*MERCHANT: (.*?)\s*)?",
    re.DOTALL
)

print("rfi_pattern: ", rfi_pattern)

# Пример строки
text = """
1. NAB RFI REF.: VCI-4180237   CARD NUMBER : 0001        MERCHANT: BLOOMEX 
2. NAB RFI REF.: VCI-4180238  CARD NUMBER : 0 MERCHANT: BLOOMEX
3. NAB RFI REF.: VCI-4180239   CARD NUMBER : 0002        MERCHANT: BLOOMEX 
"""

matches = rfi_pattern.findall(text)

print("matches: ", matches)

for match in matches:
    nab_rfi_ref = match[0]
    card_number = match[1]
    merchant = match[2]

    print("NAB RFI REF.:", nab_rfi_ref)
    print("CARD NUMBER:", card_number)
    print("MERCHANT:", merchant)
    print("--------------")
