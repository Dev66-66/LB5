import tkinter as tk
from tkinter import filedialog, messagebox
from pathlib import Path


class NotesApp:
    def __init__(self, root: tk.Tk) -> None:
        self.root = root
        self.root.title("Заметки")
        self.root.geometry("700x500")

        self.current_path: Path | None = None

        self._build_ui()
        self._set_status("Готово")

    def _build_ui(self) -> None:
        toolbar = tk.Frame(self.root)
        toolbar.pack(fill=tk.X, padx=5, pady=5)

        tk.Button(
            toolbar, text="Новая", command=self.new_note
        ).pack(side=tk.LEFT, padx=3)
        tk.Button(
            toolbar, text="Открыть…", command=self.open_note
        ).pack(side=tk.LEFT, padx=3)
        tk.Button(
            toolbar, text="Сохранить", command=self.save_note
        ).pack(side=tk.LEFT, padx=3)

        self.status = tk.Label(toolbar, text="", anchor="w")
        self.status.pack(side=tk.RIGHT, fill=tk.X, expand=True, padx=5)

        text_frame = tk.Frame(self.root)
        text_frame.pack(fill=tk.BOTH, expand=True, padx=5, pady=(0, 5))

        self.text = tk.Text(text_frame, wrap=tk.WORD, undo=True)
        self.text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        scroll = tk.Scrollbar(text_frame, command=self.text.yview)
        scroll.pack(side=tk.RIGHT, fill=tk.Y)
        self.text.configure(yscrollcommand=scroll.set)

    def _set_status(self, msg: str) -> None:
        self.status.config(text=msg)

    def new_note(self) -> None:
        self.text.delete("1.0", tk.END)
        self.current_path = None
        self.root.title("Заметки — новая")
        self._set_status("Новая заметка")

    def open_note(self) -> None:
        path = filedialog.askopenfilename(
            title="Открыть файл",
            filetypes=[
                ("Текстовые файлы", "*.txt"),
                ("Все файлы", "*.*"),
            ],
        )
        if not path:
            return

        try:
            content = Path(path).read_text(encoding="utf-8")
        except OSError as err:
            messagebox.showerror("Ошибка", f"Не удалось открыть файл:\n{err}")
            return

        self.text.delete("1.0", tk.END)
        self.text.insert(tk.END, content)
        self.current_path = Path(path)
        self.root.title(f"Заметки — {self.current_path.name}")
        self._set_status(f"Открыто: {self.current_path}")

    def save_note(self) -> None:
        if self.current_path is None:
            path = filedialog.asksaveasfilename(
                defaultextension=".txt",
                filetypes=[("Текстовые файлы", "*.txt"), ("Все файлы", "*.*")],
                title="Сохранить",
            )
            if not path:
                return
            self.current_path = Path(path)
            self.root.title(f"Заметки — {self.current_path.name}")
            self._write(self.current_path)
        else:
            self._write(self.current_path)

    def _write(self, path: Path) -> None:
        try:
            path.write_text(self.text.get("1.0", tk.END), encoding="utf-8")
        except OSError as err:
            messagebox.showerror("Ошибка", f"Не удалось сохранить файл:\n{err}")
            return
        self._set_status(f"Сохранено: {path}")


if __name__ == "__main__":
    root = tk.Tk()
    NotesApp(root)
    root.mainloop()

