import tkinter as tk
import customtkinter as ctk
from tkinter import messagebox

# Configure appearance window settings matching iOS preferences
ctk.set_appearance_mode("Dark")  # Default to Dark Mode (Theme 0)
ctk.set_default_color_theme("blue")

# --- Data Structures ---
class Question:
    def __init__(self, text, options, correct_index, explanation):
        self.text = text
        self.options = options
        self.correct_answer_index = correct_index
        self.explanation = explanation

# Full question bank layout matching your application's schema
cybersecurity_questions = [
    Question(
        text="What does the 's' in 'https://' stand for?",
        options=["Simple", "Secure", "Speed", "System"],
        correct_index=1,
        explanation="The 'S' stands for Secure. It means all data sent between your browser and the website is fully encrypted."
    ),
    Question(
        text="Which of the following is a strong password practice?",
        options=["Using your birthdate", "Reusing passwords", "Using a password manager", "Keeping it under 5 characters"],
        correct_index=2,
        explanation="Using a unique passphrase managed securely by an encrypted password manager keeps accounts safest."
    ),
    Question(
        text="What is phishing?",
        options=["A fast downloading method", "An attempt to trick you into revealing private keys", "A type of firewall system", "A secure network protocol"],
        correct_index=1,
        explanation="Phishing involves fraudulent communications designed to trick individuals into revealing sensitive credentials."
    )
]

# --- Color Management ---
class ThemePalette:
    def __init__(self, mode):
        if mode == 0:  # Dark Mode
            self.lava = "#FF4500"
            self.background = "#1C1C1E"
            self.card_background = "#2C2C2E"
            self.text = "#FFFFFF"
            self.button_text = "#FFFFFF"
        else:          # Light Mode
            self.lava = "#FF4500"
            self.background = "#F2F2F7"
            self.card_background = "#E5E5EA"
            self.text = "#000000"
            self.button_text = "#000000"

