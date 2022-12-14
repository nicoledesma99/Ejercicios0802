import unittest
import examen as ch

class SUP0802_Modulo1_cp(unittest.TestCase):

    def test_Pregunta01(self):
        valor_test = ch.Ret_Pregunta01()
        valor_esperado = 5170
        self.assertEqual(valor_test, valor_esperado)
        
    def test_Pregunta02(self):
        valor_test = ch.Ret_Pregunta02()
        valor_esperado = 9
        self.assertEqual(valor_test, valor_esperado)

    def test_Pregunta03(self):
        valor_test = ch.Ret_Pregunta03()
        valor_esperado = 146585.30
        self.assertEqual(valor_test, valor_esperado) 

    def test_Pregunta04(self):
        valor_test = ch.Ret_Pregunta04()
        valor_esperado = 'Mapas Mentales'
        self.assertEqual(valor_test, valor_esperado)

    def test_Pregunta05(self):
        valor_test = ch.Ret_Pregunta05()
        valor_esperado = 5
        self.assertEqual(valor_test, valor_esperado)

    def test_Pregunta06(self):
        valor_test = ch.Ret_Pregunta06()
        valor_esperado = (9649, 111024)
        self.assertEqual(valor_test, valor_esperado)

resultado_test = unittest.main(argv=[''], verbosity=2, exit=False)

hc_tests = resultado_test.result.testsRun
hc_fallas = len(resultado_test.result.failures)
hc_errores = len(resultado_test.result.errors)
hc_ok = hc_tests - hc_fallas - hc_errores

archivo_test = open('resultado_test.csv', 'w')
archivo_test.write('Total_Tests,Total_Fallas,Total_Errores,Total_Correctos\n')
archivo_test.write(str(hc_tests)+','+str(hc_fallas)+','+str(hc_errores)+','+str(hc_ok)+'\n')
archivo_test.close()

print('Resumen')
print('Total Tests:', str(hc_tests))
print('Total Fallas:', str(hc_fallas))
print('Total Errores:', str(hc_errores))
print('Total Correctos:', str(hc_ok))
