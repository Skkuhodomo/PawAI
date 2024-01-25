from st_pages import Page, Section, show_pages, add_page_title

show_pages(
    [
        Page("home.py", "Home", "🏠"),
        Page("ui_classifier.py", "PawAI", ":paw_prints:"),
        Page("chat.py", "Chat", ":robot_face:"),
        Page("dalle.py", "Image generator", ":art:"),       
    ]
)