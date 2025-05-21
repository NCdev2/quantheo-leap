import streamlit as st
import streamlit.components.v1 as components
import os

# --- Page Configuration ---
st.set_page_config(
    page_title="Quantheo Leap Platform",
    page_icon="⚛️",
    layout="wide",
    initial_sidebar_state="expanded",
)

# --- Helper Function to Load HTML file ---
def load_html_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        return "<p>Error: HTML file not found.</p>"
    except Exception as e:
        return f"<p>Error loading HTML file: {e}</p>"

# --- Main Application ---
def main():
    st.sidebar.title("Navigation")
    app_mode = st.sidebar.radio(
        "Choose a section:",
        ("Quantheo Leap Benchmark", "Quantum Computing Deep Dive")
    )

    if app_mode == "Quantheo Leap Benchmark":
        st.title("⚛️ Quantheo Leap - ICT Benchmark Explorer")
        st.markdown("""
            Welcome to the Quantheo Leap Benchmark Explorer. 
            Select an ICT problem and complexity level, then run the benchmark to compare 
            classical and quantum-enhanced solver performance.
            """)
        
        # Construct the absolute path to the HTML file
        # IMPORTANT: This path needs to be correct for your Streamlit deployment environment.
        # If deploying, ensure this file is in the same directory as your Streamlit app script, or adjust the path.
        benchmark_html_path = os.path.join(os.path.dirname(__file__), "main_benchmark_app.html")
        
        html_content = load_html_file(benchmark_html_path)
        
        if "Error:" not in html_content:
            components.html(html_content, height=1200, scrolling=True)
        else:
            st.error(f"Could not load the benchmark application: {html_content}")
        
        st.sidebar.markdown("--- ")
        st.sidebar.info("The benchmark interface above is an interactive HTML/JS application embedded within Streamlit.")

    elif app_mode == "Quantum Computing Deep Dive":
        st.title("🌌 Quantum Computing Deep Dive")
        st.markdown("""
            Explore the fundamentals and advancements in quantum computing. 
            This section provides a comprehensive overview based on the Quantheo website.
            """)
        
        # IMPORTANT: This path needs to be correct for your Streamlit deployment environment.
        # Ensure 'quantum_computing.html' is in the same directory or provide the correct relative/absolute path.
        deep_dive_html_path = os.path.join(os.path.dirname(__file__), "quantum_computing.html")
        # If your quantum_computing.html is in a different location, adjust this path:
        # e.g., deep_dive_html_path = "C:\\Users\\nevel\\PycharmProjects\\Proof_of_concept\\quantheo_poc2\\quantheo-website\\quantum_computing.html"
        # However, for deployment, it's best to keep related files together.

        html_content = load_html_file(deep_dive_html_path)

        if "Error:" not in html_content:
            components.html(html_content, height=800, scrolling=True)
        else:
            st.error(f"Could not load the Quantum Computing Deep Dive page: {html_content}")
        
        st.sidebar.markdown("--- ")
        st.sidebar.info("The content above is loaded from an external HTML page detailing quantum computing concepts.")

# --- Entry Point ---
if __name__ == "__main__":
    # Create a dummy quantum_computing.html if it doesn't exist for local testing
    # In a real deployment, you'd ensure this file is present.
    dummy_qc_html_path = os.path.join(os.path.dirname(__file__), "quantum_computing.html")
    if not os.path.exists(dummy_qc_html_path):
        with open(dummy_qc_html_path, "w", encoding="utf-8") as f_dummy:
            f_dummy.write("""
            <!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>Quantum Computing Deep Dive - Placeholder</title>
                <style>
                    body { font-family: sans-serif; margin: 20px; line-height: 1.6; background-color: #f0f2f5; color: #333; }
                    .container { max-width: 800px; margin: auto; background-color: white; padding: 20px; border-radius: 8px; box-shadow: 0 0 10px rgba(0,0,0,0.1); }
                    h1 { color: #0056b3; }
                </style>
            </head>
            <body>
                <div class="container">
                    <h1>Quantum Computing Deep Dive - Placeholder</h1>
                    <p>This is a placeholder for the <code>quantum_computing.html</code> file.</p>
                    <p>Please replace this file with the actual content from <code>C:\Users\nevel\PycharmProjects\Proof_of_concept\quantheo_poc2\quantheo-website\quantum_computing.html</code> for the full experience.</p>
                    <p>This page will display detailed information about quantum computing concepts, technologies, and applications.</p>
                </div>
            </body>
            </html>
            """)
        print(f"Created a dummy '{dummy_qc_html_path}' for testing.")

    main()
