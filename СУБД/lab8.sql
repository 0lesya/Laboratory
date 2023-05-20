-- Создание процедуры на увеличение числа подчиненных строк --
CREATE PROCEDURE addNORR(
@Id  int
) 
AS
-- Прибавляет 1 к числу подчиненных строк в таблице Passengers
-- Входной параметр @Id задает индентификатор пассажира
-- Процедура возвращает код –100, если пассажир с 
-- идентификатором @Id отсутствует 
SET NOCOUNT ON;
UPDATE dbo.Passengers SET NORR = NORR + 1
  WHERE Id = @Id;
IF @@RowCount=0
   RETURN -100;
RETURN;
GO

--Создание процедуры на добавление строки в таблицу Tickets
CREATE PROCEDURE addTicket(
@TripCode int,
@PassegerId int,
@Seat int,
@Cost money,
@Date date
)
AS
-- Добавляет строку  в таблицу Tickets и корректирует общий количество подчиненных строк
--Входной параметр @TripCode задает номер поезда
--Входной параметр @PassangerId задает индентификатор пассажира
--Входной параметр @Seat задает номер места
--Входной параметр @Cost задет стоимость билета
--Входной параметр @Date задает дату отправления
--Процедура возвращает код –100, если пассажир с 
--идентификатором @Id отсутствует 
SET NOCOUNT ON;
INSERT INTO dbo.Tickets([Trip code], [Passenger id], Seat, Cost, Date)
	VALUES(@TripCode, @PassegerId, @Seat, @Cost, @Date)
RETURN;
GO


-- Создание процедуры на уменьшение числа подчиненных строк --
CREATE PROCEDURE subNORR( 
@Id  int
) 
AS
-- Вычитает 1 из числа подчиненных строк в таблице Passengers
-- Входной параметр @Id задает индентификатор пассажира
-- Процедура возвращает код –100, если пассажир с 
-- идентификатором @Id отсутствует 
SET NOCOUNT ON;
UPDATE dbo.Passengers SET NORR = NORR - 1
  WHERE Id = @Id;
IF @@RowCount=0
   RETURN -100;
RETURN;
GO

--Создание процедуры на удаление строки из таблицы Tickets
CREATE PROCEDURE removeTicket(
@Number int,
@PassegerId int
)
AS
-- Удаляет строку из таблицы Tickets и корректирует общий количество подчиненных строк
-- Входной параметр @Number задает индентификатор билета
-- Входной параметр @PassegerId задает индентификатор пассажира
-- Процедура возвращает код –100, если пользователь с 
-- идентификатором @PassegerId отсутствует 
-- Процедура возвращает код –101, если запрос с 
-- идентификатором @Id отсутствует 
SET NOCOUNT ON;
DELETE FROM dbo.Tickets
	WHERE (Number = @Number AND [Passenger id]=@PassegerId)
IF @@ROWCOUNT=0
	RETURN -101;
RETURN;
GO

-- Создание триггера afterInsert --
CREATE TRIGGER ai_Tickets_trig ON Tickets
AFTER Insert
AS
SET NOCOUNT ON
Declare @RetCode int,
@Inserted int;
SELECT TOP 1 @Inserted = [Passenger id] FROM inserted;
EXEC @RetCode = addNORR @Inserted;
GO

-- Создание триггера afterDelete --
CREATE TRIGGER ad_Tickets_trig ON Tickets
AFTER Delete
AS
SET NOCOUNT ON
Declare @RetCode int,
@Inserted int;
SELECT TOP 1 @Inserted = [Passenger id] FROM deleted;
EXEC @RetCode = subNORR @Inserted;
GO

ALTER TABLE Tickets ENABLE TRIGGER  ad_Tickets_trig


-- тестирование триггера afterDelete
--Declare @RetCode int; 
--EXEC @RetCode = removeTicket 116, 11;
--SELECT @RetCode;
