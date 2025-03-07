# pyEmotionDetect2LED

Using DeepFace to detect emotions and control an LED for interaction.

## Pre-setup
Ensure that Python is installed (this project is based on Python 3.10).

## How to Run

### 1. Clone the Repository
```sh
git clone https://github.com/JingJayYu/pyEmotionDetect2LED.git
```
Or, if you don't have Git installed, you can download and extract the repository manually.

### 2. Create a Virtual Environment
```sh
python -m venv ./pyEnv
```

### 3. Activate the Virtual Environment
- On Windows:
  ```sh
  ./pyEnv/Scripts/activate.bat
  ```
- On macOS/Linux:
  ```sh
  source ./pyEnv/bin/activate
  ```

### 4. Install Required Packages
```sh
pip install -r requirements.txt
```

### 5. Setup Arduino
Ensure your **Arduino Uno** setup matches the `controllerLED.ino` configuration.
Modify `serial2ino.py` to match your Arduino's COM port.

### 6. Run the Main Script
```sh
python emotionDetect.py
