"""
MiniBlog - A Premium Desktop Blog Management Application.
Reinforces basic programming concepts:
- Tkinter GUI (Flat dark-theme visual system with micro-interactions)
- File Handling (Robust read/write and directory management)
- OOP principles (User and Post classes with validation)
- Exception Handling (Try-except validation & robust file I/O error dialogs)
"""

import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import os
import re
import datetime

# Enable High DPI awareness on Windows for razor-sharp fonts and borders
try:
    from ctypes import windll
    windll.shcore.SetProcessDpiAwareness(1)
except ImportError:
    pass


# =========================================================================
# MODELS (OOP CLASSES)
# =========================================================================

class User:
    """Represents a User of the MiniBlog system."""
    def __init__(self, username: str):
        self.username = self.validate_username(username)

    @staticmethod
    def validate_username(username: str) -> str:
        """Validates and cleanses the username."""
        if not username or not username.strip():
            raise ValueError("Author name cannot be empty.")
        if len(username.strip()) < 2:
            raise ValueError("Author name must be at least 2 characters long.")
        return username.strip()

    def __str__(self):
        return self.username


class Post:
    """Represents a Blog Post written by a User."""
    def __init__(self, title: str, content: str, author: User, timestamp: str = None):
        self.title = self.validate_title(title)
        self.content = self.validate_content(content)
        self.author = author
        self.timestamp = timestamp or datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    @staticmethod
    def validate_title(title: str) -> str:
        """Validates and cleanses the blog post title."""
        if not title or not title.strip():
            raise ValueError("Post title cannot be empty.")
        if len(title.strip()) < 3:
            raise ValueError("Post title must be at least 3 characters long.")
        return title.strip()

    @staticmethod
    def validate_content(content: str) -> str:
        """Validates and cleanses the post content."""
        if not content or not content.strip():
            raise ValueError("Post content cannot be empty.")
        return content.strip()

    def get_filename(self) -> str:
        """Generates a clean, sanitized filename matching 'username_title.txt'."""
        # Sanitize author name (only alphanumeric and underscores)
        clean_author = re.sub(r'[^a-zA-Z0-9\s_-]', '', self.author.username)
        clean_author = clean_author.strip().replace(' ', '_').lower()

        # Sanitize post title
        clean_title = re.sub(r'[^a-zA-Z0-9\s_-]', '', self.title)
        clean_title = clean_title.strip().replace(' ', '_').lower()

        return f"{clean_author}_{clean_title}.txt"

    def save_to_file(self, directory: str):
        """Saves the post content to a text file in the given directory using custom headers."""
        if not os.path.exists(directory):
            os.makedirs(directory)

        filename = self.get_filename()
        filepath = os.path.join(directory, filename)

        try:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(f"Title: {self.title}\n")
                f.write(f"Author: {self.author.username}\n")
                f.write(f"Date: {self.timestamp}\n")
                f.write("-" * 50 + "\n")
                f.write(self.content)
        except IOError as e:
            raise IOError(f"Unable to write to file '{filename}': {str(e)}")

    @classmethod
    def load_from_file(cls, filepath: str) -> 'Post':
        """Loads and parses a post from a file path."""
        if not os.path.exists(filepath):
            raise FileNotFoundError(f"The selected post file was not found: {os.path.basename(filepath)}")

        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                lines = f.readlines()

            if len(lines) < 4:
                raise ValueError("The post file is corrupted or not in the valid MiniBlog format.")

            title = ""
            author_name = ""
            timestamp = ""

            # Parse metadata headers from the first three lines
            for line in lines[:3]:
                if line.startswith("Title: "):
                    title = line[7:].strip()
                elif line.startswith("Author: "):
                    author_name = line[8:].strip()
                elif line.startswith("Date: "):
                    timestamp = line[6:].strip()

            # Content starts after the separator line (index 3)
            content = "".join(lines[4:])

            # Validation checks on parsed data
            if not title or not author_name or not content:
                raise ValueError("Missing header fields or body text in post file.")

            user = User(author_name)
            return cls(title, content, user, timestamp)

        except Exception as e:
            raise ValueError(f"Failed to load and parse post: {str(e)}")


