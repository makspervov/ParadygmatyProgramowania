--Polecenie 1
-- foldr (*) 1 [1,2,3]
{-# OPTIONS_GHC -Wno-incomplete-patterns #-}
il :: [Int] -> Int
il = foldr (*) 1

--Polecenie 2
czyUp x 
    |x `elem` ['a'..'z'] = False
    |x `elem` ['A'..'Z'] = True

--Polecenie 3
rm1 x = [ c | c <- x , c `notElem` ['A'..'Z']] 

--Polecenie 4
pythagorean = [ [a,b,c] |a <- [1..20], b <- [1..20], c <- [1..20], a*a+b*b==c*c]

--Polecenie 5
silnia :: Integer -> Integer
silnia 0 = 1
silnia n = n * silnia (n - 1)

p5 = [silnia x | x <- [0..20], even x]
p5v2 = map (\x -> silnia x) (filter (even) [1..20])

--Polecenie 6
kwadraty = map (\x -> x*x) [0..20]

--Polecenie 7
najw = last (filter (\x -> x `mod` 3829 == 0) [3829..999999])

--Polecenie 8

p8 = length (filter (odd) [x*x | x <- [1..10000]])