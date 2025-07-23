import os
import subprocess
import tkinter as tk
from tkinter import filedialog, messagebox, Menu

class PDFCompressorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Compresor PDF")

        # Variables
        self.pdf_file = ""
        self.output_file = ""
        self.compression_level = "ebook"

        # Idiomas disponibles
        self.languages = {
            "es": "Español",
            "gl": "Galego",
            "fr": "Français",
            "de": "Deutsch",
            "pt": "Português",
            "it": "Italiano",
            "en": "English"
        }
        self.current_language = tk.StringVar(value="es")
        self.translations = {
            "es": {
                "select_pdf": "Seleccionar PDF",
                "compress_pdf": "Comprimir PDF",
                "pdf_selected": "PDF seleccionado",
                "file_selected": "Se ha seleccionado el archivo: ",
                "check_tools": "Chequeo de Herramientas",
                "no_gs": "No se ha localizado la herramienta Ghostscript (gs). Debe instalarla para poder usar este programa.",
                "no_gm": "No se ha localizado la herramienta GraphicsMagick (gm). Debe instalarla para la compresión máxima.",
                "error_pdf": "Error - Fichero PDF",
                "select_pdf_error": "Debe de seleccionar un fichero PDF",
                "compression_done": "Compresión Finalizada",
                "compression_success": "Se ha comprimido el fichero PDF. Lo puede encontrar en: ",
                "compression_fail": "La compresión ha fallado. Por favor, intente de nuevo."
            },
            "gl": {
                "select_pdf": "Seleccionar PDF",
                "compress_pdf": "Comprimir PDF",
                "pdf_selected": "PDF seleccionado",
                "file_selected": "Seleccionouse o arquivo: ",
                "check_tools": "Verificación de Ferramentas",
                "no_gs": "Non se localizou a ferramenta Ghostscript (gs). Debe instalala para poder usar este programa.",
                "no_gm": "Non se localizou a ferramenta GraphicsMagick (gm). Debe instalala para a máxima compresión.",
                "error_pdf": "Erro - Ficheiro PDF",
                "select_pdf_error": "Debe seleccionar un ficheiro PDF",
                "compression_done": "Compresión Rematada",
                "compression_success": "Comprimíuse o ficheiro PDF. Pode atopalo en: ",
                "compression_fail": "A compresión fallou. Por favor, inténteo de novo."
            },
            "fr": {
                "select_pdf": "Sélectionner un PDF",
                "compress_pdf": "Compresser PDF",
                "pdf_selected": "PDF sélectionné",
                "file_selected": "Fichier sélectionné : ",
                "check_tools": "Vérification des Outils",
                "no_gs": "L'outil Ghostscript (gs) n'a pas été trouvé. Vous devez l'installer pour utiliser ce programme.",
                "no_gm": "L'outil GraphicsMagick (gm) n'a pas été trouvé. Vous devez l'installer pour une compression maximale.",
                "error_pdf": "Erreur - Fichier PDF",
                "select_pdf_error": "Vous devez sélectionner un fichier PDF",
                "compression_done": "Compression Terminée",
                "compression_success": "Le fichier PDF a été compressé. Vous pouvez le trouver à : ",
                "compression_fail": "La compression a échoué. Veuillez réessayer."
            },
            "de": {
                "select_pdf": "PDF auswählen",
                "compress_pdf": "PDF komprimieren",
                "pdf_selected": "PDF ausgewählt",
                "file_selected": "Datei ausgewählt: ",
                "check_tools": "Werkzeugprüfung",
                "no_gs": "Ghostscript (gs) nicht gefunden. Bitte installieren Sie es, um dieses Programm zu verwenden.",
                "no_gm": "GraphicsMagick (gm) nicht gefunden. Bitte installieren Sie es für maximale Komprimierung.",
                "error_pdf": "Fehler - PDF-Datei",
                "select_pdf_error": "Sie müssen eine PDF-Datei auswählen",
                "compression_done": "Komprimierung abgeschlossen",
                "compression_success": "Die PDF-Datei wurde komprimiert. Sie finden sie unter: ",
                "compression_fail": "Komprimierung fehlgeschlagen. Bitte versuchen Sie es erneut."
            },
            "pt": {
                "select_pdf": "Selecionar PDF",
                "compress_pdf": "Comprimir PDF",
                "pdf_selected": "PDF selecionado",
                "file_selected": "Arquivo selecionado: ",
                "check_tools": "Verificação de Ferramentas",
                "no_gs": "A ferramenta Ghostscript (gs) não foi encontrada. Você deve instalá-la para usar este programa.",
                "no_gm": "A ferramenta GraphicsMagick (gm) não foi encontrada. Você deve instalá-la para a compressão máxima.",
                "error_pdf": "Erro - Arquivo PDF",
                "select_pdf_error": "Você deve selecionar um arquivo PDF",
                "compression_done": "Compressão Finalizada",
                "compression_success": "O arquivo PDF foi comprimido. Você pode encontrá-lo em: ",
                "compression_fail": "A compressão falhou. Por favor, tente novamente."
            },
            "it": {
                "select_pdf": "Seleziona PDF",
                "compress_pdf": "Comprimi PDF",
                "pdf_selected": "PDF selezionato",
                "file_selected": "File selezionato: ",
                "check_tools": "Controllo degli Strumenti",
                "no_gs": "Lo strumento Ghostscript (gs) non è stato trovato. È necessario installarlo per utilizzare questo programma.",
                "no_gm": "Lo strumento GraphicsMagick (gm) non è stato trovato. È necessario installarlo per la massima compressione.",
                "error_pdf": "Errore - File PDF",
                "select_pdf_error": "Devi selezionare un file PDF",
                "compression_done": "Compressione Completata",
                "compression_success": "Il file PDF è stato compresso. Puoi trovarlo in: ",
                "compression_fail": "La compressione è fallita. Per favore riprova."
            },
            "en": {
                "select_pdf": "Select PDF",
                "compress_pdf": "Compress PDF",
                "pdf_selected": "PDF Selected",
                "file_selected": "File selected: ",
                "check_tools": "Tool Check",
                "no_gs": "Ghostscript (gs) not found. Please install it to use this program.",
                "no_gm": "GraphicsMagick (gm) not found. Please install it for maximum compression.",
                "error_pdf": "Error - PDF File",
                "select_pdf_error": "You must select a PDF file",
                "compression_done": "Compression Finished",
                "compression_success": "The PDF file has been compressed. You can find it at: ",
                "compression_fail": "Compression failed. Please try again."
            }
        }

        # Menú de idioma
        self.create_language_menu()

        # UI Setup
        self.create_widgets()

        # Check Tools
        self.check_tools()

    def create_language_menu(self):
        menubar = Menu(self.root, bg="white", fg="black")
        language_menu = Menu(menubar, tearoff=0, bg="white", fg="black")
        for lang_code, lang_name in self.languages.items():
            language_menu.add_radiobutton(label=lang_name, variable=self.current_language, value=lang_code, command=self.update_language)
        menubar.add_cascade(label="Idioma", menu=language_menu)
        self.root.config(menu=menubar)

    def update_language(self):
        lang = self.current_language.get()
        self.select_pdf_button.config(text=self.translations[lang]["select_pdf"])
        self.compress_button.config(text=self.translations[lang]["compress_pdf"])

    def create_widgets(self):
        title_frame = tk.Frame(self.root)
        title_frame.pack(pady=10, padx=10)

        title_label = tk.Label(title_frame, text="Compresor PDF", font=("Helvetica", 16))
        title_label.pack()

        subtitle_label = tk.Label(title_frame, text="(c) Charlie Martínez - Quirinux, GPLv2", font=("Helvetica", 10))
        subtitle_label.pack(pady=(5, 10), padx=10)

        self.select_pdf_button = tk.Button(self.root, text="Seleccionar PDF", command=self.select_pdf)
        self.select_pdf_button.pack(pady=10)

        self.compress_button = tk.Button(self.root, text="Comprimir PDF", command=self.compress_pdf)
        self.compress_button.pack(pady=10)

    def select_pdf(self):
        lang = self.current_language.get()
        desktop_path = os.path.join(os.path.expanduser("~"), "Escritorio")
        self.pdf_file = filedialog.askopenfilename(initialdir=desktop_path, filetypes=[("PDF files", "*.pdf")])
        if self.pdf_file:
            messagebox.showinfo(self.translations[lang]["pdf_selected"], self.translations[lang]["file_selected"] + self.pdf_file)

    def check_tools(self):
        gs_installed = subprocess.call(["which", "gs"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL) == 0
        lang = self.current_language.get()

        if not gs_installed:
            messagebox.showerror(self.translations[lang]["check_tools"], self.translations[lang]["no_gs"])
            self.compress_button.config(state="disabled")

    def compress_pdf(self):
        lang = self.current_language.get()
        if not self.pdf_file:
            messagebox.showerror(self.translations[lang]["error_pdf"], self.translations[lang]["select_pdf_error"])
            return

        self.output_file = os.path.splitext(self.pdf_file)[0] + "_comprimido.pdf"

        if os.path.exists(self.output_file):
            os.remove(self.output_file)

        cmd = [
            "gs",
            "-sDEVICE=pdfwrite",
            "-dCompatibilityLevel=1.4",
            "-dPDFSETTINGS=/ebook",
            "-dNOPAUSE",
            "-dQUIET",
            "-dBATCH",
            f"-sOutputFile={self.output_file}",
            self.pdf_file
        ]

        subprocess.run(cmd)

        if os.path.exists(self.output_file):
            messagebox.showinfo(self.translations[lang]["compression_done"], self.translations[lang]["compression_success"] + self.output_file)
        else:
            messagebox.showerror(self.translations[lang]["compression_fail"])

if __name__ == "__main__":
    root = tk.Tk()
    app = PDFCompressorApp(root)
    root.mainloop()
