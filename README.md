# Evaluation_et_gestion_medicale

# Guide d'installation et d'exécution d'un projet Django 🚀

## Prérequis
Avant de commencer, assurez-vous d'avoir installé :

- Python 
- pip (gestionnaire de paquets Python)
- virtualenv (optionnel mais recommandé)

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
     
