#Aldo López Barrios
#21310106
#--------------------------
class ControladorPID:
    def __init__(self, Kp, Ki, Kd, consigna):
        # Inicializamos los parámetros del controlador PID
        self.Kp = Kp  # Ganancia proporcional
        self.Ki = Ki  # Ganancia integral
        self.Kd = Kd  # Ganancia derivativa
        self.consigna = consigna  # Valor deseado (setpoint)
        self.error_previo = 0  # Error anterior
        self.integral = 0  # Integral del error

    def actualizar(self, variable_proceso):
        # Calculamos el error entre la consigna y la variable del proceso
        error = self.consigna - variable_proceso
        # Sumamos el error actual a la integral acumulada
        self.integral += error
        # Calculamos el término derivativo como la diferencia entre el error actual y el anterior
        derivada = error - self.error_previo
        # Calculamos la señal de control utilizando la fórmula del controlador PID
        señal_control = self.Kp * error + self.Ki * self.integral + self.Kd * derivada
        # Actualizamos el error previo para la próxima iteración
        self.error_previo = error
        return señal_control

# Ejemplo de uso:
if __name__ == "__main__":
    # Definimos la consigna (valor deseado)
    consigna = 100
    # Parámetros del controlador PID
    Kp = 0.5
    Ki = 0.1
    Kd = 0.2
    # Inicializamos el controlador PID
    pid = ControladorPID(Kp, Ki, Kd, consigna)
    # Simulamos el proceso (por ejemplo, la posición de un motor)
    variable_proceso = 0
    for _ in range(100):
        # Actualizamos la variable del proceso (simulada)
        variable_proceso += 0.5
        # Calculamos la señal de control utilizando el controlador PID
        señal_control = pid.actualizar(variable_proceso)
        # Aplicamos la señal de control al proceso (por ejemplo, ajustamos la velocidad del motor)
        # En este ejemplo, simplemente imprimimos la señal de control
        print("Señal de Control:", señal_control)
