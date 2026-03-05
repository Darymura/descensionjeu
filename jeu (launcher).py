from random import randint
import sys
import combat

#_________________________________________JOUEUR______________________________________________________

joueur={"nom":"placeholder","nv":1,"pv":150,"mana":100,"pv_limite":150,"mana_limite":100,"xp":0,"or":50}

mode={"mode":"normal"}

#_______________________________________SORTS_____________________________________________________________

#Dictionnaire du joueur, permet d'obtenir et modifier le nom, le sexe, le niveau, les PVs et le MANA ainsi que leur limite, l'expérience et l'or.
#Dictionnaire vide pour un joueur custom : {"nom":"","sexe":"masculin/feminin","nv":0,"pv":0,"mana":0,"pv_limite":0,"mana_limite":0,"xp":0,"or":0}

electricite={"nom":"élec","cout":20,"degat":25,"obt":False}
feu={"nom":"Feu","cout":25,"degat":30,"obt":False}
maudit={"nom":"Maudit","cout":50,"degat":60,"obt":False}
angelique={"nom":"Angélique","cout":80,"degat":150,"obt":False,"prix":300}
vent={"nom":"vent","cout":15,"degat":20, "obt":False}

liste_sorts=[electricite,feu,vent,maudit,angelique]

#Les dictionnaires contenant les infos de tout les sorts. La liste permet de les utiliser avec la fonction "sort" écrite plus bas
#Dictionnaire vide pour rajouter un sort : {"nom":"","cout":0,"degat":0,"obt":False/True}
#Ne pas oublier de rajouter le sort dans liste_sorts

#____________________________________________OBJETS_____________________________________________


potion_soin={"nom":"Potion de soin","stock":0,"effet":"soin","effet_nb":35,"prix":20}
couteau_lancer={"nom":"Couteau de lancer","stock":0,"effet":"degat","effet_nb":30,"prix":40}
potion_mana={"nom":"Potion de mana","stock":0,"effet":"mana","effet_nb":25,"prix":25}
super_potion_soin={"nom":"Super potion de soin","stock":0,"effet":"soin","effet_nb":80,"prix":45}
couteau_angelique={"nom":"Couteau angélique","stock":0,"effet":"degat","effet_nb":100,"prix":60}
super_potion_mana={"nom":"Super potion de mana","stock":0,"effet":"mana","effet_nb":65,"prix":50}
eau={"nom":"Eau","stock":0,"effet":"soin","effet_nb":20,"prix":10}

liste_obj=[eau,potion_soin,couteau_lancer,potion_mana,super_potion_mana,super_potion_soin,couteau_angelique]

#Les dictionnaires contenant les informations de tout les objets du jeu ainsi que la liste permettant d'utiliser la fonction "objets_choix"
#Dictionnaire vide pour rajouter un objet : {"nom":"","stock":0,"effet":"soin/degat/mana","effet_nb":0,"prix":0}

#___________________________________________EPEE___________________________________________

epee_strd={"nom":"épée standard","dégats":25}
arme=epee_strd

#Dictionnaires des armes utilisables par le joueur, contiendra plus tard plus d'infos

#___________________________________ENNEMIS______________________________________________________________


mannequin={"nom":"Mannequin de combat","pv":50,"pv_limite":50,"xp":0,"or":0,"battu":False,"achevé":False,"boss":False}
d_mannequin={"di1":"......","test":False,"di2":"......"}
coup_mannequin={"coup1_nom":"Rien","coup1degats":0,"coup2_nom":"Rien","coup2degats":0}

garde_Lance={"nom":"Garde Lancier","pv":75,"pv_limite":75,"xp":75,"or":40,"battu":False,"achevé":False,"boss":False}
d_Garde_Lance={"di1":"Tu ne m'échapperas pas!","test":False,"di2":"Plus un geste!"}
coup_Garde_Lance={"coup1_nom":"coup de lance","coup1degats":10,"coup2_nom":"coup de pied","coup2degats":7}



garde_epee={"nom":"Garde épéiste","pv":80,"pv_limite":80,"xp":75,"or":44,"battu":False,"achevé":False,"boss":False}
d_Garde_epee={"di1":"Tu ne m'échapperas pas!","test":False,"di2":"Ne bouge plus!"}
coup_Garde_epee={"doup1_nom":"coup d'épée","coup1degats":12,"coup2_nom":"coup de poing","coup2degats":8}



garde_arc={"nom":"Garde Archer","pv":55,"pv_limite":55,"xp":100,"or":40,"battu":False,"achevé":False,"boss":False}
d_Garde_arc={"di1":"Reste tranquille","test":False,"di2":"Je t'ai à l'oeil"}
coup_Garde_arc={"coup1_nom":"flèche","coup1degats":9,"coup2_nom":"flèche de lumière","coup2degats":14}



le_Clown={"nom":"Le Clown","pv":100,"pv_limite":100,"xp":100,"or":60,"battu":False,"achevé":False,"boss":False}
d_Le_Clown={"di1":"Tu vas mourir de rire!","test":False,"di2":"Ce qu'on s'amuse!"}
coup_Le_Clown={"coup1_nom":"piège","coup1degats":8,"coup2_nom":"lancer de couteaux","coup2degats":9}



che_Peg={"nom":"Chevalier pégase","pv":200,"pv_limite":200,"xp":150,"or":100,"battu":False,"achevé":False,"boss":False}
d_Che_Peg={"di1":"Vole mon pégase!","test":False,"di2":"Ton chemin se termine ici!"}
coup_Che_Peg={"coup1_nom":"attaque en piqué","coup1degats":14,"coup2_nom":"coup de sabots","coup2degats":9}



es_So={"nom":"Esprit Solitaire","pv":50,"pv_limite":50,"xp":65,"or":10,"battu":False,"achevé":False,"boss":False}
d_Es_So={"di1":"Laisse moi...","test":False,"di2":"C'est mon espace personnel ici..."}
coup_Es_So={"coup1_nom":"ce qu'il trouve","coup1degats":3,"coup2_nom":"le rejet","coup2degats":1}



ange={"nom":"Ange","pv":80,"pv_limite":80,"xp":80,"or":50,"battu":False,"achevé":False,"boss":False}
d_ange={"di1":"Pourquoi se battre?","test":False,"di2":"Tu m'y obliges"}
coup_ange={"coup1_nom":"coup d'aile","coup1degats":6,"coup2_nom":"tentative de persuasion","coup2degats":3}



garde_Lance2={"nom":"Garde Lancier","pv":75,"pv_limite":75,"xp":75,"or":40,"battu":False,"achevé":False,"boss":False}
d_Garde_Lance2={"di1":"Tu ne m'échapperas pas!","test":False,"di2":"plus un geste!"}
coup_Garde_Lance2={"coup1_nom":"coup de lance","coup1degats":10,"coup2_nom":"coup de pied","coup2degats":7}


che_Peg2={"nom":"Chevalier pégase","pv":200,"pv_limite":200,"xp":150,"or":100,"battu":False,"achevé":False,"boss":False}
d_Che_Peg2={"di1":"Vole mon pégase!","test":False,"di2":"Ton chemin se termine ici!"}
coup_Che_Peg2={"coup1_nom":"attaque en piqué","coup1degats":14,"coup2_nom":"coup de sabots","coup2degats":9}


garde_arc2={"nom":"Garde Archer","pv":55,"pv_limite":55,"xp":100,"or":40,"battu":False,"achevé":False,"boss":False}
d_Garde_arc2={"di1":"Reste tranquille","test":False,"di2":"Je t'ai à l'oeil"}
coup_Garde_arc2={"coup1_nom":"flèche","coup1degats":9,"coup2_nom":"flèche de lumière","coup2degats":14}


