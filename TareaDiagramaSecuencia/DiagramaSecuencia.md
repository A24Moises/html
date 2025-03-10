``` mermaid 
sequenceDiagram
    participant Cliente
    participant InterfazCajero
    participant Tarjeta
    participant LectorTarjeta
    participant SistemaAutenticacion
    participant CuentaBancaria
    participant DispensadorEfectivo

    Cliente ->> InterfazCajero: Insertar tarjeta
    InterfazCajero ->> LectorTarjeta: Leer tarjeta
    LectorTarjeta ->> Tarjeta: Obtener datos
    Tarjeta -->> LectorTarjeta: Datos de la tarjeta
    LectorTarjeta -->> InterfazCajero: Datos de la tarjeta

    InterfazCajero ->> Cliente: Solicitar PIN
    Cliente ->> InterfazCajero: Ingresar PIN
    InterfazCajero ->> SistemaAutenticacion: Validar PIN y tarjeta
    SistemaAutenticacion -->> InterfazCajero: Respuesta validación

    alt Autenticación exitosa
        InterfazCajero ->> Cliente: Solicitar monto de retiro
        Cliente ->> InterfazCajero: Ingresar monto
        InterfazCajero ->> CuentaBancaria: Verificar saldo y procesar retiro
        CuentaBancaria -->> InterfazCajero: Aprobación/rechazo

        alt Saldo suficiente
            InterfazCajero ->> DispensadorEfectivo: Entregar dinero
            DispensadorEfectivo -->> Cliente: Dinero dispensado
            InterfazCajero ->> Cliente: ¿Desea otra transacción?
            Cliente -->> InterfazCajero: No
            InterfazCajero ->> Cliente: Expulsar tarjeta
            Cliente ->> InterfazCajero: Retira tarjeta
        else Saldo insuficiente
            InterfazCajero ->> Cliente: Mensaje de saldo insuficiente
        end
    else Autenticación fallida
        InterfazCajero ->> Cliente: Mensaje de error
    end

```

Descripción del Diagrama

El diagrama de secuencia representa el proceso de retiro de dinero en un cajero automático. A continuación, se detallan los pasos involucrados:

Inserción de la Tarjeta: El cliente introduce su tarjeta en el cajero, que es leída por el lector de tarjetas.

Autenticación: Se solicita el PIN al cliente y se envía para validación al sistema de autenticación.

Selección del Monto: Si la autenticación es exitosa, el cliente ingresa el monto que desea retirar.

Verificación de Fondos: El cajero consulta la cuenta bancaria para verificar si hay saldo suficiente.

Entrega del Dinero:

Si hay saldo suficiente, el dispensador de efectivo entrega el dinero al cliente.

Si no hay saldo suficiente, se muestra un mensaje de error.

Finalización: Se consulta al cliente si desea otra transacción. Si no, se expulsa la tarjeta y el proceso finaliza.

Elementos Adicionales Considerados

Sistema de Autenticación: Necesario para validar el PIN del usuario.

Dispensador de Efectivo: Responsable de entregar el dinero físico.

Cuenta Bancaria: Permite verificar si el usuario tiene fondos suficientes para completar el retiro.

Este diagrama cubre los casos de éxito y error más comunes en el proceso de retiro de efectivo en un cajero automático.