import subprocess
import sys

def build_react_app():
    try:
        # Build the React app
        subprocess.check_call(['npm', 'run', 'build'], cwd='./new-client',shell=True)
        print("React app built successfully.")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while building the React app: {e}")
        sys.exit(1)

def run_python_script():
    try:
        # Run the other Python script
        subprocess.check_call([sys.executable, 'main.py'])
        print("Python script executed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while running the Python script: {e}")
        sys.exit(1)


build_react_app()
run_python_script()