mage={"nom":"Mage","pv":65,"pv_limite":65,"xp":125,"or":56,"battu":False,"achevé":False,"boss":False}
d_mage={"di1":"J'en appelle à la magie!","test":False,"di2":"Enfin, un cobaye"}
coup_mage={"coup1_nom":"feu","coup1degats":20,"coup2_nom":"glace","coup2degats":16}


haut_mage={"nom":"Haut Mage","pv":100,"pv_limite":100,"xp":150,"or":80,"battu":False,"achevé":False,"boss":False}
d_haut_mage={"di1":"Tu ne fera pas long feu","test":False,"di2":"disparais"}
coup_haut_mage={"coup1_nom":"foudre","coup1degats":25,"coup2_nom":"lame d'air","coup2degats":17}


ancien_boxeur={"nom":"Ancien Boxeur","pv":125,"pv_limite":125,"xp":155,"or":100,"battu":False,"achevé":False,"boss":False}
d_ancien_boxeur={"di1":"montres moi ce que tu sais faire!","test":False,"di2":"pas sous la ceinture!"}
coup_ancien_boxeur={"coup1_nom":"uppercut","coup1degats":15,"coup2_nom":"direct","coup2degats":11}


ancienne_star={"nom":"Ancienne star","pv":55,"pv_limite":55,"xp":75,"or":60,"battu":False,"achevé":False,"boss":False}
d_ancienne_star={"di1":"c'est un talent naturel chez moi!","test":False,"di2":"fais toi beau pour le public!"}
coup_ancienne_star={"coup1_nom":"pose dramatique","coup1degats":6,"coup2_nom":"jeu d'acteur incroyable","coup2degats":10}



ancien_mil={"nom":"Ancien militaire","pv":100,"pv_limite":100,"xp":100,"or":80,"battu":False,"achevé":False,"boss":False}
d_ancien_mil={"di1":"la vie me manque aussi","test":False,"di2":"je n'ai pas pu profiter comme il se doit"}
coup_ancien_mil={"coup1_nom":"arme blanche","coup1degats":15,"coup2_nom":"prise de MMA","coup2degats":10}


liste_ennemis=[garde_arc2,garde_epee,garde_arc,garde_Lance2,le_Clown,che_Peg,che_Peg2,es_So,ange,mage,haut_mage,ancien_boxeur,ancienne_star,ancien_mil]

#Tout les ennemis
#Rajouter un ennemi : {"nom":"","pv":0,"pv_limite":0,"xp":0,"or":0,"battu":False,"achevé":False,"boss":False}
#                     {"di1":"","test":False,"di2":""}
#                     {"coup1_nom":"","coup1degats":0,"coup2_nom":"","coup2degats":0}

#_____________________________________________BOUCLIER__________________________________________________________________

bouclier_strd={"nom":"Bouclier standard","garde":0.25,"actif":False}
bouclier=bouclier_strd

#Informations des boucliers, contiendra plus tard plus d'infos

fuiteTest={"fuite":False}

#_____________________________________________BOSS___________________________________________________________

romulus_boss_normal={"nom":"Romulus, chef des archanges","pv":1250,"pv_limite":1250,"xp":1000,"or":680,"battu":False,"achevé":False,"boss":True}
coup_romulus_normal={"coup1_nom":"Coup d'épée angélique","coup1degats":17,"coup2_nom":"Sort de l'au-delà","coup2degats":30,"coup3_nom":"Flèche de lumière","coup3degats":22,"coup4_nom":"Lance longue","coup4degats":20}
d_romulus_normal={"test0":False,"di1":"Je peux déjà voir ton envie de repartir auprès de tiens, cependant, ce n'est pas assez!","test1":False,"di2":"Sache que je respecte ta dévotion, mais je ne peux pas te laisser passer.","test2":False,"di3":"On m'a confié comme mission de protéger cet artefact sacré...Ils m'observent tous et comptent sur moi pour assurer qu'il reste ou il est!","test3":False,"di4":"Ceci est donc un combat qui va déterminer lequel de nous deux tiens le plus à accomplir son but...Sache que je ne suis pas près d'abandonner!!","test4":False,"di5":"Assez parlé...A présent, voyons à qui mérite la victoire.","test5":False,"di6":"....."}

d_romulus_fuite={"test0":False,"di1":"Je peux déjà voir ton envie de repartir auprès de tiens, cependant, ce n'est pas assez!","test1":False,"di2":"Sache que je respecte ta dévotion, mais je ne peux pas te laisser passer.","test2":False,"di3":"On m'a confié comme mission de protéger cet artefact sacré...Ils m'observent tous et comptent sur moi pour assurer qu'il reste ou il est!","test3":False,"di4":"Ceci est donc un combat qui va déterminer lequel de nous deux tiens le plus à accomplir son but...Sache que je ne suis pas près d'abandonner!!","test4":False,"di5":"Tu as passé ton temps à fuir, sans affronter un seul de mes soldats...Comment espères-tu me battre, à moi?!","test5":False,"di6":"Assez parlé...A présent, voyons à qui mérite la victoire.","test6":False,"di7":"....."}

romulus_boss_hard={"nom":"Romulus, vengeur des archanges","pv":2000,"pv_limite":2000,"xp":2000,"or":850,"battu":False,"achevé":False,"boss":True}
coup_romulus_hard={"coup1_nom":"Coup d'épée angélique","coup1degats":35,"coup2_nom":"Sort de l'au-delà","coup2degats":45,"coup3_nom":"Flèche de lumière","coup3degats":32,"coup4_nom":"Lance longue","coup4degats":30,"coup5_nom":"Vengeance","coup5degats":65}
d_romulus_hard={"test0":False,"di1":"Tu peux penser que je n'ai plus aucune raison de me battre maintenant que tout mes soldats ne sont plus là...Cependant, j'ai encore plus envie de me battre, pour que leurs seconde mort ne soit pas en vain.","test1":False,"di2":"Chaqu'un d'entre eux étaient des soldats admirables, tu sais. J'ai du mal à me rendre compte que tu les as tous battus.","test2":False,"di3":"Mais moi...","test3":False,"di4":"...Moi, je vais t'écraser...","test4":False,"di5":"...Pour leur faire honneur, et pour protéger tout ceux que tu vas probablement planifier d'assassiner aussi.","test5":False,"di6":"Donc si tu veux abréger toute suite tes souffrances, je te conseille de rester là ou tu es...","test6":False,"di7":"...Car tu vas mourir ici, et maintenant.","test7":False,"di8":"Mais assez parlé...Meurt, démon.","test8":False,"di9":"....."}

#_______________________________________________________________________________________________________________________________________________________

#________________________________________________________________________________________________________________________________________________________



def salle_tuto(joueur,ennemi,ennemiCoups,ennemiDialogue,armeJ,sortsJ,objetsJ,bouclierJ,fuiteTest):
    print("Vous vous faufilez dans ce qui semble être une salle d'entrainement vide...Votre premier réflexe est d'aller prendre l'épée et le bouclier accrochés sur le mur.")
    print("Vous obtenez une épée standard!")
    print("Vous obtenez un bouclier standard!")
    print("Vous décidez de vous entraîner contre le mannequin d'entrainement.")
    combat.combat(joueur,ennemi,objetsJ,sortsJ,armeJ,bouclierJ,ennemiDialogue,ennemiCoups,fuiteTest)
    print("Vous continuez vers la prochaine salle.")
    print("_____________________________________________________________________________________________")

