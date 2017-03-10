from PIL import Image
from math import *

#LISTE DES IMG POUR LES QUESTIONS
img_q_un = Image.new("RGB", (512,512), "white")
img_q_deux = Image.new("RGB", (512,512), "white")
img_q_trois = Image.new("RGB", (512,512), "white")
img_q_quatre = Image.new("RGB", (512,512), "white")
img_q_six = Image.new("RGB", (512,512), "white")


def remap(i):
    return (i*4/511)-2

# Compute the square modulus of a complex number
def module(z):
    return (z[0]*z[0] + z[1]*z[1])

# Julia function of the form z = z^2 + c
def func_z(z,c):
    return [z[0]*z[0]-(z[1]*z[1])+c[0], 2*z[0]*z[1]+c[1]]

print("▁ ▂ ▄ ▅ ▆ ▇ █ FRACTALES █ ▇ ▆ ▅ ▄ ▂ ▁")
print("▁ ▂ ▄ ▅ ▆ ▇ █ GENERATOR █ ▇ ▆ ▅ ▄ ▂ ▁")
print("▁ ▂ ▄ ▅ ▆ ▇ █ BY JABO █ ▇ ▆ ▅ ▄ ▂ ▁")
print("      "+"███▀▀▐██▌██▌██▌███──▐██▀▀")
print("      "+"▀▀███▐█████▌██▌███──▐██▀")
print("      "+"█████▐█▐█▌█▌██▌█████▐████")

while True:
    n_question_generer = int(input("Quel question voulez vous générer (1,2,3,4,6) ?"))

    #Question 1
    if n_question_generer == 1:
        pix_un = img_q_un.load()
        for i in range(512):
            for j in range(512):
                pix_un[i,j] = ((i+j)%255, 0, 0)
        img_q_un.save("img_q_un.png")
        print("L'image de la question",(n_question_generer),"à été généré")
    #Question 2
    elif n_question_generer == 2:
        pix_deux = img_q_deux.load()
        for i in range(512):
            for j in range(512):
                pix_deux[i,j] = (0, 255, (i+j)%255)
        img_q_deux.save("img_q_deux.png")
        print("L'image de la question",(n_question_generer),"à été généré")
    #Question 3
    elif n_question_generer == 3:
        pix_trois = img_q_trois.load()
        for i in range(512):
            for j in range(512):
                pix_trois[i, j] = ((i*j)%255, 255, (i+j)%255)
        img_q_trois.save("img_q_trois.png")
        print("L'image de la question",(n_question_generer),"à été généré")
    #Question 4
    elif n_question_generer == 4:
        pix_quatre = img_q_quatre.load()
        for i in range(512):
            for j in range(512):
                z_img_quatre = [remap(i), remap(j)]
                pix_quatre[i,j] = (int(module(z_img_quatre)*50), 0,0)
        img_q_quatre.save("img_q_quatre.png")
        print("L'image de la question",(n_question_generer),"à été généré")
    #Question 6 et 7
    elif n_question_generer == 6:
        c = [-0.2, 0.8]
        print("Entrer la valeur de c (2 float séparés par un espace)")
        a = input().split()
        couleur = str(input("Quelle couleur principal voulez vous (bleu, rouge ou vert) ?"))
        if couleur == "bleu":
            vert = int(input("Quelle dose de vert voulez vous (entre 0 et 255) ? "))
            rouge = int(input("Quelle dose de rouge voulez vous (entre 0 et 255) ? "))
            pix_color = (rouge, vert, 255)
        elif couleur == "vert":
            rouge = int(input("Quelle dose de rouge voulez vous (entre 0 et 255) ? "))
            bleu = int(input("Quelle dose de bleu voulez vous (entre 0 et 255) ? "))
            pix_color = (rouge, 255, bleu)
        elif couleur == "rouge":
            bleu = int(input("Quelle dose de bleu voulez vous (entre 0 et 255) ? "))
            vert = int(input("Quelle dose de vert voulez vous (entre 0 et 255) ? "))
            pix_color = (255, vert, bleu)

        c = [float(a[0]), float(a[1])]
        pix_six = img_q_six.load()
        for i in range(512):
            for j in range(512):
                julia = [remap(i), remap(j)]
                for u in range(50):
                    julia = func_z(julia,c )
                mod_julia = module(julia)
                if mod_julia > 1000 or isnan(mod_julia):
                    pix_six[i,j] = (255,255,255)
                else:
                    pix_six[i,j] = pix_color

        img_q_six.save("img_q_six"+str(c[0])+"_"+"et"+"_"+str(c[1])+(couleur)+".png")
        print("L'image de la question",(n_question_generer),"à été généré")
