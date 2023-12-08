import re
import pandas as pd

def extract_data_from_email(email_text):
    # Паттерн для извлечения данных из раздела REQUESTS FOR INFORMATION REPORT
    rfi_pattern = re.compile(r"NAB RFI REF(\S+)", re.DOTALL)
    print(rfi_pattern)

    # Извлечение данных из текста письма
    rfi_matches = rfi_pattern.findall(email_text)

    # Если есть данные, создаем DataFrame
    if rfi_matches:
        rfi_data = {
            'NAB RFI REF.': rfi_matches
        }

        df_rfi = pd.DataFrame(rfi_data)

        return df_rfi
    else:
        return None

# Пример текста письма
email_text = """
========================================================================================================================
REQUESTS FOR INFORMATION REPORT - EMAIL                                                               28/01/2021 - 21:05
========================================================================================================================
NAB RFI REF.: VCI-4180117   CARD NUMBER : 4116 38xx xxxx 5118        MERCHANT: BLOOMEX PTY LTD
DEADLINE    : 08.12.2023    REQUEST TYPE: RANDOM - CBK                      UNIT 9/11-11 RANDOM ST
TRAN. DATE  : 11/01/2021    AMOUNT (NZD): 10.90                                RANDOM NSW 2111
TRAN TIME   : 20:02:46      TERMINAL ID.: 21147840 Y111TE            STORE NO: 000547840     CUSTNO: 811281113
REASON      : Services/Merchandise not received                      AUTH. ID: 006673
LOCATION    : RANDOM PTY LTD         EAST RANDOM                       RRN: 200246844836
CUSTOMER REF: z_202311110902_11119
------------------------------------------------------------------------------------------------------------------------
NAB RFI REF.: VCI-1111115   CARD NUMBER : 4117 34xx xxxx 2116        MERCHANT: BLOOMEX PTY LTD
DEADLINE    : 08.12.2023    REQUEST TYPE: RANDOM - CBK                      UNIT 9/12-18 RANDOM ST
TRAN. DATE  : 18/01/2021    AMOUNT (NZD): 11.90                                RANDOM NSW 2111
TRAN TIME   : 14:36:15      TERMINAL ID.: 20117110 Y111TE            STORE NO: 000547840     CUSTNO: 811281113
REASON      : Services/Merchandise not received                      AUTH. ID: 01185D
LOCATION    : RANDOM PTY LTD         EAST RANDOM                       RRN: 111615820893
CUSTOMER REF: z_211311180336_11119
------------------------------------------------------------------------------------------------------------------------
TOTAL RFI DETAIL RECORDS:             2
TOTAL VALUE OF RECORDS  :        23.80
------------------------------------------------------------------------------------------------------------------------
"""

# Извлечение данных
df_rfi = extract_data_from_email(email_text)

# Если есть данные, выведите DataFrame
if df_rfi is not None:
    print("Данные из раздела REQUESTS FOR INFORMATION REPORT:")
    print(df_rfi)
else:
    print("В тексте письма нет данных о REQUESTS FOR INFORMATION REPORT.")
