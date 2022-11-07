# Entrega-intermedia-del-proyecto-final---Coderhouse

El proyecto es sobre un Notebook - blog que permite agregar Homework, appointments y Meetings cada uno mediante su propio formulario alojando los datos en la base de datos.

El app principal llamada (web_own) donde se configuran las settings se dejo intacta y se trabajo sobre una app adicional nombrada (blog_own).

La pagina principal de la app adicional, permite navegar por formularios de agregacion y busqueda para cada uno de los modelos (Homework, appointment y Meetings), a travez de botones intuitivos.

Adiconalmente, se tomo como criterio de busqueda para los modelos una fecha (la del objeto) que se asigno cuando se creo, todos los objetos de esa clase que tengan esa relacionada esa fecha se mostraran.
La forma de agregar la fecha en los Adders (los formularios de agregación) es así: yyyy-mm-dd.

Para hacer los htmls se emplea herencia en los templates partiendo siempre del archivo father.html alojado en el directorio templates, de la app blog_own.
