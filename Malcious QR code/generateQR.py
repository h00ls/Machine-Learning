import qrcode
import requests
import csv
import os
from tqdm import tqdm
import time
import random
from concurrent.futures import ThreadPoolExecutor

csvFile = open("phishing.csv", "r", encoding="utf8")
reader = csv.reader(csvFile)

result = {}
for item in reader:
    # 忽略第一行
    if reader.line_num == 1:
        continue
    result[item[0]] = item[1]

csvFile.close()

data = list(result)
labels = list(result.values())

length = [len(data[i]) for i in range(len(data))]

# good = 0
# bad = 0
# for i in range(len(data)):
#     if length[i] <= 30:
#         if labels[i] == "good":
#             good += 1
#         else:
#             bad += 1
    
#     else:
#         pass


def qr_gen(url, path, index):
    qr = qrcode.QRCode(
            version=2,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=5,
            border=0
        )#设置二维码的大小
    qr.add_data(url)
    qr.make(fit=True)
    img = qr.make_image()

    filename = os.path.join(path, str(index) + ".png")

    print(filename)
    img.save(filename)


good_cnt = 0
bad_cnt = 0

with ThreadPoolExecutor(10) as executor:

    for index in tqdm(range(len(data))):

        if length[index] <= 30:
            
            if labels[index] == "good" and good_cnt <= 30000:

                executor.submit(qr_gen, data[index], labels[index], index)

                good_cnt += 1
            
            elif labels[index] == "bad" and bad_cnt <= 30000:

                executor.submit(qr_gen, data[index], labels[index], index)

                bad_cnt += 1
            
            else:
                pass
        else:
            pass            
