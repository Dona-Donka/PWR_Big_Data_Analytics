# późno, bo miało byc poprawione XD

package SCALA_programming_and_classification
import scala.collection.mutable.ListBuffer

object PrimeNumber {
  def main(parameters: Array[String]): Unit = {

    var number_list = new ListBuffer[Int]()
    if (parameters.length == 0)
      println("Set an argument!")

    parameters.foreach(number =>
      try {
          number_list += number.toInt
      }
      catch {
        case exception: NumberFormatException =>
          println(number, "invalid argument")
      })

    var n : Int = number_list.head
    number_list -= number_list.head
    var prime_list = new ListBuffer[Int]()



    for (i <- 2 until n) {

        var counter: Int = 0
        for (div <- 2 until n) {
          if (i != div && i % div == 0) {
            counter = counter + 1
          }
        }
        if (counter == 0) {
          prime_list += i
        }
      }
    println("range: " + 0 + " - " + n)
    println(number_list)
    println(prime_list)

    for (item <-number_list){
      try {
        println(item + " - " + prime_list.apply(item))
      } catch{
        case exception: IndexOutOfBoundsException =>
          println(item + "is out of range")
      }
    }
    }
}

#------------task 2---------------
package SCALA_programming_and_classification.theGreatestDivisor_ver2

import scala.collection.mutable.ListBuffer

object PascalsTriangle2 {
  def main(args: Array[String]): Unit = {

    var n: Int = 7
    var k: Int = 0

    var list = new ListBuffer[Int]()

    for (line <- 1 to n){
      list.clear()
        var C: Int = 1
        for (i <- 1 to line) {
          k += 1
          if (k > line -k) { k = line - k}
          C = C * (line - i) / i
          list += C
        }

      println(list)

    }
    }

}


