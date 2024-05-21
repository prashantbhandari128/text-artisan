# TextArtisan

Author: **Prashant Bhandari**

The `TextArtisan` class is designed to facilitate the printing of colored and formatted text in **Python** terminal environments using **ANSI** escape codes. It provides methods to apply various text formatting styles and colors to text strings.

---

## Class Overview

The `TextArtisan` class provides the following attributes and methods:

### Attributes

- `ESCAPE`: The escape sequence used to initiate color and formatting changes in the terminal.
- `ENDC`: The escape sequence used to reset the text formatting to default.

#### Text Formatting Attributes

- `REGULAR`: Regular text formatting.
- `BOLD`: Bold text formatting.
- `LOW_INTENSITY`: Low intensity text formatting (_not widely supported_).
- `ITALIC`: Italic text formatting.
- `UNDERLINE`: Underlined text formatting.
- `BLINKING`: Blinking text formatting.
- `REVERSE`: Reverse text formatting (_not widely supported_).
- `BACKGROUND`: Background text formatting.
- `INVISIBLE`: Invisible text formatting.

#### Text Color Attributes

- `COLORS`: A dictionary mapping color names to their respective ANSI color codes for foreground text.
    ```python
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
    ```
- `BACKGROUND_COLORS`: A dictionary mapping color names to their respective ANSI color codes for background text.
    ```python
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
    ```

### Methods

- `decorate(styleformat, message)`: Apply the specified formatting to the message using ANSI escape codes.

- `colorize(text, color, bgcolor)`: Apply the specified color to the text with a background color using ANSI escape codes.

- `underline(text)`: Apply underline style to the text using ANSI escape codes.

- `blink(text)`: Apply blinking style to the text using ANSI escape codes.

- `bold(text)`: Apply bold style to the text using ANSI escape codes.

- `italic(text)`: Apply italic style to the text using ANSI escape codes.

- `reverse(text)`: Apply reverse style to the text using ANSI escape codes.

- `invisible(text)`: Apply invisible style to the text using ANSI escape codes.

---

## Installation

No additional installation steps are necessary. Simply include the ``text_artisan.py`` file in your project.

## Usage

To use the `TextArtisan` class, follow these steps:

- ``Step 1`` : Import the `TextArtisan` class.
- ``Step 2`` : Create an instance of the `TextArtisan` class.
- ``Step 3`` : Use the `decorate` method to format and print text.

## Example

```python
from textartisan.text_artisan import TextArtisan

# Create an instance of TextArtisan
printer = TextArtisan()
# Format and print text
formatted_text = printer.decorate([printer.BOLD, printer.COLORS["red"]], "Hello, World!")
print(formatted_text)
```

> This will print the text "Hello, World!" in bold red color.

## Notes

- Ensure that your terminal supports **ANSI** escape codes for proper rendering of colored and formatted text.

- Experiment with different combinations of text formatting and colors to achieve the desired visual effect.

- Refer to the **ANSI** escape code documentation for more information on text formatting and color codes.

## References

- [Linux ANSI Escape Codes](https://www.embedded.pub/linux/misc/escape-codes.html)
- [ANSI Escape Codes](https://cwoebker.com/posts/ansi-escape-codes)