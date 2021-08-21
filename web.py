from Hand_Detection import hand_data
import cv2
import streamlit as st
import time
camera = st.selectbox("Camera ",("Default","IP Cam"))
if camera=="Default":
    cap=cv2.VideoCapture(0)
if camera=="IP Cam":
    address = st.text_input('Enter your ip') 
    cap=cv2.VideoCapture(str(address))
    which_cam = st.selectbox("Select Which camere you are using",("Front","Back"))
selfie = st.selectbox("Selfi Mirror ",("ON","OFF"))
if st.button("Start"):
    image_placeholder = st.empty()
    while True:
        
        success,img=cap.read()
        if camera=="IP Cam":
            if which_cam=="Front":
                img = cv2.rotate(img, cv2.cv2.ROTATE_90_CLOCKWISE)
                img = cv2.rotate(img, cv2.cv2.ROTATE_90_CLOCKWISE)
                img = cv2.rotate(img, cv2.cv2.ROTATE_90_CLOCKWISE)
            if which_cam=="Back":
                img = cv2.rotate(img, cv2.cv2.ROTATE_90_CLOCKWISE)
        if selfie=="ON":
            img=cv2.flip(img,1)
        img,lmList_all,bbox=hand_data(img,bdraw=True)
        image_placeholder.image(img, channels="BGR")
        time.sleep(0.01)

        