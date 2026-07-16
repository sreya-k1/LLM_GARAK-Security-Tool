import os
import json

# ----------------------------
# OWASP LLM Top 10 Mapping
# ----------------------------

OWASP_MAP = {
    "promptinject": ("LLM01: Prompt Injection", "HIGH"),
    "ansiescaped": ("LLM01: Prompt Injection", "MEDIUM"),
    "ansiraw": ("LLM01: Prompt Injection", "MEDIUM"),
    "systempromptextraction": ("LLM07: System Prompt Leakage", "CRITICAL"),
    "colabaidataleakage": ("LLM02: Sensitive Information Disclosure", "HIGH"),
    "realtoxicityprompts": ("LLM06: Harmful Content", "HIGH"),
    "hijackkillhumans": ("LLM06: Harmful Content", "CRITICAL"),
    "hijacklongprompt": ("LLM01: Prompt Injection", "HIGH"),
    "markdownurimageexfilextended": (
        "LLM02: Sensitive Information Disclosure",
        "HIGH",
    ),
    "stringassemblydataexfil": (
        "LLM02: Sensitive Information Disclosure",
        "HIGH",
    ),
    "tapcached": ("LLM08: Excessive Agency", "MEDIUM"),
    "gcgcached": ("LLM08: Excessive Agency", "MEDIUM"),
}


# ----------------------------
# Find Garak Reports
# ----------------------------

REPORT_DIR = "garak_reports"

files = [
    file
    for file in os.listdir(REPORT_DIR)
    if file.endswith(".report.jsonl")
]

print(f"\nFound {len(files)} report files.\n")


# ----------------------------
# Create Reports Folder
# ----------------------------

os.makedirs("reports", exist_ok=True)

output = open(
    "reports/final_report.md",
    "w",
    encoding="utf-8"
)

output.write("# LLM Security Assessment Report\n\n")


# ----------------------------
# Parse JSONL Files
# ----------------------------

for file in files:

    filepath = os.path.join(REPORT_DIR, file)

    print("=" * 60)
    print(file)
    print("=" * 60)

    output.write(f"\n## File: {file}\n\n")

    with open(filepath, encoding="utf-8") as f:

        for line in f:

            try:

                data = json.loads(line)

            except:
                continue

            probe = str(data.get("probe", "")).lower()

            if probe == "":
                continue

            for key in OWASP_MAP:

                if key in probe:

                    category, severity = OWASP_MAP[key]

                    output.write(
                        f"- Probe: {probe}\n"
                    )

                    output.write(
                        f"  - OWASP Mapping: {category}\n"
                    )

                    output.write(
                        f"  - Severity: {severity}\n\n"
                    )

                    print(
                        f"{probe} --> {category} ({severity})"
                    )


# ----------------------------
# Finish Report
# ----------------------------

output.write("\n---\n")
output.write(
    "Generated using Garak + Custom OWASP Mapping Engine\n"
)

output.close()

print("\nReport Generated Successfully!")
print("Location: reports/final_report.md")