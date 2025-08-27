# Password Generator Project

This project is about creating a **Password Generator** using Python. It allows you to make passwords with numbers, letters, or both. We also improved the code to make it **stronger and safer**.

---

## ✅ What This Program Does
- Asks the user for password length.
- Asks what type of password:
  - `number` → only numbers.
  - `string` → only letters.
  - `both` → letters and numbers.
  - `strong` → letters + numbers + special characters.
- Generates a random password.
- Shows the password to the user.

---

## ✅ Changes We Made to Make It Better
1. **Added Special Characters Option**
   - Now we have `strong` option that includes symbols like `!@#$%^&*`.
2. **Strong Password Check**
   - If the user selects `strong`, the password must have:
     - At least one lowercase letter
     - At least one uppercase letter
     - At least one number
     - At least one special character
3. **Error Handling**
   - If the password length is too small (less than 4), show a message.
4. **Multiple Suggestions**
   - Show 5 different passwords so the user can choose one.
5. **Better Security**
   - Use `secrets` module instead of `random` for stronger security.
6. **Option to Copy Password**
   - We can copy the password to the clipboard using `pyperclip`.

---

## ✅ How to Make This Code
1. **Import modules**: `string`, `random` or `secrets`.
2. **Ask user for input**: length and type of password.
3. **Choose characters based on user choice**.
4. **Generate password using a loop**.
5. **Add checks for strong password**.
6. **Print the password or copy it to clipboard**.

---

## ✅ How to Run
1. Copy the code into a Python file.
2. Run it in the terminal or VS Code.
3. Enter the length and type when asked.
4. Choose one of the generated passwords.

---

This project teaches:
- **Python loops**
- **Conditions (if-else)**
- **Working with strings**
- **Random and secrets module**