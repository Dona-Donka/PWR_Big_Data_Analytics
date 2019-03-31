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
package SCALA_programming_and_classification

import scala.collection.mutable.ListBuffer

object PascalsTriangle {

  def main(args: Array[String]): Unit = {
    println("Hello World!")

    var n: Int = 7
    var list = new ListBuffer[Int]()

    def print_triangle(n: Int): Unit ={
      for(line <- 0 until n){
        for( i <- 0 until line){
          println("dupa" + i + line)
          println("triang: " + pascals_triangle(line, i))
          println("\n")
        }
      }
    }

    def pascals_triangle(n: Int, k: Int): Unit ={
      var res : Int = 1
      if (k > n - k){k == n - k}
      for (item <- 0 until k){
        println("pascal funct" + item + k + n)
        res = res*(n - 1)/(item + 1)
        list += res

        /* println("res: " + res) */
      }
      return res

    }

    print_triangle(n)
  }
}



