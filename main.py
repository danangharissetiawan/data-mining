def trans_cate(row):
    if 100000 <= row['Average_Transaction_Amount'] <= 200000:
        val = '1. 100.000 - 250.000'
    elif 250000 <= row['Average_Transaction_Amount'] <= 500000:
        val = '2. 250.000 - 500.000'
    elif 500000 <= row['Average_Transaction_Amount'] <= 750000:
        val = '3. 500.000 - 750.000'
    elif 750000 <= row['Average_Transaction_Amount'] <= 1000000:
        val = '4. 750.000 - 1.000.000'
    elif 1000000 <= row['Average_Transaction_Amount'] <= 2500000:
        val = '5. 1.000.000 - 2.500.000'
    elif 2500000 <= row['Average_Transaction_Amount'] <= 5000000:
        val = '6. 2.500.000 - 5.000.000'
    elif 5000000 <= row['Average_Transaction_Amount'] <= 10000000:
        val = '7. 5.000.000 - 10.000.000'

    return val