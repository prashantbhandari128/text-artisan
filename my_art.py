from textartisan.text_artisan import TextArtisan

class MyArt(TextArtisan):
    def __init__(self):
        super().__init__()

    def print_red_bold_underline(self, message):
        style = [self.BOLD, self.UNDERLINE, self.COLORS["red"]]
        print(self.decorate(style, message))

    def print_blue_bold_italic(self, message):
        style = [self.BOLD, self.ITALIC, self.COLORS["blue"]]
        print(self.decorate(style, message))

    def print_rainbow(self, message):
        rainbow_colors = [
            self.COLORS["red"], 
            self.COLORS["yellow"], 
            self.COLORS["green"],
            self.COLORS["cyan"], 
            self.COLORS["blue"], 
            self.COLORS["magenta"]
        ]
        rainbow_text = ""
        for i, char in enumerate(message):
            color = rainbow_colors[i % len(rainbow_colors)]
            rainbow_text += self.decorate([color], char)
        print(rainbow_text)

    def print_warning(self, message):
        style = [self.BOLD, self.BLINKING, self.COLORS["red"]]
        warning_message = "WARNING: " + message
        print(self.decorate(style, warning_message))