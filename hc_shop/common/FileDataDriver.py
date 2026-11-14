# coding = utf-8
# Author: Yang
# Date: 2024/3/5 21:56
import openpyxl


class FileReader():
    path = r"./test_excel/api_cases_V1.xlsx"
    sheet_name = "Sheet1"

    # 读取excel
    @staticmethod  # 使用静态方法,直接调用户类中的函数
    def read_excel(path=path, sheet_name=sheet_name):
        # 打开excel文件
        try:
            file_open = openpyxl.load_workbook(path)
        except Exception as e:
            print("用例excel文件不存在,需要新建!", e)
            # 若不存在需要创建新的excel文件
            file_open = openpyxl.Workbook()
        # 判断需要打开的sheet页是否存在于excel中
        if sheet_name in file_open.sheetnames:
            sheet_name_info = file_open[sheet_name]
        else:
            # 如果不存在需要重新创建sheet页
            sheet_name_info = file_open.create_sheet(sheet_name)
        # 获取excel中的列名
        header = [column.value for column in sheet_name_info[2]]
        # 创建一个空的列表
        data = list()
        # 把数据从第三行取出
        for row in sheet_name_info.iter_rows(min_row=3, max_row=None, min_col=None, max_col=None, values_only=True):
            data.append(dict(zip(header, row)))
        file_open.close()
        # print(f"读取excel文件内容:{data}")
        return data

    # 写入excel文件
    @staticmethod
    def write_excel(path=path, sheet_name=sheet_name, row=None, column=None, value=None):
        try:
            file_open = openpyxl.load_workbook(path)
        except Exception as e:
            print("需要写入的excel文件不存在,系统自行创建",e)
            file_open = openpyxl.Workbook()
        # 判断sheet_name页是否存在于file_open文件中
        if sheet_name in file_open.sheetnames:
            sheet_name_info = file_open[sheet_name]
        else:
            # 重新创建一个sheet_name页
            sheet_name_info = file_open.create_sheet(sheet_name)
        # 使用cell方法将需要写入的值写入sheet_name
        sheet_name_info.cell(row=row, column=column, value=value)
        # 将修改后的文件保存
        file_open.save(path)

if __name__ == '__main__':
    FileReader.read_excel()
    # FileReader.write_excel(row=3,column=12,value="测试通过")
