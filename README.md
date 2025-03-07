# pyEmotionDetect2LED

Using DeepFace to detect emotions and control an LED for interaction.

## 切換語言 | Language Switch
- [English](#english)
- [繁體中文](#繁體中文)

---

## English

### Pre-setup
Ensure that Python is installed (this project is based on Python 3.10).

### How to Run

#### 1. Clone the Repository
```sh
git clone https://github.com/JingJayYu/pyEmotionDetect2LED.git
```
Or, if you don't have Git installed, you can download and extract the repository manually.

#### 2. Create a Virtual Environment
```sh
python -m venv ./pyEnv
```

#### 3. Activate the Virtual Environment
- On Windows:
  ```sh
  ./pyEnv/Scripts/activate.bat
  ```
- On macOS/Linux:
  ```sh
  source ./pyEnv/bin/activate
  ```

#### 4. Install Required Packages
```sh
pip install -r requirements.txt
```

#### 5. Setup Arduino
Ensure your **Arduino Uno** setup matches the `controllerLED.ino` configuration.
Modify `serial2ino.py` to match your Arduino's COM port.

#### 6. Run the Main Script
```sh
python emotionDetect.py
```

---

## 繁體中文

### 預先準備
確保已安裝 Python（本專案基於 Python 3.10）。

### 執行步驟

#### 1. 複製程式碼
```sh
git clone https://github.com/JingJayYu/pyEmotionDetect2LED.git
```
或者，如果你沒有安裝 Git，可以手動下載並解壓縮。

#### 2. 建立虛擬環境
```sh
python -m venv ./pyEnv
```

#### 3. 啟動虛擬環境
- Windows:
  ```sh
  ./pyEnv/Scripts/activate.bat
  ```
- macOS/Linux:
  ```sh
  source ./pyEnv/bin/activate
  ```

#### 4. 安裝所需套件
```sh
pip install -r requirements.txt
```

#### 5. 設置 Arduino
確保 **Arduino Uno** 的設定與 `controllerLED.ino` 相符。
修改 `serial2ino.py` 以匹配你的 Arduino COM 端口。

#### 6. 執行主程式
```sh
python emotionDetect.py
```
