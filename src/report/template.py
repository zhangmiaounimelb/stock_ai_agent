"""股票分析报告 HTML 模板"""

REPORT_TEMPLATE = """<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<title>{{ stock_name }} 分析报告</title>
<style>
  body { font-family: "Microsoft YaHei", Arial, sans-serif; margin: 40px; background: #f5f5f5; }
  .container { max-width: 900px; margin: 0 auto; background: #fff; padding: 40px; border-radius: 8px; }
  h1 { color: #1a1a2e; border-bottom: 2px solid #1a1a2e; padding-bottom: 10px; }
  h2 { color: #2c3e50; margin-top: 30px; background: #eaf0fb; padding: 8px 12px; border-radius: 4px; }
  p { line-height: 1.8; color: #333; }
  .placeholder { color: #999; font-style: italic; }
  .meta { color: #666; font-size: 14px; }
  .warning { color: #e74c3c; }
  .section { margin-bottom: 30px; }
</style>
</head>
<body>
<div class="container">
  <h1>{{ company_name }}（{{ ts_code }}）分析报告</h1>
  <p class="meta">生成日期：{{ report_date }}</p>

  <div class="section">
    <h2>一、公司基本情况</h2>
    <p><strong>创建时间：</strong>{{ basic_info.founded }}</p>
    <p><strong>上市时间：</strong>{{ basic_info.listed }}</p>
    <p><strong>公司性质：</strong>{{ basic_info.nature }}</p>
    <p><strong>大股东：</strong>{{ basic_info.major_shareholder }}</p>
    <p><strong>主要业务：</strong>{{ basic_info.main_business }}</p>
    <p><strong>业务特征：</strong>{{ basic_info.business_features }}</p>
    <p><strong>行业地位：</strong>{{ basic_info.industry_position }}</p>
  </div>

  <div class="section">
    <h2>二、近3-5年股价表现</h2>
    <p class="placeholder">（待接入真实数据）</p>
  </div>

  <div class="section">
    <h2>三、历史财务数据</h2>
    <p class="placeholder">（待接入真实数据：营收、利润、毛利率、净利率、ROE、杠杆率）</p>
  </div>

  <div class="section">
    <h2>四、资产负债情况</h2>
    <p class="placeholder">（待接入真实数据）</p>
  </div>

  <div class="section">
    <h2>五、历史发展与行业特点</h2>
    <p><strong>公司历史：</strong>{{ history_and_industry.company_history }}</p>
    <p><strong>行业特点：</strong>{{ history_and_industry.industry_features }}</p>
  </div>

  <div class="section">
    <h2>六、与竞争对手比较</h2>
    <p class="placeholder">（待接入真实数据：毛利率、净利率、ROE、杠杆率对比）</p>
  </div>

  <div class="section">
    <h2>七、分红与回购历史</h2>
    <p class="placeholder">（待接入真实数据）</p>
  </div>

  <div class="section">
    <h2>八、历史污点</h2>
    {% if controversy.has_issues %}
    <p class="warning">{{ controversy.details }}</p>
    {% else %}
    <p>{{ controversy.details }}</p>
    {% endif %}
  </div>

  <div class="section">
    <h2>九、未来战略与发展前景</h2>
    <p><strong>战略规划：</strong>{{ future_outlook.strategy }}</p>
    <p><strong>发展前景：</strong>{{ future_outlook.prospects }}</p>
  </div>

</div>
</body>
</html>"""