def salle_1(joueur,ennemi,ennemiCoups,ennemiDialogue,armeJ,sortsJ,objetsJ,bouclierJ,fuiteTest):
    print("Vous entrez dans la salle. Il fait sombre et vous avez l'impression que quelqu'un vous observe.")
    print("choix 1 : fouiller à l'aveugle'")
    print("choix 2 : combattre qui que ce soit")
    print("choix 3 : partir")
    test=False
    while test==False:
        choix=input("quel choix prenez vous? (1/2/3) /// Inventaire :")
        if choix=="1":
            print("il y a surement un objet ici mais il fait trop sombre pour espérer le trouver.")
            test=True
        elif choix=="2":
            print("Ne voyant rien,vous agitez votre épée dans tous les sens dans l'éspoir de toucher un ennemi quand vous entendez une voix qui vous dis de vous en aller. vous decidez donc de vous rapprochez de cette voix et")
            combat.combat(joueur,ennemi,objetsJ,sortsJ,armeJ,bouclierJ,ennemiDialogue,ennemiCoups,fuiteTest)
            test=True
        elif choix=="3":
            print("vous mettez les mains en avant pour plus de sécurité et finissez par trouver le chemin.")
            test=True
        elif choix=="Inventaire":
            inventaire(joueur,liste_obj,liste_sorts)
        else:
            print("vous ne savez pas faire ça!")
    print("vous continuez vers la prochaine salle.")
    print("_____________________________________________________________________________________________")


def salle_2(joueur,ennemi,ennemiCoups,ennemiDialogue,armeJ,sortsJ,objetsJ,bouclierJ,fuiteTest):
    print("Vous entrez dans la salle et sentez une légère brise. En levant les yeux vous pouvez apercevoir le ciel ainsi que ce qui vous semble être un pégase  qui hypnotiserait presque vôtre regard bien que vous ne croyez pas en ces créatures.")
    print("choix 1 : fouiller")
    print("choix 2 : combattre")
    print("choix 3 : partir")
    test=False
    while test==False:
        choix=input("quel choix prenez vous? (1/2/3) /// Inventaire  :")
        if choix=="1":
            print("Vous regardez autour de vous et remarquez...bingo! Une potion de soin!")
            potion_soin["stock"]+=1
            test=True
        elif choix=="2":
            print("Vous vous dites que vous n'avez jamais combattu un pégase auparavant et decidez donc de crier pour attirer son attention. Il vient vers vous et vous avez à peine le temps de l'admirer que le chevalier qui le chevauche vous attaque.")
            combat.combat(joueur,ennemi,objetsJ,sortsJ,armeJ,bouclierJ,ennemiDialogue,ennemiCoups,fuiteTest)
            vent["obt"]=True
            print("Vous avez appris le sort du vent!")
            test=True
        elif choix=="3":
            print("Vous passez tranquillement votre chemin quand soudain le pégase descend à tout vitesse pour vous barrer la route, le chevalier qui le monte semble très fier de cette performance.")
            combat.combat(joueur,ennemi,objetsJ,sortsJ,armeJ,bouclierJ,ennemiDialogue,ennemiCoups,fuiteTest)
            vent["obt"]=True
            print("Vous avez appris le sort du vent!")
            test=True
        elif choix=="Inventaire":
            inventaire(joueur,liste_obj,liste_sorts)
        else:
            print("vous ne savez pas faire ça!")
    print("vous continuez vers la prochaine salle.")
    print("_____________________________________________________________________________________________")


def salle_3(joueur,ennemi,ennemiCoups,ennemiDialogue,armeJ,sortsJ,objetsJ,bouclierJ,fuiteTest):
    print("Vous entrez dans la salle. Il fait plutot sombre mais vous apercevez un bureau avec une multitude de livres qui vous sont inconnus éclairés par une torche. Quelqu'un semble dormir sur sa chaise à coté du mur.")
    print("choix 1 : regarder les livres")
    print("choix 2 : le réveiller et le combattre")
    print("choix 3 : partir")
    test=False
    while test==False:
        choix=input("quel choix prenez vous? (1/2/3) /// Inventaire  :")
        if choix=="1":
            print("Vous prenez discrètement la torche afin de mieux inspecter les livres. certains sont trop compliqués pour vous mais vous arrivez à dénicher un livre de sort simple.")
            electricite["obt"]=True
            print("vous avez appris le sort d'électricité!")
            print("oups! Vous venez de faire tomber un livre ce qui réveille le mage.")
            combat.combat(joueur,ennemi,objetsJ,sortsJ,armeJ,bouclierJ,ennemiDialogue,ennemiCoups,fuiteTest)
            test=True
        elif choix=="2":
            print("Vous vous approchez de ce qui s'avère etre un mage.Sans un bruit, vous prenez la chaise et la tirez d'un coup sec pour le faire tomber.Il est confus,c'est le moment!")
            combat.combat(joueur,ennemi,objetsJ,sortsJ,armeJ,bouclierJ,ennemiDialogue,ennemiCoups,fuiteTest)
            electricite["obt"]=True
            print("vous avez appris le sort d'électricité!")
            test=True
        elif choix=="3":
            print("Vous préférez ne pas pértuber son sommeil et marchez tranquillement vers la prochaine salle. vous vous sentez fier de ne pas l'avoir dérangé.")
            test=True
        elif choix=="Inventaire":
            inventaire(joueur,liste_obj,liste_sorts)
        else:
            print("vous ne sevez pas faires ça!")
    print("vous continuez vers la prochaine salle.")
    print("_____________________________________________________________________________________________")


def salle_4(joueur,armeJ,sortsJ,objetsJ,bouclierJ):
    print("A peine rentré dans la salle que vous sentez une odeur infecte, semblable à de la bouse de vache. De la paille est présente un peu partout et le toit est dégagé sur un ciel dégagé.")
    print("choix 1 : fouiller")
    print("choix 2 : chercher quelqu'un à combattre'")
    print("choix 3 : partir")
    test=False
    while test==False:
        choix=input("quel choix prenez vous? (1/2/3) /// Inventaire  :")
        if choix=="1":
            print("Vous prenez votre mal en patience et commencez à fouiller dans la paille. Vous trouvez une gourde remplie d'eau. Vous décidez d'arrêter vos recherches et de vous en aller le plus vite possible après avoir trouvé un crottin de cheval... ")
            eau["stock"]+=1
            test=True
        elif choix=="2":
            print("il n'y a personne ici. vous criez pour essayer d'attirer l'attention de qui que ce soit...sans succès. Vous décidez donc de partir pour ne plus avoir à subir cette odeur.")
            test=True
        elif choix=="3":
            print("vous ne supportez pas cette odeur atroce et courrez le plus vite possible vers la salle suivante.")
            test=True
        elif choix=="Inventaire":
            inventaire(joueur,liste_obj,liste_sorts)
        else:
            print("vous ne sevez pas faires ça!")
    print("vous continuez vers la prochaine salle.")
    print("_____________________________________________________________________________________________")

