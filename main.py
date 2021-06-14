guion = open ("Texto.txt", encoding='utf8')
i=0
contador=0

"_________Word for looking___"
someWord=("Harry") 
"____________________________"

for line in guion.readlines():
   SinComa=line.split(",")
   TextoSinComa=" ".join(SinComa)

   Texto=TextoSinComa.split()

   i=Texto.count(someWord)
   contador=contador+i

print(someWord +", "+ str (contador))
guion.close()