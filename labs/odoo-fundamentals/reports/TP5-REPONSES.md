# Réponses au TP5 - Sécurité et Gestion des Droits

## Partie 1 : Création des Groupes de Sécurité

### Exercice 1 & 2 : Groupes et Hiérarchie
Nous avons créé le fichier `security/security.xml` avec deux groupes principaux sous une nouvelle catégorie "Éducation / Gestion Étudiants" :
*   **Enseignant (`group_enseignant`)** : Groupe de base pour les professeurs.
*   **Admin Éducation (`group_admin_education`)** : Groupe administrateur qui hérite des droits du groupe Enseignant via `implied_ids`.

```xml
<record id="group_admin_education" model="res.groups">
    <field name="name">Admin Éducation</field>
    <field name="implied_ids" eval="[(4, ref('group_enseignant'))]"/>
</record>
```

## Partie 2 : Configuration des Droits d'Accès

### Exercice 3 & 4 : Droit sur le modèle Professeur
Le fichier `security/ir.model.access.csv` a été configuré pour différencier les accès :
*   **Enseignants** : Peuvent lire (`perm_read=1`) et modifier (`perm_write=1`) les professeurs, mais ne peuvent pas créer (`perm_create=0`) ni supprimer (`perm_unlink=0`).
*   **Admins Éducation** : Ont un accès complet (CRUD) sur le modèle professeur.
*   **Tous les utilisateurs (`base.group_user`)** : Conservent un accès complet aux modèles Étudiant et Cours pour simplifier les tests du TP.

### Exercice 5 : Manifeste
Le fichier `security/security.xml` a été ajouté dans le `__manifest__.py` **avant** le fichier CSV pour s'assurer que les groupes existent au moment où les droits d'accès sont définis.

## Partie 3 : Test des Permissions

### Exercice 6, 7 & 8 : Observations des tests

| Utilisateur | Groupe | Accès Professeurs | Accès Étudiants/Cours |
| :--- | :--- | :--- | :--- |
| **Prof Test** | Enseignant | Lecture et Edition possible. Les boutons "Nouveau" et "Supprimer" sont masqués. | Accès complet. |
| **Admin Test** | Admin Éducation | Accès complet. Les boutons "Nouveau" et "Supprimer" sont visibles. | Accès complet. |

**Différences d'interface observées :**
1.  **Boutons d'action** : L'interface d'Odoo s'adapte dynamiquement. Pour l'Enseignant, le bouton "Créer" (ou "Nouveau") disparaît de la vue liste et du formulaire des professeurs.
2.  **Menu Action** : L'option "Supprimer" dans le menu "Action" est absente pour l'utilisateur ayant uniquement le groupe Enseignant sur le modèle Professeur.
3.  **Héritage** : L'Admin Test voit tout ce que le Prof Test voit, plus les droits de création/suppression, confirmant que l'héritage (`implied_ids`) fonctionne correctement.

## Questions de réflexion

### 1. Quelle est l'utilité des catégories dans les groupes ?
Les catégories permettent d'organiser les groupes dans l'interface de gestion des utilisateurs (Configuration > Utilisateurs). Cela permet de regrouper les droits par métier ou par module, rendant la configuration plus lisible.

### 2. Pourquoi l'ordre des fichiers dans le manifeste est-il important ?
Odoo charge les fichiers dans l'ordre de la liste `data`. Si le fichier CSV fait référence à un groupe (ex: `group_enseignant`) défini dans un fichier XML, ce fichier XML doit être chargé en premier, sinon Odoo lèvera une erreur car il ne trouvera pas l'identifiant du groupe.
