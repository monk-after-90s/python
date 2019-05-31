class A:
    def _f(self):
        print('A')


class B(A):
    pass


a = B()
a._f()
