import pokebase as pb
import tkinter as tk
import tkinter.messagebox
from io import BytesIO
from urllib3 import *
from PIL import Image,ImageTk
window = tk.Tk()
window.geometry("1000x800")
frame = tk.Frame(window)
frame.pack

var = tk.BooleanVar()
var2= tk.BooleanVar()
var3= tk.BooleanVar()

def onclick():   #Fonction du boutton

    Pokemon = entry.get()  #Récupération de l'id
    Type = type(Pokemon)
    if Type != int:
        try:
            Pokemon = int(Pokemon)  #Changement en int
        except:
            Pokemon = str(Pokemon)  #Changement en str

    
    #try:
    pokemon = pb.pokemon(Pokemon)  #La variable récupere les informations du pokemon choisit

    if var.get() == True and var2.get() == True:
        tkinter.messagebox.showwarning("Trop d'images","Tu ne peux pas mettre plusieurs images en même temps")
        Image1 = pb.SpriteResource('pokemon', Pokemon,front_default=True).url
    elif var.get() == True:
        Image1 = pb.SpriteResource('pokemon', Pokemon,front_default=True).url #La variable récupere les images du pokémon choisit
    elif var2.get() == True:
        Image1 = pb.SpriteResource('pokemon', Pokemon,front= True,shiny=True).url  #La variable récupere les images du pokémon choisit
        print(Image1.url)
    elif var3.get() == True:
        #Image1 = pb.SpriteResource('pokemon', Pokemon,other= True,showdown=True)
        #print(Image1.url)
        #Image1 = pokemon.other_sprites.get('showdown').front.get('shiny')
        Image1 = f"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/showdown/{Pokemon}.gif"
    else:
        tkinter.messagebox.showwarning("Aucune images","Tu ne peux pas ne pas mettre d'images")
        Image1 = pb.SpriteResource('pokemon', Pokemon,front_default=True).url

    http = PoolManager()
    response = http.request('GET',Image1)
    print(Image1)
    image = Image.open(BytesIO(response.data))
    global img
    img = ImageTk.PhotoImage(image.resize((300,300)))
    #pokemon_image.config(image = img)
#   pokemon_image.image = img
    #photo = tk.PhotoImage(file=Image1.path) #Récupère l'image du pokemon choisit via son chemin d'accès
    #global photoUp #Rend la variable global pour ne pas que l'image disparaisse
    #photoUp = img.zoom(3,3)   #Récupération et agrandissement de l'image choisit
    pokemonName.config(text = pokemon.name)  #Changement du titre pour le nom du pokemon
    pokemonName.place(x=75,y=85)
    pokemonUrl.config(image = img)  #Changement de l'image pour l'image du pokemon choisi
    pokemonInfo.config(text ="Hp : " + str(pokemon.stats[0].base_stat) + "\n" + "Type : " + pokemon.types[0].type.name + "\n" + " Hauteur : " + str(pokemon.height/10) + " metres")
    pokemonInfo.place(x=65,y=150)
    button.place(x=250,y=275)
    check.place(x=65,y= 250)
    check2.place(x=65,y=300)
    check3.place(x=65,y=350)
    entry.place(x=65,y=400)
    def color(clr):
        window.configure(background=clr)
        button.configure(background=clr)
        entry.configure(background=clr)
        check.configure(backgroun=clr)
        check2.configure(backgroun=clr)
        check3.configure(backgroun=clr)
        pokemonInfo.configure(backgroun=clr)
        pokemonName.configure(backgroun=clr)
    if pokemon.types[0].type.name == "grass":
        color('#0ee89c')
        
    elif pokemon.types[0].type.name == "fire":
        color('#0ee89c')
    elif pokemon.types[0].type.name == "water":
        color('#0ee89c')
    elif pokemon.types[0].type.name == "electric":
        color('#0ee89c')
    else:
        color('SystemButtonFace')
        

    #except:
        #tkinter.messagebox.showwarning("Pokemon introuvable",f"Le pokemon ou l'id {Pokemon} n'existe pas.")
    
    #tmpl.config(image = Tmpl)
    pokemonUrl.place(x = 600,y = 300)
    

#Tmpl = tk.PhotoImage(file="Tmpl.png")
#Tmpl = Tmpl.subsample(2,2)
#Tmpl = Tmpl.resize((window.winfo_width(),window.winfo_height()),PIL.Image.ANTIALIAS)
#tmpl = tk.Label(window,image = "")
#tmpl.place(x=0,y=0)
#tmpl.pack()

Fond = tk.PhotoImage(file="Pokemon.png")
Fond1 = Fond.subsample(2,2)  #Logo pokemon

pokemonName = tk.Label(window,text = "Nom du pokemon", font=("Arial",40))
pokemonName.pack(pady=50,padx=50)  #Nom du pokemon

pokemonUrl = tk.Label(window,image = Fond1)
pokemonUrl.pack(pady=5,padx=5)   #Emplacement de l'image

pokemonInfo = tk.Label(window,font=("Arial",16))
pokemonInfo.pack(pady=1,padx=1)

button = tk.Button(window, text="click",command=onclick, font=("ARIAL",16))
button.pack(pady=50,padx=50)     #Boutton

check = tk.Checkbutton(window,text = "Front default",font=("Arial"),variable=var)
check.pack(pady=1,padx=1)
check2 = tk.Checkbutton(window,text = "Shiny default",font=("Arial"),variable=var2)
check2.pack(pady=1,padx=1)
check3 = tk.Checkbutton(window,text = "gif front default",font=("Arial"),variable=var3)
check3.pack(pady=1,padx=1)

entry = tk.Entry(window , font=("Arial",16))
entry.pack(pady=25,padx=25)    #Entrée


tk.mainloop()
