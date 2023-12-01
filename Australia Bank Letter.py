import re
import pandas as pd

def extract_data_from_email(email_text):
    # Паттерн для извлечения данных из раздела REQUESTS FOR INFORMATION REPORT
    rfi_pattern = re.compile(
        r"NAB RFI REF.: (\S+).*?CARD NUMBER : (\S+).*?MERCHANT: (.*?).*?DEADLINE : (\S+).*?TRAN. DATE : (\S+).*?AMOUNT \(.*?\): ([\d.]+).*?REASON : (.*?)\n",
        re.DOTALL
    )

    # Извлечение данных из текста письма
    rfi_matches = rfi_pattern.findall(email_text)

    # Если есть данные, создаем DataFrame
    if rfi_matches:
        rfi_data = {
            'NAB RFI REF.': [match[0] for match in rfi_matches],
            'CARD NUMBER': [match[1] for match in rfi_matches],
            'MERCHANT': [match[2] for match in rfi_matches],
            'DEADLINE': [match[3] for match in rfi_matches],
            'TRAN. DATE': [match[4] for match in rfi_matches],
            'AMOUNT': [float(match[5]) for match in rfi_matches],
            'REASON': [match[6] for match in rfi_matches],
        }

        df_rfi = pd.DataFrame(rfi_data)

        return df_rfi
    else:
        return None

# Пример текста письма
email_text = """
========================================================================================================================
REQUESTS FOR INFORMATION REPORT - EMAIL                                                               28/11/2023 - 21:05
========================================================================================================================
NAB RFI REF.: VCI-4180237   CARD NUMBER : 4546 38xx xxxx 5378        MERCHANT: BLOOMEX PTY LTD
DEADLINE    : 08.12.2023    REQUEST TYPE: RETRIEVAL - CBK                      UNIT 9/12-18 VICTORIA ST
TRAN. DATE  : 11/11/2023    AMOUNT (NZD): 83.90                                LIDCOMBE NSW 2141
TRAN TIME   : 20:02:46      TERMINAL ID.: 20547840 Y1T5TE            STORE NO: 000547840     CUSTNO: 895281823
REASON      : Services/Merchandise not received                      AUTH. ID: 006673
LOCATION    : BLOOMEX PTY LTD         EAST LIDCOMBE                       RRN: 200246844836
CUSTOMER REF: z_202311110902_89509
------------------------------------------------------------------------------------------------------------------------
NAB RFI REF.: VCI-4180215   CARD NUMBER : 4147 34xx xxxx 2136        MERCHANT: BLOOMEX PTY LTD
DEADLINE    : 08.12.2023    REQUEST TYPE: RETRIEVAL - CBK                      UNIT 9/12-18 VICTORIA ST
TRAN. DATE  : 18/11/2023    AMOUNT (NZD): 74.90                                LIDCOMBE NSW 2141
TRAN TIME   : 14:36:15      TERMINAL ID.: 20547840 Y1T5TE            STORE NO: 000547840     CUSTNO: 895281823
REASON      : Services/Merchandise not received                      AUTH. ID: 02585D
LOCATION    : BLOOMEX PTY LTD         EAST LIDCOMBE                       RRN: 143615820893
CUSTOMER REF: z_202311180336_90709
------------------------------------------------------------------------------------------------------------------------
TOTAL RFI DETAIL RECORDS:             2
TOTAL VALUE OF RECORDS  :        158.80
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
