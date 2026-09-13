# ESIC Medellín — Respuestas para WhatsApp

**Posición:** Líder de Fábrica de IA y Automatización · **Contacto:** María Isabel Valencia
**Fecha:** 2026-09-08 · **Formato:** WhatsApp (negrita con un solo asterisco)

> ⚠️ Antes de enviar: confirmar la ciudad (mensaje 3) y decidir la cifra salarial (mensaje 3).

---

## Mensaje 1 — saludo y preguntas 1 a 4

¡Hola María Isabel! Muy bien, gracias 😊 Un gusto saludarte.

Claro que sí, con mucho gusto te respondo cada punto. Te las mando en tres mensajes para que sea más fácil de leer.

*1. Años de experiencia y tipo de proyectos*
Llevo 8 años en desarrollo de software profesional, y antes de eso estuve 11 años como profesor de Machine Learning, Ciencia de Datos y Matemáticas en la Universidad de Antioquia, donde además construí el currículo de la electiva de IA/ML del Instituto de Matemáticas. Soy matemático de formación, con maestría.

En estos 8 años he trabajado en plataformas blockchain y de analítica (BCFort), 3 años de desarrollo full stack en Monadical con un equipo distribuido entre Canadá, Estados Unidos y Latinoamérica, y en los últimos 2 años he construido productos de IA de punta a punta como consultor independiente.

*2. Experiencia con LLMs e IA generativa*
Es mi foco de los últimos 3 años. Tres sistemas concretos:

• *Plixiq* (plixiq.com): SaaS multi-tenant donde un negocio despliega agentes de IA sobre WhatsApp. Usa RAG para el contexto de cada empresa, LiteLLM para trabajar con varios proveedores y tener respaldo si uno falla, y escala a un agente humano cuando el bot no puede resolver. Resuelve en unos 2 segundos.
• *Aluna* (aluna.works): plataforma de reclutamiento con IA. Un pipeline analiza las hojas de vida, las puntúa de 0 a 100 contra el perfil del cargo, y un agente conversacional entrevista a los candidatos por WhatsApp o chat web.
• En *Lapzo* diseñé un "Profesor Digital" que conversa en tiempo real con los estudiantes, con LangChain y LangGraph y síntesis de voz con ElevenLabs.

Trabajo habitualmente con LangChain, LangGraph, LiteLLM, RAG, MCP, y modelos de OpenAI, Anthropic y Google.

*3. n8n y automatización*
Con n8n llevo unos 2 años a nivel intermedio: en Lapzo lo uso para orquestar el generador de contenido educativo con IA.

Donde tengo más profundidad es construyendo la automatización a la medida cuando el flujo se pasa de lo que aguanta una herramienta no-code. En Aluna diseñé un pipeline durable de 9 pasos con checkpoint y 3 reintentos, donde la deduplicación corre antes del control de cuota: si alguien reanaliza una hoja de vida que no cambió, se reutiliza el resultado y no se gasta ni una llamada al modelo ni cupo del plan. Al revés, le estarías cobrando al cliente un trabajo que no hiciste.

También diseñé la arquitectura de datos de una plataforma de automatización de flujos (parecida a n8n) para un cliente.

Te lo digo con transparencia: si el rol exige n8n a nivel experto desde el día uno, ahí mi curva es de semanas, no de meses.

*4. AWS*
5 años a nivel intermedio: EC2, S3, Docker y pipelines de CI/CD con GitHub Actions, para desplegar y mantener aplicaciones web y servicios de IA. También he trabajado con GCP e IBM Cloud, y hoy despliego bastante en Railway con Postgres (Neon) y Redis (Upstash).

Para ser claro con el alcance: no he trabajado con Kubernetes ni Terraform. Mi fuerte es llevar aplicaciones a producción y sostenerlas, no infraestructura a gran escala.

---

## Mensaje 2 — preguntas 5 a 8

*5. Integraciones por API*
Es buena parte de mi trabajo diario. Algunos ejemplos:

• *WhatsApp Cloud API* por webhooks, en Plixiq y en Aluna. Lo difícil ahí no es conectar, es la idempotencia: WhatsApp reintenta el envío, y si no lo manejas el cliente recibe la misma respuesta dos veces.
• *Aluna* integra 11 proveedores externos: Anthropic, Gemini, WhatsApp, Inngest, Resend para correo, Polar para pagos y suscripciones, Cloudflare R2 para archivos, entre otros.
• Stripe para pagos, ElevenLabs para voz, Whisper para transcripción, y APIs REST y GraphQL propias durante mis años en Monadical.

*6. Python y otras tecnologías*
Python: 8 años, nivel avanzado. FastAPI, Django y Flask del lado del backend, y la parte de datos y ML con NumPy, Pandas, Scikit-learn, PyTorch, TensorFlow y JAX.

