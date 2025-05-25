# Numpad Right Click Mapper

This Python script maps the **numpad decimal (.)** key to perform a right mouse click.  
It uses the `keyboard` and `pynput` libraries to listen for key events and control mouse actions.

---

## ✨ Features

- Press **numpad . (decimal)** → triggers a right-click.
- Runs silently in the background.
- Press **Esc** → cleanly exits the script.

---

## 🛠 Requirements

- Python 3.x
- Python packages:
  - `keyboard`
  - `pynput`

Install the required packages using:

```bash
pip install keyboard pynput
````

⚠ **Important:**
On some systems (especially Windows or Linux), you may need to run the script as **administrator/root** because it listens to global keyboard events.

---

## 🚀 Usage

1. Clone or download this repository.
2. Run the script:

```bash
python numpad_right_click.py
```

3. Press the **numpad .** key to perform right-clicks.
4. Press **Esc** to stop the script.

---

## 📂 Code Overview

* **`keyboard.hook_key('decimal', on_numpad_dot)`**: Hooks into the numpad decimal key events.
* **`mouse.click(Button.right)`**: Executes a right-click action when the key is pressed.
* **`keyboard.wait('esc')`**: Waits until the Esc key is pressed to exit.

---

## 💡 Customization

Want to map a different key or mouse button?
You can modify the following in the script:

```python
keyboard.hook_key('your_key_here', on_numpad_dot)
mouse.click(Button.left)  # or Button.middle
```

Refer to the [`keyboard` documentation](https://github.com/boppreh/keyboard) and [`pynput` documentation](https://pynput.readthedocs.io/) for more customization.

---

## 📜 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## 🤝 Contributions

Feel free to open issues or submit pull requests for improvements!

```

---

If you want, I can also generate the actual **`LICENSE` file** or **GitHub Actions workflow** for Python linting or packaging. Want me to include those? Let me know! 🚀
```