def salle_5(joueur,ennemi,ennemiCoups,ennemiDialogue,armeJ,sortsJ,objetsJ,bouclierJ,fuiteTest):
    print("Vous croyez entrer dans un cirque. Des balles de toutes les couleurs rangées dans une boîte rouge à rayures jaunes; des cerceaux au sol, ainsi que des quilles pour jongler. Vous ne voyez personne, pourtant, vous entendez du bruit près des balles.")
    print("choix 1 : aller voir d'ou vient ce bruit")
    print("choix 2 : chercher un adversaire pour se défouler sur lui")
    print("choix 3 : partir")
    test=False
    while test==False:
        choix=input("quel choix prenez vous? (1/2/3) /// Inventaire  :")
        if choix=="1":
            print("Vous vous approchez de la boîte a balles, vous fuoillez un peu dedans en enlevant petit à petit chaque balle quand soudain l'une des balles rouges se met à couiner. -Nya-ha-ha!, tu as réussi à me trouver! Prépare toi! Mes nouveaux tours vont t'impressioner!-")
            combat.combat(joueur,ennemi,objetsJ,sortsJ,armeJ,bouclierJ,ennemiDialogue,ennemiCoups,fuiteTest)
            feu["obt"]=True
            print("Vous avez appris le sort du feu!")
            test=True
        elif choix=="2":
            print("vous avez beau regarder de partout vous ne voyez personne. Déçu, vous partez en direction de la salle suivante.")
            test=True
        elif choix=="3":
            print("Pas de temps à perdre avec ces gamineries,vous vous dirigez vers la prochaine salle...quand soudain-CLACK- votre pied est bloqué! -NYA HA HA, tu es pris dans mon magnifique piège que j'ai soigneusement câché! Cette salle c'est moi qui la protège et maintenant tu ne peux plus m'échapper! ")
            combat.combat(joueur,ennemi,objetsJ,sortsJ,armeJ,bouclierJ,ennemiDialogue,ennemiCoups,fuiteTest)
            feu["obt"]=True
            print("Vous avez appris le sort du feu!")
            test=True
        elif choix=="Inventaire":
            inventaire(joueur,liste_obj,liste_sorts)
        else:
            print("vous ne sevez pas faires ça!")
    print("vous continuez vers la prochaine salle.")
    print("_____________________________________________________________________________________________")

def salle_6(joueur,ennemi,ennemiCoups,ennemiDialogue,armeJ,sortsJ,objetsJ,bouclierJ,fuiteTest):
    print("Vous entrez dans une salle plutôt bien éclairée. Les murs violet et les cristaux suspendus au plafond ne vous mettent pas à l'aise'. vous avancez légèrement et vous voyez une grande silhouette en face de vous. En vous rapprochant encore plus vous vous rendez compte que ce n'est qu'un grand miroir qui est installé devant vous. La silhouette n'était pas la vôtre mais celle du grand mage qui se dressait derrière vous.")
    print("choix 1 : dire bonjour et voir si quelque chose pourrait vous être utile")
    print("choix 2 : le combattre")
    print("choix 3 : partir au plus vite")
    test=False
    while test==False:
        choix=input("quel choix prenez vous? (1/2/3) /// Inventaire  :")
        if choix=="1":
            print("Vous lui dites bonjour,il vous répond avec une voix intimidante et vous lance un duel...que vous ne pouvez refuser.")
            combat.combat(joueur,ennemi,objetsJ,sortsJ,armeJ,bouclierJ,ennemiDialogue,ennemiCoups,fuiteTest)
            maudit["obt"]=True
            print("Vous avez appris le sort maudit!")
            test=True
        elif choix=="2":
            print("La première chose que vous dites au sorcier est que vous voulez le combattre, il sourit et ce met à préparer ses sorts. A l'attaque!")
            combat.combat(joueur,ennemi,objetsJ,sortsJ,armeJ,bouclierJ,ennemiDialogue,ennemiCoups,fuiteTest)
            maudit["obt"]=True
            print("Vous avez appris le sort maudit!")
            test=True
        elif choix=="3":
            print(" Tout en évitant de regarder le mage dans les yeux,vous cherchez la sortie mais n'en trouvez pas. Il vous informe d'une voix grave et imposante qu'il faut le combattre pour pouvoir quitter la salle.")
            combat.combat(joueur,ennemi,objetsJ,sortsJ,armeJ,bouclierJ,ennemiDialogue,ennemiCoups,fuiteTest)
            maudit["obt"]=True
            print("Vous avez appris le sort maudit!")
            test=True
        elif choix=="Inventaire":
            inventaire(joueur,liste_obj,liste_sorts)
        else:
            print("vous ne sevez pas faires ça!")
    print("vous continuez vers la prochaine salle.")
    print("_____________________________________________________________________________________________")

def salle_7(joueur,ennemi,ennemiCoups,ennemiDialogue,armeJ,sortsJ,objetsJ,bouclierJ,fuiteTest):
    print("On se croirait à l'avant-première d'un film, un tapis rouge s'étand de vos pieds jusqu'à lautre bout de la salle. les murs sont noirs et le plafond est comme couvert d'étoiles et les flash d'appareils photos vous rendent encore plus confus. - Merci,Merci...oh? Mais qu'avons nous là? Ne serais-tu pas la vedette dont le monde parle? je suis désolée je ne t'entends pas avec tout ce raffut, mes fans sont complètement fous de moi! Viens,allons discuter.")
    print("choix 1 : Accepter de discuter")
    print("choix 2 : la provoquer devant ses fans")
    print("choix 3 : partir")
    test=False
    while test==False:
            choix=input("quel choix prenez vous? (1/2/3) /// Inventaire  :")
            if choix=="1":
                print("Vous l'accompagnez jusqu'à un coin plus éloigné pour parler un peu avec elle: -Alors, c'est toi qui est prêt à tout pour rentrer chez lui hmm? Tout le monde ne parle plus que de toi en ce moment et à quel point ils sont prêt à t'affronter ou je ne sais quelles autres bétises. personnellement je n'en ai rien a faire. Tu sais quoi,tu m'as l'air sympathique alors e vais te donner ça. Aller amuse toi bien!")
                potion_mana["stock"]+=1
                test=True
            elif choix=="2":
                print("-Comment oses-tu me faire affront devant mes fans? C'est inadmissible! Je vais me faire le plaisir de t'humilier devant tout le monde!")
                combat.combat(joueur,ennemi,objetsJ,sortsJ,armeJ,bouclierJ,ennemiDialogue,ennemiCoups,fuiteTest)
                test=True
            elif choix=="3":
                print("-Ooo zut tu t'en vas déjà, j'aurais aimé papoter un peu. Bon et bien, bon vent!")
                test=True
            elif choix=="Inventaire":
                inventaire(joueur,liste_obj,liste_sorts)
            else:
                print("vous ne sevez pas faires ça!")
    print("vous continuez vers la prochaine salle.")
    print("_____________________________________________________________________________________________")

def salle_8(joueur,ennemi,ennemiCoups,ennemiDialogue,armeJ,sortsJ,objetsJ,bouclierJ,fuiteTest):
    print("vous entrez dans ce qui semble être une salle d'entraînement: les murs sont rayés, des poutres en bois sont abimées, un mannequin bourré de fouin est également présent et il est en train de se faire tailler par un garde")
    print("choix 1 : fouiller")
    print("choix 2 : combattre")
    print("choix 3 : partir")
    test=False
    while test==False:
        choix=input("quel choix prenez vous? (1/2/3) /// Inventaire  :")
        if choix=="1":
            print("vous regardez autour de vous mais il semble ne rien avoir d'intéressant. Ah! De l'eau. Vous la prenez et quittez la salle.")
            eau["stock"]+=1
            test=True
        elif choix=="2":
            print("Vous provoquez le garde en duel,il accepte et se dit que  c'est l'occasion de voir si son entraînement porte ses fruits.")
            combat.combat(joueur,ennemi,objetsJ,sortsJ,armeJ,bouclierJ,ennemiDialogue,ennemiCoups,fuiteTest)
            test=True
        elif choix=="3":
            print("Rien d'intéressant ici, pas la peine de perdre son temps, vous continuez vers la salle suivante.")
            test=True
        elif choix=="Inventaire":
            inventaire(joueur,liste_obj,liste_sorts)
        else:
            print("vous ne sevez pas faires ça!")
    print("vous continuez vers la prochaine salle.")
    print("_____________________________________________________________________________________________")

