# Recomendaciones

## Branching

<img src="../../images/branching.png" width="600" >

Los temas de Branching en Git son una forma de organizar y agrupar ramas relacionadas en un proyecto.
En lugar de tener una gran cantidad de ramas independientes, puedes crear temas para categorizarlas por función, objetivo o proyecto.

**Ejemplos de temas de Branching:**

* **Por función:**
    * `feature/nueva-funcionalidad`
    * `bugfix/corregir-error-x`
* **Por objetivo:**
    * `release/preparar-version-1.0`
    * `hotfix/solucionar-problema-urgente`
* **Por proyecto:**
    * `proyecto-a/feature/nueva-caracteristica`
    * `proyecto-b/bugfix/corregir-error-y`

**Recomendaciones para usar temas de Branching:**

* **Define una convención de nombres clara y consistente.** Esto te ayudará a identificar fácilmente a qué tema pertenece una rama.
* **Utiliza temas para agrupar ramas relacionadas.** Esto te ayudará a mantener tu proyecto organizado y fácil de navegar.
* **Crea temas para cada nueva función o proyecto.** Esto te ayudará a aislar los cambios y evitar conflictos entre ramas.
* **Elimina los temas que ya no sean necesarios.** Esto te ayudará a mantener tu proyecto limpio y organizado.

**Tipos de Branching:**

* **Git Flow:** Este flujo de trabajo utiliza cuatro ramas principales:

    * **Master:** Rama principal del proyecto que contiene el código estable.
    * **Develop:** Rama donde se integran las nuevas funcionalidades y correcciones de errores.
    * **Feature:** Ramas que se crean para desarrollar nuevas funcionalidades.
    * **Hotfix:** Ramas que se crean para corregir errores críticos en la rama master.

* **GitHub Flow:** Este flujo de trabajo es más simple que Git Flow y solo utiliza dos ramas principales:

    * **Main:** Rama principal del proyecto que contiene el código estable.
    * **Feature:** Ramas que se crean para desarrollar nuevas funcionalidades o corregir errores.

* **Trunk-Based Development:** Este flujo de trabajo no utiliza ramas長期. Todos los cambios se realizan directamente en la rama principal.

**Ejemplos según tipo de branching:**

* **Git Flow:**

    * Se crea una rama `feature/nueva-funcionalidad` para desarrollar una nueva funcionalidad.
    * Cuando la nueva funcionalidad está lista, se fusiona con la rama `develop`.
    * Cuando la rama `develop` está lista para ser publicada, se fusiona con la rama `master`.

* **GitHub Flow:**

    * Se crea una rama `feature/nueva-funcionalidad` para desarrollar una nueva funcionalidad.
    * Cuando la nueva funcionalidad está lista, se crea una solicitud de pull para fusionarla con la rama `main`.
    * Si la solicitud de pull se aprueba, la nueva funcionalidad se fusiona con la rama `main`.

* **Trunk-Based Development:**

    * Se crea un commit directamente en la rama `trunk` para implementar una nueva funcionalidad.
    * Se realizan pruebas y revisiones del código antes de que se fusione con la rama `trunk`.

**Comparaciones:**

| Tipo de Branching | Ventajas | Desventajas |
|---|---|---|
| Git Flow | **Buena organización** | **Complejidad** |
| GitHub Flow | **Simpleza** | **Menos control** |
| Trunk-Based Development | **Rapidez** | **Mayor riesgo de errores** |

## Buenas prácticas

<img src="../../images/gp.svg" width="300" >

1. **Planificación y Diseño:**
      - Definir claramente los requisitos del proyecto y establecer metas realistas.
      - Utilizar metodologías de desarrollo ágil, como Scrum o Kanban, para iterar rápidamente y adaptarse a los cambios en los requisitos.
      - Realizar una arquitectura sólida y diseño antes de comenzar la implementación.

2. **Control de Versiones:**
      - Utilizar un sistema de control de versiones, como Git, para rastrear cambios en el código y facilitar la colaboración entre miembros del equipo.
      - Emplear una estrategia de branching que se adapte al flujo de trabajo del equipo, como Gitflow o Trunk-Based Development.
      - Realizar commits atómicos y descriptivos para mantener un historial claro y comprensible del código.

3. **Pruebas y QA:**
      - Implementar pruebas unitarias, de integración y de aceptación automatizadas para garantizar la estabilidad y el correcto funcionamiento del software.
      - Realizar pruebas de forma continua y regular, integrándolas en el proceso de desarrollo con herramientas como Jenkins, Travis CI o GitHub Actions.
      - Establecer estándares de calidad y realizar revisiones de código entre pares para identificar y corregir errores de manera temprana.

4. **Documentación:**
      - Mantener una documentación clara y actualizada del código, incluyendo comentarios en el código fuente, documentación de API y guías de usuario.
      - Utilizar herramientas de generación de documentación, como Sphinx o MkDocs, para generar documentación automáticamente a partir del código fuente.

5. **Refactorización y Mantenibilidad:**
      - Realizar refactorizaciones regulares para mejorar la legibilidad, la eficiencia y la mantenibilidad del código.
      - Seguir principios de diseño de software, como SOLID y DRY, para escribir código limpio y modular.
      - Utilizar patrones de diseño comunes para resolver problemas recurrentes de manera eficiente y consistente.

6. **Seguridad:**
      - Implementar prácticas de seguridad en todas las etapas del desarrollo de software para proteger contra vulnerabilidades y ataques.
      - Realizar análisis estático y dinámico de código para identificar posibles riesgos de seguridad.
      - Mantener todas las dependencias del proyecto actualizadas y parcheadas para evitar vulnerabilidades conocidas.

7. **Colaboración y Comunicación:**
      - Fomentar la colaboración y la comunicación efectiva entre los miembros del equipo utilizando herramientas como Slack, Microsoft Teams o Discord.
      - Mantener reuniones regulares para discutir el progreso del proyecto, identificar obstáculos y tomar decisiones estratégicas.
      - Establecer un ambiente de trabajo inclusivo y respetuoso que fomente la creatividad y la innovación.

## Referencias

* [Git Branch](https://www.atlassian.com/git/tutorials/using-branches)
* [Top 10 Software Development Best Practices](https://bigohtech.com/software-development-best-practices/)
