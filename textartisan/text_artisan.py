banner = r"""
             ╔╦╗┌─┐─┐ ┬┌┬┐   ╔═╗┬─┐┌┬┐┬┌─┐┌─┐┌┐┌
              ║ ├┤ ┌┴┬┘ │    ╠═╣├┬┘ │ │└─┐├─┤│││
              ╩ └─┘┴ └─ ┴    ╩ ╩┴└─ ┴ ┴└─┘┴ ┴┘└┘          
+------------------------------------------------------------+
|                        TextArtisan                         |
|                      ===============                       |
|                Author : Prashant Bhandari                  |
+------------------------------------------------------------+
| The TextArtisan class is designed to facilitate the        |
| printing of colored and formatted text in Python terminal  |
| environments using ANSI escape codes. It provides methods  |
| to apply various text formatting styles and colors to text |
| strings.                                                   |
+------------------------------------------------------------+
|                        References                          |
|                       ============                         |
| [+] https://cwoebker.com/posts/ansi-escape-codes           |
| [+] https://www.nayab.xyz/linux/escapecodes                |
+------------------------------------------------------------+
"""

class TextArtisan(object):
    # +-------------------------------------------------+
    # |    Format : ESC[{attr1};{attr2};....{attrn)m    |
    # +-------------------------------------------------+

    ESCAPE = '\033[%sm'
    ENDC = ESCAPE % '0'
    
    # ---------------[ Text Formatting ]--------------
    REGULAR = '0'
    BOLD = '1'
    LOW_INTENSITY = '2' # Not widely supported
    ITALIC = '3'
    UNDERLINE = '4'
    BLINKING = '5'
    REVERSE = '6' # Not widely supported
    BACKGROUND = '7'
    INVISIBLE = '8'
    # ------------------------------------------------

    # -----------------[ Text Colors ]----------------
    COLORS = {
        'black': '30',
        'red': '31',
        'green': '32',
        'yellow': '33',
        'blue': '34',
        'magenta': '35',
        'cyan': '36',
        'white': '37'
    }
    # ------------------------------------------------

    # -------------[ Background Colors ]--------------
    BACKGROUND_COLORS = {
        'black': '40',
        'red': '41',
        'green': '42',
        'yellow': '43',
        'blue': '44',
        'magenta': '45',
        'cyan': '46',
        'white': '47'
    }
    # ------------------------------------------------

    def __init__(self):
        pass

    @staticmethod
    def decorate(styleformat, message):
        """
        ======================================================================
        Apply the specified formatting to the message using ANSI escape codes.
        ======================================================================

        Args:
            styleformat (list): List of formatting attributes.
            message (str): The message to be formatted.

        Returns:
            str: The formatted message.
        """
        formatstring = ';'.join(styleformat)
        format_sequence = TextArtisan.ESCAPE % formatstring
        return f"{format_sequence}{message}{TextArtisan.ENDC}"
    
    @staticmethod
    def colorize(text, color , bgcolor):
        """
        ==============================================================
        Apply the specified color to the text using ANSI escape codes.
        ==============================================================

        Args:
            text (str): The text to be colorized.
            color (str): The color to apply to the text.
            bgcolor (str): The color to apply to the background.

        Returns:
            str: The colorized text.
        """
        return TextArtisan.decorate([TextArtisan.COLORS[color],TextArtisan.BACKGROUND_COLORS[bgcolor]], text)

    @staticmethod
    def underline(text):
        """
        ==========================================================
        Apply underline style to the text using ANSI escape codes.
        ==========================================================

        Args:
            text (str): The text to be underlined.

        Returns:
            str: The underlined text.
        """
        return TextArtisan.decorate([TextArtisan.UNDERLINE], text)
    
    @staticmethod
    def blink(text):
        """
        =========================================================
        Apply blinking style to the text using ANSI escape codes.
        =========================================================

        Args:
            text (str): The text to be formatted.

        Returns:
            str: The formatted text with blinking effect.
        """
        return TextArtisan.decorate([TextArtisan.BLINKING], text)
    
    @staticmethod
    def bold(text):
        """
        =====================================================
        Apply bold style to the text using ANSI escape codes.
        =====================================================

        Args:
            text (str): The text to be formatted.

        Returns:
            str: The formatted text with bold style.
        """
        return TextArtisan.decorate([TextArtisan.BOLD], text)

    @staticmethod
    def italic(text):
        """
        =======================================================
        Apply italic style to the text using ANSI escape codes.
        =======================================================

        Args:
            text (str): The text to be formatted.

        Returns:
            str: The formatted text with italic style.
        """
        return TextArtisan.decorate([TextArtisan.ITALIC], text)

    @staticmethod
    def reverse(text):
        """
        ========================================================
        Apply reverse style to the text using ANSI escape codes.
        ========================================================

        Args:
            text (str): The text to be formatted.

        Returns:
            str: The formatted text with reverse style.
        """
        return TextArtisan.decorate([TextArtisan.REVERSE], text)

    @staticmethod
    def invisible(text):
        """
        ==========================================================
        Apply invisible style to the text using ANSI escape codes.
        ==========================================================

        Args:
            text (str): The text to be formatted.

        Returns:
            str: The formatted text with invisible style.
        """
        return TextArtisan.decorate([TextArtisan.INVISIBLE], text)
    
if __name__ == "__main__":
    printer = TextArtisan()
    print(printer.decorate([printer.BOLD, printer.COLORS["green"]], banner))