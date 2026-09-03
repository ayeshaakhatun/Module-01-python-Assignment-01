* Subtotal 5000 or more ➔ **20% Discount**
  * Subtotal 3000 to 4999 ➔ **10% Discount**
  * Subtotal 1000 to 2999 ➔ **5% Discount**
  * Subtotal under 1000 ➔ **No Discount**

  # Python Programming Assignment

A collection of foundational Python programs focusing on user inputs, data processing, conditional formatting logic (`if-elif-else`), arithmetic computations, and formatted string output (`f-strings`).

---

## 🚀 Projects Included

### 1. Student Grade Calculator (`grade_calculator.py`)
This program tracks a student's marks across three subjects, computes performance metrics, and assigns a letter grade based on specific thresholds.

*   **Inputs:** Student Name, Marks for 3 subjects.
*   **Calculations:** Total Marks, Average Marks.
*   **Grading Logic:**
    *   `80 - 100` $\rightarrow$ **A+**
    *   `70 - 79` $\rightarrow$ **A**
    *   `60 - 69` $\rightarrow$ **B**
    *   `50 - 59` $\rightarrow$ **C**
    *   `Below 50` $\rightarrow$ **F**
*   **Output:** Formatted performance summary using Python `f-strings`.

### 2. Simple Shopping Cart (`shopping_cart.py`)
A simulated retail script that accepts products and prices, aggregates costs, determines eligibility for promotional tier discounts, and generates a detailed checkout invoice.

*   **Inputs:** Customer Name, Names and prices of 3 distinct products.
*   **Calculations:** Subtotal, Dynamic Discount, Final Total.
*   **Discount Logic:**
  * Subtotal 5000 or more ➔ **20% Discount**
  * Subtotal 3000 to 4999 ➔ **10% Discount**
  * Subtotal 1000 to 2999 ➔ **5% Discount**
  * Subtotal under 1000 ➔ **No Discount**

*   **Output:** Comprehensive transactional receipt styled cleanly via `f-strings`.

---

## 🛠️ Technologies Used

*   **Programming Language:** Python 3.x
*   **Version Control System:** Git
*   **Hosting Platform:** GitHub
*   **Development Environment:** Visual Studio Code (VS Code)

---

## 📦 Getting Started

## ## 📋 Prerequisites (Before Things to Have)

Make sure you have the following software installed on your machine before running the project:

1. **Python 3.x** - Download and install it from [python.org](https://python.org). Verify by running this command in your terminal:
   ```bash
   python --version
   ```
2. **Git** - Download and install it from [git-scm.com](https://git-scm.com). Verify by running:
   ```bash
   git --version
   ```
3. **Visual Studio Code** - An integrated editor to view and execute the project files seamlessly.

---

## 🛠️ Installation & Execution

Follow these simple steps to download and run this project on your machine:

1. **Clone this repository** to your local computer using your terminal:
   ```bash
   git clone https://github.com
   ```
 2. **Open the project folder** inside **VS Code**:
   * Open VS Code, go to `File > Open Folder...`, and select the cloned repository folder.

3. **Run the programs** using the built-in VS Code terminal (`Ctrl + \``):
   * To run the Grade Calculator:
     ```bash
     python grade_calculator.py
     ```
   * To run the Shopping Cart:
     ```bash
     python shopping_cart.py
     ```
----

## 🛠️ File Structure Alignment
This repository is configured to filter out system meta-files and temporary build elements via a robust local `.gitignore`.
```text
├── .gitignore
├── README.md
├── grade_calculator.py
└── shopping_cart.py
```