def salle_9(joueur,ennemi,ennemiCoups,ennemiDialogue,armeJ,sortsJ,objetsJ,bouclierJ,fuiteTest):
    print("Quelle belle salle. Tout est blanc et sens la joie et la tranquilité. Vous avez l'impression de marcher de marcher sur un nuage. Des objets volent un peu partout dans la pièce grâce à de petites ailes et un ange se repose sur un fauteuil volant.")
    print("choix 1 : attraper un objet")
    print("choix 2 : combattre")
    print("choix 3 : partir")
    test=False
    while test==False:
        choix=input("quel choix prenez vous? (1/2/3) /// Inventaire  :")
        if choix=="1":
            print("Vous essayez d'attraper un objet au hasard, ils volent haut...ah!C'est bon! vous avez réussi à attraper une potion. L'ange n'a pas l'air d'y prêter attention.")
            potion_soin["stock"]+=1
            test=True
        elif choix=="2":
            print("Vous attrapez un des pieds du fauteuil et le tirez vers le bas, l'ange vous regarde d'un air méprisant, vous commencez à le combattre sans lui demander son avis.")
            combat.combat(joueur,ennemi,objetsJ,sortsJ,armeJ,bouclierJ,ennemiDialogue,ennemiCoups,fuiteTest)
            test=True
        elif choix=="3":
            print("Vous laissez cet ange se relaxer tranquillement et partez explorer la salle suivante.")
            test=True
        elif choix=="Inventaire":
            inventaire(joueur,liste_obj,liste_sorts)
        else:
            print("vous ne sevez pas faires ça!")
    print("vous continuez vers la prochaine salle.")
    print("_____________________________________________________________________________________________")

def salle_10(joueur,ennemi,ennemiCoups,ennemiDialogue,armeJ,sortsJ,objetsJ,bouclierJ,fuiteTest):
    print("Vous entrez dans une salle de repos,il y a plusieurs bancs  à gauche sur lesquels vous pouvez vous asseoir ou même vous allonger avec un peu d'eau à coté; il y également un garde qui prend sa pause à droite.")
    print("choix 1 : se reposer un peu")
    print("choix 2 : combattre")
    print("choix 3 : partir")
    test=False
    while test==False:
        choix=input("quel choix prenez vous? (1/2/3) /// Inventaire  :")
        if choix=="1":
            print("Vous vous asseyez sur le banc,un peu de repos ne fait jamais de mal. Vous en profitez pour prendre un peu d'eau.Une fois bien reposé vous décidez de reprendre la route.")
            eau["stock"]+=1
            test=True
        elif choix=="2":
            print("Le garde n'a même pas eu le temps de se reposer que vous le poussez à combattre, c'est avec un mal de dos qu'il accepte votre défi")
            combat.combat(joueur,ennemi,objetsJ,sortsJ,armeJ,bouclierJ,ennemiDialogue,ennemiCoups,fuiteTest)
            test=True
        elif choix=="3":
            print("Pas de repos pour les braves! Vous foncez directement vers la salle suivante.")
            test=True
        elif choix=="Inventaire":
            inventaire(joueur,liste_obj,liste_sorts)
        else:
            print("vous ne sevez pas faires ça!")
    print("vous continuez vers la prochaine salle.")
    print("_____________________________________________________________________________________________")

def salle_11(joueur,ennemi,ennemiCoups,ennemiDialogue,armeJ,sortsJ,objetsJ,bouclierJ,fuiteTest):
    print("Vous commencez à être fatigué et vous dites que cela ne finira donc jamais. Vous arrivez dans une salle qui ressemble à un chalet de luxe: cheminée avec feu allumé qui est la seule source de lumière de la pièce, peau de bête étalée sur le sol en bois,les murs sont fais de poutres de bois empilées méthodiquement les unes sur les autres, et pour seules décorations une étagère ou sont éxposées de nombreuses médailles ainsi qu'un uniforme de grande classe décoré lui aussi de plusieurs médailles. Devant vous un homme assit sur un fauteuil rouge et qui admire tranquillement le feu. ")
    print("Choix 1 :aller observer les médailles de plus près.")
    print("Choix 2 :combattre")
    print("Choix 3 :ne pas le déranger et partir")
    test=False
    while test==False:
	    choix=input("Quel choix prenez vous? (1/2/3) // Inventaire :")
	    if choix=="1":
		    print("-Belles médailles n'est-ce pas? j'ai passé la plus grande partie de ma vie à tout faire pour les avoir, et c'est à ma mort que j'ai tout le temps de les admirer-. Le monsieur n'a pas bougé de son fauteuil, en bas de l'étagère vous trouvez une potion.")
		    potion_soin["stock"]+=1
		    test=True
	    elif choix=="2":
		    print("-Tu veux vraiment me combattre? Bon très bien.- Le monsieur se lève doucement de son fauteuil, vous pouvez à présent admirer son corps musclé se mettre en postion de combat. Cependant, vous pouvez voir la trsitesse dans son regard.")
		    combat.combat(joueur,ennemi,objetsJ,sortsJ,armeJ,bouclierJ,ennemiDialogue,ennemiCoups,fuiteTest)
		    test=True
	    elif choix=="3":
		    print("vous passez derrière le monsieur, il tourne la tête pour vous regarder mais ne fais rien. Vous vous demandez ce qu'il fait là mais ne vous attardez pas sur la question.")
		    test=True
	    elif choix=="Inventaire":
		    inventaire(joueur,liste_obj,liste_sorts)
	    else:
		    print("Vous ne savez pas faire ça!")
    print("Vous continuez vers la prochaine salle.")
    print("_____________________________________________________________________________________________")


def salle_12(joueur,ennemi,ennemiCoups,ennemiDialogue,armeJ,sortsJ,objetsJ,bouclierJ,fuiteTest):
    print("Oh? Vous entrez dans la salle et la première chose que vous voyez est un sac de frappe bien amoché. Il y aussi de l'eau, un banc, un vraie salle d'entrainement à la boxe. - Alors c'est toi qui veut à tout prix partir?- Vous vous demandez d'ou vient cette voix et vous rendez compte qu'il y a quelqu'un dans le coin à gauche de vous qui est en train de s'essuyer le visage avec une serviette déjà usagée. - Si tu veux vraiment t'en aller tu vas devoir me prouver ta valeur!")
    print("Choix 1 :relever le défi.")
    print("Choix 2 :prendre de l'eau avant de commencer.")
    print("Choix 3 :non merci, je chosis de vivre")
    test=False
    while test==False:
        choix=input("Quel choix prenez vous? (1/2/3) //Inventaire :")
        if choix=="1":
            print("Le boxeur a l'air ravi d'entendre ça. Préparez vous, il est prêt à en découdre!")
            combat.combat(joueur,ennemi,objetsJ,sortsJ,armeJ,bouclierJ,ennemiDialogue,ennemiCoups,fuiteTest)
            test=True
        elif choix=="2":
            print("vous vous précipitez sur l'eau pour avoir un réserve mais après ça le boxeur ayant perdu patience commence le duel sans vous demander votre avis!")
            combat.combat(joueur,ennemi,objetsJ,sortsJ,armeJ,bouclierJ,ennemiDialogue,ennemiCoups,fuiteTest)
            test=True
        elif choix=="3":
            print("-Minute papillon, tu crois pouvoir sortir en douce!? Ha! Comme si tu avais le choix!")
            combat.combat(joueur,ennemi,objetsJ,sortsJ,armeJ,bouclierJ,ennemiDialogue,ennemiCoups,fuiteTest)
            test=True
        elif choix=="Inventaire":
            inventaire(joueur,liste_obj,liste_sorts)
        else:
            print("Vous ne savez pas faire ça!")
    print("Vous continuez vers la prochaine salle.")
    print("____________________________________________________________________________________________")

