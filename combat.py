from random import randint
import sys


#_________________________________________________________________________________________________________________________________________________________

#BUGS A CORRIGER :
    #Aucun pour l'instant

#______________________AFFICHAGE DES INFOS_____________________


def affiche_infos(joueur,ennemi): #Fonction permettant d'afficher les informations du joueur et de l'ennemi pendant le combat
    nom=joueur.get("nom")
    pv=joueur.get("pv")
    pv_l=joueur.get("pv_limite")
    mana=joueur.get("mana")
    mana_l=joueur.get("mana_limite")
    #Récupération des informations sur le joueur
    nom_e=ennemi.get("nom")
    pv_e=ennemi.get("pv")
    pv_e_l=ennemi.get("pv_limite")
    #Récupération des informations sur l'ennemi
    print("_____________________________________________________________________________________")
    print(nom,": PV=",pv,"/",pv_l,"| MANA=",mana,"/",mana_l) # On affiche les informations du joueur
    print(nom_e,": PV=",pv_e,"/",pv_e_l) #On afficge les informations de l'ennemi



#______________________ATTAQUE____________________________





def attaque(joueur,ennemi,arme): #Fonction pour donner un coup à l'ennemi avec l'arme de mélée
    degat=randint(arme.get("dégats")-3,arme.get("dégats")+3) #Les dégats sont hasardeux, allant de 3 dégats de moins jusqu'a 3 dégats de plus que la moyenne de l'arme
    pv_e=ennemi.get("pv")-degat #On inflige les dégats
    if pv_e<0:
        pv_e=0 #Afin que le compteur de PV de l'ennemi n'aille pas en dessous de 0
    nom_a=arme.get("nom")
    print("Vous attaquez avec",nom_a,"et infligez",degat,"dégats!")
    if degat==arme.get("dégats")+3:
        print("Coup critique!")
    ennemi["pv"]=pv_e #On change la valeur du dictionnaire des PV de l'ennemi
    return True




#______________________SORTS______________________________





def sort(joueur,ennemi,objets,sorts,arme,bouclier): #La fonction pour choisir des sorts
    obtenu=[]
    #On crée une liste vide pour y mettre, sur tout les sorts du jeu, uniquement ceux que le joueur à récupéré
    mana=joueur.get("mana")
    pv_e=ennemi.get("pv")
    #On récupère le mana du joueur et les PV de l'ennemi
    for element in sorts:
        nom=element.get("nom")
        cout=element.get("cout")
        degat=element.get("degat")
        obt=element.get("obt")
        #On récupère les infos des sorts dans la liste contenant tout les sorts du jeu
        if obt==True:
            print("Sort:",nom,"| Coût:",cout,"| Dégats:",degat)
            obtenu.append(element)
            #Si le sort est marqué comme obtenu par le joueur, on affiche ses informations puis on l'ajoute a la liste des sorts récupérés par le joueur
    if obtenu==[]:
        print("Aucun sort!")
    choix=input("Quel sort choisissez vous? /// Retour : ")
    if choix=="Retour":
        return False
        #Afin de pouvoir quitter le menu si voulu
    test=False
    for element in obtenu:
        if choix==element["nom"]:
            choix=element.copy()
            test=True
            #Afin de vérifier si le choix du joueur correspond bien au nom d'un des sorts proposés et pour arrêter la boucle si c'est le cas
            #Et aussi pour récupérer précisément le dictionnaire du sort choisi
    if test==False:
        print("Vous n'avez pas ce sort!")
        return False
        #Si la variable reste False, cela veut dire que le choix ne correspond pas a un des sorts demandé et cela relancera la fonction depuis le début
    nom=choix.get("nom")
    cout=choix.get("cout")
    degat=choix.get("degat")
    #Récupération des infos du sort choisi
    if mana<cout:
        print("Vous n'avez pas assez de MANA!")
        return False
        #Relance la fonction depuis le début si pas assez de mana
    else:
        pv_e=pv_e-degat
        mana=mana-cout
        if pv_e<0:
            pv_e=0
        print("Vous utilisez le sort '",nom,"' et infligez",degat,"dégats!")
        #Afin d'infliger les dégats à l'ennemi et retirer du mana au joueur après l'attaque
        ennemi["pv"]=pv_e
        joueur["mana"]=mana
        return True
        #Remplacement des anciennes valeurs dans les dictionnaires



