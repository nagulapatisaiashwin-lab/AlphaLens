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

    --bg:#0B1220;
    --surface:#111827;
    --surface-2:#1F2937;
    --border:#334155;

    --text:#F8FAFC;
    --muted:#94A3B8;

    --accent:#38BDF8;
    --shadow:rgba(0,0,0,.35);

}}

* {{
    margin:0;
    padding:0;
    box-sizing:border-box;
}}

html {{
    scroll-behavior:smooth;
}}

body {{

    background:var(--bg);
    color:var(--text);

    font-family:'Inter',sans-serif;
    line-height:1.6;

}}

.container {{

    max-width:1650px;

    margin:auto;

    padding:42px;

}}

.report-header {{

    text-align:center;

    margin-bottom:50px;

}}

.report-header h1 {{

    font-size:3rem;
    font-weight:800;
    letter-spacing:-1px;

}}

.report-header p {{

    margin-top:14px;

    color:var(--muted);

    font-size:1.05rem;

}}

.kpi-grid {{

    display:grid;

    grid-template-columns:
        repeat(auto-fit,minmax(220px,1fr));

    gap:24px;

    margin-bottom:42px;

}}

.kpi {{

    position:relative;

    overflow:hidden;

    background:
        linear-gradient(
            180deg,
            var(--surface-2),
            var(--surface)
        );

    border:1px solid var(--border);

    border-radius:20px;

    padding:28px;

    text-align:center;

    transition:.25s ease;

    box-shadow:
        0 10px 30px var(--shadow);

}}

.kpi::before {{

    content:"";

    position:absolute;

    left:0;
    top:0;

    width:100%;
    height:4px;

    background:
        linear-gradient(
            90deg,
            #3B82F6,
            #38BDF8
        );

}}

.kpi:hover {{

    transform:translateY(-4px);

}}

.kpi-value {{

    font-size:2.2rem;

    font-weight:800;

    margin-bottom:8px;

}}

.kpi-label {{

    color:var(--muted);

    font-size:.92rem;

}}

.grid {{

    display:grid;

    grid-template-columns:
        repeat(auto-fit,minmax(470px,1fr));

    gap:28px;

}}

.section {{

    background:
        linear-gradient(
            180deg,
            var(--surface-2),
            var(--surface)
        );

    border:1px solid var(--border);

    border-radius:20px;

    padding:30px;

    margin-bottom:28px;

    overflow:hidden;

    box-shadow:
        0 12px 30px var(--shadow);

}}

.section h2 {{

    color:var(--accent);

    font-size:1.35rem;

    font-weight:700;

    margin-bottom:22px;

}}

.section > div[style] {{

    width:100%!important;
    max-width:100%!important;
    min-width:0!important;

}}

.section .plotly-graph-div {{

    width:100%!important;
    max-width:100%!important;

}}

.metric-row {{

    display:flex;

    justify-content:space-between;

    align-items:center;

    padding:16px 0;

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

    font-weight:700;

    font-variant-numeric:tabular-nums;

}}

.report-footer {{

    text-align:center;

    margin-top:70px;

    color:var(--muted);

    font-size:.92rem;

}}

@media (max-width:1000px) {{

.grid {{
    grid-template-columns:1fr;
}}

.container {{
    padding:20px;
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