TypeScript y JavaScript: 6 años, nivel avanzado. React, Next.js, Node.js y NestJS.
SQL y PostgreSQL: 6 años. También manejo C a nivel intermedio y estoy aprendiendo Rust.

*7. Liderazgo de equipos*
Te respondo con precisión, para no venderte algo distinto a lo que es: tengo liderazgo técnico, no he tenido personas con reporte directo a mi cargo.

• En *Lapzo* soy miembro líder del Comité de IA: definimos cómo toda la organización desarrolla con IA y qué lineamientos siguen los proyectos.
• En *Monadical*, 3 años en un equipo distribuido, lideré la arquitectura de frontend y la estrategia de pruebas, hacía revisión de código y acompañaba a los ingenieros junior.
• Como consultor fui el revisor de código del equipo de desarrollo de un cliente.
• Y 11 años dirigiendo proyectos de investigación de estudiantes en la universidad.

Si la posición implica armar y dirigir un equipo, es exactamente el paso que quiero dar, y llego con 11 años de práctica formando gente.

*8. De la idea a producción*
Plixiq es el mejor ejemplo. Salió de un problema muy concreto: un negocio pequeño no puede atender WhatsApp 24/7, y el cliente no espera.

Mi rol fue arquitecto y desarrollador único: desde las conversaciones iniciales para entender el problema hasta el despliegue.

La decisión que más defiendo: lo construí como un monolito modular con 10 contextos delimitados (DDD) cuyas fronteras las valida un linter en CI, en lugar de microservicios. La respuesta "limpia" eran microservicios, pero una sola persona no opera 10 servicios. Y una regla que no se valida automáticamente es apenas una sugerencia.

El resultado: unas 40.000 líneas y un MVP casi completo en 4 meses trabajando medio tiempo, desplegado y con un costo de infraestructura de 60 a 80 dólares al mes, porque el costo escala con el uso del modelo y no con servidores.

---

## Mensaje 3 — preguntas 9 a 11 y cierre

*9. Traducir negocio a soluciones*
Sí, es justamente como trabajo. Como consultor independiente dirijo las sesiones de diseño técnico con los clientes: traduzco lo que necesita el negocio a una arquitectura y le pongo nombre al trade-off de cada decisión, para que la escojan entendiéndola.

Un ejemplo claro es *VitaStock*, un sistema de cadena de suministro para clínicas quirúrgicas en Colombia. Lo verdaderamente difícil no era técnico sino del dominio: trazabilidad por lote, alertas de vencimiento y costo real por paciente. Eso lo entendí sentándome con la farmacéutica de la clínica, no leyendo un documento de requerimientos. Hoy son 12 módulos y 5 roles distintos. Está desplegado, aunque la clínica todavía no lo tiene en operación diaria.

Creo que ahí me ayuda mucho haber sido profesor: buena parte de este trabajo es explicarle un sistema a alguien que no es técnico y ayudarle a decidir.

*10. Dónde vivo*
Vivo en Medellín, Colombia.

*11. Aspiración salarial*
[VER NOTA ABAJO — decidir antes de enviar]

Quedo muy atento a lo que siga y con gusto profundizo en lo que necesites. Te dejo mi perfil por si te sirve tener el detalle a la mano:

• LinkedIn: linkedin.com/in/asanchezyali
• Sitio: asanchezyali.com
• Los productos que mencioné: plixiq.com · aluna.works

¡Gracias a ti por el espacio, María Isabel! Quedo pendiente 😊

---

## Nota sobre la pregunta 11 — decidir antes de enviar

**Opción A (recomendada): devolver la pregunta primero.**

> *11. Aspiración salarial*
> Antes de darte una cifra me gustaría entender un poco mejor el alcance del rol: si implica equipo a cargo, si es presencial, híbrido o remoto, y qué tan amplio es el mandato de la "fábrica". ¿Me compartes el rango que tienen contemplado para la posición? Con eso te doy un número aterrizado. Si el proyecto y el equipo encajan, soy flexible dentro de un rango razonable.

**Opción B: dar la cifra de entrada.**

> *11. Aspiración salarial*
> Mi aspiración está en COP $______ mensuales. De todas formas, si el rol y el equipo encajan bien, hay margen para conversarlo.

**Contexto para decidir:** tu referencia hasta ahora ha sido USD 7.500/mes en roles remotos internacionales (≈ COP 30M) y USD 63/hora en consultoría. ESIC Medellín es una escuela de negocios con operación local: es probable que su banda esté bastante por debajo de esa referencia. Por eso la Opción A protege mejor — si sueltas 30M de entrada en un proceso local, es posible que te descarten antes de conversar. Si su banda resulta baja para ti, siempre puedes retirarte después; al revés no se puede.
