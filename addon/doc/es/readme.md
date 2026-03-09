# EAB Extender#

* El autor: LUMEN PL
* La compatibilidad con NVDA: 2019.3

#Descripción#
Este complemento permite a los usuarios asignar atajos de teclado personalizados a la Easy-Access Bar (EAB) en los dispositivos braille de Papenmeier. El complemento reconoce automáticamente la aplicación activa, lo que permite crear múltiples configuraciones de EAB para cada aplicación.

Es posible cambiar rápidamente entre varias configuraciones de una misma aplicación, lo que amplía significativamente la funcionalidad de la EAB. Por ejemplo, una configuración puede utilizarse para mover la línea braille en un documento de texto, mientras que otra se puede configurar para navegar por el menú de la aplicación.

#Dispositivos compatibles#
A continuación se muestra una lista de dispositivos Papenmeier compatibles:
* BRAILLEX Live / Live+ / Live 20
* BRAILLEX Trio
* BRAILLEX EL 40c/60c/80c
* BRAILLEX 40s/66s/80s

#Definiciones#
Para conocer las definiciones de las teclas mencionadas en este documento, consulte el manual del dispositivo.

#Configuración predeterminada#
De manera predeterminada, el dispositivo Papenmeier utiliza la configuración estándar de NVDA para la EAB, que se aplica al crear una nueva configuración.
A continuación se muestra la lista de ajustes de EAB en la configuración predeterminada:
* EAB izquierda: mueve la visualización hacia la izquierda
* EAB derecha: mueve la línea braille hacia la derecha
* EAB arriba: mueve la línea braille una columna hacia arriba
* EAB abajo: mueve la línea braille una columna hacia abajo
* Routing + EAB izquierda: mueve el objeto del navegador al objeto anterior
* Routing + EAB derecha: mueve el objeto del navegador al siguiente objeto
* Routing + EAB arriba: mueve el objeto del navegador al objeto padre
* Routing + EAB abajo: mueve el objeto del navegador al primer objeto hijo

#Ventana del menú principal#
Para abrir el menú principal, presione el botón R1 en el dispositivo braille Papenmeier. Este menú se puede navegar fácilmente usando la EAB.

En el menú de EAB Extender, la EAB funciona de la siguiente manera:
* Presionar EAB arriba, abajo, izquierda o derecha emula las flechas arriba/abajo, permitiendo desplazarse por las configuraciones disponibles.
* Tecla de Routing + EAB derecha emula la tecla Tab, lo que permite moverse entre los botones de la ventana.
* Tecla de Routing + EAB izquierda emula Shift+Tab, lo que permite moverse entre los botones en orden inverso.
* Tecla de Routing + EAB abajo emula la tecla Enter.
* Tecla de Routing + EAB arriba emula la tecla Esc.

#Botones del menú principal#
* OK – activa la configuración seleccionada y cierra la ventana.
* Definir – permite definir los atajos de teclado en una configuración.
* Cambiar nombre – cambia el nombre de la configuración seleccionada.
* Eliminar – elimina la configuración seleccionada.
* Nuevo – crea una nueva configuración y abre un cuadro de diálogo para asignarle un nombre.
* Cerrar – cierra el menú sin realizar cambios.

#Ventana de configuración#
Esta ventana muestra ocho posiciones de la EAB, a las que se pueden asignar atajos de teclado personalizados.
* Use las teclas de flecha para seleccionar una posición de EAB.
* Presione Enter en una posición para activar el modo de captura de teclas, luego presione el atajo de teclado deseado para asignarlo a la posición seleccionada.
* Cuando termine, seleccione OK para guardar o Cerrar para salir sin guardar.

#Configuración de braille#
Al presionar la tecla L2, se abre un menú de NVDA que contiene las configuraciones de braille.