# FDE-Technical-Screen-Assignment  
**Author:** Hasini Patlolla  

## Package Sorter  

This project contains a Python solution for sorting packages at Thoughtful’s robotic automation factory.  

## Overview  

The function `sort_package(width, height, length, mass)` determines the dispatch stack based on:  

- **Bulky:**  
  - Volume (width × height × length) ≥ 1,000,000 cm³, **or**  
  - Any dimension (width, height, or length) ≥ 150 cm.  
- **Heavy:**  
  - Mass ≥ 20 kg.  

### **Dispatch Stacks:**  
- **STANDARD:** Package is neither bulky nor heavy.  
- **SPECIAL:** Package is either bulky or heavy (but not both).  
- **REJECTED:** Package is both bulky and heavy.  

The code includes at least one ternary operator and comprehensive test cases.  

## Running the Code  

1. Ensure you have Python 3 installed.  
2. Clone the repository:  
   ```bash
   git clone https://github.com/yourusername/package-sorter.git  
