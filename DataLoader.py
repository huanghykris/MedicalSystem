import os
import json

class DataLoader:
    def __init__(self,input_file_path,output_file_path,limit=None):
        # 获取当前脚本文件的目录
        cur_dir = os.path.dirname(os.path.abspath(__file__))
        # 构建完整的文件路径
        self.input_file_path = os.path.join(cur_dir, input_file_path)
        self.output_file_path = os.path.join(cur_dir, output_file_path)
        self.limit = limit
        # 加载 JSON 数据，并只保留前 1000 条
        self.load_data()

    def load_data(self):
        # 打开并读取json文件
        with open(self.input_file_path,'r',encoding='utf-8') as file:
            count = 0
            self.data = []
            for line in file:
                if self.limit and count >= self.limit:
                    break
                try:
                    # item = json.loads(line)
                    self.data.append(line)
                except json.JSONDecodeError as e:
                    print(f"Error decoding JSON on line: {e}")
                count += 1
        return self.data

    def save_data(self):
        cur_dir = os.path.dirname(os.path.abspath(__file__))
        os.makedirs(cur_dir,exist_ok=True)
        with open(self.output_file_path,'w',encoding='utf-8') as file:
            for line in self.data:
                file.write(line)
        print(f"The data has been saved in {self.output_file_path}")
