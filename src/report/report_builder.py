import json
from datetime import date
from pathlib import Path

from jinja2 import Template

from .template import REPORT_TEMPLATE
from ..agent.prompts import COMPANY_ANALYSIS_PROMPT
from ..tools.llm import call_llm

def generate_report(
    stock_name: str,
    output_dir: str = "output",
) -> str:
    """调用 LLM 生成分析内容，渲染 HTML 报告，返回文件路径"""

    prompt = COMPANY_ANALYSIS_PROMPT.format(
        stock_name=stock_name,
    )
    raw = call_llm(prompt)
    data = json.loads(raw)

    tmpl = Template(REPORT_TEMPLATE)
    html_content = tmpl.render(
        stock_name=stock_name,
        report_date=date.today().isoformat(),
        **data,
    )

    out_path = Path(output_dir)
    out_path.mkdir(parents=True, exist_ok=True)
    file_path = out_path / f"{date.today().isoformat()}_{stock_name}.html"
    file_path.write_text(html_content, encoding="utf-8")

    return str(file_path)
