Feature: Calculator testing

Scenario Outline: Add two numbers
  Given I have entered "<value>" into the calculator
  And I have entered "<second_value>" into the calculator
  When I press <action>
  Then the <result> should be on the screen

  Examples: names
    | value| second_value | action| result|
    |25   | 25    | onPlusClicked     |Ответ: 50                          |
    |0    | 44    | onMinusClicked    |Ответ: -44                         |
    |2    | 0     | onMultiplyClicked |Ответ: 0                           |
    |101  | 2     | onDivideClicked   |Ответ: 50.5                        |
    |32   | fg    | onPlusClicked     |Ошибка! Введите число              |
    |101  | 0     | onDivideClicked   |Ответ: Ошибка! Попытка деления на 0|
    |2    | 4.6   | onMultiplyClicked |Ответ: 9.2                         |
    |25   | 2.05  | onPlusClicked     |Ответ: 27.05                        |





