##Parse Tree for TINY Language.

## How to run:
clone the repo
pip3 install -r requirements.txt
python3 main.py

## Input:
Place your Tiny syntax in sample_input.txt file

## Output:
output.png

## Examples:

```
read x; 
if 0 < x then 
fact := 1;
repeat
fact := fact * x;
x := (x - 1);
until (x = 0)
write fact
end
```
![alt parse tree](https://imgur.com/a/NIAGXAe)
```
x:= 2 ;
y := 3 ;
z := 5 ;
a := x+y+z ;
if z < 8 then
repeat
a:= a*2 ;
z:= z-1 
until z = 0 ;
write a
else
read b;
if b = 1 then
wtite b*(x-y)
else
write a 
end
end ;
write z
```
![alt parse tree](https://drive.google.com/open?id=1xJXOa5n9xj1GGGfUC8P0nun6Y6DuRC-x)
