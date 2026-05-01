"""股票分析报告 Prompt 模板"""

COMPANY_ANALYSIS_PROMPT = """
你是一位专业的股票分析师。请对以下公司进行分析，并严格按照 JSON 格式返回结果，不要有任何多余的文字。

公司名称：{stock_name}


请返回以下 JSON 格式：
{{
    "basic_info": {{
        "company_name": "公司名称",
        "ts_code": "股票代码",
        "founded": "创建时间",
        "listed": "上市时间",
        "nature": "公司性质（国企/民企/外资等）",
        "major_shareholder": "大股东名称及持股比例",
        "main_business": "主要业务描述（3-5句话）",
        "business_features": "业务特征（3-5句话）",
        "industry_position": "行业地位（3-5句话）"
    }},
    "history_and_industry": {{
        "company_history": "公司历史发展（3-5句话）",
        "industry_features": "所在行业特点,公司在上下游产业链的位置（5-10句话）"
    }},
    "controversy": {{
        "has_issues": true或false,
        "details": "历史污点详情，如无则填'暂无重大负面记录'"
    }},
    "future_outlook": {{
        "strategy": "公司未来战略规划（2-3句话）",
        "prospects": "发展前景分析（2-3句话）"
    }}
}}
"""
