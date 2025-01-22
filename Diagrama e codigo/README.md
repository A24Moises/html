
```java
    classDiagram

    class Conferencia{
        +String nombreConf
        +String Lugar
        +Int numParticipantes
    }

    class Sesion{
        +String Fecha
        +String Hora inicio
    }
    Conferencia"1"<.."*" Sesion:"tiene"

    
    class ArticulosCientificos{
      +String TemaArticulo
      +Tamano()
    }
    Sesion"1"<.."*" ArticulosCientificos:"presentado"

    class Participantes{
        +String Inscripcion
        +Orador()
        +Publico()
    }
    Conferencia"1"<.."*" Participantes:"inscrito"

    class Autor{
        -numArticulos()
    }
    ArticulosCientificos"*"<.."1" Autor:"Publicó"

```