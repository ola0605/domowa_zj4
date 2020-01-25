import unittest
import zad1
import random

class TestStringMethods(unittest.TestCase):

    def test_g(self):
        self.assertTrue(True)

    def test_f1_1(self):
        a=zad1.suma (0)
        self.assertEqual(a,0)

    def test_f1_2(self):
        a=zad1.suma (1)
        self.assertEqual(a,1)

    def test_f1_3(self):
        a=zad1.suma (2)
        self.assertEqual(a,4)

    def test_f1_4(self):
        a=zad1.suma (2,1)
        self.assertEqual(a,5)

    def test_f1_5(self):
        a=zad1.suma (2,3)
        self.assertEqual(a,7)

    def test_f2_1(self):
        c=zad1.pierwszy_znak ("ala")
        self.assertEqual(c,"a")

    def test_f2_2(self):
        c=zad1.pierwszy_znak ([1,2,3])
        self.assertEqual(c,1)

    def test_f2_3(self):
        c=zad1.pierwszy_znak ()
        self.assertEqual(c,"BUUM")

    def test_f3_1(self):
        e=zad1.cyfry (1)
        self.assertEqual(e,"jeden")

    def test_f3_2(self):
        e=zad1.cyfry (2)
        self.assertEqual(e,"dwa")

    def test_f3_3(self):
        e=zad1.cyfry (3)
        self.assertEqual(e,"trzy")

    def test_f3_4(self):
        e=zad1.cyfry (random.choice(range(4,1000)))
        self.assertEqual(e,"inna")

    def test_f4_1(self):
        d=zad1.kot ("ala")
        self.assertEqual(d,"ala ma kota")

    def test_f4_2(self):
        d=zad1.kot ("kot")
        self.assertEqual(d,"kot ma kota")

    def test_f4_3(self):
        d=zad1.kot ("kot","psa")
        self.assertEqual(d,"kot ma kota i psa")

    def test_f4_4(self):
        d=zad1.kot ("kot","mysz")
        self.assertEqual(d,"kot ma kota i mysz")

    def test_f5_1(self):
        f=zad1.liczenie (0)
        self.assertEqual(f,[])

    def test_f5_2(self):
        f=zad1.liczenie (1)
        self.assertEqual(f,[0])

    def test_f5_3(self):
        f=zad1.liczenie (2)
        self.assertEqual(f,[0,1])

    def test_f5_4(self):
        f=zad1.liczenie (7)
        self.assertEqual(f,[0,1,2,3,4,5,6])

    def test_f5_5(self):
        f=zad1.liczenie (7,2)
        self.assertEqual(f,[0,2,4,6])

    def test_f5_6(self):
        f=zad1.liczenie (17,2)
        self.assertEqual(f,[0,2,4,6,8,10,12,14,16])

    def test_f5_7(self):
        f=zad1.liczenie (17,5)
        self.assertEqual(f,[0,5,10,15])

    def test_f6_1(self):
        b=zad1.powtarzanie (1,"*")
        self.assertEqual(b,"*")

    def test_f6_2(self):
        b=zad1.powtarzanie (7,"*")
        self.assertEqual(b,"*******")


if __name__ == '__main__':
    unittest.main()

