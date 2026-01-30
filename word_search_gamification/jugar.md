# 🎮 Cómo Jugar al Word Search Gamification

## Descripción General

Word Search Gamification es un módulo de gamificación empresarial para Odoo 19 que permite crear y jugar sopas de letras interactivas. El sistema registra los intentos de los jugadores, calcula puntuaciones y mantiene una tabla de clasificación.

---

## 📋 Requisitos Previos

- Módulo instalado: **Word Search Gamification**
- Acceso al menú: **Gamification**
- Usuario con permisos adecuados (base.group_user)

---

## 🎯 Estructura del Juego

### Componentes Principales

1. **Juegos (Games)**: Sopas de letras configurables con palabras específicas
2. **Palabras (Words)**: Banco de palabras que se pueden usar en los juegos
3. **Intentos (Attempts)**: Registro de cada partida jugada
4. **Tabla de Clasificación (Leaderboard)**: Ranking de jugadores por puntuación

---

## 🚀 Paso a Paso para Jugar

### 1. Crear o Seleccionar Palabras

**Ruta**: `Gamification > Words`

1. Haz clic en **"Crear"**
2. Completa los campos:
   - **Word**: La palabra a buscar (2-15 caracteres, solo letras)
   - **Category**: Categoría temática (opcional)
   - **Language**: Idioma (Español, Inglés o Francés)
   - **Difficulty**: Dificultad (Easy, Medium, Hard)
3. Guarda la palabra

**Ejemplo**:
- Word: `ODOO`
- Category: `Software`
- Language: `Spanish`
- Difficulty: `Easy`

---

### 2. Crear un Nuevo Juego

**Ruta**: `Gamification > Games`

1. Haz clic en **"Crear"**
2. Completa la información básica:

   **Pestaña Principal**:
   - **Game Name**: Nombre del juego (obligatorio)
   - **Theme**: Tema del juego (opcional)
   - **Difficulty**: Nivel de dificultad (Easy/Medium/Hard)
   - **Grid Size**: Tamaño de la cuadrícula (5-20)
   - **Language**: Idioma del juego
   - **Active From**: Fecha de inicio (opcional)
   - **Active Until**: Fecha de fin (opcional)
   - **Active**: Marcar si está activo
   - **Total Attempts**: Se calcula automáticamente

   **Pestaña Description**:
   - Descripción del juego y las reglas

   **Pestaña Words**:
   - Selecciona las palabras que aparecerán en la sopa de letras
   - Puedes agregar múltiples palabras desde el banco de palabras

3. Cambia el **State** a **"Active"** cuando esté listo
4. Guarda el juego

**Ejemplo de Juego**:
```
Name: "Tecnología Empresarial"
Theme: "Software y Herramientas"
Difficulty: Medium
Grid Size: 12
Language: Spanish
Words: ODOO, ERP, CRM, PYTHON, DATABASE
```

---

### 3. Jugar una Partida

#### Método Actual (Backend)

Actualmente el módulo está configurado para registro manual de intentos:

**Ruta**: `Gamification > Attempts`

1. Haz clic en **"Crear"**
2. Completa los datos del intento:
   - **Player**: Se autoselecciona el usuario actual
   - **Game**: Selecciona el juego a jugar
   - **Time Spent**: Tiempo en segundos que tardaste
   - **Score**: Puntuación obtenida
   - **Completed**: Marca si completaste el juego
   - **Found Words JSON**: JSON con las palabras encontradas (opcional)

3. Guarda el intento

**Ejemplo de Intento**:
```
Player: Admin
Game: Tecnología Empresarial
Time Spent: 120 (2 minutos)
Score: 500
Completed: ✓
```

#### Sistema de Puntuación

- **Score**: Depende de las palabras encontradas
- **Time Spent**: El tiempo más bajo es mejor
- **Completed**: Indica si se encontraron todas las palabras

---

### 4. Ver la Tabla de Clasificación

**Ruta**: `Gamification > Leaderboard`

Aquí puedes ver:
- **User**: Nombre del jugador
- **Total Score**: Puntuación acumulada total
- **Games Played**: Número de partidas jugadas
- **Best Time**: Mejor tiempo registrado
- **Last Played**: Última vez que jugó

**Colores de Destacado**:
- 🟢 Verde: Jugadores con 1000+ puntos
- 🔵 Azul: Jugadores con 500-999 puntos

---

## 🎨 Características Técnicas

### Niveles de Dificultad

- **Easy**: Cuadrículas pequeñas (5-8), palabras cortas
- **Medium**: Cuadrículas medianas (9-14), palabras variadas
- **Hard**: Cuadrículas grandes (15-20), palabras largas

