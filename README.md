# Python Static Analyzer for ELF Binaries

This project is a simple yet effective static analysis tool written in Python. It automates the initial reconnaissance phase of reverse engineering for ELF (Executable and Linkable Format) binaries on Linux. The script runs a series of standard command-line tools, parses their output, and aggregates the findings into a structured JSON report.

This tool was developed as a hands-on project to combine skills in Linux system utilities, Python scripting, and the fundamentals of malware analysis.

## Features

-   **Modular, Object-Oriented Design:** The analysis logic is encapsulated within an `AnalyzerFunctions` class, making the code clean and easily extensible.
-   **Comprehensive Analysis:** Gathers information from multiple sources:
    -   **File Type Identification:** Uses the `file` command to determine the binary's nature (e.g., ELF 64-bit, dynamically linked).
    -   **String Extraction:** Uses the `strings` command to extract embedded text, providing clues about functionality.
    -   **Library Call Tracing:** Uses `ltrace` to identify high-level library functions called by the program.
    -   **System Call Tracing:** Uses `strace` to uncover low-level interactions with the OS kernel.
-   **Automated Reporting:** All collected data is compiled into a single, well-formatted **JSON report**, perfect for logging and further analysis.
-   **Efficient Parsing:** Leverages **Regular Expressions (`re`)** to parse complex output from tools like `strace` and extract only the relevant information (e.g., system call names).

## Core Concepts Demonstrated

-   **Python Scripting for Automation:** Using Python to orchestrate Linux command-line tools.
-   **`subprocess` Module:** Interacting with the operating system and capturing command output.
-   **Object-Oriented Programming (OOP):** Structuring the tool with classes and methods.
-   **Data Handling:** Parsing text output and structuring it for JSON serialization.
-   **Regular Expressions:** Advanced text processing for precise data extraction.
-   **Fundamentals of Static Analysis:** Applying a standard methodology for initial binary reconnaissance.

## How to Use

The script is designed to be run from the command line.

```bash
# Clone the repository
git clone https://github.com/ArtemArmash/Python-Static-Analyzer.git
cd Python-Static-Analyzer

# Run the analysis on a binary (e.g., /bin/ls)
python3 static_analyzer.py /bin/ls

# Check the results
cat report.json
```
```
