import cv2
import mediapipe as mp
import pyautogui
import math
import time
import numpy as np

class Config:
    CAMERA_INDEX = 0
    MIN_DETECTION_CONFIDENCE = 0.8
    MIN_TRACKING_CONFIDENCE = 0.8
    
    CLICK_THRESHOLD = 0.06  
    CLICK_COOLDOWN = 0.3    
    
    SCROLL_THRESHOLD = 0.07  
    SCROLL_DEAD_ZONE = 0.02  
    SCROLL_SENSITIVITY = 40  
    

    SMOOTHING_FACTOR = 0.3  
    CURSOR_SPEED = 1.5      


mp_hands = mp.solutions.hands
hands = mp_hands.Hands(
    min_detection_confidence=Config.MIN_DETECTION_CONFIDENCE,
    min_tracking_confidence=Config.MIN_TRACKING_CONFIDENCE,
    max_num_hands=2  # Supports two hands (one for cursor, one for scroll)
)
mp_drawing = mp.solutions.drawing_utils

cap = cv2.VideoCapture(Config.CAMERA_INDEX)

# ===== STATE VARIABLES ===== #
prev_x, prev_y = 0, 0
is_scrolling = False
scroll_start_y = 0
last_click_time = 0

# ===== FUNCTIONS ===== #
def get_distance(p1, p2):
    return math.sqrt((p1.x - p2.x)**2 + (p1.y - p2.y)**2)

def smooth_cursor(current_x, current_y, prev_x, prev_y):
    smooth_x = prev_x + (current_x - prev_x) * Config.SMOOTHING_FACTOR
    smooth_y = prev_y + (current_y - prev_y) * Config.SMOOTHING_FACTOR
    return smooth_x, smooth_y

# ===== MAIN LOOP ===== #
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        continue
    
    # Flip & convert frame
    frame = cv2.flip(frame, 1)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    
    # Process hand landmarks
    results = hands.process(rgb_frame)
    
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            
            landmarks = hand_landmarks.landmark
            index_tip = landmarks[8]
            middle_tip = landmarks[12]
            thumb_tip = landmarks[4]
            
            # === CURSOR CONTROL (INDEX FINGER) === #
            cursor_x = index_tip.x * pyautogui.size()[0] * Config.CURSOR_SPEED
            cursor_y = index_tip.y * pyautogui.size()[1] * Config.CURSOR_SPEED
            
            # Smooth cursor movement
            smooth_x, smooth_y = smooth_cursor(cursor_x, cursor_y, prev_x, prev_y)
            prev_x, prev_y = smooth_x, smooth_y
            
            # === SCROLL GESTURE (INDEX + MIDDLE FINGER) === #
            index_middle_dist = get_distance(index_tip, middle_tip)
            
            # Activate scroll if fingers are close
            if index_middle_dist < Config.SCROLL_THRESHOLD:
                if not is_scrolling:
                    is_scrolling = True
                    scroll_start_y = smooth_y
                    cv2.putText(frame, "SCROLL MODE", (50, 70), 
                               cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
                
                # Calculate scroll amount (with dead zone)
                scroll_delta = (scroll_start_y - smooth_y) * Config.SCROLL_SENSITIVITY
                
                if abs(scroll_delta) > Config.SCROLL_DEAD_ZONE * Config.SCROLL_SENSITIVITY:
                    pyautogui.scroll(int(scroll_delta))
                    scroll_start_y = smooth_y  # Reset scroll origin
            else:
                is_scrolling = False
                pyautogui.moveTo(int(smooth_x), int(smooth_y))
            
            # === CLICK GESTURE (INDEX + THUMB) === #
            index_thumb_dist = get_distance(index_tip, thumb_tip)
            current_time = time.time()
            
            if index_thumb_dist < Config.CLICK_THRESHOLD:
                if current_time - last_click_time > Config.CLICK_COOLDOWN:
                    pyautogui.click()
                    last_click_time = current_time
                    cv2.putText(frame, "CLICK", (50, 120), 
                               cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            
            # === VISUAL FEEDBACK === #
            # Distance indicators
            cv2.putText(frame, f"Index-Middle: {index_middle_dist:.3f}", (10, 30), 
                       cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
            cv2.putText(frame, f"Index-Thumb: {index_thumb_dist:.3f}", (10, 60), 
                       cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
            
            # Finger highlights
            cv2.circle(frame, (int(index_tip.x * frame.shape[1]), int(index_tip.y * frame.shape[0])), 
                      10, (0, 255, 0), -1)  # Green = Index
            cv2.circle(frame, (int(middle_tip.x * frame.shape[1]), int(middle_tip.y * frame.shape[0])), 
                      10, (0, 255, 255), -1)  # Yellow = Middle
            cv2.circle(frame, (int(thumb_tip.x * frame.shape[1]), int(thumb_tip.y * frame.shape[0])), 
                      10, (0, 0, 255), -1)  # Red = Thumb
    
    # Show mode status
    mode_text = "SCROLL MODE" if is_scrolling else "CURSOR MODE"
    mode_color = (255, 0, 0) if is_scrolling else (0, 255, 0)
    cv2.putText(frame, mode_text, (frame.shape[1] - 200, 30), 
               cv2.FONT_HERSHEY_SIMPLEX, 0.7, mode_color, 2)
    
    cv2.imshow('Advanced Virtual Mouse', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()