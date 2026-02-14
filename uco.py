#!/usr/bin/env python3
import os
import re
import json
import fnmatch
import shutil
from pathlib import Path

CONFIG_FILE = "uco_config.json"

DEFAULT_CONFIG = {
    "_instructions": "Configure UCO here. Add '@UCO: Folder/Name' inside any file's comments to auto-route it!",
    "workspace_dir": "_UCO_Workspace_",
    "tag_pattern": "@UCO:\\s*([a-zA-Z0-9_/-]+)", 
    "lines_to_scan": 50,
    "ignore_folders": [".git", "node_modules", "venv", "env", ".venv", "__pycache__", "dist", "build", ".vscode", ".idea"],
    "ignore_files": ["uco_config.json", "uco.py"],
    "auto_group_untagged_by_extension": True,
    "custom_extension_rules": {
        "1_Docs": ["*.md", "*.txt"],
        "2_Configs": ["*.json", "*.yaml", "*.yml", "*.toml", "*.ini", "*.env", ".gitignore"]
    },
    "catch_all_folder": "Misc_Files"
}

def load_config():
    """Loads custom preferences, or generates them on first run."""
    if not os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, 'w') as f:
            json.dump(DEFAULT_CONFIG, f, indent=4)
        print(f"[+] Generated universal config: {CONFIG_FILE}")
        return DEFAULT_CONFIG
    with open(CONFIG_FILE, 'r') as f:
        return json.load(f)

def match_custom_rules(filename, rules):
    for folder, patterns in rules.items():
        for pattern in patterns:
            if fnmatch.fnmatch(filename.lower(), pattern.lower()):
                return folder
    return None

def extract_tag(filepath, pattern, lines_to_scan):
    """Safely reads the top lines of ANY file as raw text to find organization tags."""
    try:
        with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
            for _ in range(lines_to_scan):
                line = f.readline()
                if not line: break
                match = re.search(pattern, line, re.IGNORECASE)
                if match:
                    return match.group(1).strip()
    except Exception:
        pass # Silently skip binary files
    return None

def main():
    print("=== Universal Code Organizer (UCO) ===")
    config = load_config()
    
    root_dir = Path.cwd()
    workspace_name = config.get("workspace_dir", "_UCO_Workspace_")
    workspace_dir = root_dir / workspace_name
    
    ignore_folders = set(config.get("ignore_folders", []))
    ignore_folders.add(workspace_name)
    ignore_files = set(config.get("ignore_files", []))
    ignore_files.add(Path(__file__).name)
    
    if workspace_dir.exists():
        shutil.rmtree(workspace_dir)
    workspace_dir.mkdir()
    
    files_processed = 0
    tag_pattern = config.get("tag_pattern", "@UCO:\\s*([a-zA-Z0-9_/-]+)")
    lines_to_scan = config.get("lines_to_scan", 50)
    
    print("[*] Scanning and organizing codebase...")
    
    for dirpath, dirnames, filenames in os.walk(root_dir):
        # Filter ignored directories dynamically
        dirnames[:] = [d for d in dirnames if d not in ignore_folders and not d.startswith('.')]
        
        for file in filenames:
            if file in ignore_files:
                continue
                
            file_path = Path(dirpath) / file
            dest_folder = None
            
            # 1. Virtual Tag Routing (Overrides everything)
            tag = extract_tag(file_path, tag_pattern, lines_to_scan)
            if tag:
                dest_folder = tag
                
            # 2. Custom Extension Rules
            if not dest_folder:
                dest_folder = match_custom_rules(file, config.get("custom_extension_rules", {}))
                
            # 3. Future-Proof Auto-Grouping
            if not dest_folder and config.get("auto_group_untagged_by_extension", True):
                ext = file_path.suffix.lstrip('.').upper()
                dest_folder = f"{ext}_Files" if ext else config.get("catch_all_folder", "Misc_Files")
            elif not dest_folder:
                dest_folder = config.get("catch_all_folder", "Misc_Files")
                
            # Create target directory
            target_dir = workspace_dir / dest_folder
            target_dir.mkdir(parents=True, exist_ok=True)
            
            # Create Symlink
            target_link = target_dir / file
            counter = 1
            while target_link.exists():
                target_link = target_dir / f"{file_path.stem}_{counter}{file_path.suffix}"
                counter += 1
                
            try:
                os.symlink(file_path, target_link) # Create live OS shortcut
                files_processed += 1
            except OSError:
                try:
                    os.link(file_path, target_link) # Hardlink fallback for Windows
                    files_processed += 1
                except OSError:
                    with open(f"{target_link}.pointer.txt", "w") as f:
                        f.write(f"Original file located at: {file_path.resolve()}")
                    files_processed += 1

    print(f"[✓] Success! {files_processed} files dynamically organized into '{workspace_name}/'.")
    print("[✓] Your original codebase was NOT moved, so your code will compile and run perfectly.")

if __name__ == "__main__":
    main()