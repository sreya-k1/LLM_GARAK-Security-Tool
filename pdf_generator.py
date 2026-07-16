from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)

from reportlab.lib.styles import getSampleStyleSheet

pdf = SimpleDocTemplate(
    "reports/final_report.pdf"
)

styles = getSampleStyleSheet()

elements = []

elements.append(
    Paragraph(
        "LLM Security Assessment Report",
        styles["Title"]
    )
)

elements.append(
    Spacer(1, 20)
)

with open(
    "reports/final_report.md",
    encoding="utf-8"
) as f:

    for line in f:

        elements.append(
            Paragraph(
                line.replace("\n", ""),
                styles["BodyText"]
            )
        )

pdf.build(elements)

print("PDF Generated!")