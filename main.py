import tkinter as tk
from tkinter import ttk
from tkinter.scrolledtext import ScrolledText
import os,sys
from PIL import Image, ImageTk
from pathlib import Path

# App: RoyalManager - Termux Packages Manager 
# Creator: Raunak Raj 
# Version: 1.1(beta)

print('''
App: RoyalManager
Creator: Raunak Raj
Version: 1.1(beta)

''')

ASSETS_PATH = Path(__file__).resolve().parent / "assets"

class aboutApp(tk.Tk):
    def __init__(self):
        super().__init__()
        
        #window setup
        self.geometry('280x320')
        self.title('About RoyalManager')
        self.resizable(False, False)
        self.config(bg="#fff")
        self.style = ttk.Style(self)
        
        self.style.configure(
            'label1.TLabel',
            background="#fff",
            foreground="#000",
            font=("Tahoma Bold",20)
            )
        self.style.configure(
            'label2.TLabel',
            background="#fff",
            foreground="#000",
            font=("Tahoma Bold",9)
            )
        self.style.configure(
            'aboutxt.TLabel',
            background="#fff",
            foreground="#1f1f1f",
            font=("Tahoma",11)
            )
        self.style.configure(
            'copyrightxt.TLabel',
            background="#313131",
            foreground="#fff",
            font=("Tahoma Bold",11)
            )
        
        self.add_logo_img()
        
        self.label1 = ttk.Label(self,text="RoyalManager",style="label1.TLabel",justify=tk.CENTER)
        self.label1.pack(side="top")
        
        self.label2 = ttk.Label(self,text="Version: 1.1(beta)",style="label2.TLabel",justify=tk.CENTER)
        self.label2.pack()
        
        self.abtxt = '''
GUI based termux packages 
manager for termux desktop,
developed by Raunak Raj.
        '''
        self.aboutxt = ttk.Label(self,text=self.abtxt,style="aboutxt.TLabel",justify=tk.CENTER)
        self.aboutxt.pack(padx=5,pady=5)
        
        self.copyrightxt = ttk.Label(self,text="Copyright © 2022 Raunak Raj",style="copyrightxt.TLabel",justify=tk.CENTER)
        self.copyrightxt.pack(side="bottom",anchor="s",pady=5,padx=5)
        
        
    def add_logo_img(self):
        self.canvas1 = tk.Canvas(self, width = 150, height = 135,background="#fff",bd=0,highlightthickness=0)  
        self.canvas1.pack()  
        self.img1 = ImageTk.PhotoImage(Image.open(ASSETS_PATH / "img2.png"),master=self.canvas1)  
        self.canvas1.create_image(75, 67, image=self.img1)

