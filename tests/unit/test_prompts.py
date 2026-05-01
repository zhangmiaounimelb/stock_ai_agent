import json
from src.tools.llm import call_llm
from src.agent.prompts import COMPANY_ANALYSIS_PROMPT

def test_prompt_returns_valid_json():
    prompt = COMPANY_ANALYSIS_PROMPT.format(
        stock_name="茅台",
    )
    print("=== PROMPT ===")
    print(prompt)
    print("=== RESPONSE ===")

    raw = call_llm(prompt)
    print(raw)

    # 验证是合法 JSON
    data = json.loads(raw)
    print("=== PARSED JSON ===")
    print(json.dumps(data, ensure_ascii=False, indent=2))

    # 验证必要字段存在
    assert "basic_info" in data
    assert "history_and_industry" in data
    assert "controversy" in data
    assert "future_outlook" in data