# =========================================================================
# GUI APPLICATION
# =========================================================================

class MiniBlogApp:
    def __init__(self, root):
        self.root = root
        self.root.title("MiniBlog - Personal Desktop Journal")
        self.root.geometry("1020x680")
        self.root.configure(bg="#121214")
        self.root.resizable(True, True)

        # Center the window on start
        self.center_window(1020, 680)

        # Base directory for storing posts
        self.posts_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "posts")
        if not os.path.exists(self.posts_dir):
            os.makedirs(self.posts_dir)

        # Track loaded filenames associated with listbox indexes
        self.loaded_filenames = []

        # Build UI layout
        self.setup_ui()
        self.refresh_library()

    def center_window(self, width, height):
        """Centers the Tkinter window on the primary screen."""
        self.root.update_idletasks()
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x = (screen_width // 2) - (width // 2)
        y = (screen_height // 2) - (height // 2)
        self.root.geometry(f"{width}x{height}+{int(x)}+{int(y)}")

    def setup_ui(self):
        """Initializes and builds the dark-themed UI components."""
        # 1. HEADER FRAME
        header_frame = tk.Frame(self.root, bg="#1a1a24", height=70)
        header_frame.pack(fill="x", side="top")
        header_frame.pack_propagate(False)

        title_label = tk.Label(
            header_frame, 
            text="✍️ MINIBLOG", 
            font=("Segoe UI", 16, "bold"), 
            bg="#1a1a24", 
            fg="#89b4fa"
        )
        title_label.pack(side="left", padx=25, pady=15)

        subtitle_label = tk.Label(
            header_frame, 
            text="Personal Offline Journal & Desktop Publisher", 
            font=("Segoe UI", 9, "italic"), 
            bg="#1a1a24", 
            fg="#9ca3af"
        )
        subtitle_label.pack(side="left", pady=22)

        # Main Body Container with padding
        main_container = tk.Frame(self.root, bg="#121214")
        main_container.pack(fill="both", expand=True, padx=20, pady=20)

        # Configure columns (Left: 55% for Editor, Right: 45% for Post Library)
        main_container.columnconfigure(0, weight=5, uniform="group1")
        main_container.columnconfigure(1, weight=4, uniform="group1")
        main_container.rowconfigure(0, weight=1)

        # -------------------------------------------------------------
        # LEFT COLUMN: POST CREATION EDITOR
        # -------------------------------------------------------------
        editor_card = tk.Frame(main_container, bg="#1a1a24", bd=0, highlightthickness=1, highlightbackground="#2d2d3d")
        editor_card.grid(row=0, column=0, sticky="nsew", padx=(0, 10))

        # Editor Padding frame
        editor_pad = tk.Frame(editor_card, bg="#1a1a24")
        editor_pad.pack(fill="both", expand=True, padx=25, pady=20)

        editor_title = tk.Label(
            editor_pad, 
            text="Create New Post", 
            font=("Segoe UI", 13, "bold"), 
            bg="#1a1a24", 
            fg="#ffffff"
        )
        editor_title.pack(anchor="w", pady=(0, 15))

        # Label + Entry: Author Name
        name_lbl = tk.Label(editor_pad, text="AUTHOR NAME", font=("Segoe UI", 8, "bold"), bg="#1a1a24", fg="#a6adc8")
        name_lbl.pack(anchor="w", pady=(5, 3))
        self.name_entry = tk.Entry(editor_pad)
        self.name_entry.pack(fill="x", ipady=8, pady=(0, 12))
        self.style_input(self.name_entry)

        # Label + Entry: Post Title
        title_lbl = tk.Label(editor_pad, text="POST TITLE", font=("Segoe UI", 8, "bold"), bg="#1a1a24", fg="#a6adc8")
        title_lbl.pack(anchor="w", pady=(5, 3))
        self.title_entry = tk.Entry(editor_pad)
        self.title_entry.pack(fill="x", ipady=8, pady=(0, 12))
        self.style_input(self.title_entry)

        # Label + Text: Post Content
        content_lbl = tk.Label(editor_pad, text="POST CONTENT", font=("Segoe UI", 8, "bold"), bg="#1a1a24", fg="#a6adc8")
        content_lbl.pack(anchor="w", pady=(5, 3))

        # Text Editor Container (for scrollbar integration)
        text_container = tk.Frame(editor_pad, bg="#1a1a24")
        text_container.pack(fill="both", expand=True, pady=(0, 15))

        text_scrollbar = tk.Scrollbar(text_container, bg="#1a1a24", activebackground="#2d2d3d")
        text_scrollbar.pack(side="right", fill="y")

        self.content_text = tk.Text(
            text_container, 
            wrap="word", 
            yscrollcommand=text_scrollbar.set,
            font=("Segoe UI", 11)
        )
        self.content_text.pack(side="left", fill="both", expand=True)
        self.style_input(self.content_text)
        text_scrollbar.config(command=self.content_text.yview)

        # Editor Button Panel
        btn_panel = tk.Frame(editor_pad, bg="#1a1a24")
        btn_panel.pack(fill="x")

        # Save Button (Accent Blue Color)
        self.save_btn = self.create_button(
            btn_panel, 
            text="💾 Save Post", 
            command=self.save_post, 
            bg_color="#6366f1", 
            fg_color="#ffffff", 
            hover_color="#4f46e5"
        )
        self.save_btn.pack(side="left", padx=(0, 10))

        # Clear Button (Secondary Slate Color)
        self.clear_btn = self.create_button(
            btn_panel, 
            text="🧹 Clear Fields", 
            command=self.clear_fields, 
            bg_color="#2a2b3d", 
            fg_color="#cdd6f4", 
            hover_color="#363752"
        )
        self.clear_btn.pack(side="left")

        # -------------------------------------------------------------
        # RIGHT COLUMN: POST LIBRARY & VIEWER
        # -------------------------------------------------------------
        library_container = tk.Frame(main_container, bg="#121214")
        library_container.grid(row=0, column=1, sticky="nsew", padx=(10, 0))

        # Configure Grid Rows for Right Column (Top 45% Listbox, Bottom 55% Viewer)
        library_container.rowconfigure(0, weight=4, uniform="right_group")
        library_container.rowconfigure(1, weight=5, uniform="right_group")
        library_container.columnconfigure(0, weight=1)

        # TOP CARD: LISTBOX
        listbox_card = tk.Frame(library_container, bg="#1a1a24", bd=0, highlightthickness=1, highlightbackground="#2d2d3d")
        listbox_card.grid(row=0, column=0, sticky="nsew", pady=(0, 10))

        listbox_pad = tk.Frame(listbox_card, bg="#1a1a24")
        listbox_pad.pack(fill="both", expand=True, padx=20, pady=15)

        # Header with Refresh Button
        listbox_header = tk.Frame(listbox_pad, bg="#1a1a24")
        listbox_header.pack(fill="x", pady=(0, 10))

        tk.Label(
            listbox_header, 
            text="Saved Posts Library", 
            font=("Segoe UI", 12, "bold"), 
            bg="#1a1a24", 
            fg="#ffffff"
        )
        listbox_header.columnconfigure(0, weight=1)

        # Inner listbox frame with scrollbar
        list_inner = tk.Frame(listbox_pad, bg="#1a1a24")
        list_inner.pack(fill="both", expand=True)

        list_scrollbar = tk.Scrollbar(list_inner, bg="#1a1a24")
        list_scrollbar.pack(side="right", fill="y")

        self.listbox = tk.Listbox(
            list_inner, 
            bg="#232330", 
            fg="#cdd6f4", 
            selectbackground="#6366f1", 
            selectforeground="#ffffff", 
            relief="flat", 
            bd=0, 
            highlightthickness=1, 
            highlightcolor="#6366f1",
            highlightbackground="#2d2d3d",
            font=("Segoe UI", 10),
            yscrollcommand=list_scrollbar.set
        )
        self.listbox.pack(side="left", fill="both", expand=True)
        list_scrollbar.config(command=self.listbox.yview)

        # Bind Listbox selection to automatic loading
        self.listbox.bind("<<ListboxSelect>>", self.on_select_post)

        # Control Panel below listbox
        list_ctrl = tk.Frame(listbox_pad, bg="#1a1a24")
        list_ctrl.pack(fill="x", pady=(10, 0))

        # View Post Button
        self.view_btn = self.create_button(
            list_ctrl, 
            text="🔍 View Post", 
            command=self.on_select_post, 
            bg_color="#313244", 
            fg_color="#cdd6f4", 
            hover_color="#45475a"
        )
        self.view_btn.pack(side="left", padx=(0, 10))

        # Delete Selected Button
        self.delete_btn = self.create_button(
            list_ctrl, 
            text="🗑️ Delete Post", 
            command=self.delete_post, 
            bg_color="#f38ba8", 
            fg_color="#11111b", 
            hover_color="#f27495"
        )
        self.delete_btn.pack(side="right")

        # BOTTOM CARD: DETAIL POST VIEWER
        viewer_card = tk.Frame(library_container, bg="#1a1a24", bd=0, highlightthickness=1, highlightbackground="#2d2d3d")
        viewer_card.grid(row=1, column=0, sticky="nsew", pady=(10, 0))

        self.viewer_pad = tk.Frame(viewer_card, bg="#1a1a24")
        self.viewer_pad.pack(fill="both", expand=True, padx=20, pady=15)

        # Placeholder label when no post is loaded
        self.view_placeholder = tk.Label(
            self.viewer_pad, 
            text="Select a post from the library above\nto view its contents here.", 
            font=("Segoe UI", 11, "italic"), 
            bg="#1a1a24", 
            fg="#6c7086", 
            justify="center"
        )
        self.view_placeholder.pack(fill="both", expand=True)

        # Viewer elements (hidden on start, packed programmatically)
        self.view_details_frame = tk.Frame(self.viewer_pad, bg="#1a1a24")

        self.view_title_label = tk.Label(
            self.view_details_frame, 
            text="", 
            font=("Segoe UI", 14, "bold"), 
            bg="#1a1a24", 
            fg="#89b4fa", 
            wraplength=380, 
            justify="left", 
            anchor="w"
        )
        self.view_title_label.pack(fill="x", pady=(0, 3))

        self.view_meta_label = tk.Label(
            self.view_details_frame, 
            text="", 
            font=("Segoe UI", 9), 
            bg="#1a1a24", 
            fg="#9ca3af", 
            anchor="w"
        )
        self.view_meta_label.pack(fill="x", pady=(0, 10))

        # Divider frame
        divider = tk.Frame(self.view_details_frame, bg="#2d2d3d", height=1)
        divider.pack(fill="x", pady=(0, 10))

        # View text block
        view_text_container = tk.Frame(self.view_details_frame, bg="#1a1a24")
        view_text_container.pack(fill="both", expand=True)

        view_text_scroll = tk.Scrollbar(view_text_container, bg="#1a1a24")
        view_text_scroll.pack(side="right", fill="y")

        self.view_content_text = tk.Text(
            view_text_container, 
            wrap="word", 
            yscrollcommand=view_text_scroll.set,
            font=("Segoe UI", 11), 
            bg="#1a1a24", 
            fg="#cdd6f4", 
            relief="flat", 
            bd=0, 
            padx=5, 
            state="disabled"
        )
        self.view_content_text.pack(side="left", fill="both", expand=True)
        view_text_scroll.config(command=self.view_content_text.yview)

    # -------------------------------------------------------------
    # CUSTOM WIDGET STYLING & BINDING UTILITIES
    # -------------------------------------------------------------
    def style_input(self, widget):
        """Styles entries and text boxes to have sleek flat dark look with dynamic focus highlights."""
        widget.config(
            bg="#232330",
            fg="#e3e3e6",
            insertbackground="#ffffff",
            relief="flat",
            highlightthickness=1,
            highlightbackground="#2d2d3d",
            highlightcolor="#6366f1"
        )
        widget.bind("<FocusIn>", lambda e: widget.config(highlightbackground="#6366f1", highlightcolor="#6366f1"))
        widget.bind("<FocusOut>", lambda e: widget.config(highlightbackground="#2d2d3d"))

    def create_button(self, parent, text, command, bg_color, fg_color, hover_color):
        """Creates a modern flat styled button with hover and active micro-interactions."""
        btn = tk.Button(
            parent,
            text=text,
            command=command,
            bg=bg_color,
            fg=fg_color,
            activebackground=hover_color,
            activeforeground=fg_color,
            font=("Segoe UI", 10, "bold"),
            relief="flat",
            bd=0,
            padx=14,
            pady=7,
            cursor="hand2"
        )
        btn.bind("<Enter>", lambda e: btn.config(bg=hover_color))
        btn.bind("<Leave>", lambda e: btn.config(bg=bg_color))
        return btn

    # -------------------------------------------------------------
    # EVENT HANDLERS & CORE LOGIC
    # -------------------------------------------------------------
    def refresh_library(self):
        """Scans the saved posts folder, populates the listbox, and updates mappings."""
        self.listbox.delete(0, tk.END)
        self.loaded_filenames = []

        try:
            if not os.path.exists(self.posts_dir):
                os.makedirs(self.posts_dir)

            # Get all text files in alphabetical order
            files = sorted(
                [f for f in os.listdir(self.posts_dir) if f.endswith(".txt")],
                key=lambda x: os.path.getmtime(os.path.join(self.posts_dir, x)),
                reverse=True # Show newest first
            )

            for filename in files:
                filepath = os.path.join(self.posts_dir, filename)
                try:
                    # Attempt to read parsed data to show rich list items
                    post = Post.load_from_file(filepath)
                    display_text = f"📝 {post.title} — by {post.author.username}"
                    self.listbox.insert(tk.END, display_text)
                    self.loaded_filenames.append(filename)
                except Exception:
                    # Fallback to displaying raw filename if file format is custom
                    self.listbox.insert(tk.END, f"📄 {filename}")
                    self.loaded_filenames.append(filename)

        except Exception as e:
            messagebox.showerror("System Error", f"Failed to refresh list: {str(e)}")

    def clear_fields(self):
        """Clears all text boxes and entries inside the Editor panel."""
        self.name_entry.delete(0, tk.END)
        self.title_entry.delete(0, tk.END)
        self.content_text.delete("1.0", tk.END)

    def save_post(self):
        """Validates input fields, creates User/Post objects, and writes to disk."""
        name = self.name_entry.get().strip()
        title = self.title_entry.get().strip()
        content = self.content_text.get("1.0", tk.END).strip()

        # Try-Except block catching validation constraints & handling errors
        try:
            # 1. Instantiate User (triggers author validation)
            author = User(name)

            # 2. Instantiate Post (triggers title and content validations)
            post = Post(title, content, author)

            # 3. Handle duplicate filenames (ask if user wants to overwrite)
            filename = post.get_filename()
            filepath = os.path.join(self.posts_dir, filename)
            
            if os.path.exists(filepath):
                confirm = messagebox.askyesno(
                    "Overwrite Post?", 
                    f"A post titled '{title}' by '{name}' already exists.\n\nDo you want to overwrite it?",
                    icon="warning"
                )
                if not confirm:
                    return

            # 4. Save post file
            post.save_to_file(self.posts_dir)
            messagebox.showinfo("Success!", "Your blog post was successfully published and saved!")

            # 5. Refresh library and automatically select & view the new post
            self.refresh_library()
            
            if filename in self.loaded_filenames:
                new_index = self.loaded_filenames.index(filename)
                self.listbox.selection_clear(0, tk.END)
                self.listbox.selection_set(new_index)
                self.listbox.activate(new_index)
                self.on_select_post()

            # Clean editor fields but KEEP the author's name for typing consecutive posts
            self.title_entry.delete(0, tk.END)
            self.content_text.delete("1.0", tk.END)

        except ValueError as val_err:
            # Catch validation exceptions from model classes
            messagebox.showwarning("Validation Error", str(val_err))
        except IOError as io_err:
            # Catch file operations exceptions
            messagebox.showerror("File Error", f"An error occurred while saving the post:\n{str(io_err)}")
        except Exception as e:
            # Universal fallback catch
            messagebox.showerror("Unexpected Error", f"An unexpected issue occurred:\n{str(e)}")

    def on_select_post(self, event=None):
        """Event handler triggered when selecting a listbox item. Loads and previews post."""
        selection = self.listbox.curselection()
        if not selection:
            return

        index = selection[0]
        filename = self.loaded_filenames[index]
        filepath = os.path.join(self.posts_dir, filename)

        try:
            # Load and parse post using Post class method
            post = Post.load_from_file(filepath)
            self.display_post_details(post)
        except FileNotFoundError:
            messagebox.showerror("File Not Found", f"The file '{filename}' was not found.\nIt might have been renamed or deleted from the folder.")
            self.refresh_library()
            self.clear_viewer()
        except Exception as e:
            messagebox.showerror("Format Error", f"Could not read post file:\n{str(e)}")
            self.clear_viewer()

    def display_post_details(self, post):
        """Packs the details panel and loads values into the viewer."""
        # Hide the empty viewer placeholder
        self.view_placeholder.pack_forget()

        # Display the details container
        self.view_details_frame.pack(fill="both", expand=True)

        # Update text labels
        self.view_title_label.config(text=post.title)
        self.view_meta_label.config(text=f"✍️ {post.author.username}  •  📅 {post.timestamp}")

        # Enable text area, clear old content, insert new content, disable text area
        self.view_content_text.config(state="normal")
        self.view_content_text.delete("1.0", tk.END)
        self.view_content_text.insert(tk.END, post.content)
        self.view_content_text.config(state="disabled")

    def clear_viewer(self):
        """Resets the detail viewer to its default empty placeholder state."""
        self.view_details_frame.pack_forget()
        self.view_placeholder.pack(fill="both", expand=True)

    def delete_post(self):
        """Deletes the currently selected post from both the UI and the file system."""
        selection = self.listbox.curselection()
        if not selection:
            messagebox.showwarning("Selection Required", "Please select a post from the list to delete.")
            return

        index = selection[0]
        filename = self.loaded_filenames[index]
        filepath = os.path.join(self.posts_dir, filename)

        confirm = messagebox.askyesno(
            "Confirm Delete", 
            f"Are you sure you want to permanently delete this post?\n\nFile: {filename}",
            icon="warning"
        )

        if confirm:
            try:
                if os.path.exists(filepath):
                    os.remove(filepath)
                    messagebox.showinfo("Deleted", "Post successfully deleted.")
                else:
                    raise FileNotFoundError()
                
                # Refresh layout
                self.refresh_library()
                self.clear_viewer()
            except Exception as e:
                messagebox.showerror("Error", f"Failed to delete the post file:\n{str(e)}")
                self.refresh_library()


if __name__ == "__main__":
    root = tk.Tk()
    app = MiniBlogApp(root)
    root.mainloop()
