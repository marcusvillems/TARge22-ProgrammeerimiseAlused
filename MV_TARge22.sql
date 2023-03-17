create table Gender

(
Id int not null primary key,
Gender nvarchar(10) not null
)
--andmete sisestamine
insert into Gender (Id,Gender)
values (1, 'Female')
insert into Gender (Id,Gender)
values (2, 'Male')
insert into Gender (Id,Gender)
values (3, 'Unknown')

--- vaatame tabeli sisu
select * from Gender

-- tabeli tegemine
create table Person
(
Id int not null primary key,
Name nvarchar(30),
Email nvarchar(30),
GenderId int
)

insert into Person (Id, Name, Email, GenderId)
values (1, 'Superman', 's@s.com', 2)
insert into Person (Id, Name, Email, GenderId)
values (2, 'Wonderwoman', 'w@w.com', 1)
insert into Person (Id, Name, Email, GenderId)
values (3, 'Batman', 'bat@bat.com', 2)
insert into Person (Id, Name, Email, GenderId)
values (4, 'Aquaman', 'a@a.com', 2)
insert into Person (Id, Name, Email, GenderId)
values (5, 'Catwoman', 'c@c.com', 1)
insert into Person (Id, Name, Email, GenderId)
values (6, 'Antman', 'ant"ant.com', 2)
insert into Person (Id, Name, Email, GenderId)
values (8, NULL, NULL, 2)

--kuidas saab tabeli sisu vaadata???
select * from Person

--v��rv�tme �henduse loomine kahe tabeli vahel
alter table Person add constraint tblPerson_GenderId_FK
foreign key (GenderId) references Gender(Id)


--kui sisestad uue rea andmeid ja ei ole sisestanud GenderId alla v��rtust,
-- siis see automaatselt sisestab sellele reale v��rtuse 3
alter table Person
add constraint DF_Person_GenderId
default 3 for GenderId

insert into Person (Id, Name, Email)
values (11, 'asdasd', 'asd@asd.com')

select * from Person

--piirangu maha v�tmine
alter table Person
drop constraint DF_Persons_GenderId

--lisame uue veeru juurde
alter table Person
add Age nvarchar(10)

--lisame nr piirangu vanuse sisestamisel
alter table Person
add constraint CK_Person_Age check (Age > 0 and Age < 155)

--andmete uuendamine
update Person
set Age = 50
where Id = 6

select * from Person

insert into Person (Id, Name, Email, GenderId, Age)
values (7, 'Robin', 'r@r.com', 2, 21)
insert into Person (Id, Name, Email, GenderId, Age)
values (9, 'Thor', 't@t.com', 2, 35)
insert into Person (Id, Name, Email, GenderId, Age)
values (10, 'Ironman', 'i@iron.com', 2, 45)

--lisame veeru juurde
alter table Person
add City nvarchar(50)

---k�ik, kes elavad Gothami linnas
select * from Person where City = 'Gotham'
--k�ik kes ei ela Gothamis
select * from Person where City != 'Gotham'
--k�ik kes ei ela Gothamis, teine variant
select * from Person where City <> 'Gotham'

--n�itab teatud vanusega inimesi
select * from Person where Age = 120 or Age = 50 or Age = 28
select * from Person where Age in (120, 50, 28)

--n�itab teatud vanusevahemikus olevaid inimisesi
select * from Person where Age between 40 and 120

--widlcardi kasutamine n�itab k�ik g-t�hega linnad
select * from Person where City like 'n%'
--emaill, milles on @ m�rk
select * from Person where Email like '%@%'

--n�itab k�iki, kellel on emailise ees ja peale @-m�rki ainult �ks t�ht
select * from Person where Email like '_@_.com'

--k�ik, kellel nimes ei ole esimene t�ht W, A ja C
select * from Person where Name like '[^WAC]%'

--- kes elavad Gothamis ja New Yorkis
select * from Person where City = 'Gotham' or City = 'New York'
--kes elavad Gothamis ja New Yorkis ning on vanemad kui 29
select * from Person where (City = 'Gotham' or City = 'New York')
and Age >= 27

