from xhtml2pdf import pisa

with open("github_summary.html", "rb") as src, open("github_summary.pdf", "wb") as dst:
    pisa.CreatePDF(src, dst)
print("✅ PDF 生成成功：github_summary.pdf")
