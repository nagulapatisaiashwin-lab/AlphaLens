"""
HTML templates for AlphaLens reports.
"""

from __future__ import annotations


def render_page(title: str, body: str) -> str:
    """
    Render the complete HTML page.
    """

    return f"""
<!DOCTYPE html>
<html lang="en">

<head>

<meta charset="UTF-8">

<meta name="viewport" content="width=device-width, initial-scale=1.0">

<title>{title}</title>

<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>

<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">

<style>

:root {{
    --bg:#0f172a;
    --card:#1e293b;
    --card-light:#263548;
    --border:#334155;

    --text:#f8fafc;
    --muted:#94a3b8;

    --accent:#38bdf8;
}}

* {{
    margin:0;
    padding:0;
    box-sizing:border-box;
}}

body {{
    background:var(--bg);
    color:var(--text);
    font-family:'Inter','Segoe UI',sans-serif;
    line-height:1.6;
}}

.container {{
    max-width:1400px;
    margin:40px auto;
    padding:30px;
}}

.report-header {{
    text-align:center;
    margin-bottom:40px;
}}

.report-header h1 {{
    font-size:3rem;
    font-weight:800;
}}

.report-header p {{
    margin-top:10px;
    color:var(--muted);
}}

.kpi-grid {{
    display:grid;
    grid-template-columns:repeat(auto-fit,minmax(220px,1fr));
    gap:20px;
    margin-bottom:35px;
}}

.kpi {{
    background:var(--card);
    border:1px solid var(--border);
    border-radius:18px;
    padding:24px;
    text-align:center;
    transition:.25s;
}}

.kpi:hover {{
    transform:translateY(-3px);
}}

.kpi-value {{
    font-size:2rem;
    font-weight:700;
    margin-bottom:8px;
}}

.kpi-label {{
    color:var(--muted);
    font-size:.9rem;
}}

.grid {{
    display:grid;
    grid-template-columns:repeat(auto-fit,minmax(420px,1fr));
    gap:24px;
}}

.section {{
    background:var(--card);
    border:1px solid var(--border);
    border-radius:18px;
    padding:28px;
    margin-bottom:24px;
}}

.section h2 {{
    color:var(--accent);
    margin-bottom:20px;
}}

.metric-row {{
    display:flex;
    justify-content:space-between;
    align-items:center;
    padding:14px 0;
    border-bottom:1px solid var(--border);
}}

.metric-row:last-child {{
    border-bottom:none;
}}

.metric-row span {{
    color:var(--muted);
}}

.metric-row strong {{
    color:white;
    font-variant-numeric:tabular-nums;
}}

.report-footer {{
    text-align:center;
    margin-top:50px;
    color:var(--muted);
    font-size:.9rem;
}}

@media (max-width:900px) {{

.grid {{
    grid-template-columns:1fr;
}}

}}

</style>

</head>

<body>

<div class="container">

{body}

</div>

</body>

</html>
"""