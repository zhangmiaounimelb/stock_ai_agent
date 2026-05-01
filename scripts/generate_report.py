import sys
from pathlib import Path

# 把项目根目录加入 sys.path，让 Python 能找到 src 包
PROJECT_ROOT = Path(__file__).parent.parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from src.report.report_builder import generate_report
directory = "G:/My Drive/股票分析-施洛斯方法"

if __name__ == "__main__":
    stock_name = "迈瑞医疗"
    file_path = generate_report(stock_name, directory)
    print(f"报告已生成：{file_path}")
