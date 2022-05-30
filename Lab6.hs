negacja :: Int -> Int
negacja x = -x

pier :: Int -> Float
pier x = if x > 0 then sqrt (fromIntegral x) else error "Liczba ujemna"

delta :: Double -> Double -> Double -> Double
delta a b c = b * b - 4 * a * c

pdelta :: Double -> Double -> Double -> Double
pdelta a b c = sqrt (delta a b c)

pdelta2 :: Double -> Double -> Double -> Double
pdelta2 a b c = if warunek > 0
               then sqrt (delta a b c)
               else if warunek == 0
                    then 0
                    else error "Delta mniejsza od zera"
                    where warunek = (delta a b c)
                    
pdelta3 :: Double -> Double -> Double -> [Double]
pdelta3 a b c = if a == 0
               then error "nie jest mozliwe dzielenie przez 0"
               else if(delta a b c) == 0 
                    then [(-b) / (2 * a)]
                    else if (delta a b c) > 0
                         then [(-b + pier) / (2 * a),
                               (-b - pier) / (2 * a)]
                         else error "delta jest mniejsza od zera, brak pierwiastkow"
               where pier = sqrt (delta a b c)