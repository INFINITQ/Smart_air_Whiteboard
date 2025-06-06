🧠 Smart Air Whiteboard with Hand Gestures
A real-time gesture-controlled virtual whiteboard built using Python, OpenCV, and CVZone. This tool turns your webcam into an intelligent drawing surface where you can draw, clear, save, and even lock your PC — all with simple finger gestures.


✨ Features
Gesture	Description
☝️ 1 Finger	Draw with red ink
✌️ 2 Fingers	Clear the entire canvas
🤟 3 Fingers	Save the current drawing as an image
✋ 5 Fingers (toggle)	Toggle Whiteboard Mode (clean white screen)
🖖 4 Fingers	Instantly Lock your Windows screen
⏎ Enter Key	Exit the application

🖥️ Whiteboard Mode
When you toggle into whiteboard mode, your camera feed is replaced with a plain white background. Your hand becomes a marker — nothing else (including your face) is visible. Toggling again returns to the normal camera background.

🛠️ Setup Instructions
🔗 Prerequisites
Python 3.7+

Webcam (internal or external)

Windows 11 (for lock screen feature)

📦 Installation
Clone this repository

git clone https://github.com/your-username/smart-air-whiteboard.git
cd smart-air-whiteboard

(Optional) Create a virtual environment

python -m venv venv
venv\Scripts\activate

Install dependencies

pip install -r requirements.txt

If requirements.txt is not available:

pip install opencv-python cvzone numpy

🚀 Run the App
python smart_whiteboard.py

📂 Saved Files
All saved drawings using the 3-finger gesture are stored in the current directory as:

drawing_YYYYMMDD_HHMMSS.jpg

👨‍💻 Technologies Used
Python 3

OpenCV

CVZone (Hand Tracking Module)

Numpy

Windows API (for lock screen)

💡 Potential Add-ons
Future features can include:

Eraser gesture with second hand

Brush size control using pinch gesture

Real-time collaborative whiteboarding

Voice command integration

Presentation control via hand swipes

🔒 Security Note
The 4-finger gesture instantly locks your Windows PC via:

os.system("rundll32.exe user32.dll,LockWorkStation")

This feature is only compatible with Windows and will not function on other operating systems.

📃 License
This project is open source under the MIT License.

✍️ Author
Abhishek Pareek

