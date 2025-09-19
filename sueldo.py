"""
Sol Valeria Gonzalez Castro
19/09/2025
Calcular el sueldo semanal de un empleado, dadas las horas trabajadas y la tarifa horaria
"""

# Entradas
horas_trabajadas = float(input("Introduzca horas trabajadas : "))
tarifa_horaria = float(input("Introduzca la tarifa: "))

# Proceso
if horas_trabajadas > 48:
    horas_extra = horas_trabajadas - 48
    pago_extra = horas_extra * tarifa_horaria * 2
    pago = 48 * tarifa_horaria
else:
    horas_extra = 0
    pago_extra = 0
    pago = horas_trabajadas * tarifa_horaria
pago_total = pago + pago_extra

# Salidas
print("Horas extra:", horas_extra)
print("Pago extra:", pago_extra)
print("Total:", pago_total)
