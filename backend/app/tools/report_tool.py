from datetime import datetime


def generate_report(
    title: str,
    summary: str,
    data: str
) -> str:
    """
    Generate a structured business report.
    """

    generated_at = datetime.now().strftime(
        "%Y-%m-%d %H:%M:%S"
    )

    report = f"""
==================================================
{title}
==================================================

Generated: {generated_at}

SUMMARY
-------
{summary}

DATA
----
{data}

==================================================
END OF REPORT
==================================================
"""

    return report