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
