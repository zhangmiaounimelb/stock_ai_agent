from src.tools.llm import call_llm

def test_call_llm():
    res = call_llm("用一句话介绍茅台公司")
    print(res)
    assert res is not None
    assert len(res) > 0 