def salle_13(joueur,ennemi,ennemiCoups,ennemiDialogue,armeJ,sortsJ,objetsJ,bouclierJ,fuiteTest):
    print("Vous entrez à peine dans la salle suivante que vous avez failli vous faire transpercer le nez par une flèche! Après avoir vérifié que vous n'avez rien vous regardez à gauche et pouvez apercevoir un cible d'entrainement au loin, vous ne pensiez pas que la salle serait si grande. -Presque! La prochaine ne te ratera pas!- Vous regardez à droite et c'est alors que vous comprenez que c'est de vous que parle ce garde en vous visant avec son arc.'")
    print("Choix 1 :Foncer vers lui pour attaquer")
    print("Choix 2 :partir")
    print("Choix 3 :chercher des objets.")
    test=False
    while test==False:
        choix=input("Quel choix prenez vous? (1/2/3) //Inventaire:")
        if choix=="1":
            print("Paniqué, l'archer n'arrive pas à bien vous viser, vous en profitez pour vous rapprocher et l'attaquer")
            combat.combat(joueur,ennemi,objetsJ,sortsJ,armeJ,bouclierJ,ennemiDialogue,ennemiCoups,fuiteTest)
            test=True
        elif choix=="2":
            print("Fuyez! vous arrivez à esquiver ses flèches et courez le plus vite possible vers la sortie,c'était moins une!'")
            test=True
        elif choix=="3":
            print("Vous esquivez tant bien que mal les flèches et arrivez à trouver un couteau de lancer. Voius voyez que l'archer s'énerve et commence à préparer une flèche spéciale. Mieux vaut s'en aller au plus vite!")
            couteau_lancer["stock"]+=1
            test=True
        elif choix=="Inventaire":
            inventaire(joueur,liste_obj,liste_sorts)
        else:
            print("Vous ne savez pas faire ça!")
        print("Vous continuez vers la prochaine salle.")
        print("_____________________________________________________________________________________________")

def salle_14(joueur,ennemi,ennemiCoups,ennemiDialogue,armeJ,sortsJ,objetsJ,bouclierJ,fuiteTest):
    print("Cette salle a l'air vide, il n'y a rien de particulier qui puisse vous intéresser. Il y a quand même un garde ici, vous vous demandez vraiment pourquoi.")
    print("Choix 1 :aller voir le garde")
    print("Choix 2 :partir")
    print("Choix 3 :Il y a peut être quelque chose")
    test=False
    while test==False:
        choix=input("Quel choix prenez vous? (1/2/3) //Inventaire:")
        if choix=="1":
            print("Le garde a vraiment l'air de s'ennuyer ici. -Y'a pas un rat ici, je m'ennuie à mourir. Et dire que je suis là uniquement pour te battre.")
            combat.combat(joueur,ennemi,objetsJ,sortsJ,armeJ,bouclierJ,ennemiDialogue,ennemiCoups,fuiteTest)
            test=True
        elif choix=="2":
            print("Le garde s'endort. il n'y vraiment rien ici, mieux vaut partir.")
            test=True
        elif choix=="3":
            print("Vous avez beau regarder de partout vous ne trouvez rien. déçu,vous préférez partir sans plus attendre.")
            test=True
        elif choix=="Inventaire":
            inventaire(joueur,liste_obj,liste_sorts)
        else:
            print("Vous ne savez pas faire ça!")
    print("Vous continuez vers la prochaine salle.")
    print("_____________________________________________________________________________________________")

def salle_15(joueur,ennemi,ennemiCoups,ennemiDialogue,armeJ,sortsJ,objetsJ,bouclierJ,fuiteTest):
    print("A l'entrée de le salle se trouve un pancarte sur laquelle est écrit : -choisissez- avec trois propositions marquées en dessous")
    print("Choix 1 :potion de soin")
    print("Choix 2 :combat")
    print("Choix 3 :potion de mana")
    test=False
    while test==False:
        choix=input("Quel choix prenez vous? (1/2/3) //Inventaire:")
        if choix=="1":
            print("Vous voyez à droite une potion de soin qui vous tend les bras. C'est louche mais vous vous dites qu'il vaut mieux en profiter. Après l'avoir prise vous sentez comme un courant d'air puissant qui vous pousse directement vers la prochaine salle.")
            potion_soin["stock"]+=1
            test=True
        elif choix=="2":
            print("Un peu de bagarre ne vous ferait pas de mal. Devant vous se dresse subitement une tornade qui se disspe rapidement et fait apparaître un chevalier pégase. c'est parti!")
            combat.combat(joueur,ennemi,objetsJ,sortsJ,armeJ,bouclierJ,ennemiDialogue,ennemiCoups,fuiteTest)
            test=True
        elif choix=="3":
            print("Vous voyez à gauche une potion de mana qui n'attend que d'être prise.C'est louche mais vous vous dites qu'il vaut mieux en profiter. Après l'avoir prise un courant d'air vous pousse directement vers l'autre salle sans vous prévenir.")
            potion_mana["stock"]+=1
            test=True
        elif choix=="Inventaire":
            inventaire(joueur,liste_obj,liste_sorts)
        else:
            print("Vous ne savez pas faire ça!")
    print("Vous continuez vers la prochaine salle.")
    print("_____________________________________________________________________________________________")


def salle_16(joueur,ennemi,ennemiCoups,ennemiDialogue,armeJ,sortsJ,objetsJ,bouclierJ,fuiteTest):
    print("Vous entrez dans la salle. Rien d'anormal jusque là, vous regardez autour de vous. Tiens? La voie pour la salle suivante est bloquée par une porte en fer fermée à clé. autour de vous se trouvent une étagère pleine de livres, un garde très mal caché, et un coffre.")
    print("Choix 1 : les livres")
    print("Choix 2 : combattre le garde")
    print("Choix 3 : le coffre")
    test=False
    while test==False:
        choix=input("Quel choix prenez vous? (1/2/3) //Inventaire:")
        if choix=="1":
            print("vous aller voir tous ces livres de plus près. Peu être que la clé est cachée quelque part par là? vous enlevez tous les livres un par un en vérifiant leur contenu à chaque fois, et au bout d'un heure de recherche vous trouvez enfin la clé qui était cachée dans livre en bas à gauche. victoire! Vous ouvrez la porte et jetez la clé sur le garde avant de partir.")
            test=True
        elif choix=="2":
            print("Vous faite signe pour lui dire que vous le voyez très bien. -Zut! J'étais pourtant sûr que tu ne me verrais pas.- vous voyez que la clé est attachée à sa ceinture. -Si tu me bats tu pourra prendre la clé et partir, hmm-hmm, bonne chance!")
            combat.combat(joueur,ennemi,objetsJ,sortsJ,armeJ,bouclierJ,ennemiDialogue,ennemiCoups,fuiteTest)
            test=True
        elif choix=="3":
            print("Vous allez ouvrir le coffre. il est rempli d'épines! Cependant vous pouvez voir que la clé se trouve au fond. Pas le choix, vous plongez la main droite dedans pour la récupérer. C'est avec une forte douleur que vous ouvrez la porte et laissez la clé tomber avant de partir.")
            test=True
        elif choix=="Inventaire":
            inventaire(joueur,liste_obj,liste_sorts)
        else:
            print("Vous ne savez pas faire ça!")
    print("Vous continuez vers la prochaine salle.")
    print("_____________________________________________________________________________________________")

#______________________________SHOP___________________________________________________________________________

