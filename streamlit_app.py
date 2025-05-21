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
    st.sidebar.header("🚀 Quantheo Leap") 
    st.sidebar.markdown("---")
    app_mode = st.sidebar.radio(
        "Explore Sections:",
        ("Quantheo Leap Benchmark", "Quantum Computing Deep Dive", "Business & Vision"), # Added "Business & Vision"
        key="nav_radio" 
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
        
        with st.expander("ℹ️ How to Use This Benchmark Tool & Understand the Technology"):
            st.markdown("""
                **1. Setup Your Benchmark:**
                *   **Select Optimization Problem:** Choose from diverse ICT challenges like Network Routing, Logistics, or Protein Folding. Each represents a class of problems where quantum-inspired approaches might offer an advantage.
                *   **Select Complexity:** Adjust the problem's difficulty (Low, Medium, High). Higher complexities often highlight the potential speedups of quantum-enhanced solvers for near-optimal solutions.

                **2. Run the Simulation:**
                *   Click the **"Run Benchmark"** button.
                *   Observe the "Solvers" panel:
                    *   **Classical Solver:** Simulates a traditional computational approach.
                    *   **Quantum-Enhanced Solver:** Simulates an approach leveraging quantum principles (like quantum annealing concepts) for optimization. The animation visually represents this distinct process.
                *   Status indicators will show if solvers are `running` or `complete`.

                **3. Analyze Results:**
                *   The **"Benchmark Results"** panel will populate once both solvers finish.
                *   **Simulated Time:** Compares the time taken to reach a near-optimal solution.
                *   **Solution Quality:** Indicates how close the found solution is to the best possible (optimal) solution. Quantum approaches often excel at finding very good solutions quickly, especially for complex problems.
                *   **Resource Units:** A conceptual measure of computational effort.
                *   **Comparison Summary & Advantage Badge:** Provides an at-a-glance interpretation of which approach performed better for the selected parameters.
                *   **Context Area (within the benchmark HTML):** Offers insights into the underlying quantum concepts (like quantum annealing) and why they can be advantageous for certain optimization tasks.

                **Understanding the "Quantum-Enhanced" Approach:**
                This demo conceptually models how techniques like quantum annealing can explore vast solution spaces more efficiently than classical methods for specific complex optimization problems. The goal is often not just the absolute *best* solution, but a *very good* (near-optimal) solution found significantly *faster*. This is crucial for real-world applications where timely decisions are paramount.
            """)
        
        benchmark_html_path = os.path.join(os.path.dirname(__file__), "main_benchmark_app.html")
        
        html_content = load_html_file(benchmark_html_path)
        
        if not html_content.startswith("<p>Error:"):
            components.html(html_content, height=1200, scrolling=True)
        else:
            error_message = html_content.replace("<p>Error: ", "").replace("</p>", "")
            st.error(f"Could not load the benchmark application: {error_message}")
        
        st.sidebar.markdown("---") 
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
            components.html(html_content, height=1500, scrolling=True) 
            st.info("""
                **Connecting to the Benchmark:** The concepts explored in this Deep Dive (qubits, superposition, entanglement, error correction, and potential applications) provide the foundational knowledge to understand *why* and *how* the "Quantum-Enhanced Solver" in our Benchmark Explorer might offer advantages for certain complex problems.
            """)
            st.markdown("---") # Separator
            st.subheader("The Quantum Revolution: Applications, Tools, and Technologies")
            st.markdown("""
A platform like Quantheo Leap, especially if it evolves to integrate real quantum processing capabilities 
alongside its simulation and benchmarking strengths, sits at the heart of a potential revolution in 
science and technology. Here's how, broken down by the tools and technologies involved:

### The Core Challenge: Intractable Problems
Many of the world's most pressing scientific and technological challenges are, at their core, incredibly 
complex optimization problems or simulations of quantum systems. Classical computers, even supercomputers, 
struggle with these because the number of possibilities or interactions grows exponentially with the size 
of the problem. Think of:
*   Drug Discovery: Finding the right molecule out of billions to target a specific disease.
*   Materials Science: Designing new materials with specific properties (e.g., better batteries, superconductors).
*   Logistics: Optimizing global supply chains with millions of variables.
*   Financial Modeling: Accurately predicting market behavior or optimizing vast portfolios.
*   Climate Modeling: Simulating complex climate interactions with high fidelity.

### How Quantum-Enhanced Platforms (like a future Quantheo Leap) Can Revolutionize:
The revolution comes from leveraging quantum mechanics to tackle these intractable problems in fundamentally new ways.

#### 1. Quantum Algorithms & Problem Solving:
*   **Tools/Technologies:** Quantum Annealing (as highlighted in the USC article), Quantum Approximate Optimization Algorithm (QAOA), Variational Quantum Eigensolver (VQE), Grover's algorithm (for search), Shor's algorithm (for factoring, though less relevant for optimization directly).
*   **Revolution:**
    *   **Optimization:** Quantum annealers (and algorithms like QAOA on gate-based computers) can find high-quality solutions to complex optimization problems much faster than classical methods. This isn't always about finding the absolute perfect solution but getting to a very good, near-optimal solution quickly, which is often what's needed in the real world (as Quantheo Leap demonstrates). This could revolutionize logistics, scheduling, and design processes.
    *   **Simulation:** Quantum computers are inherently good at simulating other quantum systems. This means accurately modeling molecular interactions for drug discovery (e.g., how a drug binds to a protein) or designing new materials at an atomic level. This is something classical computers can only approximate, often poorly, for complex systems.
    *   **Search:** For certain types of problems, quantum algorithms can search through vast datasets or possibility spaces quadratically faster than classical algorithms.

#### 2. Quantum Hardware (The Engine):
*   **Tools/Technologies:**
    *   Quantum Annealers (e.g., D-Wave Systems): These are specialized quantum computers built specifically for optimization problems. They use quantum tunneling to find low-energy states, which correspond to optimal solutions.
    *   Gate-Based Quantum Computers (e.g., IBM, Google, Rigetti, IonQ): These are more universal quantum computers that use quantum bits (qubits) and quantum gates to perform computations. They can run a wider variety of quantum algorithms.
    *   Error Correction & Suppression: A critical ongoing development. Real quantum systems are noisy. Advanced techniques (as mentioned in the USC research) are crucial to get reliable results and achieve true "quantum advantage."
*   **Revolution:** As quantum hardware becomes larger, more stable (less noisy), and more accessible, it will provide the raw computational power to:
    *   **Science:** Simulate molecules and materials with unprecedented accuracy, leading to new drugs, catalysts, and materials with tailored properties (e.g., for energy storage, carbon capture). Unravel mysteries in fundamental physics by simulating complex quantum phenomena.
    *   **Technology:** Drive breakthroughs in AI by enabling more powerful machine learning models, optimize complex systems in real-time (e.g., traffic flow, energy grids), and potentially break current encryption standards (though this also drives research into quantum-resistant cryptography).

#### 3. Hybrid Quantum-Classical Systems:
*   **Tools/Technologies:** Platforms like NVIDIA's CUDA-Q, Amazon Braket, Azure Quantum, Google Quantum AI. These platforms allow classical computers (often GPUs for pre- and post-processing) to work in tandem with Quantum Processing Units (QPUs).
*   **Revolution:** For the foreseeable future, most practical quantum applications will be hybrid. Classical computers will handle data preparation, control the quantum computation, and interpret the results. This approach: 
    *   Maximizes the strengths of both types of computing.
    *   Allows us to tackle parts of a problem that are classically hard with a QPU, while using classical resources for the rest.
    *   Makes quantum computing more accessible and easier to integrate into existing workflows.

#### 4. Simulation, Benchmarking, and Development Platforms (like Quantheo Leap):
*   **Tools/Technologies:** The Quantheo Leap application itself, quantum software development kits (SDKs) like Qiskit (IBM), Cirq (Google), PennyLane (Xanadu), OpenQASM.
*   **Revolution:** These platforms are essential for:
    *   Algorithm Development & Testing: Researchers can design, test, and refine quantum algorithms in a simulated environment before running them on expensive and limited real hardware.
    *   Identifying Quantum Advantage: Benchmarking tools are crucial to rigorously compare quantum approaches against the best classical methods for specific problems and determine where and when quantum computers truly offer an advantage (as Quantheo Leap aims to show).
    *   Education & Workforce Development: Making the concepts of quantum computing and its applications more accessible to students, researchers, and industry professionals.
    *   Democratization: Lowering the barrier to entry for exploring quantum solutions.

### Specific Examples of Revolution:
*   **Personalized Medicine:** Simulating how different drug candidates interact with an individual's specific genetic makeup to design highly effective, personalized treatments with fewer side effects. 
    *   *Tools:* Gate-based quantum computers, VQE, quantum chemistry software, hybrid systems.
*   **Hyper-Efficient Logistics:** Optimizing global shipping routes, delivery schedules, and warehouse operations to a degree currently impossible, saving billions and reducing emissions. 
    *   *Tools:* Quantum annealers, QAOA, hybrid systems.
*   **Discovery of Novel Materials:** Designing materials from first principles for things like room-temperature superconductors, more efficient solar cells, or biodegradable plastics. 
    *   *Tools:* Gate-based quantum computers, quantum simulators, materials science simulation packages.
*   **Breakthroughs in AI:** Creating AI models that can learn from much less data, understand context more deeply, or solve more complex reasoning tasks. 
    *   *Tools:* Quantum machine learning algorithms, gate-based computers.
*   **Financial Systems:** Developing financial models that more accurately predict risk, optimize trading strategies in real-time, or detect complex fraud patterns. 
    *   *Tools:* Quantum annealers, quantum Monte Carlo methods.

In essence, platforms like Quantheo Leap (and the broader quantum ecosystem) are paving the way for a paradigm shift. 
They provide the tools to explore, understand, and eventually harness the power of quantum mechanics to solve problems 
that have long been beyond our reach, leading to accelerated innovation across virtually every field of science and technology.
            """, unsafe_allow_html=True)
        else:
            error_message = html_content.replace("<p>Error: ", "").replace("</p>", "")
            st.error(f"Could not load the Quantum Computing Deep Dive page: {error_message}")
        
        st.sidebar.markdown("---") 
        st.sidebar.info("""
            **About this Section:**
            This content is loaded from `quantum_computing.html`.
            It offers a detailed look into quantum principles and applications.
            """)

    elif app_mode == "Business & Vision": # New section
        st.markdown("""
            <div style="text-align: center; margin-bottom: 20px;">
                <h1 style="color: #0D9488; font-size: 2.5em;">📈 Business & Vision: Monetizing Quantheo Leap</h1>
            </div>
            <p style="font-size: 1.1em;">
                The Quantheo Leap platform, currently a powerful demonstrator, holds significant potential for commercialization. 
                Here are key strategies to transform it into a profitable venture, leveraging its unique capabilities in 
                benchmarking and showcasing quantum-inspired solutions.
            </p>
            """, unsafe_allow_html=True)

        st.subheader("Pathways to a Profitable Business")

        st.markdown("""
            #### 1. Educational & Training Platform (Subscription-Based)
            *   **Target:** Universities, research institutions, corporate R&D, individuals.
            *   **Offering:** Subscription access to an expanded Quantheo Leap with more problems, user-defined problem uploads, interactive tutorials on quantum principles (annealing, approximate optimization), and simulated quantum environments.
            *   **Revenue:** Tiered subscriptions (student, researcher, enterprise).

            #### 2. Benchmarking & Assessment Services (Consultancy/Service-Based)
            *   **Target:** Businesses in logistics, finance, pharma, materials science facing optimization challenges.
            *   **Offering:** Utilize Quantheo Leap (or an advanced internal version) for:
                *   Assessing problem suitability for quantum/quantum-inspired solutions.
                *   "Quantum-readiness" assessments.
                *   Comparing classical solutions against simulated quantum approaches based on KPIs (speed, solution quality, resource savings).
            *   **Revenue:** Project-based fees, retainers, "Benchmarking-as-a-Service".

            #### 3. Quantum Solution Prototyping & PoC Development (Service-Based)
            *   **Target:** Companies ready for pilot quantum projects.
            *   **Offering:** Develop Proof-of-Concept (PoC) quantum or hybrid algorithms for client-specific problems, using the platform for rapid prototyping and performance simulation before real hardware use.
            *   **Revenue:** Fees for PoC development, leading to larger implementation projects.

            #### 4. SaaS Platform for Optimization Problem Solvers (Subscription/Usage-Based)
            *   **Target:** Data scientists, operations researchers, domain experts.
            *   **Offering:** A full SaaS platform to upload problems, select solvers (classical & quantum-enhanced), run benchmarks, get reports, and integrate via APIs.
            *   **Revenue:** Tiered subscriptions based on usage, pay-as-you-go, premium access to advanced quantum backends.

            #### 5. Specialized Industry Solutions (Vertical SaaS)
            *   **Target:** Niche markets within specific industries.
            *   **Offering:** Tailored versions like "Quantheo Leap for Drug Discovery" or "Quantheo Leap for Financial Portfolio Optimization" with industry-specific templates, metrics, and case studies.
            *   **Revenue:** Higher-value subscriptions or licensing fees.
        """)

        st.subheader("Key Success Factors for Commercialization")
        st.markdown("""
            *   **Access to Real Quantum Resources:** Integration with actual quantum hardware or sophisticated simulators.
            *   **Exceptional User Experience (UX):** Intuitive interface abstracting quantum complexity.
            *   **Scalability:** Handling complex problems and more users.
            *   **Clear Value Proposition:** Demonstrating tangible business benefits (cost/time savings, improved quality).
            *   **Strong Team:** Expertise in quantum computing, optimization, software, UX, and business.
            *   **Strategic Partnerships:** Collaborations with hardware providers, cloud platforms, and industry vendors.
            *   **Continuous R&D:** Staying updated with the latest algorithms and hardware.

            This platform serves as a foundational step, illustrating the core concepts that can be expanded into these robust business models.
        """)
        st.sidebar.markdown("---")
        st.sidebar.info("""
            **About this Section:**
            Explore potential business models and strategic considerations for developing Quantheo Leap into a commercial success.
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
