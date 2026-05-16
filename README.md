# compiler-project
# Compiler Warning Analysis and Clustering System

## Project Overview
This project is an intelligent compiler analysis system that automatically generates C programs, compiles them using the GCC compiler, extracts compiler warnings, and applies Machine Learning techniques to analyze and cluster similar warning patterns. The system helps in understanding common programming mistakes, unused variables, type conversion issues, and compiler behavior through automated analysis and visualization.

---

## System Architecture

The system consists of multiple stages working together in a pipeline:

1. **Program Generator (Python Script)**
   - Automatically generates multiple C programs with different coding patterns and errors.

2. **Generated C Programs**
   - Stores the generated source code files which are used for testing and analysis.

3. **GCC Compiler Compilation Process**
   - Compiles all generated C programs using the GCC compiler.
   - Captures compiler outputs, warnings, and errors.

4. **Warning Extraction and Parsing**
   - Parses compiler logs and extracts warning information such as:
     - Unused variables
     - Type conversion warnings
     - Syntax-related issues
     - Semantic warnings

5. **Feature Dataset Creation**
   - Converts extracted warning information into a structured dataset.
   - Features are prepared for machine learning analysis.

6. **K-Means Clustering (Machine Learning)**
   - Uses the K-Means clustering algorithm to group similar compiler warnings.
   - Helps identify common categories of programming issues.

7. **Results and Visualization**
   - Generates reports, graphs, and Excel sheets.
   - Visualizes warning clusters and analysis results.

---

## Technologies Used

- Python
- GCC Compiler
- Machine Learning
- K-Means Clustering
- Pandas
- Matplotlib
- Excel Report Generation

---

## Features

- Automatic C program generation
- Compiler warning extraction
- Log parsing and analysis
- Dataset creation for ML
- K-Means clustering implementation
- Graph and report visualization
- Excel-based result reports

---

## Applications

- Compiler behavior analysis
- Programming error pattern detection
- Educational compiler learning systems
- Automated code quality analysis
- Research on compiler warnings

---

## Future Enhancements

- Support for multiple compilers
- Deep learning-based warning prediction
- Web dashboard visualization
- Real-time compiler analysis
- Advanced static code analysis

---

## Conclusion

This project demonstrates the integration of compiler technology with machine learning techniques to analyze programming errors efficiently. By automating warning extraction and clustering, the system provides useful insights into coding patterns and compiler diagnostics, making it valuable for both educational and research purposes.
