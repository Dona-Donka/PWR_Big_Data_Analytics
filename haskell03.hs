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
