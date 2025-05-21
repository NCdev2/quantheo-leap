import streamlit as st
import streamlit.components.v1 as components
import os
import datetime # Added for dynamic year

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
    st.sidebar.header("🚀 Quantheo Leap") # Changed from st.sidebar.title
    st.sidebar.markdown("---")
    app_mode = st.sidebar.radio(
        "Explore Sections:", # Changed label
        ("Quantheo Leap Benchmark", "Quantum Computing Deep Dive"),
        key="nav_radio" # Added a key
    )

    if app_mode == "Quantheo Leap Benchmark":
        st.markdown("""
            <div style="text-align: center; margin-bottom: 20px;">
                <h1 style="color: #0D9488; font-size: 2.5em;">⚛️ Quantheo Leap - ICT Benchmark Explorer</h1>
            </div>
            <p style="font-size: 1.1em;">
                Step into the future of computation! Select an ICT problem, adjust the complexity, 
                and witness a real-time performance comparison between classical and quantum-enhanced solvers.
            </p>
            <p style="font-size: 1.0em; color: #555;">
                <em>This interactive tool demonstrates the potential of quantum algorithms in tackling complex challenges.</em>
            </p>
            """, unsafe_allow_html=True)
        
        benchmark_html_path = os.path.join(os.path.dirname(__file__), "main_benchmark_app.html")
        
        html_content = load_html_file(benchmark_html_path)
        
        if not html_content.startswith("<p>Error:"):
            components.html(html_content, height=1200, scrolling=True)
        else:
            error_message = html_content.replace("<p>Error: ", "").replace("</p>", "")
            st.error(f"Could not load the benchmark application: {error_message}")
        
        st.sidebar.markdown("---") # Standardized separator
        st.sidebar.info("""
            **About this Section:**
            The benchmark explorer is an interactive HTML/JS application. 
            It's embedded here to showcase solver comparisons.
            """)

    elif app_mode == "Quantum Computing Deep Dive":
        st.markdown("""
            <div style="text-align: center; margin-bottom: 20px;">
                <h1 style="color: #0D9488; font-size: 2.5em;">🌌 Quantum Computing Deep Dive</h1>
            </div>
            <p style="font-size: 1.1em;">
                Embark on a journey through the fascinating world of quantum computing. 
                Discover the core principles, cutting-edge advancements, and the transformative potential of this revolutionary technology.
            </p>
            <p style="font-size: 1.0em; color: #555;">
                <em>Content sourced and adapted for an immersive learning experience.</em>
            </p>
            """, unsafe_allow_html=True)
        
        deep_dive_html_path = os.path.join(os.path.dirname(__file__), "quantum_computing.html")

        html_content = load_html_file(deep_dive_html_path)

        if not html_content.startswith("<p>Error:"):
            components.html(html_content, height=1500, scrolling=True) # Increased height
        else:
            error_message = html_content.replace("<p>Error: ", "").replace("</p>", "")
            st.error(f"Could not load the Quantum Computing Deep Dive page: {error_message}")
        
        st.sidebar.markdown("---") # Standardized separator
        st.sidebar.info("""
            **About this Section:**
            This content is loaded from `quantum_computing.html`.
            It offers a detailed look into quantum principles and applications.
            """)

    # Common sidebar footer elements
    st.sidebar.markdown("---")
    st.sidebar.success("UI Enhancements Applied!") 
    st.sidebar.caption(f"Quantheo Leap Platform | © {datetime.date.today().year} Quantheo")
    st.sidebar.caption("Version 1.1.0")

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
                    <p>Please replace this file with the actual content from <code>C:\\\\Users\\\\nevel\\\\PycharmProjects\\\\Proof_of_concept\\\\quantheo_poc2\\\\quantheo-website\\\\quantum_computing.html</code> for the full experience.</p>
                    <p>This page will display detailed information about quantum computing concepts, technologies, and applications.</p>
                </div>
            </body>
            </html>
            """)
        print(f"Created a dummy '{dummy_qc_html_path}' for testing.")

    main()
