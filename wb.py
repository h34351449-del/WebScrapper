#!/usr/bin/env python3
import sys
import urllib.request
import urllib.error
from urllib.parse import urlparse

class WB:
    def __init__(self):
        self.target_url = None
        self.html_content = None
    
    def banner(self):
        print("\n" + "="*50)
        print("  WB - WebScrapper v0.1")
        print("="*50 + "\n")
    
    def fetch(self, url):
        try:
            print(f"[*] Fetching: {url}")
            headers = {'User-Agent': 'Mozilla/5.0'}
            req = urllib.request.Request(url, headers=headers)
            response = urllib.request.urlopen(req, timeout=10)
            self.html_content = response.read().decode('utf-8', errors='ignore')
            print(f"[+] Success! Size: {len(self.html_content)} bytes\n")
            return True
        except Exception as e:
            print(f"[-] Error: {e}\n")
            return False
    
    def show_html(self, lines=30):
        if not self.html_content:
            print("[-] No HTML fetched yet\n")
            return
        html_lines = self.html_content.split('\n')
        for i, line in enumerate(html_lines[:lines], 1):
            print(f"{i} | {line}")
        print(f"\n[*] Total lines: {len(html_lines)}\n")
    
    def save(self, filename="output.html"):
        if not self.html_content:
            print("[-] No HTML to save\n")
            return
        with open(filename, 'w') as f:
            f.write(self.html_content)
        print(f"[+] Saved to: {filename}\n")
    
    def menu(self):
        print("Commands:")
        print("  fetch <url>  - Fetch HTML")
        print("  show [N]     - Show HTML (N lines)")
        print("  save [file]  - Save HTML")
        print("  help         - Show this menu")
        print("  exit         - Quit\n")
    
    def run(self):
        self.banner()
        self.menu()
        
        while True:
            try:
                cmd = input("WB> ").strip()
                
                if not cmd:
                    continue
                
                parts = cmd.split(' ', 1)
                command = parts[0].lower()
                arg = parts[1] if len(parts) > 1 else None
                
                if command == "fetch" and arg:
                    self.fetch(arg)
                elif command == "show":
                    lines = int(arg) if arg else 30
                    self.show_html(lines)
                elif command == "save":
                    self.save(arg if arg else "output.html")
                elif command == "help":
                    self.menu()
                elif command == "exit":
                    print("[*] Goodbye!\n")
                    break
                else:
                    print("[-] Unknown command\n")
            
            except KeyboardInterrupt:
                print("\n[!] Interrupted\n")
                break
            except Exception as e:
                print(f"[-] Error: {e}\n")

if __name__ == "__main__":
    wb = WB()
    wb.run()
#then press ctrl + o then enter then ctrl + x and type "chmod +x wb.py