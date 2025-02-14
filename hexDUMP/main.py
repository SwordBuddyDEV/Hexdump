# / IMPORTS
import tkinter as tk
from tkinter import filedialog

# / CLASSES AND FUNCTIONS
class hexdumpLIB:
    def __init__(self):
        self.BYTES = ""

    # / GET USER FILE AND FORMAT HEX RESPONSE.
    def GET_FILE(self):
        # / GET FILE
        PATH = filedialog.askopenfilename(title="Hex a file.",filetypes=(("All files", "*.*"),))

        if PATH:
            with open(PATH, "rb") as f:
                self.BYTES = f.read()

            HEX_data = self.HEX_IT()
            HEXDUMP.delete('1.0', tk.END)

            # / FORMATTING
            for offset, hex, ascii in HEX_data:
                HEXDUMP.insert(tk.END, offset, "address")
                HEXDUMP.insert(tk.END, "  ")
                HEXDUMP.insert(tk.END, hex, "hex")
                HEXDUMP.insert(tk.END, "  |", "separator")
                HEXDUMP.insert(tk.END, ascii, "ascii")
                HEXDUMP.insert(tk.END, "|\n", "separator")

    # / MAIN HEX HANDLER
    def HEX_IT(self):
        if self.BYTES is None:
            return []

        LINES = []
        for i in range(0, len(self.BYTES), 16):
            CH=self.BYTES[i:i+16]
            offset = f"{i:08X}"

            #///////////////////////////////////////////////////////?
            #///////////////////////////////////////////////////////?
            f1 = ' '.join(f"{b:02X}" for b in CH[:8])
            f2 = ' '.join(f"{b:02X}" for b in CH[8:16])
            f1 = f1.ljust(23)
            f2 = f2.ljust(23)
            #///////////////////////////////////////////////////////?
            hex = f"{f1}  {f2}"
            ascii = ''.join(chr(b) if 32 <= b <= 126 else '.' for b in CH)
            #///////////////////////////////////////////////////////?
            #///////////////////////////////////////////////////////?

            LINES.append((offset, hex, ascii))

        return LINES

class tkinLIB:
    @staticmethod
    def WINDOW(TITLE, GEOMETRY):
        __NWINDOW__ = tk.Tk()
        __NWINDOW__.title(TITLE)
        __NWINDOW__.geometry(GEOMETRY)
        __NWINDOW__.configure(bg="#232323")
        return __NWINDOW__

    @staticmethod
    def BUTTON(TEXT, WINDOW, FUNC):
        __NBUTTON__ = tk.Button(WINDOW, text=TEXT, command=FUNC, bg="#444444", fg="white", activebackground="#555555", activeforeground="white")
        return __NBUTTON__

    @staticmethod
    def T_TEXT(WINDOW, WIDTH, HEIGHT):
        __NTEXT__ = tk.Text(WINDOW, width=WIDTH, height=HEIGHT, wrap=tk.NONE, font=("Consolas", 10), bg="#1e1e1e", fg="white", insertbackground="white", highlightbackground="#1e1e1e", selectbackground="#555555", selectforeground="white")
        return __NTEXT__

# / MAIN CODE

#///////////////////////////////////////////////////////?
ROOT = tkinLIB.WINDOW("HEXDUMP", "800x600")
#///////////////////////////////////////////////////////?
BT_OPEN = tkinLIB.BUTTON("OPEN FILE", ROOT, hexdumpLIB().GET_FILE)
BT_OPEN.pack(pady=0, padx=2.5, anchor="nw")
#///////////////////////////////////////////////////////?
#///////////////////////////////////////////////////////?
HEXDUMP = tkinLIB.T_TEXT(ROOT, 150, 50)
HEXDUMP.pack(expand=True,fill="both", padx=2.5, pady=2.5)
#///////////////////////////////////////////////////////?
#///////////////////////////////////////////////////////?
HEXDUMP.tag_config("address", foreground="#297f26")
HEXDUMP.tag_config("hex", foreground="#6daf6b")
HEXDUMP.tag_config("ascii", foreground="#58c954")
HEXDUMP.tag_config("separator", foreground="lightgray")
#///////////////////////////////////////////////////////?

ROOT.mainloop()
