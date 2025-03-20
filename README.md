# Evaluation et gestion medicale

# Guide d'installation et d'exécution d'un projet Django 🚀

## Prérequis
Avant de commencer, assurez-vous d'avoir installé :

- Python 
- pip (gestionnaire de paquets Python)
- virtualenv (optionnel mais recommandé)
- pdfkit
## Keep in mind

C'est essentiel d'installer wkhtmltopdf pour faire fonctionner pdfkit parce que pdfkit est simplement une interface Python qui s'appuie sur wkhtmltopdf pour convertir des pages HTML en PDF.

📌 Pourquoi pdfkit a besoin de wkhtmltopdf ?
pdfkit ne fait pas la conversion lui-même
→ Il envoie simplement des commandes à wkhtmltopdf pour effectuer la conversion.

wkhtmltopdf est un moteur de rendu basé sur WebKit
→ Il prend du HTML, le "rend" comme un navigateur, et génère un PDF.

Sans wkhtmltopdf, pdfkit ne peut pas fonctionner
→ Si wkhtmltopdf n'est pas installé, pdfkit ne sait pas quoi exécuter et renvoie une erreur du type :

sh
Copier
Modifier
No wkhtmltopdf executable found
## Installation
1. Créer un environnement virtuel (optionnel mais recommandé)

        python -m venv venv
   
2. Activer l'environnement virtuel
Windows :

        venv\Scripts\activate
   
Mac/Linux :

        source venv/bin/activate  
        
3. Installer Django

        pip install django
   
4. Création d'un projet Django

        django-admin startproject nom_du_projet  
        cd nom_du_projet  
5. Lancer le serveur de développement

        python manage.py runserver  
        Accédez à l'application via : http://127.0.0.1:8000/

6.Création d'une application Django

        python manage.py startapp nom_de_l_application  
        
7. Ajoutez l'application dans settings.py :


INSTALLED_APPS = [
    ...  
    'nom_de_l_application',  
]  

8. Exécuter les migrations

        python manage.py makemigrations  
        python manage.py migrate  
        
9. Création d'un superutilisateur (Admin)

        python manage.py createsuperuser  

RMQ:     
Suivez les instructions pour définir un nom d'utilisateur et un mot de passe.
Accédez à l'administration via : http://127.0.0.1:8000/admin/

_______________________________________________________________________________

Autres commandes utiles
- Vérifier les erreurs

      python manage.py check 

- Collecter les fichiers statiques

      python manage.py collectstatic  
    
- Créer un fichier de requirements

      pip freeze > requirements.txt  
    
- Installer les dépendances depuis un fichier requirements.txt

      pip install -r requirements.txt  
     ![Capture d'écran 2025-03-19 143855](https://github.com/user-attachments/assets/b29abc8e-c569-4b90-88a1-a5567951b11b)
![Capture d'écran 2025-03-19 144336](https://github.com/user-attachments/assets/e64cf6c7-58e0-4540-bd41-b1e4eb49e129)
![Capture d'écran 2025-03-19 145220](https://github.com/user-attachments/assets/4262a485-13c2-441c-981b-3dcc1dbc4e92)
![Capture d'écran 2025-03-19 141449](https://github.com/user-attachments/assets/aadd07f8-7970-4a02-86b2-0d649594a628)

