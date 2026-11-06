<p align="center">
  <img src="header.svg" alt="Adrien Lavigne - Étudiant Data & IA" width="100%">
</p>

## À propos

Étudiant en Bachelor Data & Intelligence Artificielle à **Ynov Campus Sophia**. Je m'intéresse beaucoup à la finance, et j'essaie de relier ce domaine à mon parcours en data et en IA à travers des projets concrets.

- Badge **AWS Educate - Introduction to Cloud 101** (novembre 2026)
- Je prépare la certification **Fortinet NSE 1**
- Je travaille en Python, et j'apprends le cloud AWS et le développement web

## Projet à la une : briefing finance quotidien

Chaque matin en semaine, un e-mail me résume l'actualité financière (Le Monde, BBC, CNBC, BCE), avec les sources citées. Le tout tourne sur AWS, sans serveur à gérer.

<p align="center">
  <a href="https://github.com/ADsansGluten/daily-finance-briefing-aws">
    <img src="briefing-architecture.gif" alt="Architecture animée du briefing finance quotidien" width="100%">
  </a>
</p>

**EventBridge Scheduler → Lambda → Amazon Bedrock → S3 + SES**, avec une page web publique et une alerte CloudWatch + SNS.

[Voir le code et le guide pas à pas](https://github.com/ADsansGluten/daily-finance-briefing-aws)

## Prochain projet : la volatilité de l'or

<p align="center">
  <img src="gold.svg" alt="Prochain projet : prédire la volatilité de l'or (XAUUSD)" width="100%">
</p>

Je prépare une plateforme cloud automatisée sur AWS qui prédit la volatilité de l'or (XAUUSD). La question de départ : le machine learning fait-il mieux que le modèle classique GARCH(1,1) ? Je veux la traiter proprement, avec un découpage strict des données dans le temps pour éviter les fuites d'information.

## Mon équipe

<p align="center">
  <img src="equipe.svg" alt="Lambdon, Orino et Datum : les trois créatures du profil" width="100%">
</p>

- **Lambdon** (type Cloud) : il veille sur mes projets AWS, comme le [briefing finance quotidien](https://github.com/ADsansGluten/daily-finance-briefing-aws).
- **Orino** (type Finance) : il garde le projet sur la volatilité de l'or (XAUUSD).
- **Datum** (type Data) : il range les données et prépare les modèles.

<p align="center">
  <img src="contributions-creatures.svg" alt="Les créatures croquent les carrés du calendrier de contributions" width="100%">
</p>

## Outils

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![AWS](https://img.shields.io/badge/AWS-232F3E?style=for-the-badge&logo=amazonwebservices&logoColor=white)
![Git](https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white)
![HTML](https://img.shields.io/badge/HTML%20%2F%20CSS-E34F26?style=for-the-badge&logo=html5&logoColor=white)
