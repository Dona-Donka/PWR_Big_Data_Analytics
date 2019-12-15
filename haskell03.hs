-- Exercise 01, Implement a function that calulates the
-- surface of a given shape

data Point = Point Float Float
data Shape = Circle Point Float | Rectangle Point Point

--pointX (Point x _) = x
--pointY (Point _ y) = y

surface :: Shape -> Float
surface (Circle _  r) = pi * r ^ 2
surface (Rectangle (Point x1 y1) (Point x2 y2)) = (abs $ x2 - x1) * (abs $ y2 - y1) 

-- main = print $ (surface (Circle (Point 10.0 10.0) 5))
-- main = print $ (surface (Rectangle (Point 2.0 3.0) (Point 7.0 8.0)))

-----------------------------------------------------------------------------------------------

-- Exercise 02, Let us define: data Vector3D a = Vector a a a
-- that models 3D vectors. Define addition, multiplication by a scalar and scalar multiplica-tion for your vectors

data Vector3D a = Vector3D a a a deriving(Show)

-- addicion <u1,u2> + <v1,v2> = <u1+v1, u2+v2>
addicion :: (Num a) =>  Vector3D a -> Vector3D a -> Vector3D a  
(Vector3D u1 u2 u3) `addicion`  (Vector3D v1 v2 v3)  = Vector3D (u1+v1) (u2+v2) (u3+v3)

-- multiplication by a scalar s  s<u1,u2> = <u1*s, u2*s>
multByScalar :: (Num a) => Vector3D a -> a -> Vector3D a
(Vector3D u1 u2 u3) `multByScalar` s = Vector3D (u1*s) (u2*s) (u3*s)

-- main = print $ ((Vector3D 1 1 1) `addicion`  (Vector3D 2 2 2) )
-- main = print $ ((Vector3D 1 1 1) `multByScalar` 4)

-----------------------------------------------------------------------------------------------

import Data.List (maximum)
import Data.Tree
{-# LANGUAGE DeriveFoldable #-}

data Tree a = Leaf a | Node (Tree a) a (Tree a) deriving(Show)

--Implementfoldrthat starts with the right-most branch.
foldTreer :: (a -> b -> b) -> b -> Tree a -> b
foldTreer f z (Leaf a)  = z
foldTreer f z (Node right a left) =
    f a (foldTreer f (foldTreer f z left) right
    

-- Implement functions that count numbers of roots and leafs.
counter(Leaf a) = 1
counter(Node left a right) = 1 + counter left + counter right


-- Implement a function that determines whether a given x is an element of a given tree.
treeToList :: (Ord a) => Tree a -> [a]   
treeToList EmptyTree = []         
treeToList (Node root left right) = treeToList left ++ [root] ++ treeToList right

isMember n [] = False
isMember n (x:xs)
    | n == x = True
    | otherwise = isMember n xs


-- Implement a function that determines the height of a given tree, i.e. the length of thelongest branch.
height :: Tree a -> Int
height (Node a val []) =1
height (Node a val xs) = 1 + maximum (map height xs)

myTree :: Tree a
myTree = root  
	where root = 0 [n1, n4]
		n1 = 1 [n2, n3]
	 	n2 = 2 []
	 	n3 = 3 []
	 	n4 = 4 []}

main = print $ "hello"

-------------------------------------------------------------------------------------------------
{-# LANGUAGE DeriveFoldable #-}

module Tree (Tree) where
data Tree a 
    = Empty
    | Node (Tree a) a (Tree a)
    | Leaf a
    deriving Foldable

treeMap :: (a -> b) -> Tree a -> Tree b
treeMap _ Empty = Empty
treeMap f (Leaf a) = Leaf (f a)
treeMAp f (Node leftPart a rightPart) = Node (treeMap f leftPart) (f a) (treeMap f rightPart)

instance Functor Tree where
    fmap = treeMap
--foldr f z Empty = z
--foldr f z (Node z leftPart rightPart) = f x (foldr f (foldr f z rightPart) lelftPart)
instance Foldable Tree where
    foldr f acc Leaf = acc
    foldr f acc (Node leftPart a rightPart) = foldr f (f a (foldr f acc rirghPart)) leftPart

main = print $ "hello"

