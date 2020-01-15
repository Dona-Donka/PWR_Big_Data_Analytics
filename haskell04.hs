-- Maybe as a Monad 
funct::Int -> Maybe Int
funct 0 = Nothing
funct x = Just x
--main = print (funct 0)


-- Ex4.01 Let f x = [x+1,x+2] and g x = [2*x,3*x]. Understand and calculate[1,1,1] >>= fand([1,1,1] >>= f) >>= g

-- >>>= and >> are functions from the Monad class. They are overloaded differenty for every monad. >>= takes function, maps it over an instance of a monad and then flattens the result. The unction has to return an instance of the monad itself. 
--(>>=) :: m a -> (a -> m b) -> m b


f x = [x+1, x+2] -- \ x -> [x-1, x+2]
g x =[2*x, 3*x]
--main = print ([1,1,1] >>= f) --[2,3,2,3,2,3]


-- Ex4.02 Simplify do x <- mx; f x. What should be the type off?
-- x <- action runs the IO action, gets its result, and binds it to x
--do
--	x <- mx
--	f x
-- equals:  y >>= \x -> f x  

-- Ex4.03 Explain how thedonotation makes the list comprehension redundant?
-- I do not know


-- Task4.1 Implement a model of ”walking a narrow path”. A ”wanderer” starts at a positionpos(an integer satisfying−3<pos<3) and moves forward and left or forward orforward and right (which changes the wanderer’s position by -1, 0, 1 respectively). Ifthe wanderer wanders too much to one of the sides of the path, he dies (|pos|>2).Implement
-- 4.1.1 a functionmove :: Int -> Int -> Maybe Intthat takes a move and a position andreturns the new position (if the wanderer lives) orNothing(if he dies). Use>>=tomake a couple of moves
-- 4.4.2 a functionmovelist :: [Int] -> Int -> Maybe Intthat does almost the samething, however it takes a list of moves instead of one move.

TODO

-- Task 4.2 Implement a function that returns a list of all the possible outcomes of two (d6and d20) dices roll. Use do notation or >>=.
-- http://learnyouahaskell.com/a-fistful-of-monads#getting-our-feet-wet-with-maybe
main = do
    print( [(item, item1) | item <- [1..6], item1 <- [1..20]]
  	print([1..6] >>= \item -> [1..20] >>= \item1 -> return (item,item1))


--Task 4.3
type KnightPos = (Int,Int)  
moveKnight :: KnightPos -> [KnightPos]
moveKnight (c,r) = filter onBoard  
        [(c+2,r-1),(c+2,r+1),(c-2,r-1),(c-2,r+1)  
        ,(c+1,r-2),(c+1,r+2),(c-1,r-2),(c-1,r+2)  
        ]  
        where onBoard (c,r) = c `elem` [1..8] && r `elem` [1..8]  


--main = (print (moveKnight (4,5))) 
