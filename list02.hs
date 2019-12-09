-- List02 Ex01, Express map via foldr (use lambda expr).
mapFunct :: (x -> y) -> [x] -> [y]
mapFunct f = foldr (\x xs -> f x : xs) []
main = print $ "hello"

-- List02 Ex02, Implement a function that for a given list of integers 
--returns the sum of squaresof its even members. Use fold.
-- http://zvon.org/other/haskell/Outputprelude/foldl_f.html
squaresSum :: Num x => [x] -> x
squaresSum = foldl(\x y -> x+y^2) 0
main = print (squaresSum (filter even[1,2,3,4])) -- "filter even" added

--list 02 Ex03 
-- Implement a function that for a given list of natural numbers
-- calculates how many members of the list are prime. Use fold
fun = foldl(\x y-> x + 1) 0 
prime n = if f n > 0 then False else True
     where f n = foldl (\acc x -> if n `mod` x == 0 then acc + 1 else acc) 0 [2..n-1]
main = print $ (fun (filter (prime)[1,2,3,4,5,6,7,8,9,10]))

--list 02 Ex04 ver 1.0
-- Implement a function that for a given natural number n calculates the approximation of e
list n  = [1 .. n]
factorial n = foldl (*) 1 [1..n]
approximation = foldl(\x y -> x+(1/(factorial y))) 1
main = print $ (approximation (list 20000))

--list 02 Ex04 ver 2.0 (turbo)
list n  = [1 .. n] 
approximation_v2 = foldl (\(x,y) item -> (x*item, (y+(1/(x*item))))) (1,1) 
main = print $ (snd $ (approximation_v2 (list 10000)))

