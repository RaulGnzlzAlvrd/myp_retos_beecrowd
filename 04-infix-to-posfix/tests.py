from main import shunting_yard

def test_shunting_yard():
    casos = [
        ("A*2", "A2*"),
        ("(A*2+c-d)/2", "A2*c+d-2/"),
        ("(2*4/a^b)/(2*c)", "24*ab^/2c*/"),
        ("a-b*c", "abc*-"),
        ("(a-b)*c", "ab-c*"),
        ("a*(b-c)", "abc-*"),
        ("(a-b)/(c+d)", "ab-cd+/"),
        ("2*(4/a)^b", "24a/b^*"),
        ("(2*(4/a)^b*1+2*(3+5))/(2*(c-3))", "24a/b^*1*235+*+2c3-*/")
    ]
    for entrada, esperado in casos:
        obtenido = shunting_yard(entrada)
        mensaje = f"Fallo en caso {entrada}\n"
        mensaje += f"Se esperaba {esperado} pero se obtuvo {obtenido}"
        assert esperado == obtenido, mensaje

if __name__ == "__main__":
    test_shunting_yard()