#_______________OBJETS________________________________________





def quel_objet(joueur,ennemi,objets,sorts,arme,bouclier): #Fonction pour ouvrir l'inventaire d'objets et en choisir un
    #Le début de la fonction est similaire à celle pour les sorts
    obtenu=[] #Liste vide pour y mettre uniquement les objets obtenus par le joueur, sur tout les objets disponibles en jeu
    for element in objets:
        stock=element.get("stock")
        #Récupération du stock de l'objet obtenu par le joueur
        if stock>0:
            nom=element.get("nom")
            print("Nom=",nom,"| Stock=",stock)
            obtenu.append(element)
    #Boucle afin de mettre dans liste vide uniquement les objets dont le stock est au dessus de 0
    if obtenu==[]:
        print("Aucun objet!")
    choix=input("Quel objet choisissez vous? /// Retour : ")
    if choix=="Retour":
        return False
    test=False
    for element in obtenu:
        if choix==element["nom"]:
            choix=element.copy()
            element["stock"]=element["stock"]-1
            test=True
            #Afin de vérifier si le choix du joueur correspond bien au nom d'un des objets proposés et pour arrêter la boucle si c'est le cas
            #Et aussi pour récupérer précisément le dictionnaire de l'objet choisi
    if test==False:
        print("Vous n'avez pas cet objet!")
        return False
    effet=choix.get("effet") #Récupération de l'effet de l'objet choisi afin de voir quelle fonction lancer après
    if effet=="soin":
        obj_soin(choix,joueur) #Lance la fonction pour les objets de soin
        return True
    elif effet=="degat":
        obj_degat(choix,joueur,ennemi) #Lance la fonction pour les objets qui infligent des dégats à l'ennemi
        return True
    elif effet=="mana":
        obj_mana(choix,joueur) #Lance la fonction pour les objets qui restaurent le mana
        return True













def obj_soin(objet,joueur): #Fonction utilisée pour les objets de soin
    soin=objet.get("effet_nb")
    #Récupération du nombre de PVs que l'objet va restaurer au joueur
    nom=objet.get("nom")
    pv=joueur.get("pv")
    pv_l=joueur.get("pv_limite")
    pv+=soin #Application des soins
    if pv>pv_l:
        pv=pv_l
        #Afin de faire en sorte que les PV du joueur ne dépassent pas la valeur maximale donnée
    print("Vous vous soignez avec",nom,"et passez à",pv,"PVs!")
    joueur["pv"]=pv #Remplacement de l'ancienne valeur du dictionnaire




def obj_degat(objet,joueur,ennemi): #Fonction utilisée pour les objets qui infligent des dégats à l'adversaire
    degat=objet.get("effet_nb")
    #Récupération du nombre de PVs que l'objet va retirer à l'ennemi
    nom=objet.get("nom")
    pv_e=ennemi.get("pv")
    pv_e=pv_e-degat
    #Déduction des PVs de l'ennemi après utilisation de l'objet
    if pv_e<0:
        pv_e=0
        #Afin que les PVs de l'ennemi ne passent pas en dessous de 0
    print("Vous utilisez",nom,"sur l'ennemi et infligez",degat,"dégats!")
    ennemi["pv"]=pv_e #Remplacement de l'ancienne valeur du dictionnaire



def obj_mana(objet,joueur): #Fonction utilisée pour les objets qui restaure le mana
    restore=objet.get("effet_nb")
    #Récupération du nombre de MANA que l'objet va restaurer
    nom=objet.get("nom")
    mana=joueur.get("mana")
    mana_l=joueur.get("mana_limite")
    mana+=restore
    #Application de l'objet
    if mana>mana_l:
        mana=mana_l
        #Pour pas que le nombre de MANA passe en dessous de 0
    print("Vous utilisez",nom,"et passez à",mana,"MANA!")
    joueur["mana"]=mana #Remplacement de l'ancienne valeur du dictionnaire






#_______________________________VICTOIRE ET DEFAITE_____________________________________








