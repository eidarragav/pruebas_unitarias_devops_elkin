
## Informe completo

El informe detallado de esta actividad, con imágenes, capturas de ejecución y evidencias del proceso, se encuentra disponible en el siguiente documento:

[Ver informe completo de pruebas unitarias (PDF)](informe/informe.pdf)

## Pruebas unitarias y DevOps

En este proyecto se realizaron pruebas unitarias con **Pytest** para los módulos de calculadora, descuentos y conversor, utilizando el patrón **AAA (Arrange, Act, Assert)**. Durante las pruebas se identificaron y corrigieron errores en las funciones evaluadas, y se verificó la cobertura de código, alcanzando más del 85 % en cada uno de los tres módulos seleccionados.

Como actividad adicional, se trabajó con el módulo `csv_parser` para aplicar *mocking* e identificar un error en el procesamiento de campos CSV entre comillas.

Finalmente, se integró **GitHub Actions** mediante un workflow que ejecuta automáticamente las pruebas cada vez que se realiza un `push` al repositorio, facilitando la detección temprana de errores y la integración continua.

