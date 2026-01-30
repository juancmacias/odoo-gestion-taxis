{
    "name": "Word Search Gamification",
    "version": "1.0.0",
    "summary": "Gamificación empresarial con sopas de letras para Odoo 19",
    "description": """
        Word Search Gamification - Sopas de Letras Interactivas
        ========================================================
        
        Impulsa el engagement de tu equipo con juegos de sopas de letras personalizables.
        
        Características principales:
        ----------------------------
        * 🎯 Creación y gestión de juegos personalizados
        * 🕹️ Interfaz interactiva con click-and-drag
        * 📊 Seguimiento completo de intentos y estadísticas
        * 🏆 Tabla de clasificación global
        * ⏱️ Temporizador y sistema de puntuación automático
        * 📱 Diseño responsive para cualquier dispositivo
        * 🎨 Animaciones y efectos visuales modernos
        
        Beneficios:
        -----------
        * Mejora la motivación laboral
        * Fomenta la competencia sana entre empleados
        * Proporciona pausas activas productivas
        * Estimula habilidades cognitivas
        * Fortalece el espíritu de equipo
        
        Configuración:
        --------------
        1. Crea un banco de palabras personalizadas
        2. Configura el tamaño del tablero (10x10 a 20x20)
        3. Activa el juego para generar la sopa de letras
        4. Los empleados acceden desde el portal web
        
        Sistema de puntuación: Longitud de palabra × 10 puntos
        
        Compatible con Odoo 19.0
    """,
    "category": "Human Resources",
    'author': 'Juan Carlos Macías',
    'website': 'https://www.juancarlosmacias.es',
    'support': 'juancarlosmaciassalvador@gmail.com',
    "icon": "/word_search_gamification/static/description/icon.png",
    "depends": ["base", "hr", "web", "website"],
    "data": [
        "security/ir.model.access.csv",
        "views/game_views.xml",
        "views/word_views.xml",
        "views/attempt_views.xml",
        "views/leaderboard_views.xml",
        "views/game_play_template.xml",
    ],
    "assets": {
        "web.assets_frontend": [
            "word_search_gamification/static/src/css/game_play.css",
            "word_search_gamification/static/src/js/game_play.js",
        ],
    },
    "installable": True,
    "application": True,
    "license": "LGPL-3",
}