def salle_shop(joueur,armeJ,sortsJ,objetsJ,bouclierJ):
    print("Vous entrez dans une salle qui ne ressemble à aucune autre. Il semblerait qu'une personne à l'air un peu menaçant se trouve derrière un comtoir plein d'objets de toutes sortes. C'est un shop!")
    print("Marchand : Bienvenue au shop. Que voulez vous acheter?")
    print("Potion de soin : 20 Or")
    print("Couteau de lancer : 30 Or")
    print("Potion de mana : 25 Or")
    print("Eau : 10 Or")
    print("Super potion de soin : 45 Or")
    print("Couteau angélique : 60 Or")
    print("Super potion de mana : 50 Or")
    print("Sort angélique : 300 Or")
    test=False
    while test==False:
        print("Vous avez",joueur["or"],"or.")
        choix=input("Que choisissez vous? /// OK : ")
        if choix=="Potion de soin":
            shop_achat_obj(joueur,potion_soin)
        elif choix=="Couteau de lancer":
            shop_achat_obj(joueur,couteau_lancer)
        elif choix=="Potion de mana":
            shop_achat_obj(joueur,potion_mana)
        elif choix=="Eau":
            shop_achat_obj(joueur,eau)
        elif choix=="Super potion de soin":
            shop_achat_obj(joueur,super_potion_soin)
        elif choix=="Couteau angélique":
            shop_achat_obj(joueur,couteau_angelique)
        elif choix=="Super potion de mana":
            shop_achat_obj(joueur,super_potion_mana)
        elif choix=="Sort angélique":
            shop_achat_sort(joueur,angelique)
        elif choix=="OK":
            test=True
        else:
            print("Cet objet n'existe pas!")
    print("Vous quittez le shop et continuez vers la prochaine salle.")
    print("_____________________________________________________________________________________________")


def shop_achat_obj(joueur,objet):
    if joueur["or"]>=objet["prix"]:
        objet["stock"]+=1
        joueur["or"]=joueur["or"]-objet["prix"]
        print("Vous achetez 1",objet["nom"])
    else:
        print("Vous n'avez pas assez d'or!")

def shop_achat_sort(joueur,sortA):
    if joueur["or"]>=sortA["prix"]:
        if sortA["obt"]==False:
            joueur["or"]=joueur["or"]-sortA["prix"]
            print("Vous achetez un sort",sortA["nom"])
            sortA["obt"]=True
        else:
            print("Vous avez déjà ce sort!")
    else:
        print("Vous n'avez pas assez d'or!")

#________________________________AVANT BOSS________________________________________________________________

def salle_avantboss(joueur,armeJ,sortsJ,objetsJ,bouclierJ,fuiteTest,ennemisListe,mode):
    print("Vous arrivez dans un hall silencieux...Vous sentez quelque chose de menaçant et fort à la fin de ce couloir...")
    test=False
    print("Avancer /// Inventaire")
    while test==False:
        choix=input("Que choisissez vous? :")
        if choix=="Avancer":
            print("Vous décidez d'avancer vers la fin du couloir...")
            test=True
        elif choix=="Inventaire":
            inventaire(joueur,liste_obj,liste_sorts)
        else:
            print("Vous ne savez pas faire ça!")
    print("Vous avancez vers la fin du couloir...L'artéfact est proche...")
    compte_ennemis_fuite(ennemisListe,mode)
    compte_ennemis_hard(ennemisListe,mode)
    if mode["mode"]=="normal" or mode["mode"]=="fuite":
        print("Vous trouvez accroché au mur une arme nouvelle!")
        armeJ["nom"]="épée du héros"
        armeJ["dégats"]+=70
        print("Vous obtenez l'épée du héros.")
    elif mode["mode"]=="hard":
        print("Vous trouvez accroché au mur une arme nouvelle!")
        armeJ["nom"]="épée sanguinaire"
        armeJ["dégats"]+=100
        print("Vous obtenez l'épée sanguinaire.")
    print("_____________________________________________________________________________________________")

def compte_ennemis_fuite(ennemisListe,mode):
    modefuite=True
    for element in ennemisListe:
        if element["battu"]==True:
            modefuite=False
    if modefuite==True:
        mode["mode"]="fuite"

def compte_ennemis_hard(ennemisListe,mode):
    modehard=True
    for element in ennemisListe:
        if element["achevé"]==False:
            modehard=False
    if modehard==True:
        mode["mode"]="hard"

#__________________BOSS______________________________________________________________________________________

def salle_boss_normal(joueur,ennemi,ennemiCoups,ennemiDialogue,armeJ,sortsJ,objetsJ,bouclierJ,fuiteTest):
    print("Vous arrivez à la fin du couloir. Un homme en armure d'argent se tiens devant vous...L'artéfact est juste derrière lui.")
    print("-C'est donc toi l'intrus...Je me présente, je suis Romulus, chef des archanges que tu as affrontés pour venir jusqu'ici. Une très belle prouesse pour un nouveau venu comme toi. J'ai cru comprendre que tu cherchais cet artéfact pour retourner sur terre...Et bien, voyons, qui de nous deux sortira vainqueur de ce combat. L'artéfact en sera le prix.")
    print("De la magie lumineuse apparait autour des mains du chef!")
    combat.combat_romulus_normal(joueur,ennemi,objetsJ,sortsJ,armeJ,bouclierJ,ennemiDialogue,ennemiCoups,fuiteTest)
    print("Vous sortez vainqueur du combat...Enfin, l'artéfact est a portée de main. Vous vous en approchez...Et vous vous en emparez.")
    print("Vous obtenez l'artéfact de la guerre!")

def salle_boss_fuite(joueur,ennemi,ennemiCoups,ennemiDialogue,armeJ,sortsJ,objetsJ,bouclierJ,fuiteTest):
    print("Vous arrivez à la fin du couloir. Un homme en armure d'argent se tiens devant vous...L'artéfact est juste derrière lui.")
    print("-C'est donc toi l'intrus...Qui se faufile entre tout mes gardes. Tu n'as combattu personne et est quand même arrivé ici...Cependant, tu n'obtiendras jamais l'artéfact que tu recherches. Car tu ne me fuira pas, à moi, Romulus.")
    print("De la magie lumineuse apparait autour des mains du chef!")
    combat.combat_romulus_fuite(joueur,ennemi,objetsJ,sortsJ,armeJ,bouclierJ,ennemiDialogue,ennemiCoups,fuiteTest)
    print("Vous sortez vainqueur du combat...Enfin, l'artéfact est a portée de main. Vous vous en approchez...Et vous vous en emparez.")
    print("Vous obtenez l'artéfact de la guerre!")

def salle_boss_hard(joueur,ennemi,ennemiCoups,ennemiDialogue,armeJ,sortsJ,objetsJ,bouclierJ,fuiteTest):
    print("Vous arrivez à la fin du couloir. Un homme en armure d'argent se tiens devant vous...L'artéfact est juste derrière lui.")
    print("-...Te voilà donc. Le guerrier qui a massacré chaqu'un de mes gardes....L'artéfact se tiens derrière moi, l'objet qui à causé tant de malheurs à cet endroit. Cependant...Je peux te garantir que tu ne l'obtiendras jamais. Pas tant que je suis encore là.")
    print("Romulus s'entoure de magie lumineuse, tandis que d'énormes et magnifiques ailes d'ange apparaissent dans son dos. Le vrai combat final approche.")
    combat.combat_romulus_hard(joueur,ennemi,objetsJ,sortsJ,armeJ,bouclierJ,ennemiDialogue,ennemiCoups,fuiteTest)
    print("Vous sortez vainqueur du combat...Enfin, l'artéfact est a portée de main. Vous vous en approchez...Et vous vous en emparez.")
    print("Vous obtenez l'artéfact de la guerre!")

#________________________INVENTAIRE________________________________________________________________________________________