class MainApp(tk.Tk):
    def __init__(self):
        super().__init__()
        
        #window setup
        self.geometry('300x285')
        self.title('RoyalManager')
        self.resizable(False, False)
        self.logo = ImageTk.PhotoImage(Image.open(ASSETS_PATH / "app_icon.png"))
        self.iconphoto(False, self.logo)
        
        self.style = ttk.Style(self)
        self.style.configure(
            'Inp1.TEntry',
            fieldbackground="#fff",
            foreground="#000",
            borderwidth=1,
            font=("Verdana",18)
        )
        self.style.configure(
            'Search_btn.TButton',
            background="#56e8e8",
            foreground="#fff",
            borderwidth=1,
            font=("Verdana",12),
            focusthickness=3,
            focuscolor="none"
            )
        self.style.map('Search_btn.TButton', background=[('active','#86f7f7')])
        
        self.style.configure(
            'inst_btn.TButton',
            background="#0dd51e",
            foreground="#fff",
            borderwidth=1,
            font=("Verdana",12),
            focusthickness=3,
            focuscolor="none"
            )
        self.style.map('inst_btn.TButton', background=[('active','#51f55f')])
        
        self.style.configure(
            'uninst_btn.TButton',
            background="#fe0000",
            foreground="#fff",
            borderwidth=1,
            font=("Verdana",12),
            focusthickness=3,
            focuscolor="none"
            )
        self.style.map('uninst_btn.TButton', background=[('active','#f55c5c')])
        
        # menubar
        menubar = tk.Menu(
            self,
            bg="#090909",
            fg="#fff",
            activebackground="#242424",
            activeforeground="#fff",
            borderwidth=0,
            activeborderwidth=0,
            font=("Tahoma",12)
            )
        self.config(menu=menubar,bg="#fff")
        
        # action menu
        action_menu = tk.Menu(menubar,tearoff=0,bg="#090909",fg="#fff",activebackground="#242424",activeforeground="#fff",borderwidth=0,activeborderwidth=0,font=("Tahoma",12))
        
        # menu items of Action menu
        action_menu.add_command(label='Update Mirrors',command=self.update_mirrors)
        action_menu.add_command(label='Upgrade Packages',command=self.upgrade_pkg)
        action_menu.add_command(label='Clean Cache',command=self.clean_cache)
        action_menu.add_command(label='Autoremove Cache Packages',command=self.autorm_cache_pkg)
        action_menu.add_separator()
        
        # Exit menu item
        action_menu.add_command(label='Exit',command=self.destroy)
        
        menubar.add_cascade(label="Actions",menu = action_menu)
        
        # help menu
        help_menu = tk.Menu(menubar,tearoff=0,bg="#090909",fg="#fff",activebackground="#242424",activeforeground="#fff",borderwidth=0,activeborderwidth=0,font=("Tahoma",13))
        
        self.abouticon = ImageTk.PhotoImage(Image.open(ASSETS_PATH / "about.png"))
        
        # menu items of Help menu
        help_menu.add_command(label='About',image=self.abouticon,compound="left",command=self.about)
        
        menubar.add_cascade(label="Help",menu=help_menu)
        # main label
        main_label = ttk.Label(
            self,
            text="Welcome to Pkg Manager",
            background="#fff",
            foreground="#000",
            font=("Verdana", '15')
            )
        main_label.place(x=20,y=7)
        
        # entry box
        self.pkg_nme_var = tk.StringVar()
        pkg_nme = ttk.Entry(self,style="Inp1.TEntry",textvar=self.pkg_nme_var)
        pkg_nme.place(x=15,y=47,height=25)
        pkg_nme.insert(0, "Enter package name...")
        
        filter_btn = ttk.Button(self,text="Search",style="Search_btn.TButton",command=self.search_pkg)
        filter_btn.place(x=188,y=45)
        
        self.terminal_area = ScrolledText(self,state="disabled",height=10,width=35,bg="black",fg="#08c614",insertbackground="#08c614",selectbackground="#fff")
        self.terminal_area.place(x=15,y=85)
        
        self.install_btn = ttk.Button(self,text="Install",style="inst_btn.TButton",command=self.install_pkg)
        self.install_btn.place_forget()
        
        self.uninstall_btn = ttk.Button(self,text="Uninstall",style="uninst_btn.TButton",command=self.uninstall_pkg)
        self.uninstall_btn.place_forget()
    
    def update_mirrors(self):
        cmd = "apt-get update"
        p = os.popen(cmd)
        self.terminal_area["state"] = "normal"
        self.terminal_area.delete(0.1,"end")
        self.terminal_area.insert("end",p.read())
        self.terminal_area.see("end")
        self.terminal_area["state"] = "disabled"
        
    
    def upgrade_pkg(self):
        cmd="apt-get upgrade -y"
        p = os.popen(cmd)
        self.terminal_area["state"] = "normal"
        self.terminal_area.delete(0.1,"end")
        self.terminal_area.insert("end",p.read())
        self.terminal_area.see("end")
        self.terminal_area["state"] = "disabled"
        
    def clean_cache(self):
        cmd='apt-get clean && apt-get autoclean'
        p = os.popen(cmd)
        self.terminal_area["state"] = "normal"
        self.terminal_area.delete(0.1,"end")
        self.terminal_area.insert("end",p.read())
        self.terminal_area.see("end")
        self.terminal_area["state"] = "disabled"
        
    def autorm_cache_pkg(self):
        cmd="apt-get autoremove -y"
        p = os.popen(cmd)
        self.terminal_area["state"] = "normal"
        self.terminal_area.delete(0.1,"end")
        self.terminal_area.insert("end",p.read())
        self.terminal_area.see("end")
        self.terminal_area["state"] = "disabled"
        
    def search_pkg(self):
        rest_keyword=["ls","la"]
        if self.pkg_nme_var.get() in rest_keyword:
            showwarning("Bad Pkg Name","Please enter correct package name, not any command.")
        else:
            cmd=f"apt show {self.pkg_nme_var.get()}"
            p = os.popen(cmd)
            p1 = os.popen("pkg list-installed").read()
            output = p.read()
            
            if self.pkg_nme_var.get() in p1:
                print(output)
                self.uninstall_btn.place_forget()
                self.terminal_area["state"] = "normal"
                self.terminal_area.delete(0.1,"end")
                self.terminal_area.insert("end",output)
                self.terminal_area.see("end")
                self.terminal_area["state"] = "disabled"
                self.uninstall_btn.place(x=20,y=250)
            elif self.pkg_nme_var.get() not in p1:
                if output == '':
                    print(f"\n\nNo any package with name : {self.pkg_nme_var.get()}")
                    self.uninstall_btn.place_forget()
                    self.install_btn.place_forget()
                    self.terminal_area["state"] = "normal"
                    self.terminal_area.delete(0.1,"end")
                    self.terminal_area.insert("end",f"No any package with name : {self.pkg_nme_var.get()}")
                    self.terminal_area.see("end")
                    self.terminal_area["state"] = "disabled"
                else:
                    print(output)
                    self.uninstall_btn.place_forget()
                    self.terminal_area["state"] = "normal"
                    self.terminal_area.delete(0.1,"end")
                    self.terminal_area.insert("end",output)
                    self.terminal_area.see("end")
                    self.terminal_area["state"] = "disabled"
                    self.install_btn.place(x=20,y=250)
    
    def install_pkg(self):
        cmd = f"apt install -y {self.pkg_nme_var.get()}"
        p = os.popen(cmd)
        output = p.read()
        self.terminal_area["state"] = "normal"
        self.terminal_area.delete(0.1,"end")
        self.terminal_area.insert("end",output)
        self.terminal_area.see("end")
        self.terminal_area["state"] = "disabled"
        self.install_btn.place_forget()
        self.uninstall_btn.place(x=20,y=250)
    
    def uninstall_pkg(self):
        cmd = f"apt purge -y {self.pkg_nme_var.get()}"
        p = os.popen(cmd)
        output = p.read()
        self.terminal_area["state"] = "normal"
        self.terminal_area.delete(0.1,"end")
        self.terminal_area.insert("end",output)
        self.terminal_area.see("end")
        self.terminal_area["state"] = "disabled"
        self.uninstall_btn.place_forget()
        self.install_btn.place(x=20,y=250)
        
    def about(self):
        aboutapp = aboutApp()
        aboutapp.mainloop

if __name__ == "__main__":
    app = MainApp()
    app.mainloop() 