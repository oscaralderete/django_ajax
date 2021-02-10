# django_ajax
## Ejemplo del uso de Ajax con Django

Este es un código sencillo hecho para testear mis recientemente adquiridos skills con Django (a febrero del 2021) mientras voy siguiendo las lecciones del curso respectivo desarrollado por **PíldorasInformáticas** y que está disponible en:
https://www.youtube.com/watch?v=da3FIYSDMGQ

Yo programo PHP profesionalmente desde hace varios años atrás y debido a las mismas exigencias de mi profesión, actualmente tengo la necesidad de aprender Django, y en la "vida real" tarde o temprano será necesario interactuar con el lenguaje de servidor usando Ajax.

Así que para ir "calentando" decidí realizar este test. En general las Progressive Web Apps usan el enfoque de renderizar un index.html y luego, cuando la página ha terminado de cargarse hacen un request a un servidor para cargar los datos iniciales mediante una API, en este caso y dado que hay un lenguaje de servidor yo uso el enfoque de renderizar la data que usará la página junto con todo el HTML (les sugiero revisar el source para ir entendiendo el enfoque que usé para este ejemplo por si alguien sale con algo parecido a: "Yo uso React/Angular/Otros JS frameworks y la carga de datos es así o asá...").

Ajax, como todos saben (o debería saber) es una técnica de programación que evita tener que renderizar TODO el contenido web de una página cuando el usuario desencadene eventos **CRUD**, de **navegación** u otras interacciones. En el ejemplo uso el muy conocido jQuery y otra librería JS para darle reactividad al ejemplo que se llama **VueJS** y que en mi opinión es la mejor en su tipo.

Espero que el ejemplo les sea útil y les sirva de inspiración para hacer cosas por cuenta propia, creo que el profesor Juan hace un gran esfuerzo transmitiendo su conocimiento de forma paciente y constante lo cual es meritorio, pero en cierto punto nos toca a nosotros hacer cosas por cuenta propia, un poco en la tónica: "él nos enseña a caminar, pero a dónde lleguemos depende por entero de nosotros".

