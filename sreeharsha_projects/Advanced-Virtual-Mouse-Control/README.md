# Advanced-Virtual-Mouse-Control

# 🖱️ Advanced Virtual Mouse - Hand Gesture Controlled Mouse

Transform your hand into a powerful virtual mouse! This project enables **gesture-based cursor movement, scrolling, and clicking** using a webcam and AI-driven hand tracking. Say goodbye to physical mice and hello to futuristic interaction! 🚀

---

## ✨ Features
✅ **Hand Gesture Control:** Move the cursor using your index finger.  
✅ **Clicking Mechanism:** Tap your index finger and thumb together to click.  
✅ **Smooth Cursor Movement:** AI-powered smoothing for natural mouse control.  
✅ **Scrolling Gestures:** Move your index and middle fingers close to enable smooth scrolling.  
✅ **Adaptive Sensitivity:** Fine-tuned settings for precise control.  
✅ **Real-Time Visual Feedback:** Displays distance metrics & gesture status on the screen.  

---

## 🎯 How It Works
📸 **Webcam Capture:** Reads hand gestures in real-time.  
🤖 **AI Hand Tracking:** Uses MediaPipe for landmark detection.  
🖥️ **Virtual Cursor Control:** Maps hand movements to screen coordinates.  
💡 **Gesture-Based Actions:** Scroll, click, and move using simple finger gestures.  

---

## 🚀 Installation & Setup

### Prerequisites
Make sure you have Python installed along with the necessary libraries:

```sh
pip install opencv-python mediapipe pyautogui numpy
```

### Running the Project
1️⃣ **Clone the repository**
```sh
git clone https://github.com/sreeharshamengji/Advanced-Virtual-Mouse.git
cd Advanced-Virtual-Mouse
```
2️⃣ **Run the script**
```sh
python virtual_mouse.py
```
3️⃣ **Control Your Computer with Hand Gestures!** ✋🤖

---

## 📸 Screenshots
📌 **Hand tracking in action:**  
![Screenshot 2025-04-03 195736](https://github.com/user-attachments/assets/2b24273a-4354-4bf2-9575-3686fb6031f5)

📌 **Clicking gesture detection:**  

![Screenshot 2025-04-03 195753](https://github.com/user-attachments/assets/3f0b8b52-5646-44fb-9ab2-2bc4d1c716cc)

📌 **Scrolling mode enabled:**  
![image](https://github.com/user-attachments/assets/048222f7-7ed4-4a5a-84ce-a893194b8d73)

*(Add screenshots above for visual appeal!)*

---

## ⚙️ Configuration
Customize gesture sensitivity and behavior in the `Config` class:

```python
class Config:
    CLICK_THRESHOLD = 0.06  # Adjust click sensitivity
    SCROLL_SENSITIVITY = 40  # Control scroll speed
    SMOOTHING_FACTOR = 0.3   # Tune cursor smoothness
```

Modify these values to match your hand movements! 🔥

---

## 🛠️ Technologies Used
- **OpenCV** - For real-time webcam processing
- **MediaPipe** - AI-powered hand tracking
- **PyAutoGUI** - Simulating mouse interactions
- **NumPy** - Performance optimizations

---

## 💡 Future Enhancements
🚀 **Multi-Hand Support:** Enable separate actions for both hands.  
🎮 **Gesture-Based Shortcuts:** Open apps, control media, and more!  
📌 **Customizable Gestures:** Train your own hand signs.  

---

## 🤝 Contributing
Want to improve this project? Fork the repo, make your changes, and create a pull request! 🙌

```sh
git clone https://github.com/sreeharshamengji/Advanced-Virtual-Mouse.git
```

---

## 📞 Contact
For any queries, feel free to reach out:  
📧 **Email:** sree.mengji@gmail.com  
🔗 **GitHub:** [Your Profile](https://github.com/sreeharshamengji)  

---

Give a ⭐ if you like this project! 🔥

