import requests
import streamlit as st


API_URL = "http://backend:8000/api/v1/agent/query"


st.set_page_config(
    page_title="Agentic AI Workflow Platform",
    page_icon="🤖",
    layout="wide"
)


st.title("🤖 Agentic AI Workflow Automation Platform")

st.write(
    "AI-powered workflow automation for HR and Finance operations."
)

st.divider()

query = st.text_area(
    "Enter your request",
    placeholder=(
        "Example: How many employees are in the company?"
    ),
    height=120
)


if st.button("Run Agent", type="primary"):

    if not query.strip():

        st.warning("Please enter a request.")

    else:

        try:

            with st.spinner(
                "Agent is analyzing your request..."
            ):

                response = requests.post(
                    API_URL,
                    json={
                        "query": query
                    },
                    timeout=120
                )

            if response.status_code == 200:

                result = response.json()

                st.subheader("Agent Response")

                st.write(
                    result["response"]
                )

            else:

                st.error(
                    f"API Error: {response.text}"
                )

        except requests.exceptions.ConnectionError:

            st.error(
                "Could not connect to the FastAPI backend. "
                "Please start the backend first."
            )

        except requests.exceptions.Timeout:

            st.error(
                "The request timed out."
            )

        except Exception as error:

            st.error(
                f"Unexpected error: {error}"
            )