def victoire(joueur,ennemi): #Fonction pour déterminer si il y a victoire à la fin d'un tour
    victoire=False
    pv_e=ennemi.get("pv")
    nom=ennemi.get("nom")
    if pv_e==0: #Si les PVs de l'ennemi sont a 0, alors la victoire est déclarée pour le joueur
        print("Vous avez vaincu",nom,"!")
        victoire=True
    return victoire #Renvoie le booléen "victoire" pour la fonction "combat"

def defaite(joueur,ennemi): #Fonction pour déterminer si il y a défaite à la fin d'un tour
    defaite=False
    pv=joueur.get("pv")
    if pv==0: #Si les PVs du joueur sont a 0, alors la défaite est déclarée pour le joueur
        print("Vous avez été vaincu...")
        print("GAME OVER")
        defaite=True
    return defaite #Renvoie le booléen "defaite" pour la fonction "combat"



#______________________RECOMPENSES SI VICTOIRE___________________________________________




def recompenses(joueur,ennemi): #Fonction qui sert à donner de l'or et de l'expérience au joueur si il bat l'ennemi
    xp=joueur.get("xp") #L'expérience déjà obtenue par le joueur
    xp_gg=ennemi.get("xp") #L'expérience donnée au joueur pour avoir battu l'ennemi
    or_jo=joueur.get("or") #L'or déjà obtenu par le joueur
    or_gg=ennemi.get("or") #L'or donné au joueur pour avoir battu l'ennemi
    acheve=ennemi.get("achevé") #Donnée qui sert a savoir si le joueur a décidé d'épargner ou d'achever l'ennemi
    if acheve==False:
        xp_gg=xp_gg/1.5
        or_gg=or_gg/1.5
        xp_gg=int(round(xp_gg,0))
        or_gg=int(round(or_gg,0))
        #Permet de réduire l'expérience et l'or donnés au joueur si il a épargné l'ennemi. Cela servira pour plus tard car si le joueur
        #décide d'achever tout les ennemis de la démo, alors le boss s'activera en mode DIFFICILE
    xp+=xp_gg
    or_jo+=or_gg
    #On additionne l'or et l'XP du joueur + ceux donnés par l'ennemi
    print("Vous obtenez",xp_gg,"XP et",or_gg,"pièces d'or.")
    joueur["xp"]=xp
    joueur["or"]=or_jo #On remplace les données du dictionnaire









def lvlup(joueur,arme): #Permet d'augmenter le niveau du joueur si besoin
    nv=joueur.get("nv")
    xp=joueur.get("xp")
    pv=joueur.get("pv_limite")
    mana=joueur.get("mana_limite")
    degat=arme.get("dégats")
    #On obtient toutes les données qui vont augmenter
    #Les niveaux augmentent jusqu'a 10 pour l'instant
    #Chaque palier augmente les PVs et le mana MAX de 3 points
    if xp>=100 and nv==1: #On vérifie a chaque fois que le joueur a assez d'XP pour passer au niveau suivant et qu'il est déjà passé au niveau inférieur
        pv+=10
        mana+=3
        nv+=1
        degat+=2
        print("Vous passez au niveau 2!")
    if xp>=300 and nv==2:
        pv+=10
        mana+=3
        nv+=1
        degat+=2
        print("Vous passez au niveau 3!")
    if xp>=400 and nv==3:
        pv+=10
        mana+=3
        nv+=1
        degat+=2
        print("Vous passez au niveau 4!")
    if xp>=550 and nv==4:
        pv+=10
        mana+=3
        nv+=1
        degat+=2
        print("Vous passez au niveau 5!")
    if xp>=700 and nv==5:
        pv+=10
        mana+=3
        nv+=1
        degat+=2
        print("Vous passez au niveau 6!")
    if xp>=850 and nv==6:
        pv+=10
        mana+=3
        nv+=1
        degat+=2
        print("Vous passez au niveau 7!")
    if xp>=950 and nv==7:
        pv+=10
        mana+=3
        nv+=1
        degat+=2
        print("Vous passez au niveau 8!")
    if xp>=1050 and nv==8:
        pv+=10
        mana+=3
        nv+=1
        degat+=2
        print("Vous passez au niveau 9!")
    if xp>=1300 and nv==9:
        pv+=10
        mana+=3
        nv+=1
        degat+=2
        print("Vous passez au niveau 10!")
    joueur["nv"]=nv
    joueur["pv_limite"]=pv
    joueur["mana_limite"]=mana
    arme["dégats"]=degat #On remplace les données du dictionnaire