### Configuración de Cuadrícula

- **Mínimo**: 5x5
- **Máximo**: 20x20
- **Recomendado**: 10x10 para balance

### Idiomas Soportados

- 🇪🇸 Español (es)
- 🇬🇧 Inglés (en)
- 🇫🇷 Francés (fr)

---

## 📊 Estados del Juego

| Estado | Descripción |
|--------|-------------|
| **Draft** | Juego en borrador, no disponible para jugar |
| **Active** | Juego activo y disponible |
| **Archived** | Juego archivado, no visible por defecto |

---

## 🔍 Filtros y Búsquedas

### En Games
- **Active**: Solo juegos activos
- **Archived**: Solo juegos archivados
- **Draft**: Juegos en borrador
- **Active Games**: Juegos en estado activo
- Agrupar por: Difficulty, State, Language

### En Words
- **Active**: Palabras activas
- **Inactive**: Palabras inactivas
- Agrupar por: Category, Language, Difficulty

### En Attempts
- **Completed**: Intentos completados
- **Incomplete**: Intentos incompletos
- **My Attempts**: Solo tus intentos
- Agrupar por: Player, Game, Date

### En Leaderboard
- **Top Performers**: Jugadores con 500+ puntos
- Agrupar por: User

---

## 💡 Consejos y Buenas Prácticas

### Para Administradores

1. **Crea palabras temáticas**: Agrupa palabras por categorías relacionadas con tu empresa
2. **Varía la dificultad**: Ofrece juegos para diferentes niveles
3. **Establece fechas**: Usa Active From/Until para eventos especiales
4. **Revisa el leaderboard**: Premia a los mejores jugadores

### Para Jugadores

1. **Practica primero**: Comienza con juegos Easy
2. **Optimiza tu tiempo**: El mejor tiempo cuenta para el ranking
3. **Completa los juegos**: Solo los intentos completados suman al total
4. **Revisa el ranking**: Compite con tus compañeros

---

## 🔧 Validaciones del Sistema

El módulo incluye validaciones automáticas:

- ✅ Las palabras deben tener entre 2 y 15 caracteres
- ✅ Las palabras solo pueden contener letras
- ✅ El tamaño de cuadrícula debe estar entre 5 y 20
- ✅ La fecha "Active From" debe ser anterior a "Active Until"
- ✅ El tiempo y la puntuación no pueden ser negativos

---

## 📈 Actualización del Leaderboard

El sistema actualiza automáticamente la tabla de clasificación cuando:

1. Se crea un nuevo intento **completado** con puntuación
2. El jugador es nuevo: Se crea su entrada con la puntuación inicial
3. El jugador existe: 
   - Se suma la nueva puntuación al total
   - Se incrementa el contador de juegos jugados
   - Se actualiza el mejor tiempo si es menor
   - Se actualiza la fecha de última partida

---

## 🎯 Objetivos del Juego

El módulo está diseñado para:

- Fomentar la participación del equipo
- Crear competencia saludable
- Mejorar el ambiente laboral
- Gamificar el aprendizaje empresarial
- Integrar la diversión en el entorno de trabajo

---

## 📝 Notas Importantes

⚠️ **El módulo actualmente está configurado para registro manual**. Para jugar de forma interactiva en el navegador, se necesitaría desarrollar:

1. Un controlador web (Python)
2. Vistas frontend (JavaScript/OWL)
3. Templates interactivos (XML/JS)
4. Generador de cuadrículas en tiempo real

El código actual incluye un generador básico (`WordSearchGenerator`) que puede colocar palabras en una cuadrícula, pero necesita implementación frontend para ser completamente jugable.

---

## 🛠️ Estructura de Archivos

```
word_search_gamification/
├── models/
│   ├── word_search_game.py      # Modelo principal de juegos
│   ├── word_search_word.py      # Banco de palabras
│   ├── word_search_attempt.py   # Registro de intentos
│   ├── word_search_leaderboard.py # Tabla de clasificación
│   └── word_search_generator.py  # Generador de cuadrículas
├── views/
│   ├── game_views.xml           # Vistas de juegos
│   ├── word_views.xml           # Vistas de palabras
│   ├── attempt_views.xml        # Vistas de intentos
│   └── leaderboard_views.xml    # Vistas del ranking
├── security/
│   └── ir.model.access.csv      # Permisos de acceso
└── __manifest__.py              # Configuración del módulo
```

---

## 📞 Soporte

Para preguntas o problemas:
- Autor: Juan Carlos
- Versión: 1.0.0
- Licencia: LGPL-3

---

¡Disfruta jugando y gamificando tu entorno empresarial con Odoo! 🎉