--kuvab t�hestiku j�rjekorras inimesi ja v�tab aluseks nime
select * from Person order by Name
--vastupidine j�rjestus
select * from Person order by Name desc

--v�tab kolm esimest rida
select top 3 * from Person

--kolm esimest, aga tabeli j�rjestuses on Age ja siis Name
select top 3 Age, Name from Person

--kuvab esimesed 50% tabelist
select top 50 percent * from Person

--v�tab neli esimest ja j�rjestab vanuse j�rgi
select top 4 * from Person order by Age desc

--muudab Age muutuja intiks ja n�itab vanuselises j�rjestuses
select * from Person order by cast(Age as int)

--kuvab k�ige nooremat isikut
select MIN(CAST(Age as int)) from Person
--kuvab k�ige vanemat isikut
select MAX(CAST(Age as int)) from Person


--n�eme konkreetsetes linnades olevate isikute koondavust
select City, SUM(Age) as TotalAge from Person group by City

--muudame koodiga andmet��pi ja selle pikkust
alter table Person
alter column Name nvarchar(25)

--kuvab esimeses reas v�lja toodud j�rjestuses ja kuvab Age-i
-- TotalAge-iks
--j�rjestab City's olevate nimede j�rgi ja siis GenderId j�rgi
select City, GenderId, SUM(Age) as TotalAge from Person
group by City, GenderId order by City

--n�itab, et mitu rida on selles tabelis
select COUNT(*) from Person

--n'itab tulemust, et mitu inimest on GenderId v��rtusega 2
--konkreetses linnas
--arvutab vanuse kokkuselles linnas
select GenderId, City, SUM(Age) as TotalAge, COUNT(Id) as [Total Person(s)]
from Person where GenderId = '2'
group by GenderId, City

--n�itab �ra, et mitu inimest on vanemad, kui 41 ja kui
--palju igas linnas elab
select GenderId, City, SUM(Age) as TotalAge, COUNT(Id) as [Total Person(s)]
from Person
group by GenderId, City having SUM(Age) > 41



--loome kaks tabelit
create table Department
(
Id int primary key,
DepartmentName nvarchar(50),
Location nvarchar(50),
DepartmentHead nvarchar(50)
)

create table Employees
(
Id int primary key,
Name nvarchar(50),
Gender nvarchar(50),
Salary nvarchar(50),
DepartmentId int
)

insert into Employees(Id, Name, Gender, Salary, DepartmentId)
values(1, 'Tom', 'Male', 4000, 1)
insert into Employees(Id, Name, Gender, Salary, DepartmentId)
values(2, 'Pam', 'Female', 3000, 3)
insert into Employees(Id, Name, Gender, Salary, DepartmentId)
values(3, 'John', 'Male', 3500, 1)
insert into Employees(Id, Name, Gender, Salary, DepartmentId)
values(4, 'Sam', 'Male', 4500, 2)
insert into Employees(Id, Name, Gender, Salary, DepartmentId)
values(5, 'Todd', 'Male', 2800, 2)
insert into Employees(Id, Name, Gender, Salary, DepartmentId)
values(6, 'Ben', 'Male', 7000, 1)
insert into Employees(Id, Name, Gender, Salary, DepartmentId)
values(7, 'Sara', 'Female', 4800, 3)
insert into Employees(Id, Name, Gender, Salary, DepartmentId)
values(8, 'Valarie', 'Female', 5500, 1)
insert into Employees(Id, Name, Gender, Salary, DepartmentId)
values(9, 'James', 'Male', 6500, NULL)
insert into Employees(Id, Name, Gender, Salary, DepartmentId)
values(10, 'Russell', 'Male', 8800, NULL)

select * from Employees

insert into Department(Id, DepartmentName, Location, DepartmentHead)
values(4, 'Other Department', 'Sydney', 'Cindrella')