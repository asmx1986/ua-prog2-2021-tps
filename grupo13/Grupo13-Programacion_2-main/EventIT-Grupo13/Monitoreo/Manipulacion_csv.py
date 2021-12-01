from _csv import reader

import pandas as pd
import csv


def write(csv_name, column1, column2, data1, data2):
    df = pd.read_csv(f"../Database/{csv_name}.csv")
    index_column1 = df.index[df[column1] == data1].tolist()
    df.at[index_column1[0], column2] = data2
    df.to_csv(f"../Database/{csv_name}.csv", index=False)


def writeRow(csv_name, data1, data2, data3, data4, data5, data6):
    f1 = open(f"../Database/DB_{csv_name}.csv", "a", newline="")
    writer1 = csv.writer(f1)
    new_tuple1 = (data1, data2, data3, data4, data5, data6)
    writer1.writerow(new_tuple1)



def writeRow1(csv_name, data1):
    f1 = open(f"../Database/DB_{csv_name}.csv", "a", newline="")
    writer1 = csv.writer(f1)
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
    df = pd.read_csv(f"../Database/{csv_name}.csv")
    df[column2] = df[column2].apply(eval)
    df.set_index(column1, inplace=True)
    return df.loc[data1, column2]


def getValue(csv_name, column1, column2, data1):
    df = pd.read_csv(f"../Database/{csv_name}.csv")
    df.set_index(column1, inplace=True)
    return df.loc[data1][column2]


def getDatabase(csv_name):
    df = pd.read_csv(f"../Database/{csv_name}.csv")
    return df


def sortDatabase(csv_name):
    df = lenoflist(csv_name, "Participants")
    df.sort_values(["Participants"], axis=0, ascending=[False], inplace=True)
    return df


def compareFirst3Row(db1, db2, column):
    one = db1.loc[0][column] == db2.loc[0][column]
    two = db1.loc[1][column] == db2.loc[0][column]
    three = db1.loc[2][column] == db2.loc[0][column]
    if one or two or three:
        return True
    else:
        return False


def sortDatabase_coords(csv_name, x, y):
    df = sortDatabase(csv_name)
    df = df[df['Coords_x'] == x]
    df = df[df['Coords_y'] == y]
    return df


def lenoflist(csv_name, column2):
    df = pd.read_csv(f"../Database/{csv_name}.csv")
    df[column2] = df[column2].apply(eval)
    num = 0
    while num < len(df):
        participants = df.at[num, column2]
        if participants == ['Nada que encontrar...']:
            df.at[num, column2] = 0
        else:
            num_participants = len(participants)
            df.at[num, column2] = num_participants
        num += 1
    return df


