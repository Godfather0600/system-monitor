🖥️ Simple System Monitor (Python)

A lightweight, real-time system monitor that displays CPU usage, memory usage, and total running processes.
Built using Python and the psutil library, this script behaves like a minimal console version of Task Manager and updates every second.

🚀 Features

📊 Real-time CPU usage (%)

🧠 Real-time Memory usage (%)

📄 Number of running processes

🔄 Refreshes automatically every second

💻 Works on Windows, Linux, and macOS

🧩 Uses psutil for accurate system information

📦 Requirements

Make sure you have:

Python 3.7+

psutil library

Install psutil with:

pip install psutil

📁 How to Run

Clone the repository:

git clone https://github.com/yourusername/system-monitor.git


Navigate into the project folder:

cd system-monitor


Run the script:

python monitor.py

📜 Code Overview

The script performs a continuous loop where it:

Measures CPU usage over 1 second

Reads memory statistics

Counts running processes

Clears the console

Prints updated system stats

This creates a simple, real-time dashboard in the terminal.

🛠️ Example Output
CPU Usage   : 27.35 %
Memory Usage: 56.92 %
Processes   : 152

💡 Future Enhancements (Optional Ideas)

If you want to improve the project, here are some ideas:

Per-core CPU usage

Colored output (e.g., red when CPU is high)

Disk usage and network speed

Logging to a file

GUI version (Tkinter / PyQt)

A curses-based UI (like htop)

📄 License

This project is licensed under the MIT License.
Feel free to modify and use it however you like.
