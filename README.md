# Sistema de Gestión de Vehículos — Actividad Individual 3

Proyecto en Python para abrir directamente en **Visual Studio Code**.

## Cómo abrirlo y ejecutarlo

1. Descomprime el archivo `.zip`.
2. En VS Code, ve a **Archivo > Abrir carpeta** y selecciona `Sistema_de_Vehiculos_VSCode`.
3. Abre `main.py` y presiona el botón **▶ Ejecutar archivo Python** (requiere Python instalado y la extensión Python de VS Code).
4. Otra opción: abre la terminal integrada y ejecuta:

   ```bash
   python main.py
   ```

   En algunos equipos funciona como `python3 main.py`.

## Pruebas

En la terminal de VS Code puedes ejecutar:

```bash
python -m unittest -v
```

## Contenido

- `main.py`: código corregido del caso, clases y demostración.
- `test_vehiculos.py`: pruebas de abstracción, herencia, métodos y polimorfismo.
- `.vscode/launch.json`: configuración para ejecutar/depurar con F5.

## Explicación breve

`Vehiculo` es abstracta. `Automovil` y `Camion` heredan por separado de ella.
Cada subclase implementa `encender()` y conserva solo sus métodos particulares.
Así se evita la herencia múltiple incorrecta y se aplica polimorfismo.

No requiere instalar librerías adicionales.
