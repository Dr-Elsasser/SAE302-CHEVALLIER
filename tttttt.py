import tkinter as tk
from tkinter import messagebox
import paramiko

def connect():
    hostname = host_entry.get()
    username = user_entry.get()
    password = pass_entry.get()
    
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname, username=username, password=password)
        messagebox.showinfo("Info", "Connexion réussie!")
    except paramiko.ssh_exception.AuthenticationException:
        messagebox.showerror("Erreur", "Nom d'utilisateur ou mot de passe incorrect")
    except paramiko.ssh_exception.SSHException as e:
        messagebox.showerror("Erreur", e)

root = tk.Tk()
root.title("Connexion SSH")

host_label = tk.Label(root, text="Adresse hôte")
host_label.grid(row=0, column=0)
host_entry = tk.Entry(root)
host_entry.grid(row=0, column=1)

user_label = tk.Label(root, text="Nom d'utilisateur")
user_label.grid(row=1, column=0)
user_entry = tk.Entry(root)
user_entry.grid(row=1, column=1)

pass_label = tk.Label(root, text="Mot de passe")
pass_label.grid(row=2, column=0)
pass_entry = tk.Entry(root, show="*")
pass_entry.grid(row=2, column=1)

connect_button = tk.Button(root, text="Se connecter", command=connect)
connect_button.grid(row=3, column=1)

root.mainloop()