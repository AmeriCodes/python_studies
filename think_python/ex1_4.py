"""Start the Python interpreter and use it as a calculator. Python’s syntax for math operations is almost the same as standard mathematical notation. For example, the symbols +, - and / denote addition, subtraction and division, as you would expect. The symbol for multiplication is *.

If you run a 10 kilometer race in 43 minutes 30 seconds, what is your average time per mile? What is your average speed in miles per hour? (Hint: there are 1.61 kilometers in a mile).
"""

def converter_para_minutos(horas=0, min=0, seg=0):
    return (horas * 60) + min + (seg / 60)


def converter_para_horas(anos=0, horas=0, minutos=0):
    return (anos * 8760) + horas + (minutos / 60)


def converter_km_em_milhas(Quilometros):
    return (Quilometros / 1.61)


def media_milhas_por_minuto(tempo,milhas):
    return tempo / milhas



quilometros = 10
minutos = 43
segundos = 30


tempo_por_milha_minutos = media_milhas_por_minuto(converter_para_minutos(0,minutos,segundos), converter_km_em_milhas(quilometros))

velocidade_media_mph = converter_km_em_milhas(quilometros) / converter_para_horas(0,0, converter_para_minutos(0,43,30))

print(f'Essa é a média de tempo por milha: {tempo_por_milha_minutos:.1f} minutos')

print(f'Essa é a média de velocidade por milha por hora: {velocidade_media_mph:.1f} mph')
