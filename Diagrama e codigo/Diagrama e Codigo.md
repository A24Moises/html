
# Diagrama y código

---

## Diagrama de clases.

Utilizando la herramienta diagrama de Mermaid, represente mediante un diagrama de clases la gestión de un congreso científico con las siguientes consideraciones:

- La conferencia podrá tener varias sesiones.
- Una sesión tiene una fecha y hora de inicio, pertenece únicamente a una conferencia y no tiene razón de existir sin una conferencia.
- Los participantes en una sesión pueden ser oradores o audiencia. Todos ellos deben registrarse para la conferencia. Una inscripción se puede cancelar o confirmar.
- En una sesión se presentan uno o más artículos científicos. Cada artículo puede ser corto o largo y tratar sobre un tema determinado.
- Un autor puede tener uno o más artículos presentados en la conferencia.
- Coloca los atributos que te parezcan convincentes.

## Código

Escribe las clases correspondientes a tu diagrama de clases en Java. Rehaga el diseño si cree que algo no está bien.

---

## Entrega
    
1) Elabora un documento en markdown que incluya lo siguiente:

    - Breve descripción del proceso realizado:

        El siguiente es un Diagrama de Clases de una conferencia cientifica, la cual tiene toda la informacion dividida en clases, ademas de tener sus interacciones y relaciones

    - Código fuente del diagrama anotado en sus etiquetas:

        ```mermaid

        classDiagram
            class Conferencia{
                +String nombreConf
                +String lugarConf
                +Int numParticipantes
            }

            class Sesion{
                +Int codSesion
                +String fecha
                +String horaInicio
                +PresentacionArticulo()
            }
            Conferencia"1"-->"*" Sesion:"tiene"

            
            class ArticuloCientifico{
            +String TemaArticulo
            +TamañoArticulo()
            }
            Sesion"1"<--"*" ArticuloCientifico:"presenta"

            class Participantes{
                -String Nombre
                -String Apellidos
                -Int DNI
                +RegistroParticipantes()
                +inscripcionConf()
            }
            Conferencia"1"<--"*" Participantes:"inscrito"

            class Publico{
                -String codAsiento
            }
            Sesion"*"<--"*" Publico: "asiste"
            Participantes"*"--|>"*" Publico: "es"
            
            class Orador{
            }
            Participantes"*"--|>"*" Orador: "es"
            Sesion"*"<|.."*" Orador :"precide"

            class Autor{
                -String codColegiado
                +numArticulos()
            }
            Autor"1"..>"1"Orador:"Es"
            ArticuloCientifico"*"<|.."1" Autor:"Publicó"
        ```

    - Código java de las clases:

        ```java
        import java.util.List;

        class Conferencia {
            private String nombreConf;
            private String lugarConf;
            private int numParticipantes;
            private List<Sesion> sesiones;
            private List<Participantes> participantes;

            public Conferencia(String nombreConf, String lugarConf, int numParticipantes) {
                this.nombreConf = nombreConf;
                this.lugarConf = lugarConf;
                this.numParticipantes = numParticipantes;
            }

            public String getNombreConf() {
                return nombreConf;
            }

            public void setNombreConf(String nombreConf) {
                this.nombreConf = nombreConf;
            }

            public String getLugarConf() {
                return lugarConf;
            }

            public void setLugarConf(String lugarConf) {
                this.lugarConf = lugarConf;
            }

            public int getNumParticipantes() {
                return numParticipantes;
            }

            public void setNumParticipantes(int numParticipantes) {
                this.numParticipantes = numParticipantes;
            }

            public List<Sesion> getSesiones() {
                return sesiones;
            }

            public void setSesiones(List<Sesion> sesiones) {
                this.sesiones = sesiones;
            }

            public List<Participantes> getParticipantes() {
                return participantes;
            }

            public void setParticipantes(List<Participantes> participantes) {
                this.participantes = participantes;
            }
        }

        class Sesion {
            private int codSesion;
            private String fecha;
            private String horaInicio;
            private List<ArticuloCientifico> articulos;
            private List<Publico> publico;
            private List<Orador> oradores;

            public Sesion(int codSesion, String fecha, String horaInicio) {
                this.codSesion = codSesion;
                this.fecha = fecha;
                this.horaInicio = horaInicio;
            }

            public int getCodSesion() {
                return codSesion;
            }

            public void setCodSesion(int codSesion) {
                this.codSesion = codSesion;
            }

            public String getFecha() {
                return fecha;
            }

            public void setFecha(String fecha) {
                this.fecha = fecha;
            }

            public String getHoraInicio() {
                return horaInicio;
            }

            public void setHoraInicio(String horaInicio) {
                this.horaInicio = horaInicio;
            }

            public List<ArticuloCientifico> getArticulos() {
                return articulos;
            }

            public void setArticulos(List<ArticuloCientifico> articulos) {
                this.articulos = articulos;
            }

            public List<Publico> getPublico() {
                return publico;
            }

            public void setPublico(List<Publico> publico) {
                this.publico = publico;
            }

            public List<Orador> getOradores() {
                return oradores;
            }

            public void setOradores(List<Orador> oradores) {
                this.oradores = oradores;
            }

            public void presentacionArticulo() {
            }
        }

        class ArticuloCientifico {
            private String temaArticulo;
            private Autor autor;

            public ArticuloCientifico(String temaArticulo, Autor autor) {
                this.temaArticulo = temaArticulo;
                this.autor = autor;
            }

            public String getTemaArticulo() {
                return temaArticulo;
            }

            public void setTemaArticulo(String temaArticulo) {
                this.temaArticulo = temaArticulo;
            }

            public Autor getAutor() {
                return autor;
            }

            public void setAutor(Autor autor) {
                this.autor = autor;
            }

            public void tamañoArticulo() {
            }
        }

        class Participantes {
            private String nombre;
            private String apellidos;
            private int dni;

            public Participantes(String nombre, String apellidos, int dni) {
                this.nombre = nombre;
                this.apellidos = apellidos;
                this.dni = dni;
            }

            public String getNombre() {
                return nombre;
            }

            public void setNombre(String nombre) {
                this.nombre = nombre;
            }

            public String getApellidos() {
                return apellidos;
            }

            public void setApellidos(String apellidos) {
                this.apellidos = apellidos;
            }

            public int getDni() {
                return dni;
            }

            public void setDni(int dni) {
                this.dni = dni;
            }

            public void registroParticipantes() {
            }

            public void inscripcionConf() {
            }
        }

        class Publico extends Participantes {
            private String codAsiento;

            public Publico(String nombre, String apellidos, int dni, String codAsiento) {
                super(nombre, apellidos, dni);
                this.codAsiento = codAsiento;
            }

            public String getCodAsiento() {
                return codAsiento;
            }

            public void setCodAsiento(String codAsiento) {
                this.codAsiento = codAsiento;
            }
        }

        class Orador extends Participantes {
            private List<Sesion> sesiones;

            public Orador(String nombre, String apellidos, int dni, List<Sesion> sesiones) {
                super(nombre, apellidos, dni);
                this.sesiones = sesiones;
            }

            public List<Sesion> getSesiones() {
                return sesiones;
            }

            public void setSesiones(List<Sesion> sesiones) {
                this.sesiones = sesiones;
            }
        }

        class Autor {
            private String codColegiado;
            private int numArticulos;

            public Autor(String codColegiado, int numArticulos) {
                this.codColegiado = codColegiado;
                this.numArticulos = numArticulos;
            }

            public String getCodColegiado() {
                return codColegiado;
            }

            public void setCodColegiado(String codColegiado) {
                this.codColegiado = codColegiado;
            }

            public int getNumArticulos() {
                return numArticulos;
            }

            public void setNumArticulos(int numArticulos) {
                this.numArticulos = numArticulos;
            }
        }
        ```
