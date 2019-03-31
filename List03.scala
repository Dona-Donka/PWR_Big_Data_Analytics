package SCALA_programming_and_classification.List03

abstract class Figure {

  def perimeter(side: Float): Unit = println(side)
  def field(side: Float): Unit = println(side*side)

  var side: Float
}

#----------Circle.scala--------
package SCALA_programming_and_classification.List03
import java.lang.Math._

class Circle(rad: Float) extends Figure(){

  override def perimeter(rad: Float): Unit = (2*PI*rad).toFloat
  override def field(rad: Float): Unit = (PI*rad*rad).toFloat

  override var side: Float = _
}

object circle{
  def main(args: Array[String]): Unit = {
    println("Hello from circle!")
  }
}

package SCALA_programming_and_classification.List03

class Rectangle(side1: Float, side2: Float) extends Figure(){

override def perimeter(rad: Float): Unit = (side1*side2).toFloat
override def field(rad: Float): Unit = (2*(side1+side2)).toFloat

  override var side: Float = _

}


object rectangle{
  def main(args: Array[String]): Unit = {
    println("Hello from rectangle!")
  }
}

#----------Hexagon.scala---------
package SCALA_programming_and_classification.List03
import scala.math.sqrt

class Hexagon(side1: Float) extends Figure(){

    override def perimeter(rad: Float): Unit = 6*side1
    override def field(rad: Float): Unit = (3*(side1*side1*sqrt(3))/2).toFloat

  override var side: Float = _
}


  object hexagon{
    def main(args: Array[String]): Unit = {
      println("Hello from hexagon!")
    }
}