#_____________________________ENNEMIS_______________________________________________________







def ennemi_strd_dialogue(ennemi,ennemiD): #Fonction qui permet d'afficher le dialogue d'un ennemi à chaque fois que c'est son tour, si il n'est pas un boss
    nom_e=ennemi.get("nom")
    test=ennemiD.get("test")
    #Permet de savoir si l'ennemi a déjà dit son premier dialogue afin de lancer le second
    di1=ennemiD.get("di1")
    #Le premier dialogue de l'ennemi
    di2=ennemiD.get("di2")
    #Et son second dialogue
    if test==False:
        print(nom_e,":",di1)
        ennemiD["test"]=True
        #Si l'ennemi n'a pas dit son premier dialogue, celui ci est affiché et la valeur testant si il a bien dit son premier dialogue devient True
    else:
        print(nom_e,":",di2)
        ennemiD["test"]=False
        #Si la valeur de test est True, le second dialogue est affiché et la valeur de test deviens False de nouveau, afin de réafficher le premier dialogue plus tard









def ennemi_atk_strd(joueur,ennemi,bouclier,coups_ennemi): #Fonction pour lancer les attaques de l'ennemi si il n'est pas un boss
    pv=joueur.get("pv")
    nom_e=ennemi.get("nom")
    garde=bouclier.get("actif") #Permet de savoir si le joueur est en mode Garde ou non
    rand=randint(1,2) #Pour que l'ennemi utilise l'une de ses deux attaques au hasard
    if rand==1:
        coup_nom=coups_ennemi.get("coup1_nom")
        coup_dg=coups_ennemi.get("coup1degats")
        #Si rand==1, alors les infos de la première attaque sont choisies
    elif rand==2:
        coup_nom=coups_ennemi.get("coup2_nom")
        coup_dg=coups_ennemi.get("coup2degats")
        #Si rand==2, alors c'est les infos de la seconde attaque qui sont choisies
    if garde==True:
        protect=bouclier.get("garde")
        coup_dg=coup_dg*protect
        coup_dg=int(round(coup_dg,0))
        bouclier["actif"]=False
        #Si la garde est activée, alors les dégats de l'attaque sont multipliés par la valeur de protection du bouclier (par exemple, dégats*0.8)
        #La valeur de la garde redeviens donc False
    print(nom_e,"vous attaque avec",coup_nom,"et vous inflige",coup_dg,"dégats!")
    pv=pv-coup_dg
    #Les PVs du joueur baissent
    if pv<0:
        pv=0
        #Pour éviter que les PVs du joueur aillent en dessous de 0
    joueur["pv"]=pv #Remplacement de la valeur du dictionnaire


#______________________________BOSS__________________________________________________________


def atk_boss_romulus_normal(joueur,ennemi,bouclier,coups_ennemi):
    pv=joueur.get("pv")
    nom_e=ennemi.get("nom")
    garde=bouclier.get("actif") #Permet de savoir si le joueur est en mode Garde ou non
    rand=randint(1,4)
    if rand==1:
        coup_nom=coups_ennemi.get("coup1_nom")
        coup_dg=coups_ennemi.get("coup1degats")
    elif rand==2:
        coup_nom=coups_ennemi.get("coup2_nom")
        coup_dg=coups_ennemi.get("coup2degats")
    elif rand==3:
        coup_nom=coups_ennemi.get("coup3_nom")
        coup_dg=coups_ennemi.get("coup3degats")
    elif rand==4:
        coup_nom=coups_ennemi.get("coup4_nom")
        coup_dg=coups_ennemi.get("coup4degats")
    if garde==True:
        protect=bouclier.get("garde")
        coup_dg=coup_dg*protect
        coup_dg=int(round(coup_dg,0))
        bouclier["actif"]=False
        #Si la garde est activée, alors les dégats de l'attaque sont multipliés par la valeur de protection du bouclier (par exemple, dégats*0.8)
        #La valeur de la garde redeviens donc False
    print(nom_e,"vous attaque avec",coup_nom,"et vous inflige",coup_dg,"dégats!")
    pv=pv-coup_dg
    #Les PVs du joueur baissent
    if pv<0:
        pv=0
        #Pour éviter que les PVs du joueur aillent en dessous de 0
    joueur["pv"]=pv #Remplacement de la valeur du dictionnaire


