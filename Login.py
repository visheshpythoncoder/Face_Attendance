# import tkinter as tk
# from tkinter import messagebox
# from PIL import Image, ImageTk
# import openpyxl
# import os
# import cv2
# from datetime import datetime

# def create_excel_file():
#     if not os.path.exists("credentials.xlsx"):
#         wb = openpyxl.Workbook()
#         sheet = wb.active
#         sheet.title = "LoginData"
#         sheet.append(["Username", "Password"])
#         wb.save("credentials.xlsx")

# def register():
#     user = reg_user_entry.get()
#     pwd = reg_pass_entry.get()
#     confirm_pwd = reg_confirm_pass_entry.get()

#     if not user or not pwd or not confirm_pwd:
#         messagebox.showerror("Error", "All fields are required.")
#         return

#     if pwd != confirm_pwd:
#         messagebox.showerror("Error", "Passwords do not match.")
#         return

#     wb = openpyxl.load_workbook("credentials.xlsx")
#     sheet = wb.active

#     for row in sheet.iter_rows(min_row=2, values_only=True):
#         if row[0] == user:
#             messagebox.showerror("Error", "Username already exists.")
#             return

#     sheet.append([user, pwd])
#     wb.save("credentials.xlsx")
#     messagebox.showinfo("Success", "Registration successful!")

#     reg_user_entry.delete(0, tk.END)
#     reg_pass_entry.delete(0, tk.END)
#     reg_confirm_pass_entry.delete(0, tk.END)
#     show_login()

# def login():
#     user = login_user_entry.get()
#     pwd = login_pass_entry.get()

#     wb = openpyxl.load_workbook("credentials.xlsx")
#     sheet = wb.active

#     for row in sheet.iter_rows(min_row=2, values_only=True):
#         if row[0] == user and row[1] == pwd:
#             show_attendance_ui(user)
#             return

#     messagebox.showerror("Login Failed", "Invalid credentials.")

# def mark_attendance(username):
#     wb = openpyxl.load_workbook("credentials.xlsx")
#     sheet = wb.active
#     today = datetime.now().strftime('%Y-%m-%d')

#     date_column_index = None
#     for col in range(1, sheet.max_column + 1):
#         if sheet.cell(row=1, column=col).value == today:  
#             date_column_index = col
#             break

#     if date_column_index is None:
#         date_column_index = sheet.max_column + 1
#         sheet.cell(row=1, column=date_column_index, value=today)

#     user_row = None
#     for row in range(2, sheet.max_row + 1):
#         if sheet.cell(row=row, column=1).value == username:
#             user_row = row
#             break

#     if user_row is None:
#         messagebox.showerror("Error", "User not found.")
#         return

#     if sheet.cell(row=user_row, column=date_column_index).value:
#         messagebox.showinfo("Info", "You have already marked attendance for today.")
#     else:
#         sheet.cell(row=user_row, column=date_column_index, value="Present")
#         wb.save("credentials.xlsx")
#         messagebox.showinfo("Success", "Face detected. Attendance marked.")

# def show_attendance_ui(username):
#     login_frame.pack_forget()
#     register_frame.pack_forget()

#     global attendance_frame
#     attendance_frame = tk.Frame(root, bg="#f5f5f5")
#     attendance_frame.pack(fill="both", expand=True, pady=10)

#     top_frame = tk.Frame(attendance_frame, bg="#f5f5f5")
#     top_frame.pack(fill="x", pady=10, padx=20)

#     tk.Label(top_frame, text="Face Attendance System", font=("Arial", 24, "bold"),
#              fg="#4CAF50", bg="#f5f5f5").pack(side="left")
#     tk.Label(top_frame, text=f"Welcome, {username}", font=("Arial", 14, "italic"),
#              fg="#333", bg="#f5f5f5").pack(side="right")

#     capture_button = tk.Button(attendance_frame, text="Capture Face & Mark Attendance", font=("Arial", 14),
#                                bg="#4CAF50", fg="white", relief="flat", width=30, height=2,
#                                command=lambda: capture_face_and_mark(username, capture_button))
#     capture_button.pack(pady=20)

#     logout_button = tk.Button(attendance_frame, text="Logout", font=("Arial", 14), bg="#f44336", fg="white",
#                               relief="flat", width=30, height=2, command=logout)
#     logout_button.pack(pady=10)

#     global camera_label
#     camera_label = tk.Label(attendance_frame)
#     camera_label.pack(pady=20)

#     start_camera()

# def start_camera():
#     global cap
#     cap = cv2.VideoCapture(0)
#     face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

#     def show_frame():
#         ret, frame = cap.read()
#         if not ret:
#             return

#         gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#         faces = face_cascade.detectMultiScale(gray, 1.3, 5)

#         for (x, y, w, h) in faces:
#             cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

#         frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
#         img = Image.fromarray(frame_rgb)
#         img = ImageTk.PhotoImage(img)
#         camera_label.config(image=img)
#         camera_label.image = img

#         camera_label.after(10, show_frame)

#     show_frame()

# def capture_face_and_mark(username, button):
#     global cap
#     cap.release()
#     cap = cv2.VideoCapture(0)