def inventaire_affiche(joueur):
    nom=joueur.get("nom")
    pv=joueur.get("pv")
    pvmax=joueur.get("pv_limite")
    mana=joueur.get("mana")
    manamax=joueur.get("mana_limite")
    lvl=joueur.get("nv")
    xp=joueur.get("xp")
    gold=joueur.get("or")
    print("___________________________")
    print("INVENTAIRE")
    print("___________________________")
    print(nom,"|","Niveau : ",lvl)
    print("PV=",pv,"/",pvmax)
    print("MANA=",mana,"/",manamax)
    print("EXP=",xp,"|","OR=",gold)
    print("___________________________")

def affiche_sorts(sorts):
    obtenuS=[]
    for element in sorts:
        nom=element.get("nom")
        cout=element.get("cout")
        degat=element.get("degat")
        obt=element.get("obt")
        if obt==True:
            print("Sort:",nom,"| Coût:",cout,"| Dégats:",degat)
            obtenuS.append(element)
    if obtenuS==[]:
        print("Aucun sort!")
    input("Entrer une touche pour quitter")

def affiche_objets(objets,joueur):
    choix=""
    while choix!="OK":
        obtenuO=[]
        for element in objets:
            stock=element.get("stock")
            if stock>0:
                nom=element.get("nom")
                print("Nom=",nom,"| Stock=",stock)
                obtenuO.append(element)
        if obtenuO==[]:
            print("Aucun objet!")
        choix=input("Quel objet choisissez vous? /// OK : ")
        if choix=="OK":
            break
        test=False
        for element in obtenuO:
            if choix==element["nom"]:
                choix=element.copy()
                choix2=element
                element["stock"]=element["stock"]-1
                test=True
            #Afin de vérifier si le choix du joueur correspond bien au nom d'un des objets proposés et pour arrêter la boucle si c'est le cas
            #Et aussi pour récupérer précisément le dictionnaire de l'objet choisi
        if test==False:
            print("Vous n'avez pas cet objet!")
            break
        effet=choix.get("effet") #Récupération de l'effet de l'objet choisi afin de voir quelle fonction lancer après
        if effet=="soin":
            combat.obj_soin(choix,joueur) #Lance la fonction pour les objets de soin
        elif effet=="degat":
            print("Vous ne pouvez pas utiliser cet objet hors combat!")
            choix2["stock"]+=1
        elif effet=="mana":
            combat.obj_mana(choix,joueur) #Lance la fonction pour les objets qui restaurent le mana


def inventaire(joueur,objets,sorts):
    choix=""
    while choix!="OK":
        inventaire_affiche(joueur)
        print("Voir sorts | Utiliser objets /// OK")
        choix=input("Que choisissez vous? :")
        if choix=="Voir sorts":
            affiche_sorts(liste_sorts)
        elif choix=="Utiliser objets":
            affiche_objets(liste_obj,joueur)
        elif choix=="OK":
            print("Retour...")
        else:
            print("Vous ne savez pas faire ça!")



#________________________________________PROGRAMME FINAL_____________________________________________________

print("_______________________________________________")
print("              DESCENSION [demo]                ")
print("_______________________________________________")
print("")
joueur["nom"]=input("Veuillez entrer votre nom : ")
if joueur["nom"]=="DebugName":
    print("Debug activé!")
    joueur["pv"]=9999999999
    joueur["pv_limite"]=9999999999
    joueur["mana"]=999999999999
    joueur["mana_limite"]=999999999
    joueur["or"]=9999999999999
    arme["dégats"]=99999999999

print("Votre nom est",joueur["nom"],". Vous êtes décedé d'un accident de voiture le 21 janvier 20XX. Vous vous retrouvez donc au Paradis, là où devrait se finir les soucis de votre ancienne vie humaine...")
print("Cependant, vous pouvez toujours voir l'espoir sur les visages de votre petite famille que vous allez revenir de votre coma. Vous ne pouvez pas rester là...")
print("Vous voilà donc à infiltrer dans une énorme caserne regroupant énormément d'archanges, afin d'y retrouver un artéfact vous permettant d'avancer dans votre quête de revenir sur terre.")
print("Votre descension commence ici.")
print("________________________________________________________________________________________________________________________")
input("Entrez quelque chose pour continuer...")


salle_tuto(joueur,mannequin,coup_mannequin,d_mannequin,arme,liste_sorts,liste_obj,bouclier,fuiteTest)
salle_1(joueur,es_So,coup_Es_So,d_Es_So,arme,liste_sorts,liste_obj,bouclier,fuiteTest)
salle_2(joueur,che_Peg,coup_Che_Peg,d_Che_Peg,arme,liste_sorts,liste_obj,bouclier,fuiteTest)
salle_3(joueur,mage,coup_mage,d_mage,arme,liste_sorts,liste_obj,bouclier,fuiteTest)
salle_4(joueur,arme,liste_sorts,liste_obj,bouclier)
salle_5(joueur,le_Clown,coup_Le_Clown,d_Le_Clown,arme,liste_sorts,liste_obj,bouclier,fuiteTest)
salle_6(joueur,haut_mage,coup_haut_mage,d_haut_mage,arme,liste_sorts,liste_obj,bouclier,fuiteTest)
salle_7(joueur,ancienne_star,coup_ancienne_star,d_ancienne_star,arme,liste_sorts,liste_obj,bouclier,fuiteTest)
salle_8(joueur,garde_Lance,coup_Garde_Lance,d_Garde_Lance,arme,liste_sorts,liste_obj,bouclier,fuiteTest)
salle_9(joueur,ange,coup_ange,d_ange,arme,liste_sorts,liste_obj,bouclier,fuiteTest)
salle_10(joueur,garde_epee,coup_Garde_epee,d_Garde_epee,arme,liste_sorts,liste_obj,bouclier,fuiteTest)
salle_11(joueur,ancien_mil,coup_ancien_mil,d_ancien_mil,arme,liste_sorts,liste_obj,bouclier,fuiteTest)
salle_12(joueur,ancien_boxeur,coup_ancien_boxeur,d_ancien_boxeur,arme,liste_sorts,liste_obj,bouclier,fuiteTest)
salle_13(joueur,garde_arc,coup_Garde_arc,d_Garde_arc,arme,liste_sorts,liste_obj,bouclier,fuiteTest)
salle_14(joueur,garde_Lance2,coup_Garde_Lance2,d_Garde_Lance2,arme,liste_sorts,liste_obj,bouclier,fuiteTest)
salle_15(joueur,che_Peg2,coup_Che_Peg2,d_Che_Peg2,arme,liste_sorts,liste_obj,bouclier,fuiteTest)
salle_16(joueur,garde_arc2,coup_Garde_arc2,d_Garde_arc2,arme,liste_sorts,liste_obj,bouclier,fuiteTest)
salle_shop(joueur,arme,liste_sorts,liste_obj,bouclier)
salle_avantboss(joueur,arme,liste_sorts,liste_obj,bouclier,fuiteTest,liste_ennemis,mode)
if mode["mode"]=="normal":
    salle_boss_normal(joueur,romulus_boss_normal,coup_romulus_normal,d_romulus_normal,arme,liste_sorts,liste_obj,bouclier,fuiteTest)
elif mode["mode"]=="fuite":
    salle_boss_fuite(joueur,romulus_boss_normal,coup_romulus_normal,d_romulus_fuite,arme,liste_sorts,liste_obj,bouclier,fuiteTest)
elif mode["mode"]=="hard":
    salle_boss_hard(joueur,romulus_boss_hard,coup_romulus_hard,d_romulus_hard,arme,liste_sorts,liste_obj,bouclier,fuiteTest)
print("Merci d'avoir joué à Descension démo!")
input("Entrez une touche pour quitter le jeu.")