def atk_boss_romulus_hard(joueur,ennemi,bouclier,coups_ennemi):
    pv=joueur.get("pv")
    nom_e=ennemi.get("nom")
    garde=bouclier.get("actif") #Permet de savoir si le joueur est en mode Garde ou non
    rand=randint(1,5)
    if rand==1:
        coup_nom=coups_ennemi.get("coup1_nom")
        coup_dg=coups_ennemi.get("coup1degats")
    elif rand==2:
        coup_nom=coups_ennemi.get("coup2_nom")
        coup_dg=coups_ennemi.get("coup2degats")
    elif rand==3:
        coup_nom=coups_ennemi.get("coup3_nom")
        coup_dg=coups_ennemi.get("coup3degats")
    elif rand==4:
        coup_nom=coups_ennemi.get("coup4_nom")
        coup_dg=coups_ennemi.get("coup4degats")
    elif rand==5:
        coup_nom=coups_ennemi.get("coup5_nom")
        coup_dg=coups_ennemi.get("coup5degats")
    if garde==True:
        protect=bouclier.get("garde")
        coup_dg=coup_dg*protect
        coup_dg=int(round(coup_dg,0))
        bouclier["actif"]=False
        #Si la garde est activée, alors les dégats de l'attaque sont multipliés par la valeur de protection du bouclier (par exemple, dégats*0.8)
        #La valeur de la garde redeviens donc False
    print(nom_e,"vous attaque avec",coup_nom,"et vous inflige",coup_dg,"dégats!")
    pv=pv-coup_dg
    #Les PVs du joueur baissent
    if pv<0:
        pv=0
        #Pour éviter que les PVs du joueur aillent en dessous de 0
    joueur["pv"]=pv #Remplacement de la valeur du dictionnaire

def dialogue_romulus_normal(ennemi,ennemiD):
    nom_e=ennemi.get("nom")
    if ennemiD["test0"]==False:
        print(nom_e,":",ennemiD["di1"])
        ennemiD["test1"]=True
        ennemiD["test0"]=True
    elif ennemiD["test1"]==True:
        print(nom_e,":",ennemiD["di2"])
        ennemiD["test2"]=True
        ennemiD["test1"]=False
    elif ennemiD["test2"]==True:
        print(nom_e,":",ennemiD["di3"])
        ennemiD["test3"]=True
        ennemiD["test2"]=False
    elif ennemiD["test3"]==True:
        print(nom_e,":",ennemiD["di4"])
        ennemiD["test4"]=True
        ennemiD["test3"]=False
    elif ennemiD["test4"]==True:
        print(nom_e,":",ennemiD["di5"])
        ennemiD["test5"]=True
        ennemiD["test4"]=False
    elif ennemiD["test5"]==True:
        print(nom_e,":",ennemiD["di6"])


def dialogue_romulus_fuite(ennemi,ennemiD):
    nom_e=ennemi.get("nom")
    if ennemiD["test0"]==False:
        print(nom_e,":",ennemiD["di1"])
        ennemiD["test1"]=True
        ennemiD["test0"]=True
    elif ennemiD["test1"]==True:
        print(nom_e,":",ennemiD["di2"])
        ennemiD["test2"]=True
        ennemiD["test1"]=False
    elif ennemiD["test2"]==True:
        print(nom_e,":",ennemiD["di3"])
        ennemiD["test3"]=True
        ennemiD["test2"]=False
    elif ennemiD["test3"]==True:
        print(nom_e,":",ennemiD["di4"])
        ennemiD["test4"]=True
        ennemiD["test3"]=False
    elif ennemiD["test4"]==True:
        print(nom_e,":",ennemiD["di5"])
        ennemiD["test5"]=True
        ennemiD["test4"]=False
    elif ennemiD["test5"]==True:
        print(nom_e,":",ennemiD["di6"])
        ennemiD["test6"]=True
        ennemiD["test5"]=False
    elif ennemiD["test6"]==True:
        print(nom_e,":",ennemiD["di7"])