#     face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

#     ret, frame = cap.read()
#     if not ret:
#         messagebox.showerror("Error", "Failed to open camera.")
#         cap.release()
#         return

#     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#     faces = face_cascade.detectMultiScale(gray, 1.3, 5)

#     if len(faces) == 0:
#         messagebox.showerror("Error", "No face detected.")
#     else:
#         for (x, y, w, h) in faces:
#             cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

#         frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
#         img = Image.fromarray(frame_rgb)
#         img = ImageTk.PhotoImage(img)

#         if camera_label.winfo_exists():
#             camera_label.config(image=img)
#             camera_label.image = img

#         mark_attendance(username)

#         cap.release()
#         if camera_label.winfo_exists():
#             camera_label.destroy()

#         button.config(state=tk.NORMAL)

# def logout():
#     global camera_label, cap, attendance_frame
#     if cap.isOpened():
#         cap.release()
#     if camera_label.winfo_exists():
#         camera_label.destroy()
#     if attendance_frame.winfo_exists():
#         attendance_frame.pack_forget()
#     show_login()

# def show_register():
#     login_frame.pack_forget()
#     register_frame.pack(pady=20)

# def show_login():
#     register_frame.pack_forget()
#     login_frame.pack(pady=20)

# def resize_image(image_path, width, height):
#     image = Image.open(image_path)
#     image = image.resize((width, height), Image.Resampling.LANCZOS)
#     return ImageTk.PhotoImage(image)

# create_excel_file()

# # Main UI
# root = tk.Tk()
# root.title("Face Login System")
# root.geometry("1000x700")
# root.config(bg="#f5f5f5")

# # Login Frame with image on left and inputs on right
# login_frame = tk.Frame(root, bg="#f5f5f5")
# login_frame.pack(pady=20)

# # Divide login_frame into two columns
# left_login = tk.Frame(login_frame, bg="#f5f5f5")
# left_login.grid(row=0, column=0, padx=20)

# right_login = tk.Frame(login_frame, bg="#f5f5f5")
# right_login.grid(row=0, column=1, padx=20)

# tk.Label(right_login, text="Face Attendance App", font=("Arial", 24, "bold"),
#          fg="#4CAF50", bg="#f5f5f5").pack(pady=10)

# tk.Label(right_login, text="Login to Continue", font=("Arial", 18, "bold"),
#          fg="#4CAF50", bg="#f5f5f5").pack(pady=10)

# tk.Label(right_login, text="Username:", font=("Arial", 12), bg="#f5f5f5").pack()
# login_user_entry = tk.Entry(right_login, font=("Arial", 12))
# login_user_entry.pack(pady=5)

# tk.Label(right_login, text="Password:", font=("Arial", 12), bg="#f5f5f5").pack()
# login_pass_entry = tk.Entry(right_login, show="*", font=("Arial", 12))
# login_pass_entry.pack(pady=5)

# tk.Button(right_login, text="Login", font=("Arial", 14), bg="#4CAF50", fg="white",
#           relief="flat", width=15, command=login).pack(pady=10)

# tk.Button(right_login, text="Register", font=("Arial", 14), bg="#2196F3", fg="white",
#           relief="flat", width=15, command=show_register).pack(pady=10)

# login_image = resize_image("p2.png", 400, 300)
# tk.Label(left_login, image=login_image, bg="#f5f5f5").pack()

# # Register Frame
# register_frame = tk.Frame(root, bg="#f5f5f5")
# register_frame.pack_forget()

# tk.Label(register_frame, text="Register", font=("Arial", 24, "bold"), fg="#4CAF50",
#          bg="#f5f5f5").grid(row=0, column=0, columnspan=2, pady=10)

# register_image = resize_image("p3e.jpg", 300, 300)
# tk.Label(register_frame, image=register_image, bg="#f5f5f5").grid(row=1, column=0, columnspan=2, pady=10)

# tk.Label(register_frame, text="Username:", font=("Arial", 12), bg="#f5f5f5").grid(row=2, column=0, pady=5)
# reg_user_entry = tk.Entry(register_frame, font=("Arial", 12))
# reg_user_entry.grid(row=2, column=1, pady=5)

# tk.Label(register_frame, text="Password:", font=("Arial", 12), bg="#f5f5f5").grid(row=3, column=0, pady=5)
# reg_pass_entry = tk.Entry(register_frame, show="*", font=("Arial", 12))
# reg_pass_entry.grid(row=3, column=1, pady=5)

# tk.Label(register_frame, text="Confirm Password:", font=("Arial", 12), bg="#f5f5f5").grid(row=4, column=0, pady=5)
# reg_confirm_pass_entry = tk.Entry(register_frame, show="*", font=("Arial", 12))
# reg_confirm_pass_entry.grid(row=4, column=1, pady=5)

# tk.Button(register_frame, text="Register", font=("Arial", 14), bg="#4CAF50", fg="white",
#           relief="flat", width=15, command=register).grid(row=5, column=0, columnspan=2, pady=10)

# root.mainloop()

print(4+4)

000000111111
11110000011
00111
