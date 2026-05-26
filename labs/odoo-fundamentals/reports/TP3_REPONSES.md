# Réponses au TP3 - Contraintes et Validations

## Partie 1 : Contraintes SQL

Les contraintes SQL ont été ajoutées aux modèles pour garantir l'intégrité des données au niveau de la base de données PostgreSQL.

### Exercice 1 : Unicité du code du cours
Dans `models/cours.py` :
```python
_sql_constraints = [
    ('code_unique', 'unique(code)', 'Le code du cours doit être unique !'),
    ...
]
```

### Exercice 2 : Crédits positifs
Dans `models/cours.py` :
```python
_sql_constraints = [
    ...
    ('credits_positif', 'CHECK(credits >= 0)', 'Le nombre de crédits doit être positif.')
]
```

### Exercice 3 & 4 : Email du professeur (Unicité et Format)
Dans `models/professeur.py` :
```python
_sql_constraints = [
    ('email_unique', 'unique(email)', 'L\'email du professeur doit être unique !'),
    ('email_format', "CHECK(email LIKE '%@%.%')", 'Le format de l\'email du professeur semble incorrect.')
]
```

## Partie 2 : Validations Python

### Exercice 5 : Limitation du nombre d'étudiants
Dans `models/cours.py`, nous avons utilisé `@api.constrains` pour limiter à 3 étudiants maximum par cours.
```python
@api.constrains('etudiant_ids')
def _check_max_etudiants(self):
    for record in self:
        if len(record.etudiant_ids) > 3:
            raise ValidationError("Un cours ne peut pas avoir plus de 3 étudiants inscrits !")
```

## Questions de réflexion

### 1. Quelle est la différence entre une contrainte SQL et une validation Python ?
*   **Contrainte SQL :** Elle est définie au niveau de la base de données (PostgreSQL). Elle est extrêmement rapide et garantit l'intégrité même si les données sont modifiées via des scripts externes ou SQL direct. Elle est limitée à des vérifications simples sur les colonnes de la même table.
*   **Validation Python (`@api.constrains`) :** Elle est exécutée par le serveur Odoo en Python. Elle est beaucoup plus flexible et permet de faire des vérifications complexes (ex: compter des enregistrements liés, comparer avec d'autres modèles, utiliser de la logique métier complexe). Elle ne s'applique que lorsque les données passent par l'ORM d'Odoo.

### 2. Dans quels cas préférez-vous utiliser l'une plutôt que l'autre ?
*   On préfère les **contraintes SQL** pour l'unicité (`unique`) et les vérifications de format ou de plage de valeurs simples (`CHECK`), car elles sont plus performantes et robustes.
*   On préfère les **validations Python** pour tout ce qui implique des relations entre modèles (Many2many, One2many) ou des calculs impossibles ou trop complexes en SQL standard.

### 3. Que se passe-t-il si vous essayez de créer un cours avec un code déjà existant ?
Le serveur Odoo intercepte l'erreur levée par PostgreSQL et affiche une fenêtre d'alerte à l'utilisateur avec le message défini dans la contrainte : *"Le code du cours doit être unique !"*. La transaction est annulée et l'enregistrement n'est pas sauvegardé.
