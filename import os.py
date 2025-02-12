import os
import signal
try:
    import psutil
except ImportError:
    print("psutil module is not installed. Please install it using 'pip install psutil'")
    exit(1)

def close_python_windows():
    for proc in psutil.process_iter(['pid', 'name']):
        if proc.info['name'] == 'python.exe' or proc.info['name'] == 'pythonw.exe':
            os.kill(proc.info['pid'], signal.SIGTERM)

if __name__ == "__main__":
    close_python_windows()
