# 🌌 Universal Code Organizer (UCO)

**The only code organizer built for *every* developer, *every* codebase, and *every* programming language in existence (even the ones that haven't been invented yet).**

Traditional code organizers fail because they either physically move your files (which destroys your import paths and crashes your app) or they rely on parsing language syntax (which means they break the second a new language or framework is invented).

**UCO does the impossible:** It doesn't parse complex syntax, it doesn't break your imports, and it doesn't require an internet connection or APIs. It simply scans your files for plain-text tags and generates a beautifully organized **Shadow Workspace** using live OS shortcuts (symlinks). 

Organize your code exactly how *you* want to see it, while keeping the actual files exactly where your compiler needs them to be.

---

## ✨ Why UCO is the Ultimate Solution

- ♾️ **100% Language Agnostic:** Works with Python, JavaScript, C++, Rust, Markdown, or a custom language invented in 2030. If a file has text in it, UCO can organize it.
- 🔗 **Zero Broken Imports:** UCO never physically moves your original files. It creates a mirrored directory of live OS shortcuts. Your app will never crash due to a broken relative path (like `import '../../utils.js'`).
- 💸 **Completely Free & No APIs:** Relies entirely on native Operating System file management. No subscriptions, no API keys, no tracking, and no internet connection required.
- 🛠️ **Zero Maintenance:** Built purely on standard built-in Python libraries. No `npm install`, no `pip install`. Native OS symlinking hasn't changed in 40 years, meaning this script will run identically today, tomorrow, and 10 years from now.
- 🧠 **Organize *Your* Way:** Group by feature, author, priority, or tech stack. You have total control over the folder structure based on what you type.

---

## 🚀 Quick Start Guide

### Step 1: Install (No Installation Required)
Simply drop the `uco.py` script into the root folder of your messy project. *(You only need Python 3 installed on your machine).*

### Step 2: Tag Your Code
Open any file and drop a comment anywhere near the top (UCO scans the first 50 lines by default). Type the `@UCO:` tag, followed by the folder path you want it to appear in. 

Because it reads raw text, it works with **any** comment syntax:

**In a JavaScript/TypeScript file:**
```javascript
// @UCO: 1_Frontend/Authentication/Hooks
export const useAuth = () => { ... }
```

**In a Python file:**
```python
# @UCO: 2_Backend/Database_Models
class User(Model):
    pass
```

**In a CSS file:**
```css
/* @UCO: 1_Frontend/Design_System/Buttons */
.btn-primary { ... }
```

**In a completely fake/future language (`.qbit`):**
```text
::: @UCO: 4_Future_Tech/Quantum_Logic
ENTANGLE(q1, q2);
```

### Step 3: Run UCO

Open your terminal, navigate to your project folder, and run the script:

```bash
python uco.py
```

### Step 4: Code in Peace

UCO will instantly generate a folder named `_UCO_Workspace_`. Inside, you will find your pristine, beautifully organized custom folder structure.

Because these are live OS shortcuts:

1.  **You open and edit the file inside `_UCO_Workspace_`**
2.  **The original messy file updates instantly in real-time.**

---

## 🤖 What about Untagged Files?

Don't want to tag every single file? No problem.
UCO has a smart **Future-Proof Auto-Grouping** fallback. If a file has no `@UCO:` tag, it is automatically grouped into logical folders based on its file extension (e.g., `JSON_Files/`, `MD_Files/`, `JS_Files/`).

---

## ⚙️ Configuration (`uco_config.json`)

The first time you run UCO, it generates a `uco_config.json` file in your root directory. You can edit this file to fully customize your experience:

- `workspace_dir`: Change the name of the generated Shadow Workspace folder.
- `tag_pattern`: Customize the tag syntax (Don't like `@UCO:`? Change it to `@Organize:` or whatever you want!).
- `ignore_folders`: Tell UCO which folders to skip entirely for lightning-fast speeds (defaults include `node_modules`, `.git`, and `venv`).
- `lines_to_scan`: How deep into a file UCO should look for your tags (Default: `50` lines).
- `custom_extension_rules`: Route specific file types automatically without needing tags (e.g., forcing all `*.md` and `*.txt` files into a `1_Docs/` folder).

---

## 🛑 Important Note for Windows Users

UCO uses Symlinks (shortcuts) to perform its magic. Windows sometimes requires "Developer Mode" to be turned on to create Symlinks natively without running your terminal as an Administrator.

- **To fix:** Open Windows Settings -> Search for "Developer Mode" -> Turn it On.
- *(Don't worry, if Symlinks are restricted, UCO is smart enough to automatically try to create Hardlinks or text pointer files as a safe fallback so the script never crashes!)*

---

*Built for developers who just want their code organized, without the headache.*

**WARNING THIS HAS NOT BEEN EXTENSIVELY TESTED**