===============================
Gestión de Taxis PRO
===============================

.. image:: static/description/icon.png
   :alt: Gestión de Taxis PRO
   :width: 100

Módulo completo para la gestión de flotas de taxis, conductores, tarifas y viajes.

**Versión**: 1.1  
**Categoría**: Transporte  
**Licencia**: LGPL-3  

Características Principales
============================

Este módulo proporciona una solución integral para empresas de taxis que necesitan gestionar:

🚕 **Gestión de Taxis**
-----------------------
- Registro completo de vehículos
- Control de matrícula, marca y modelo
- Estado activo/inactivo de cada taxi
- Seguimiento de la flota completa



👨‍✈️ **Gestión de Conductores**
-------------------------------
- Base de datos de conductores
- Información de contacto (teléfono)
- Número de licencia
- Asignación de taxi a conductor
- Estado activo/inactivo



💰 **Gestión de Tarifas**
-------------------------
- Tarifas personalizables
- Precio base del servicio
- Precio por kilómetro
- Precio por minuto de espera
- Múltiples tarifas (diurna, nocturna, festiva, etc.)



🚖 **Gestión de Viajes**
------------------------
- Registro detallado de cada viaje
- Selección de conductor y taxi
- Puntos de origen y destino
- Cálculo automático de precio basado en:
  * Distancia recorrida (km)
  * Tiempo de espera (minutos)
  * Tarifa aplicada
- Control de estados del viaje:
  * **Pendiente**: Viaje programado
  * **En progreso**: Viaje en curso
  * **Completado**: Viaje finalizado
  * **Cancelado**: Viaje cancelado
- Registro automático de fechas de inicio y fin



Flujo de Trabajo
================

1. **Configuración Inicial**
   
   a. Registrar taxis en el sistema
   b. Dar de alta conductores
   c. Configurar tarifas

2. **Operación Diaria**
   
   a. Crear nuevo viaje (estado: Pendiente)
   b. Asignar conductor, taxi y tarifa
   c. Ingresar origen, destino, distancia y tiempo de espera
   d. El sistema calcula automáticamente el precio
   e. Iniciar el viaje (cambia a: En progreso)
   f. Completar el viaje (cambia a: Completado)

3. **Gestión y Control**
   
   - Visualizar todos los viajes activos
   - Filtrar por estado, conductor o taxi
   - Generar reportes de ingresos
   - Analizar rendimiento de la flota

Instalación
===========

1. Copiar el módulo en la carpeta `addons` de Odoo
2. Actualizar la lista de aplicaciones
3. Buscar "Gestión de Taxis PRO"
4. Hacer clic en "Instalar"

Configuración
=============

Después de instalar el módulo:

1. Ir a **Gestión Taxis → Taxis** y registrar los vehículos
2. Ir a **Gestión Taxis → Conductores** y dar de alta al personal
3. Ir a **Gestión Taxis → Tarifas** y configurar los precios
4. Ir a **Gestión Taxis → Viajes** para comenzar a registrar servicios

Requisitos
==========

- Odoo 19.0
- Módulos base: `base`, `account`

Cálculo de Precios
==================

El precio de cada viaje se calcula automáticamente con la fórmula:

.. code-block:: text

   Precio Total = Precio Base + (Distancia × Precio/km) + (Minutos Espera × Precio/min)

**Ejemplo:**

- Precio Base: €3.00
- Distancia: 10 km × €1.50/km = €15.00
- Tiempo de Espera: 5 min × €0.50/min = €2.50
- **Total: €20.50**

Permisos y Seguridad
====================

El módulo incluye reglas de acceso para:

- `taxi.taxi`: Gestión de vehículos
- `taxi.conductor`: Gestión de conductores
- `taxi.tarifa`: Gestión de tarifas
- `taxi.viaje`: Gestión de viajes

Por defecto, todos los usuarios tienen acceso completo. Se recomienda configurar grupos de usuarios específicos según las necesidades de la empresa.

Soporte Técnico
===============

Para soporte técnico o consultas:

- **Empresa**: Tu Empresa
- **Website**: https://www.tuempresa.com
- **Email**: soporte@tuempresa.com

Actualizaciones y Mejoras
==========================

**v1.1** (Actual)
- Gestión básica de taxis, conductores, tarifas y viajes
- Cálculo automático de precios
- Control de estados de viajes
- Interfaz intuitiva compatible con Odoo 19

Créditos
========

- **Autor**: Tu Empresa
- **Mantenedor**: Tu Empresa
- **Licencia**: LGPL-3


