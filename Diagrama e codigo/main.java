
//falta terminar

class Conferencia{
    String nombreConf
    String lugarConf
    Int numParticipantes
}

class Sesion{
    Int codSesion
    String fecha
    String horaInicio
    
}

fun PresentacionArticulo()


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
