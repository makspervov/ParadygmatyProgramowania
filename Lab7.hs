-- LAB 7
-- Polecenie 1
sign1 x = if x < 0 then -1
    else if x == 0 then 0
    else  1

sign2 x
    | x < 0 = -1
    | x == 0 = 0
    | x > 0 = 1

-- Polecenie 2
myComp :: Ord a => a -> a -> Ordering
myComp x y
    | x < y = GT
    | x == y = EQ
    | x > y = LT

-- Polecenie 3
mul1 :: Int -> Int -> Int
mul1 a 1 = a
mul1 1 a = a
mul1 _ 0 = 0
mul1 0 _ = 0
mul1 a b 
    | (a < 0) && (b < 0) = mul1 (-a) (-b)
    | b > 0 = a + mul1 a (b-1)
    | b < 0 = b + mul1 b (a-1)

-- Polecenie 4
silnia :: Int -> Int
silnia 0 = 1
silnia n = case n > 0 of
    True -> n * silnia (n - 1)
    False -> error "liczba <0"

silnia2 :: Int -> Int
silnia2 0 = 1
silnia2 n = if n < 0 then error "liczba <0"
   else n * silnia (n - 1)

silnia3 :: Int -> Int
silnia3 n
    | n == 0 = 1
    | n > 0 = n * silnia (n - 1)
    | otherwise = error "liczba <0"

fib :: Integer -> Integer
fib 0 = 0
fib 1 = 1
fib n = fib (n-1) + fib (n-2)