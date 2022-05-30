{-# OPTIONS_GHC -Wno-incomplete-patterns #-}
signumn x n
    | x < 0 = -1 * n
    | x == 0 = 0 * n
    | x > 0 = 1 * n