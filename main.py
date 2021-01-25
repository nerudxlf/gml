import pandas as pd

label = "    label "
faculty = "    faculty "
f_department = "    f_department "
n = "\n"


def main():
    arr_for_out = []
    df = pd.read_excel('data.xlsx')
    name_list = list(df['name'])
    f_list = list(df['f'])
    dep_list = list(df['dep'])

    with open("WoS_All_new.txt", "r", encoding="utf-8") as file:
        len_str = file.read()

    split_len_str = len_str.split("node")

    for i in split_len_str:
        flag = True
        for j in range(len(name_list)):
            arr_name_equals = name_list[j].split("; ")
            for x in arr_name_equals:
                if i.find(label + '"' + x + '"' + n) != -1:
                    name_list[j] = "0"
                    new = i.replace(faculty + '"1"' + n, faculty + '"' + str(f_list[j]) + '"' + n)
                    new = new.replace(f_department + '"2"' + n, f_department + '"' + str(dep_list[j]) + '"' + n)
                    arr_for_out.append(new)
                    flag = False
        if flag:
            arr_for_out.append(i)

    out_str = "node".join(arr_for_out)

    f = open('out.txt', 'w')
    f.write(out_str)
