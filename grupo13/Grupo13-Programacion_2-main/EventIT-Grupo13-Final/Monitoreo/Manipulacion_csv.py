from _csv import reader

import pandas as pd
import csv


def write(csv_name, column1, column2, data1, data2):
    df = pd.read_csv(f"../Database/DB_{csv_name}.csv")
    index_column1 = df.index[df[column1] == data1].tolist()
    df.at[index_column1[0], column2] = data2
    df.to_csv(f"../Database/DB_{csv_name}.csv", index=False)


def writeRow(csv_name, data1, data2, data3, data4, data5, data6, data7):
    f1 = open(f"../Database/DB_{csv_name}.csv", "a", newline="")
    writer1 = csv.writer(f1)
    if data7 == 0:
        new_tuple1 = (data1, data2, data3, data4, data5, data6, data7)
        writer1.writerow(new_tuple1)
    else:
        new_tuple1 = (data1, data2, data3, data4, data5, data6)
        writer1.writerow(new_tuple1)


def writeRow1(csv_name, data1):
    f1 = open(f"../Database/DB_{csv_name}.csv", "a", newline="")
    writer1 = csv.writer(f1)
    if isinstance(data1, str):
        new_tuple2 = [data1]
    else:
        new_tuple2 = data1
    writer1.writerow(new_tuple2)


def writeRow2(csv_name, data1, data2):
    f1 = open(f"../Database/DB_{csv_name}.csv", "a", newline="")
    writer1 = csv.writer(f1)
    new_tuple2 = (data1, data2)
    writer1.writerow(new_tuple2)


def writelist(csv_name, column1, column2, data1, data2, condition):
    request_list = getList(csv_name, column1, column2, data1)
    if request_list == condition:
        if isinstance(data2, list):
            new_request_list = data2
        else:
            new_request_list = [data2]
        write(csv_name, column1, column2, data1, new_request_list)
    else:
        request_list.append(data2)
        write(csv_name, column1, column2, data1, request_list)


def sumValue(csv_name, column1, column2, data1, num):
    df = pd.read_csv(f"../Database/DB_{csv_name}.csv")
    df.loc[df[column1] == data1, column2] += num
    df.to_csv(f"../Database/DB_{csv_name}.csv", index=False)


def getRow(csv_name, data1):
    csv_name1 = csv_name.lower()
    with open(f"../Database/DB_{csv_name1}.csv", "r") as read:
        database = reader(read)
        for line in database:
            for element in line:
                if element == data1:
                    info = line
                    return info


def getList(csv_name, column1, column2, data1):
    df = pd.read_csv(f"../Database/DB_{csv_name}.csv")
    df[column2] = df[column2].apply(eval)
    df.set_index(column1, inplace=True)
    return df.loc[data1, column2]


def getValue(csv_name, column1, column2, data1):
    df = pd.read_csv(f"../Database/DB_{csv_name}.csv")
    df.set_index(column1, inplace=True)
    return df.loc[data1][column2]


def getDatabase(csv_name):
    df = pd.read_csv(f"../Database/DB_{csv_name}.csv")
    return df


def sortDatabase(csv_name):
    df = pd.read_csv(f"../Database/DB_{csv_name}.csv")
    df.sort_values(["Participants"], axis=0, ascending=[False], inplace=True)
    return df


def sortDatabase_coords(csv_name, x, y):
    df = sortDatabase(csv_name)
    df = df[df['Coords_x'] == x]
    df = df[df['Coords_y'] == y]
    return df


def compareFirst3Row(db1, db2):
    lista1 = db1.values.tolist()
    lista2 = db2.values.tolist()
    num = 0
    while num <= 3:
        if not lista1[num][0] == lista2[num][0]:
            return True
        num += 1
    return False


def confirmation(csv_type, data, num):
    with open(f"../Database/DB_{csv_type}.csv", "r") as file:
        database = csv.reader(file, delimiter=",")
        for line in database:
            if str(data) == line[num]:
                return True
        return False