# --- Main App Frame View Engine ---
class MagmaSecurityApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Window Frame Constraints
        self.title("Magma Security")
        self.geometry("450x750")
        self.resizable(True, True)

        # State Tracker Variables
        self.current_theme = 0  # 0 = Dark, 1 = Light
        self.score = 0
        self.current_question_index = 0
        self.selected_answer_index = None
        self.is_answer_submitted = False
        
        # Load Color Palette configuration
        self.palette = ThemePalette(self.current_theme)
        self.configure(fg_color=self.palette.background)

        # Container viewport representing our ZStack frame root
        self.main_container = ctk.CTkFrame(self, fg_color="transparent")
        self.main_container.pack(fill="both", expand=True, padx=20, pady=20)

        # Draw Persistent Button Layers Overlay
        self.draw_overlay_controls()

        # Route directly to entry point
        self.show_main_menu()

    def draw_overlay_controls(self):
        """Generates floating action overlays mimicking original iOS view presentation layer."""
        self.overlay_frame = ctk.CTkFrame(self, fg_color="transparent", height=40)
        self.overlay_frame.place(relx=0.0, rely=0.0, relwidth=1.0, anchor="nw", x=15, y=15)

        # Fixed explicit system backgrounds to prevent hex alpha parsing errors
        btn_bg = "#2C2C2E" if self.current_theme == 0 else "#E5E5EA"

        # Theme Swapping Control (Top Left Position Alignment)
        self.theme_btn = ctk.CTkButton(
            self.overlay_frame, 
            text="◐", 
            width=36, 
            height=36, 
            corner_radius=18,
            fg_color=btn_bg,
            text_color=self.palette.text,
            font=("Arial", 16),
            command=self.toggle_theme
        )
        self.theme_btn.pack(side="left")

        # Exit Context Guard Intermediary (Top Right Position Alignment)
        self.exit_btn = ctk.CTkButton(
            self.overlay_frame, 
            text="✕", 
            width=36, 
            height=36, 
            corner_radius=18,
            fg_color=btn_bg,
            text_color=self.palette.text,
            font=("Arial", 14, "bold"),
            command=self.confirm_abandon_quiz
        )
        self.exit_btn.pack_forget()

    def toggle_theme(self):
        """Shifts UI view palettes reactively across runtime contexts."""
        self.current_theme = 1 if self.current_theme == 0 else 0
        self.palette = ThemePalette(self.current_theme)
        
        self.configure(fg_color=self.palette.background)
        ctk.set_appearance_mode("Light" if self.current_theme == 1 else "Dark")
        
        btn_bg = "#2C2C2E" if self.current_theme == 0 else "#E5E5EA"
        self.theme_btn.configure(fg_color=btn_bg, text_color=self.palette.text)
        self.exit_btn.configure(fg_color=btn_bg, text_color=self.palette.text)
        
        self.refresh_view()

    def confirm_abandon_quiz(self):
        """Displays native system modal window dialog to verify destructive intent."""
        confirm = messagebox.askokcancel(
            title="Abandon Quiz?",
            message="Are you sure you want to leave? Your current quiz progress and score will be permanently lost.",
            icon="warning"
        )
        if confirm:
            self.reset_game_state_to_menu()

    def reset_game_state_to_menu(self):
        self.score = 0
        self.current_question_index = 0
        self.selected_answer_index = None
        self.is_answer_submitted = False
        self.show_main_menu()

    def clear_container(self):
        for widget in self.main_container.winfo_children():
            widget.destroy()

    def refresh_view(self):
        for widget in self.main_container.winfo_children():
            widget.pack_forget()
        self.clear_container()
        
        if hasattr(self, 'view_state'):
            if self.view_state == "menu": self.show_main_menu()
            elif self.view_state == "trivia": self.show_trivia_view()
            elif self.view_state == "score": self.show_score_view()

    # --- Main Menu View ---
    def show_main_menu(self):
        self.view_state = "menu"
        self.clear_container()
        self.exit_btn.pack_forget()

        ctk.CTkLabel(self.main_container, text="", height=40).pack()

        icon_label = ctk.CTkLabel(self.main_container, text="🛡️", font=("Arial", 80), text_color=self.palette.lava)
        icon_label.pack(pady=20)

        title_label = ctk.CTkLabel(self.main_container, text="Magma Security", font=("Arial", 32, "bold"), text_color=self.palette.lava)
        title_label.pack(pady=5)

        subtitle_label = ctk.CTkLabel(self.main_container, text="Learn Web Safety & Stay Safe Online", font=("Arial", 16), text_color=self.palette.lava)
        subtitle_label.pack(pady=10)

        ctk.CTkFrame(self.main_container, fg_color="transparent").pack(fill="both", expand=True)

        start_btn = ctk.CTkButton(
            self.main_container, 
            text="Start Game", 
            font=("Arial", 18, "bold"),
            fg_color="#4CD964",
            text_color="#FFFFFF",
            height=55,
            corner_radius=12,
            command=self.start_new_game
        )
        start_btn.pack(fill="x", pady=20)

    def start_new_game(self):
        self.score = 0
        self.current_question_index = 0
        self.selected_answer_index = None
        self.is_answer_submitted = False
        self.show_trivia_view()

    # --- Trivia Mode View ---
    def show_trivia_view(self):
        self.view_state = "trivia"
        self.clear_container()
        self.exit_btn.pack(side="right")

        current_q = cybersecurity_questions[self.current_question_index]

        scroll_container = ctk.CTkScrollableFrame(self.main_container, fg_color="transparent", label_fg_color="transparent")
        scroll_container.pack(fill="both", expand=True, pady=(40, 0))

        header_frame = ctk.CTkFrame(scroll_container, fg_color="transparent")
        header_frame.pack(fill="x", pady=(10, 15))

        q_counter = ctk.CTkLabel(header_frame, text=f"Question {self.current_question_index + 1} of {len(cybersecurity_questions)}", font=("Arial", 14), text_color=self.palette.text)
        q_counter.pack(side="left")

        score_counter = ctk.CTkLabel(header_frame, text=f"Score: {self.score}", font=("Arial", 14, "bold"), text_color=self.palette.text)
        score_counter.pack(side="right")

        question_card = ctk.CTkLabel(
            scroll_container,
            text=current_q.text,
            font=("Arial", 18, "bold"),
            text_color=self.palette.text,
            fg_color=self.palette.card_background,
            corner_radius=15,
            wraplength=360,
            padx=20,
            pady=20
        )
        question_card.pack(fill="x", pady=15)

        self.option_buttons = []
        for idx, option_text in enumerate(current_q.options):
            bg_color, border_color, border_width = self.get_option_styles(idx, current_q)
            
            # FIXED: Avoid setting border_color to "transparent", use explicit width control
            btn = ctk.CTkButton(
                scroll_container,
                text=option_text,
                font=("Arial", 15),
                text_color=self.palette.text,
                fg_color=bg_color,
                border_color=border_color,
                border_width=border_width,
                height=50,
                corner_radius=10,
                anchor="w",
                command=lambda i=idx: self.select_option(i)
            )
            if self.is_answer_submitted:
                btn.configure(state="disabled")
            
            btn.pack(fill="x", pady=6, padx=15)
            self.option_buttons.append(btn)

        if self.is_answer_submitted:
            tip_card = ctk.CTkFrame(scroll_container, fg_color="#007AFF" if self.current_theme==1 else "#1A2E40", corner_radius=12)
            tip_card.pack(fill="x", pady=15, padx=2)
            
            tip_title = ctk.CTkLabel(tip_card, text="💡 Educational Tip:", font=("Arial", 15, "bold"), text_color=self.palette.text, anchor="w")
            tip_title.pack(fill="x", padx=15, pady=(10, 2))
            
            tip_body = ctk.CTkLabel(tip_card, text=current_q.explanation, font=("Arial", 13), text_color=self.palette.text, wraplength=340, justify="left", anchor="w")
            tip_body.pack(fill="x", padx=15, pady=(2, 10))

        submit_btn_color = "#007AFF" if self.selected_answer_index is not None else "#8E8E93"
        submit_text = "Submit" if not self.is_answer_submitted else ("See Results" if self.current_question_index == len(cybersecurity_questions) - 1 else "Next Question")

        submit_btn = ctk.CTkButton(
            scroll_container,
            text=submit_text,
            font=("Arial", 16, "bold"),
            fg_color=submit_btn_color,
            text_color="#FFFFFF",
            height=50,
            corner_radius=12,
            state="normal" if self.selected_answer_index is not None else "disabled",
            command=self.handle_action_submit
        )
        submit_btn.pack(fill="x", pady=(25, 20), padx=15)

    def select_option(self, index):
        if not self.is_answer_submitted:
            self.selected_answer_index = index
            self.show_trivia_view()

    def get_option_styles(self, index, question):
        """Returns (bg_color, border_color, border_width) avoiding transparency errors."""
        if self.is_answer_submitted:
            if index == question.correct_answer_index:
                return ("#243D2C", "#4CD964", 2) if self.current_theme == 0 else ("#E2F6EA", "#4CD964", 2)
            elif self.selected_answer_index == index:
                return ("#3D2424", "#FF3B30", 2) if self.current_theme == 0 else ("#FCE8E6", "#FF3B30", 2)
        elif self.selected_answer_index == index:
            return ("#1A2E40", "#007AFF", 2) if self.current_theme == 0 else ("#E1F0FF", "#007AFF", 2)
        
        # Unselected/Default styles: Pass background color as border color with 0 width to ensure safety
        return (self.palette.card_background, self.palette.card_background, 0)

    def handle_action_submit(self):
        current_q = cybersecurity_questions[self.current_question_index]
        if not self.is_answer_submitted:
            self.is_answer_submitted = True
            if self.selected_answer_index == current_q.correct_answer_index:
                self.score += 1
            self.show_trivia_view()
        else:
            if self.current_question_index < len(cybersecurity_questions) - 1:
                self.current_question_index += 1
                self.selected_answer_index = None
                self.is_answer_submitted = False
                self.show_trivia_view()
            else:
                self.show_score_view()

    # --- Score Screen View ---
    def show_score_view(self):
        self.view_state = "score"
        self.clear_container()
        self.exit_btn.pack_forget()

        ctk.CTkLabel(self.main_container, text="", height=30).pack()

        finish_title = ctk.CTkLabel(self.main_container, text="🎉 Quiz Completed!", font=("Arial", 28, "bold"), text_color=self.palette.text)
        finish_title.pack(pady=20)

        score_frame = ctk.CTkFrame(self.main_container, fg_color="transparent")
        score_frame.pack(pady=15)

        meta_score_lbl = ctk.CTkLabel(score_frame, text="Your Final Score", font=("Arial", 16), text_color=self.palette.text)
        meta_score_lbl.pack()

        score_digits = ctk.CTkLabel(score_frame, text=f"{self.score} / {len(cybersecurity_questions)}", font=("Arial", 54, "bold"), text_color="#007AFF")
        score_digits.pack(pady=10)

        msg_lbl = ctk.CTkLabel(self.main_container, text=self.get_score_msg_string(), font=("Arial", 15), text_color=self.palette.text, wraplength=320, justify="center")
        msg_lbl.pack(pady=15)

        ctk.CTkFrame(self.main_container, fg_color="transparent").pack(fill="both", expand=True)

        share_btn = ctk.CTkButton(
            self.main_container,
            text="📤 Share Score",
            font=("Arial", 16, "bold"),
            fg_color="#4CD964",
            text_color="#FFFFFF",
            height=50,
            corner_radius=12,
            command=lambda: messagebox.showinfo("Share Data", "Copied scorecard message safely to clipboard!")
        )
        share_btn.pack(fill="x", pady=10)

        menu_btn = ctk.CTkButton(
            self.main_container,
            text="Main Menu",
            font=("Arial", 14),
            fg_color="transparent",
            text_color="#8E8E93",
            hover_color=f"{self.palette.text}1A",
            height=35,
            command=self.reset_game_state_to_menu
        )
        menu_btn.pack(pady=10)

    def get_score_msg_string(self):
        pct = float(self.score) / float(len(cybersecurity_questions))
        if pct == 1.0:
            return "Perfect score! You are a digital security expert! 🛡️"
        elif pct >= 0.5:
            return "Good job! You understand core internet safe practices. Keep practicing! 💻"
        else:
            return "Keep reading up! Web safety steps secure your online accounts and identity. 🔐"

if __name__ == "__main__":
    app = MagmaSecurityApp()
    app.mainloop()
