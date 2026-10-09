# 🏠 Smart Home Automation System

## 📌 Overview

The **Smart Home Automation System** is a Python-based, menu-driven application designed to simulate the automation and management of common household activities. It integrates multiple home management features into a single program, providing a simple and interactive way to control lighting, manage temperature settings, view weekly meal plans, operate household appliances, and simulate security monitoring.

The project demonstrates the practical application of core Python programming concepts, including functions, dictionaries, loops, conditional statements, input validation, file handling, and time-based operations.

## ✨ Features

* **Human Detection & Smart Lighting:** Simulates human detection, automatically unlocks the door, turns on the lights, and adjusts light intensity according to the time of day.
* **Temperature Control:** Provides options to simulate cold, normal, and hot temperature settings.
* **Weekly Kitchen Menu:** Stores and displays breakfast, lunch, and dinner plans for all seven days of the week, including today's menu.
* **Home Appliances Management:** Simulates the operation of a washing machine, dryer, television, dishwasher, and oven.
* **Security System:** Simulates motion detection, alarm activation, and door unlocking.
* **Activity Logging:** Records important system events with timestamps in a text file (`system_log.txt`).
* **Interactive Menu System:** Uses nested menus to organize features and allow users to navigate between different modules.
* **Input Validation:** Checks that menu inputs are numeric and handles invalid menu selections.

## 🛠️ Technologies Used

* **Programming Language:** Python
* **Modules:** `time`
* **Data Structures:** Dictionaries and variables
* **File Handling:** Text file operations
* **Programming Concepts:** Functions, loops, conditional statements, global variables, and input validation

## ⚙️ How It Works

1. Launch the program to access the main menu.
2. Select the human detection option to activate the simulated home automation features.
3. Choose a feature from the home control menu.
4. Interact with the available options to manage temperature settings, view meal plans, operate appliances, or access security features.
5. System events are recorded in `system_log.txt` for activity tracking.
6. Return to the main menu or turn off the system to exit.

## 🚀 Getting Started

### Prerequisites

* Python 3.x installed on your computer.

### Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY.git
   ```

2. Navigate to the project directory:

   ```bash
   cd YOUR-REPOSITORY
   ```

3. Run the Python program:

   ```bash
   python main.py
   ```

   Replace `main.py` with the actual name of your Python file if it is different.

## 📂 Project Structure

```text
Smart-Home-Automation/
├── main.py
├── system_log.txt    # Created automatically when events are logged
└── README.md
```

## 🔮 Future Improvements

* Integrate real motion sensors for human detection.
* Connect smart lights and electronic door locks.
* Implement actual temperature monitoring and control.
* Add user authentication for improved security.
* Develop a graphical user interface (GUI).
* Integrate IoT devices for real-time home automation.

## ⚠️ Project Limitations

This project is currently a simulation of a smart home environment. It does not directly communicate with physical sensors, appliances, smart locks, or temperature-control devices. Its purpose is to demonstrate the logic and structure of a home automation system using Python.

## 🎯 Learning Outcomes

Through this project, I practiced modular programming, menu-driven application development, dictionary-based data management, input validation, time-based logic, and file handling. It also helped me understand how different functions can work together to simulate a real-world automation system.

## 👨‍💻 Author

**Your Name**

Developed as a Python programming project to explore the fundamentals of smart home automation.

---

⭐ If you find this project useful, consider giving the repository a star!