def dialogue_romulus_hard(ennemi,ennemiD):
    nom_e=ennemi.get("nom")
    if ennemiD["test0"]==False:
        print(nom_e,":",ennemiD["di1"])
        ennemiD["test1"]=True
        ennemiD["test0"]=True
    elif ennemiD["test1"]==True:
        print(nom_e,":",ennemiD["di2"])
        ennemiD["test2"]=True
        ennemiD["test1"]=False
    elif ennemiD["test2"]==True:
        print(nom_e,":",ennemiD["di3"])
        ennemiD["test3"]=True
        ennemiD["test2"]=False
    elif ennemiD["test3"]==True:
        print(nom_e,":",ennemiD["di4"])
        ennemiD["test4"]=True
        ennemiD["test3"]=False
    elif ennemiD["test4"]==True:
        print(nom_e,":",ennemiD["di5"])
        ennemiD["test5"]=True
        ennemiD["test4"]=False
    elif ennemiD["test5"]==True:
        print(nom_e,":",ennemiD["di6"])
        ennemiD["test6"]=True
        ennemiD["test5"]=False
    elif ennemiD["test6"]==True:
        print(nom_e,":",ennemiD["di7"])
        ennemiD["test7"]=True
        ennemiD["test6"]=False
    elif ennemiD["test7"]==True:
        print(nom_e,":",ennemiD["di8"])
        ennemiD["test8"]=True
        ennemiD["test7"]=False
    elif ennemiD["test8"]==True:
        print(nom_e,":",ennemiD["di9"])


#______________________CHOIX COMBAT________________________________________________________________

def choix_combat(joueur,ennemi,objets,sorts,arme,bouclier,fuiteTest): #Permet au joueur de choisir une option de combat
    test=False
    while test!=True:
        print("Attaque|Sort|Objets|Garde|Fuite") #Affichage des différentes options
        choix=input("Que voulez vous faire? : ") #Le joueur rentre une commande
        if choix=="Attaque":
            if attaque(joueur,ennemi,arme)==True:
                test=True
        elif choix=="Sort":
            if sort(joueur,ennemi,objets,sorts,arme,bouclier)==True:
                test=True
        elif choix=="Objets":
            if quel_objet(joueur,ennemi,objets,sorts,arme,bouclier)==True:
                test=True
        elif choix=="Garde":
            if garde(bouclier)==True:
                test=True
        elif choix=="Fuite":
            if ennemi["boss"]==True:
                print("Vous ne pouvez pas fuir ce combat!")
            else:
                fuiteTest["fuite"]=True
                print("Vous fuiyez le combat!")
                test=True
        else:
            print("Vous ne savez pas faire ça!")
        #Au cas ou le joueur rentre une mauvaise commande




#________________________GARDE_____________________________________________________





def garde(bouclier): #Pour activer la garde
    testchoix=True
    nom=bouclier.get("nom")
    bouclier["actif"]=True #Pour indiquer a la fonction d'attaque de l'ennemi que la garde est activée
    print("Vous utilisez votre",nom,"pour vous protéger de la prochaine attaque!")
    return True



#______________________________ACHEVER______________________________________________________




def achever(ennemi): #Afin de faire choisir au joueur si il achève l'ennemi ou non. Achever tout les ennemis de la démo fait passer le boss de fin en mode DIFFICILE
    nom_e=ennemi.get("nom")
    choix=input("Achever? O/N : ")
    if choix=="O":
        ennemi["achevé"]=True
        print("Vous avez achevé",nom_e,". Ce qu'il restait de son être s'en va pour les Limbes.")
    elif choix=="N":
        print("Vous avez épargné",nom_e,".")
        ennemi["achevé"]=False
    else:
        print("Choix invalide")
        achever(ennemi)
        #Au cas ou le joueur rentre une mauvaise commande




#____________________FONCTION DE COMBAT STANDARD___________________________________________





