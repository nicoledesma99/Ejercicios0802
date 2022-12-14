### 1. FORK

Primero debes forkear este repo, haciendo click en el botón `fork` de arriba a la derecha.

Una vez que tengas una copia de este repo en tu cuenta de `github`, cloná el repo dentro de una nueva carpeta (asegurate de no utilizar la misma que el prep curse). Una vez clonado entrá a esa carpeta y ejecutá los siguientes comandos:

    python testeo_ejercicios.py

>Si ves los tests fallando, estás listo para comenzar, si no lee bien el output para identificar el error.


### 2. RESOLVER LOS EJERCICIOS

Tu tarea es completar el código en `examen.py` de tal forma que pasen la mayoría de los tests.

### 3. ENTREGAR TU EXAMEN

Correr por ultima vez los tests y verificar cuantos pasan. Ten en cuenta que si te aparece "1 failed;1 total" es porque tienes un error de sintaxis: seguramente falta o sobra un corchete, paréntesis, dos puntos, etc.
Saca un print de pantalla de tus tests.
Luego, debes subir un commit a tu repo. Para hacerlo, debes ejecutar el siguiente comando:

    git add .
    git commit -m 'checkpoint commit'
    git push origin main

Una vez finalizado, chequea:
1. Que veas los cambios reflejados en el repo de tu cuenta de github (entrando a tu repo desde el browser.)
2. Que no haya un require - solo debe haber codigo dentro de las funciones de cada ejercicio 


### GUIA DE ERRORES COMUNES

Para identificar el error, vas a tener que leerlo en la consola.

* 1 failed, 1 total:
    1. Tenes un error de sintaxis. Revisa el último ejercicio que hayas hecho, seguramente falta o sobra un corchete, paréntesis, dos puntos, etc.

* Author identity unknown.  
    1. Intenta ejecutar los siguientes comandos para configurar tu cuenta:
        * git config --global user.name "Tu usuario de GitHub aca"
        * git config --global user.email "Tu email aca"

    2. Ingresa a [Github](https://docs.github.com/es/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token) y sigue las instrucciones para configurar tu token. 

* La consola se tilda en `Runs`:
    1. Revisa tu código, tenes un bucle infinito. Tenes que checkear la condición de corte de tus bucles.
