

# --------------------------
# Confirm AI prediction
# --------------------------

print(f"\nAI detected your face shape as: {predicted_face_shape}") 

correct = input("Is this correct? (yes/no): ").lower() 

if correct == "no": 

    print("\nChoose your actual face shape:") 

    options = [
        "Heart",
        "Oblong",
        "Oval",
        "Round",
        "Square"
    ]

    for i, option in enumerate(options):
        print(f"{i+1}. {option}") 

    predicted_face_shape = options[int(input("Choice: ")) - 1] 


# --------------------------
# Hair Length
# --------------------------

print("\nCurrent Hair Length")

lengths = [
    "Short",
    "Medium",
    "Long"
]

for i,l in enumerate(lengths):
    print(f"{i+1}. {l}")

hair_length = lengths[int(input("Choice: "))-1]


# --------------------------
# Hair Texture
# --------------------------

print("\nHair Texture")

textures = [
    "Straight",
    "Wavy",
    "Curly",
    "Coily"
]

for i,t in enumerate(textures):
    print(f"{i+1}. {t}")

hair_texture = textures[int(input("Choice: "))-1]


# --------------------------
# Style
# --------------------------

print("\nPreferred Style")

styles = [
    "Masculine",
    "Feminine",
    "Neutral"
]

for i,s in enumerate(styles):
    print(f"{i+1}. {s}")

style = styles[int(input("Choice: "))-1]


# ============================================================
# HAIRSTYLE DATABASE
# ============================================================

hairstyles = {

"Oval":{

"good":[
"Textured Crop",
"Curtain Bangs",
"Wolf Cut",
"Layered Bob",
"French Bob",
"Pixie Cut",
"Long Layers",
"Buzz Cut",
"Pompadour"
],

"avoid":[
"Very heavy bangs",
"Styles hiding the face"
]

},

"Round":{

"good":[
"Long Layers",
"Butterfly Cut",
"Side Part",
"Textured Quiff",
"Wolf Cut",
"Shag",
"Long Bob"
],

"avoid":[
"Blunt Bob",
"Straight heavy bangs",
"Rounded bowl cuts"
]

},

"Square":{

"good":[
"Curtain Bangs",
"Side Swept Fringe",
"Layered Cuts",
"Textured Crop",
"Long Waves",
"Wolf Cut"
],

"avoid":[
"Very sharp jaw-length bobs",
"Buzz cut"
]

},

"Heart":{

"good":[
"Curtain Bangs",
"Layered Lob",
"Side Part",
"Pixie",
"Shoulder Layers"
],

"avoid":[
"Too much crown volume"
]

},

"Oblong":{

"good":[
"Curtain Bangs",
"Wavy Bob",
"Shoulder Layers",
"French Bob",
"Layered Shag"
],

"avoid":[
"Very long flat hair",
"Extra height on top"
]

}

}


# ============================================================
# HAIR COLORS
# ============================================================

hair_colors = {

"Black":[
"Jet Black",
"Dark Brown",
"Burgundy",
"Blue Black",
"Deep Red"
],

"Brown":[
"Chocolate Brown",
"Caramel",
"Honey",
"Auburn",
"Chestnut"
],

"White":[
"Blonde",
"Ash Blonde",
"Light Brown",
"Copper",
"Platinum"
]

}


# ============================================================
# STYLE FILTERS
# ============================================================

masculine_bonus = [
"Buzz Cut",
"Pompadour",
"Textured Crop",
"Side Part",
"Quiff"
]

feminine_bonus = [
"Butterfly Cut",
"French Bob",
"Layered Bob",
"Long Layers",
"Curtain Bangs",
"Pixie"
]


# ============================================================
# BUILD RECOMMENDATIONS
# ============================================================

recommended = hairstyles[predicted_face_shape]["good"][:] 

if style == "Masculine": #check what user prefers
    recommended = sorted( #sort hairstyle list
        recommended, #sort list
        key=lambda x: x not in masculine_bonus 
    )

elif style == "Feminine":
    recommended = sorted(
        recommended,
        key=lambda x: x not in feminine_bonus
    )


# ============================================================
# RESULTS
# ============================================================

print("\n")
print("="*60)
print("          STYLIE PERSONALIZED RESULTS")
print("="*60)

#Displays all the perferences plus a heading
print(f"\nFace Shape: {predicted_face_shape}")

print(f"Skin Tone: {predicted_skin_tone}")

print(f"Hair Texture: {hair_texture}")

print(f"Hair Length: {hair_length}")

print(f"Preferred Style: {style}")

print("\nRecommended Hairstyles")

for i,hair in enumerate(recommended[:5],1): 
    print(f"{i}. {hair}") 

print("\nHairstyles To Avoid")

for bad in hairstyles[predicted_face_shape]["avoid"]:
    print("-",bad) 

print("\nHair Colors That Usually Suit You")

for color in hair_colors[predicted_skin_tone]:
    print("-",color)

print("\nGeneral Tips")

#checks the face shape and prints the advice
if predicted_face_shape=="Round":
    print("- Add height and vertical volume.")
    print("- Avoid width around the cheeks.")

elif predicted_face_shape=="Square":
    print("- Soften strong jawlines with layers.")
    print("- Texture works well.")

elif predicted_face_shape=="Oval":
    print("- Almost every hairstyle works.")
    print("- Experiment freely.")

elif predicted_face_shape=="Heart":
    print("- Balance a wider forehead.")
    print("- Add volume around the jaw.")

elif predicted_face_shape=="Oblong":
    print("- Add width instead of height.")
    print("- Bangs work especially well.")

print("\nEnjoy your Stylie recommendations!")
print("="*60)
