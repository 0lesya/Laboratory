Feature: Calculator testing

Scenario Outline: Add two numbers
  Given I have entered <val> into the calculator
  And I have entered <second_val> into the calculator
  When I press <action>
  Then the <result> should be on the screen

  Examples: names
    | val| second_val | action| result|
    | 10 | 10         | plus  | 20    |
    | 10 | 10         | minus | 0     |
    | 20 | 30         | plus  | 50    |
    | 10 | 10         | multiply  | 100    |
    | 10 | 10         | divide | 1    |
    | 10 | 0         | divide | Ошибка! Попытка деления на 0|