def combat(joueur,ennemi,objets,sorts,arme,bouclier,ennemiD,ennemiCoup,fuiteTest): #Fonction principale de combat
    vict=False
    deft=False
    #Variables de défaite et victoire
    nom_e=ennemi.get("nom")
    print("Vous rencontrez",nom_e,"!")
    while vict==False or deft==False: #La boucle qui permet de lancer les tours tant que la victoire ou défaite du joueur n'est pas atteinte
        affiche_infos(joueur,ennemi) #Affiche les infos du joueur et de l'ennemi à chaque tour du joueur
        choix_combat(joueur,ennemi,objets,sorts,arme,bouclier,fuiteTest) #Il choisi son action
        if fuiteTest["fuite"]==True:
            break
        if defaite(joueur,ennemi)==True: #Test de la défaite
            deft=True
            break
        if victoire(joueur,ennemi)==True: #Test de la victoire
            vict=True
            break
        ennemi_strd_dialogue(ennemi,ennemiD) #Dialogue de l'ennemi
        ennemi_atk_strd(joueur,ennemi,bouclier,ennemiCoup) #Attaque de l'ennemi
        if defaite(joueur,ennemi)==True: #Test de la défaite
            deft=True
            break
        if victoire(joueur,ennemi)==True: #Test de la victoire
            vict=True
            break
    #Si l'un des tests s'annonce True, la boucle est alors cassée
    if vict==True: #Dans le cas ou le joueur à gagné
        ennemi["battu"]=True #La valeur du dictionnaire est changée pour indiquer que l'ennemi a été vaincu
        achever(ennemi) #Le joueur choisi ou non d'achever l'ennemi
        recompenses(joueur,ennemi)
        lvlup(joueur,arme)
        #Envoie les récompenses et teste si le joueur augmente de niveau
        stop=input("Entrez une touche pour arrêter : ")
        return None
    elif deft==True: #Dans le cas ou le joueur à perdu, le jeu s'arrête
        stop=input("Entrez une touche pour arrêter : ")
        sys.exit()
        return None
    elif fuiteTest["fuite"]==True:
        fuiteTest["fuite"]=False
        stop=input("Entrez une touche pour arrêter : ")
        return None


#____________________FONCTIONS DE COMBAT BOSS___________________________________________


def combat_romulus_normal(joueur,ennemi,objets,sorts,arme,bouclier,ennemiD,ennemiCoup,fuiteTest): #Fonction principale de combat
    vict=False
    deft=False
    #Variables de défaite et victoire
    nom_e=ennemi.get("nom")
    print("Vous rencontrez",nom_e,"!")
    while vict==False or deft==False: #La boucle qui permet de lancer les tours tant que la victoire ou défaite du joueur n'est pas atteinte
        affiche_infos(joueur,ennemi) #Affiche les infos du joueur et de l'ennemi à chaque tour du joueur
        choix_combat(joueur,ennemi,objets,sorts,arme,bouclier,fuiteTest) #Il choisi son action
        if fuiteTest["fuite"]==True:
            break
        if defaite(joueur,ennemi)==True: #Test de la défaite
            deft=True
            break
        if victoire(joueur,ennemi)==True: #Test de la victoire
            vict=True
            break
        dialogue_romulus_normal(ennemi,ennemiD) #Dialogue de l'ennemi
        atk_boss_romulus_normal(joueur,ennemi,bouclier,ennemiCoup) #Attaque de l'ennemi
        if defaite(joueur,ennemi)==True: #Test de la défaite
            deft=True
            break
        if victoire(joueur,ennemi)==True: #Test de la victoire
            vict=True
            break
    #Si l'un des tests s'annonce True, la boucle est alors cassée
    if vict==True: #Dans le cas ou le joueur à gagné
        ennemi["battu"]=True #La valeur du dictionnaire est changée pour indiquer que l'ennemi a été vaincu
        achever(ennemi) #Le joueur choisi ou non d'achever l'ennemi
        recompenses(joueur,ennemi)
        lvlup(joueur,arme)
        #Envoie les récompenses et teste si le joueur augmente de niveau
        stop=input("Entrez une touche pour arrêter : ")
        return None
    elif deft==True: #Dans le cas ou le joueur à perdu, le jeu s'arrête
        stop=input("Entrez une touche pour arrêter : ")
        sys.exit()
        return None
    elif fuiteTest["fuite"]==True:
        fuiteTest["fuite"]=False
        stop=input("Entrez une touche pour arrêter : ")
        return None

