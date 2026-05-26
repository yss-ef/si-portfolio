# Réponses au TP4 - Vues Avancées

## Partie 1 : Vue Kanban (Étudiants)

### Exercice 1, 2 & 3 : Implémentation Kanban et Photo
*   **Modèle :** Ajout d'un champ `photo = fields.Binary(string='Photo')` dans `models/etudiant.py`.
*   **Vue Formulaire :** Utilisation du widget `image` pour le champ photo :
    ```xml
    <field name="photo" widget="image" class="oe_avatar"/>
    ```
*   **Vue Kanban :** Création de la vue `<kanban>` dans `views/etudiant_view.xml` affichant la photo, le nom, le prénom, le numéro d'étudiant et le sexe.
*   **Action :** Mise à jour de `etudiant_action` pour définir `kanban` comme vue par défaut :
    ```xml
    <field name="view_mode">kanban,tree,form</field>
    ```

## Partie 2 : Vue Graphique (Cours)

### Exercice 4 & 5 : Statistiques des cours
*   **Vue Graphique :** Création de la vue `<graph>` dans `views/cours_view.xml` :
    ```xml
    <graph string="Statistiques des cours">
        <field name="niveau" type="row"/>
        <field name="credits" type="measure"/>
    </graph>
    ```
*   **Action :** Ajout de la vue `graph` dans `cours_action` :
    ```xml
    <field name="view_mode">tree,form,graph</field>
    ```

## Partie 3 : Vue de Recherche Avancée (Professeurs)

### Exercice 6 : Filtres et Groupements
*   **Vue Search :** Création de la vue `<search>` dans `views/professeur_view.xml` avec :
    *   **Champs de recherche :** nom, prénom, email, spécialité.
    *   **Filtres :** "Avec email", "Sans email", "Avec cours", "Sans cours".
    *   **Groupements :** "Spécialité", "Prénom".

## Questions de réflexion

### 1. Quels sont les avantages de la vue Kanban par rapport à la vue liste ?
La vue Kanban est beaucoup plus visuelle et intuitive. Elle permet d'identifier rapidement un enregistrement grâce à des éléments comme la photo ou des codes couleurs. Elle est idéale pour une navigation rapide sur des volumes de données modérés et offre une expérience utilisateur plus moderne.

### 2. Dans quels contextes utiliseriez-vous une vue graphique ?
On utilise la vue graphique pour l'analyse de données (Reporting). Elle permet de visualiser instantanément des répartitions (ex: nombre de cours par niveau) ou des cumuls (ex: somme des crédits par niveau), ce qui aide à la prise de décision.

### 3. Comment les filtres de recherche améliorent-ils l'expérience utilisateur ?
Ils permettent de trouver l'information pertinente beaucoup plus rapidement en limitant le bruit visuel. Les filtres prédéfinis évitent à l'utilisateur de devoir construire des requêtes complexes manuellement, et les groupements permettent de structurer l'information de manière logique (ex: voir tous les professeurs regroupés par leur spécialité).
