
package SCALA_programming_and_classification

/* mport SCALA_programming_and_classification.List01.args /*


/* ------ HelloScala---------/* 

object HelloScala {
  def main(args: Array[String]): Unit = {
    println("Hello World!")
  }
}

/*------ScalaParameters---------/*

object ScalaParameters {
  def main(parameters: Array[String]): Unit = {
    if (parameters.length == 0)
    println("Set an argument!")
    else{
      parameters.foreach(println(_))
    }
  }
}

/*------TheGreatestDivisior----------/*

import scala.collection.mutable.ListBuffer
import scala.util.control.Breaks._

object TheGreatestDivisor{
   def main(parameters: Array[String]): Unit = {
     var sum: Int = 0
     var divList = new ListBuffer[Int]()
     val numbers_list: List[Int] = List(24, 13, 50, 46, 9)
     for (number <- numbers_list) {
       for (div <- 1 to number) {
         divList += div
       }
       divList -= number
       breakable {for (item <- divList.reverseIterator){
         if (number % item == 0){
           println(number + " : " + item)
           break()
         }}
       }
       divList.clear()

     }
  }
}


/*------TheGreatestDivisior_ver.1.1----------/*

import scala.collection.mutable.ListBuffer
import scala.util.control.Breaks._

object TheGreatestDivisor_ver2 {
  def main(parameters: Array[String]): Unit = {


    var number_list = new ListBuffer[Int]()
    var divList = new ListBuffer[Int]()

    if (parameters.length == 0)
      println("Set an argument!")

    parameters.foreach(number =>
      try {
       number_list += number.toInt
      }
      catch {
        case exception: NumberFormatException =>
          println(number ,"Conversion not possible")
      })

      println(number_list)
    for (number <- number_list) {
      for (div <- 1 to number) {
        divList += div
      }

      divList -= number
      breakable {for (item <- divList.reverseIterator){
        if (number % item == 0){
          println(number + " : " + item)
          break()
        }}
      }
      divList.clear()
    }
  }
}
