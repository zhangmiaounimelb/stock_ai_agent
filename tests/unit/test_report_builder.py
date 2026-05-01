from src.report.report_builder import generate_report

def test_generate_report():
    file_path = generate_report(
        stock_name="贵州茅台",
    )
    print(f"报告已生成：{file_path}")

    # 验证文件存在
    import os
    assert os.path.exists(file_path), f"报告文件未生成: {file_path}"
