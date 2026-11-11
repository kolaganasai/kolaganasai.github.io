"""Builds index.html (GitHub Pages) from content.html."""
import re
from pathlib import Path
src = Path(__file__).parent / "content.html"
s = src.read_text(encoding="utf-8")
head_end = s.index("<style>")
head_bits, body = s[:head_end], s[head_end:]
head_bits = head_bits.replace('<meta name="claude:viewport-fit-sides" content="cover">\n', "")
style_end = body.index("</style>") + len("</style>")
style, rest = body[:style_end], body[style_end:]
RESUMES = [("SAP ABAP resume", "Kola_Gana_Sai_Resume_SAP_ABAP.pdf", "ABAP resume"),
           ("Software and AI resume", "Kola_Gana_Sai_Resume_Software_AI.pdf", "AI resume")]
resume = "".join(
    f'<a href="assets/{f}" target="_blank" rel="noopener"><span class="ico"><svg><use href="#i-doc"/></svg></span>'
    f'<span><small>{label}</small><span class="v">{f}</span></span><svg class="arrow" aria-hidden="true"><use href="#i-arrow"/></svg></a>'
    for label, f, _ in RESUMES)
resume_btn = "".join(
    f'<a class="btn btn-ghost" href="assets/{f}" target="_blank" rel="noopener"><svg aria-hidden="true"><use href="#i-doc"/></svg>{short}</a>'
    for _, f, short in RESUMES)
rest = rest.replace("<!--RESUME-->", resume).replace("<!--RESUME_BTN-->", resume_btn)
# both resume buttons replace the hero's "Get in touch" button (Contact stays in the top bar)
rest = rest.replace('          <a class="btn btn-ghost" href="#contact">Get in touch</a>\n', "")
favicon = ("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'%3E%3Crect width='32' height='32' rx='6' fill='%230D2240'/%3E"
           "%3Ctext x='16' y='22' font-family='monospace' font-size='15' font-weight='700' fill='white' text-anchor='middle'%3EKGS%3C/text%3E%3C/svg%3E")
page = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<meta name="description" content="Kola Gana Sai: SAP ABAP and Python developer. Projects, skills and contact.">
<meta property="og:title" content="Kola Gana Sai">
<meta property="og:description" content="SAP ABAP and Python developer, final-year CSE student in Guntur.">
<link rel="icon" href="{favicon}">
{head_bits.strip()}
{style}
</head>
<body>
{rest.strip()}
</body>
</html>
"""
(Path(__file__).parent.parent / "index.html").write_text(page, encoding="utf-8")
(Path(__file__).parent.parent / "artifact.html").write_text(s.replace("<!--RESUME-->", "").replace("<!--RESUME_BTN-->", ""), encoding="utf-8")
print("built")
