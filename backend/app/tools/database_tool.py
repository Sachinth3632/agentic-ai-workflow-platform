from sqlalchemy import text

from backend.app.database.db import SessionLocal


def query_employee_data(query: str) -> str:
    """
    Query internal HR and Finance employee data.
    """

    db = SessionLocal()

    try:
        normalized_query = query.lower()

        if "count" in normalized_query or "how many" in normalized_query:
            result = db.execute(
                text("SELECT COUNT(*) FROM employees")
            ).scalar()

            return f"Total employees: {result}"

        if (
            "average salary" in normalized_query
            or "avg salary" in normalized_query
        ):
            result = db.execute(
                text("SELECT AVG(salary) FROM employees")
            ).scalar()

            return f"Average employee salary: ₹{result:,.2f}"

        if "finance" in normalized_query:
            rows = db.execute(
                text("""
                    SELECT name, role, salary, performance_score
                    FROM employees
                    WHERE department = 'Finance'
                """)
            ).fetchall()

            if not rows:
                return "No Finance employees found."

            return "\n".join(
                [
                    (
                        f"{row.name} | "
                        f"{row.role} | "
                        f"₹{row.salary:,.0f} | "
                        f"Performance: {row.performance_score}"
                    )
                    for row in rows
                ]
            )

        if "hr" in normalized_query:
            rows = db.execute(
                text("""
                    SELECT name, role, salary, performance_score
                    FROM employees
                    WHERE department = 'HR'
                """)
            ).fetchall()

            if not rows:
                return "No HR employees found."

            return "\n".join(
                [
                    (
                        f"{row.name} | "
                        f"{row.role} | "
                        f"₹{row.salary:,.0f} | "
                        f"Performance: {row.performance_score}"
                    )
                    for row in rows
                ]
            )

        rows = db.execute(
            text("""
                SELECT name, department, role,
                       salary, performance_score
                FROM employees
            """)
        ).fetchall()

        if not rows:
            return "No employee data found."

        return "\n".join(
            [
                (
                    f"{row.name} | "
                    f"{row.department} | "
                    f"{row.role} | "
                    f"₹{row.salary:,.0f} | "
                    f"Performance: {row.performance_score}"
                )
                for row in rows
            ]
        )

    finally:
        db.close()