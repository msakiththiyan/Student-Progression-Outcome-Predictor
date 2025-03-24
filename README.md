# Student Progression Outcome Predictor

This Python program helps determine students' academic progression based on their credit scores. It categorizes students into **Progress**, **Module Trailer**, **Module Retriever**, or **Exclude** based on their **PASS, DEFER, and FAIL credits**. Additionally, the program generates a **histogram visualization** using the `graphics.py` library.

---

## Features
1. Input validation for credits (ensuring only valid integer values from `{0, 20, 40, 60, 80, 100, 120}` are accepted).  
2. Categorizes students based on their total **PASS, DEFER, and FAIL credits**.  
3. Stores student outcomes in separate lists (`progress`, `module_trailer`, `module_retriever`, `exclude`).  
4. Generates a **graphical histogram** of the outcomes using the `graphics.py` module.  
5. Saves results into a text file (`part3.txt`) for future reference.  

---

## Installation & Setup

### 🔹 Prerequisites
Make sure you have **Python 3** installed on your system. If you haven't installed it yet, download it from [Python's official website](https://www.python.org/downloads/).

### 🔹 Install Required Modules
This program requires `graphics.py`, which is not a built-in module. You can install it using:
```bash
pip install PythonGraphics
```
Alternatively, download `graphics.py` manually from [Zelle's Graphics Library](https://mcsp.wartburg.edu/zelle/python/graphics.py) and place it in the same folder as the script.

---

## How to Run the Program

 Clone this repository:  
   ```bash
   git clone https://github.com/yourusername/your-repository.git
   cd your-repository
   ```

 Run the Python script:  
   ```bash
   python w2053488.py
   ```

 Follow the on-screen prompts to enter **PASS, DEFER, and FAIL credits**.  
 View the results in **console output, histogram visualization, and `part3.txt`** file.  

---

## Example Output
```
Enter Your total PASS Credits: 100
Enter Your total DEFER Credits: 20
Enter Your total FAIL Credits: 0
Progress (Module Trailer)

Would you like to enter another set of data?
Enter 'y' for yes or 'q' to quit and view results: q
```
✔ If you enter `q`, a histogram window will pop up showing the total outcomes for **Progress, Module Trailer, Module Retriever, and Exclude**.

---

## License
This project is for educational purposes.

 **Date:** 13/12/2023  
 **Author:** *Magenthirarajah Sakiththiyan*  