def combat_romulus_fuite(joueur,ennemi,objets,sorts,arme,bouclier,ennemiD,ennemiCoup,fuiteTest): #Fonction principale de combat
    vict=False
    deft=False
    #Variables de défaite et victoire
    nom_e=ennemi.get("nom")
    print("Vous rencontrez",nom_e,"!")
    while vict==False or deft==False: #La boucle qui permet de lancer les tours tant que la victoire ou défaite du joueur n'est pas atteinte
        affiche_infos(joueur,ennemi) #Affiche les infos du joueur et de l'ennemi à chaque tour du joueur
        choix_combat(joueur,ennemi,objets,sorts,arme,bouclier,fuiteTest) #Il choisi son action
        if fuiteTest["fuite"]==True:
            break
        if defaite(joueur,ennemi)==True: #Test de la défaite
            deft=True
            break
        if victoire(joueur,ennemi)==True: #Test de la victoire
            vict=True
            break
        dialogue_romulus_fuite(ennemi,ennemiD) #Dialogue de l'ennemi
        atk_boss_romulus_normal(joueur,ennemi,bouclier,ennemiCoup) #Attaque de l'ennemi
        if defaite(joueur,ennemi)==True: #Test de la défaite
            deft=True
            break
        if victoire(joueur,ennemi)==True: #Test de la victoire
            vict=True
            break
    #Si l'un des tests s'annonce True, la boucle est alors cassée
    if vict==True: #Dans le cas ou le joueur à gagné
        ennemi["battu"]=True #La valeur du dictionnaire est changée pour indiquer que l'ennemi a été vaincu
        achever(ennemi) #Le joueur choisi ou non d'achever l'ennemi
        recompenses(joueur,ennemi)
        lvlup(joueur,arme)
        #Envoie les récompenses et teste si le joueur augmente de niveau
        stop=input("Entrez une touche pour arrêter : ")
        return None
    elif deft==True: #Dans le cas ou le joueur à perdu, le jeu s'arrête
        stop=input("Entrez une touche pour arrêter : ")
        sys.exit()
        return None
    elif fuiteTest["fuite"]==True:
        fuiteTest["fuite"]=False
        stop=input("Entrez une touche pour arrêter : ")
        return None

def combat_romulus_hard(joueur,ennemi,objets,sorts,arme,bouclier,ennemiD,ennemiCoup,fuiteTest): #Fonction principale de combat
    vict=False
    deft=False
    #Variables de défaite et victoire
    nom_e=ennemi.get("nom")
    print("Vous rencontrez",nom_e,"!")
    while vict==False or deft==False: #La boucle qui permet de lancer les tours tant que la victoire ou défaite du joueur n'est pas atteinte
        affiche_infos(joueur,ennemi) #Affiche les infos du joueur et de l'ennemi à chaque tour du joueur
        choix_combat(joueur,ennemi,objets,sorts,arme,bouclier,fuiteTest) #Il choisi son action
        if fuiteTest["fuite"]==True:
            break
        if defaite(joueur,ennemi)==True: #Test de la défaite
            deft=True
            break
        if victoire(joueur,ennemi)==True: #Test de la victoire
            vict=True
            break
        dialogue_romulus_hard(ennemi,ennemiD) #Dialogue de l'ennemi
        atk_boss_romulus_hard(joueur,ennemi,bouclier,ennemiCoup) #Attaque de l'ennemi
        if defaite(joueur,ennemi)==True: #Test de la défaite
            deft=True
            break
        if victoire(joueur,ennemi)==True: #Test de la victoire
            vict=True
            break
    #Si l'un des tests s'annonce True, la boucle est alors cassée
    if vict==True: #Dans le cas ou le joueur à gagné
        ennemi["battu"]=True #La valeur du dictionnaire est changée pour indiquer que l'ennemi a été vaincu
        achever(ennemi) #Le joueur choisi ou non d'achever l'ennemi
        recompenses(joueur,ennemi)
        lvlup(joueur,arme)
        #Envoie les récompenses et teste si le joueur augmente de niveau
        stop=input("Entrez une touche pour arrêter : ")
        return None
    elif deft==True: #Dans le cas ou le joueur à perdu, le jeu s'arrête
        stop=input("Entrez une touche pour arrêter : ")
        sys.exit()
        return None
    elif fuiteTest["fuite"]==True:
        fuiteTest["fuite"]=False
        stop=input("Entrez une touche pour arrêter : ")
        return None














