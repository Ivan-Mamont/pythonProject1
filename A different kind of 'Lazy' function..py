def lazy(n):
    # Remember that lazy is a decorator!
    pass


from solution import lazy
import codewars_test as test


@test.describe("Examples")
def tests():
    @test.it("Should work for positive n")
    def test_pos():
        for i in range(1, 6):
            @lazy(i)
            def mul(a, b):
                return a * b

            for j in range(3 * i):
                val = None if j % i else 56
                test.assert_equals(mul(7, 8), val)

    @test.it("Should work for negative n")
    def test_neg():
        for i in range(1, 6):
            @lazy(-i)
            def mul(a, b):
                return a * b

            for j in range(1, 3 * i + 1):
                val = 56 if j % i else None
                test.assert_equals(mul(7, 8), val)