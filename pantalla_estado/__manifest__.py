{
    "name": "Pantalla Estado",
    "version": "1.0",
    "category": "Custom",
    "summary": "Pantalla a pantalla completa con actualización en tiempo real",
    "depends": ["base", "website"],
    "data": [
        "security/ir.model.access.csv",
        "views/template.xml",
        "views/views_backend.xml",
    ],
    "assets": {
        "web.assets_backend": [
            "/pantalla_estado/static/src/js/pantalla_estado.js"
        ]
    },
    "installable": True,
    "application": True,
    "auto_install": False,
}
