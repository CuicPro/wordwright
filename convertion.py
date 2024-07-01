def convertir_en_format(texte):
    mots = texte.split()  # Sépare le texte en mots
    mots_format = ['"{}"'.format(mot) for mot in mots]  # Crée une liste de mots formatés
    texte_format = ",\n".join(mots_format)  # Combine les mots formatés avec une virgule et un saut de ligne
    return texte_format

# Exemple d'utilisation :
espace_de_texte = """
grand
petit
autre
seul
jeune
premier
bon
quel
beau
vieux
noir
nouveau
dernier
blanc
cher
long
pauvre
plein
vrai
toute
bas
gros
doux
heureux
haut
profond
rouge
humain
général
français
froid
sombre
sûr
ancien
propre
politique
possible
immense
public
pareil
bleu
fort
entier
simple
nécessaire
mauvais
social
important
certain
triste
joli
différent
ne
pas
plus
bien
si
là
même
tout
encore
aussi
peu
alors
toujours
jamais
non
très
ainsi
moins
ici
oui
trop
déjà
tant
enfin
maintenant
beaucoup
assez
loin
point
presque
ailleurs
seulement
aujourd'hui
mieux
autour
souvent
dessus
longtemps
fort
comme
comment
autant
d'abord
surtout
cependant
vite
tard
pourtant
ci
mal
parfois
vraiment
bientôt
partout
debout
plutôt
lentement
combien
hier
et
que
comme
mais
ou
quand
si
puis
donc
car
ni
parce que
pourquoi
lorsque
tandis que
puisque
comment
soit
or
deux
cent
mille
trois
quatre
vingt
cinq
dix
neuf
six
huit
sept
trente
quarante
cinquante
quinze
douze
un

dans
pour
par
sur
avec
sans
sous
après
entre
vers
chez
jusque
contre
devant
depuis
pendant
avant
voilà
près
malgré
voici
selon
derrière
parmi
afin de
auprès
hors
durant
gràce
plein

homme
mari
femme
jour
mer
temps
main
chose
vie
yeux
heure
monde
enfant
fois
moment
tête
père
fille
coeur
terre
dieu
monsieur
voix
maison
coup
air
mot
nuit
eau
ami
porte
amour
pied
gens
nom
pays
ciel
frère
regard
âme
mort
esprit
ville
rue
soir
chambre
pas
soleil
roi
état
corps
bras
place
parti
année
visage
bruit
lettre
franc
fond
force
effet
milieu
saint
idée
travail
lumière
mois
fils
raison
point
personne
peuple
fait
parole
guerre
pensée
affaire
matin
pierre
vent
doute
front
ombre
part
maître
besoin
question
peine
tour
famille
madame
sorte
figure
droit
peur
bout
lieu
silence
chef
bois
mari
histoire
feu
partie
face
mouvement
fin
route
livre
arbre
cas
mur
ordre
est
bonheur
intérêt
argent
cause
travers
grand
instant
façon
oeil
forme
chemin
cheveu
plaisir
suite
sang
sentiment
fleur
service
table
paix
moyen
lit
voiture
être
nature
or
pouvoir
nouveau
joie
président
bouche
petit
sens
cri
espèce
cheval
loi
ministre
société
politique
oreille
fenêtre
fortune
compte
champ
manier
action
garçon
exemple
couleur
papier
mal
pièce
montagne
sol
oeuvre
cours
désir
cour
bord
douleur
salle
premier
projet
étude
journal
geste
situation
oiseau
siècle
million
prix
groupe
centre
malheur
honneur
garde
problème
larme
chien
peau
reste
nombre
mesure
article
vue
âge
système
long
effort
rêve
passion
rapport
soldat
lèvre
signe
vérité
mariage
plan
dos
marche
souvenir
dame
conseil
sou
coin
jardin
doigt
objet
fer
lendemain
train
papa
valeur
jeu
secret
haut
vieillard
docteur
ton
jambe
endroit
minute
nuage
présence
épaule
feuille
liberté
journée
avenir
sourire
résultat
hôtel
semaine
forêt
qualité
prince
bien
médecin
volonté
seigneur
art
foule
ligne
intérieur
beauté
soin
hasard
condition
classe
voyage
avoir
faire
dire
pouvoir
aller
voir
vouloir
venir
devoir
prendre
trouver
donner
falloir
parler
mettre
savoir
passer
regarder
aimer
croire
demander
rester
répondre
entendre
penser
arriver
connaître
devenir
sentir
sembler
tenir
comprendre
rendre
attendre
sortir
vivre
entrer
reprendre
porter
chercher
revenir
appeler
mourir
partir
jeter
suivre
écrire
montrer
tomber
ouvrir
arrêter
perdre
commencer
paraître
marcher
lever
permettre
asseoir
écouter
monter
apercevoir
recevoir
servir
finir
rire
crier
jouer
tourner
garder
reconnaître
quitter
manger
courir
continuer
oublier
descendre
cacher
poser
tirer
présenter
ajouter
agir
retrouver
offrir
apprendre
tuer
retourner
rencontrer
envoyer
dormir
pousser
rappeler
lire
changer
essayer
compter
occuper
expliquer
frapper
travailler
obtenir
rentrer
pleurer
répéter
payer
apporter
exister
boire
sourire
coucher
causer
raconter
serrer
songer
manquer
nommer
conduire
saisir
demeurer
remettre
disparaître
battre
toucher
apparaître
souffrir
fermer
accepter
tendre
naître
sauver
avancer
traverser
souvenir
couvrir
gagner
former
plaire
embrasser
oser
empècher
refuser
décider
produire
charger
espérer
cesser
ressembler
chanter
approcher
prier
échapper
glisser
briller
brûler
placer
juger
suffire
atteindre
annoncer
élever
acheter
mener
préparer
assurer
deviner
considérer
appartenir
représenter
tromper
vendre
craindre
emporter
exprimer
rouler
possèder
réveiller
aider
découvrir
choisir
prononcer
taire
rêver
appuyer
étendre
trembler
défendre
créer
maintenir
indiquer
promettre
relever
abandonner
ignorer
accompagner
adresser
observer
séparer
marier
prévoir
amener
obliger
éclairer
poursuivre
livrer
contenir
fuir
couler
proposer
éprouver
retenir
attacher
voler
entraîner
surprendre
briser
imaginer
diriger
parvenir
pénétrer
remarquer
éviter
établir
réussir
pencher
habiter
entourer
déclarer
étonner
dresser
durer
fixer
désirer
arracher
soutenir
couper
examiner
douter
retirer
promener
forcer
revoir
remplir
terminer
tenter
remonter
installer
soulever
allumer
imposer
respirer
baisser
souffler
attirer
prêter
amuser
éclater
réunir
traiter
engager
traîner
employer
marquer
prouver
importer
exiger
reposer
danser
saluer
accorder
achever
avouer
distinguer
emmener
agiter
hésiter
sonner
composer
enlever
chemise
siège
as
patron
calme
printemps
angoisse
habitant
métier
note
fusil
agent
roman
plante
réflexion
accent
repas
étendue
secours
corde
saison
paupière
tapis
chasse
clef
sueur
ferme
instinct
paquet
drame
savoir
mine
vision
sentier
demain
planche
dehors
salut
tâche
abri
rencontre
rouge
lien
queue
bande
grain
mensonge
contenter
mériter
précipiter
rompre
caresser
étouffer
animer
casser
fonder
franchir
abattre
discuter
fatiguer
consentir
regretter
joindre
vaincre
consulter
repousser
exécuter
exposer
voyager
renverser
rassurer
retomber
décrire
mentir
armer
étaler
essuyer
précéder
désigner
détacher
recueillir
croiser
entretenir
surveiller
réserver
confondre
dégager
"""

texte_converti = convertir_en_format(espace_de_texte)
print(texte_converti)
