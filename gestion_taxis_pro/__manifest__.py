{
    'name': 'Gestión de Taxis PRO',
    'version': '1.1',
    'category': 'Transport',
    'summary': 'Gestión completa de flota de taxis, conductores, tarifas y viajes',
    'description': """
    Gestión de Taxis PRO
    ====================
    
    Sistema completo para la gestión de flotas de taxis que incluye:
    
    * 🚕 Gestión de vehículos (taxis) con matrícula, marca y modelo
    * 👨‍✈️ Gestión de conductores con licencias y asignación de taxis
    * 💰 Sistema de tarifas personalizables (diurna, nocturna, festivos, aeropuerto)
    * 🚖 Control completo de viajes con estados (pendiente, en progreso, completado, cancelado)
    * 💵 Cálculo automático de precios según tarifa, distancia y tiempo de espera
    * 📊 Datos de demostración incluidos para pruebas rápidas
    * 🎯 Interfaz intuitiva y fácil de usar
    
    Características principales:
    - Registro completo de vehículos con estado activo/inactivo
    - Control de conductores con información de contacto y licencia
    - Tarifas configurables con precio base, precio/km y precio/minuto
    - Gestión de viajes de principio a fin con seguimiento de fechas
    - Cálculo automático: Precio = Base + (Distancia × Precio/km) + (Espera × Precio/min)
    
    Perfecto para empresas de taxis, flotas privadas y servicios de transporte.
    
    Documentación completa: https://juancarlosmacias.es/article/modulo-de-gestion-de-flotas-de-taxis-con-odoo
    """,
    'author': 'Juan Carlos Macías',
    'website': 'https://www.juancarlosmacias.es/article/modulo-de-gestion-de-flotas-de-taxis-con-odoo',
    'support': 'juancarlosmaciassalvador@gmail.com',
    
    # Pricing for Odoo Apps Store
    'price': 49.99,
    'currency': 'EUR',
    
    # Images for store
    'images': [
        'static/description/banner.png',
        'static/description/completado.png',
        'static/description/lista_conductor.png',
        'static/description/lista_tarifa.png',
        'static/description/lista_taxis.png',
        'static/description/lista_viajes.png',
    ],
    
    'depends': ['base', 'account'],
    'data': [
        'security/ir.model.access.csv',
        'views/viaje_views.xml',
        'views/taxi_views.xml',
        'views/conductor_views.xml',
        'views/tarifa_views.xml',
    ],
    'demo': [
        'demo/demo_tarifas.xml',
        'demo/demo_taxis.xml',
        'demo/demo_conductores.xml',
        'demo/demo_viajes.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
