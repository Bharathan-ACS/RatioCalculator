# 📱 Ratio Calculator Web App

A simple and responsive Ratio Calculator web application built using Django, HTML, CSS, and Bootstrap. This app allows users to input two numbers and get a simplified ratio along with step-by-step calculation using GCD.

---

## 🚀 Features

- 🔢 Calculate simplified ratio instantly
- 📊 Displays step-by-step solution
- 🧠 Uses GCD (Greatest Common Divisor) logic
- 📱 Mobile-style UI design
- 🎨 Clean and responsive interface using Bootstrap
- 🔐 CSRF protection with Django forms

---

## 🛠️ Tech Stack

- **Frontend:** HTML, CSS, Bootstrap  
- **Backend:** Python, Django  
- **Logic Used:** math.gcd() for ratio simplification  

---

## 📸 Output

- User enters two numbers  
- App calculates GCD  
- Displays:
  - Simplified ratio
  - Step-by-step calculation

---

## ⚙️ How It Works

1. User inputs two numbers
2. Backend calculates: gcd = math.gcd(num1, num2)
3. Each number is divided by GCD
4. Final simplified ratio is displayed

---

## ▶️ Installation & Setup

```bash
# Clone the repository
git clone https://github.com/your-username/ratio-calculator.git

# Navigate to project folder
cd ratio-calculator

# Create virtual environment
python -m venv venv

# Activate virtual environment
venv\Scripts\activate   # Windows
source venv/bin/activate  # Mac/Linux

# Install dependencies
pip install django

# Run server
python manage.py runserver
