import pandas as pd

label = "    label "
faculty = "    faculty "
f_department = "    f_department "
n = "\n"


def main():
    df = pd.read_excel('data.xlsx')
    name_list = list(df['name'])
    f_list = list(df['f'])
    dep_list = list(df['dep'])
    with open("WoS_All_new.txt", "r", encoding="utf-8") as file:
        len_str = file.read()
    split_len_str = len_str.split("node")
    new_arr = []
    for i in split_len_str:
        for j in range(len(name_list)):
            arr_name_equals = name_list[j].split(";")
            for x in arr_name_equals:
                if i.find(label + '"' + x + '"' + n) != -1:
                    name_list[j] = "0"
                    new = i.replace(faculty+'"1"'+n, faculty+'"' + f_list[j] + '"' + n)
                    new = new.replace(f_department+'"2"'+n, f_department + '"' + dep_list[j] + '"' + n)
                    new_arr.append(new)
        new_arr.append(i)
    out_str = ""
    for i in new_arr:
        out_str += i+"  node"
    print(out_str)
    f = open('out.txt', 'w')
    f.write(out_str[:-6])


if __name__ == '__main__':
    main()
