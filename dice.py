import random

def rollingFunction():
    Total = 1000
    f1=f2=f3=f4=f5=f6=0
	
  
    for i in range(Total):
        num = random.random()
		
        if(num >=0 and num<1/6):
            f1 +=1
        elif(num>=1/6 and num<1/3):
            f2 += 1
        elif(num>=1/3 and num<1/2):
            f3 += 1
        elif(num>=1/2 and num<2/3):
            f4 += 1
        elif(num>=2/3 and num<5/6):
            f5 += 1
        elif (num<1):
            f6 += 1 
        
    p1 = str ("%.1f"%(f1/Total*100))	
    p2 = str ("%.1f"%(f2/Total*100))
    p3 = str ("%.1f"%(f3/Total*100))
    p4 = str ("%.1f"%(f4/Total*100))
    p5 = str ("%.1f"%(f5/Total*100))	
    p6 = str ("%.1f"%(f6/Total*100))						
    
    print("Face\t Frequency\t Percentage")
    
    print("1" +"\t"  +str(f1) +"\t\t" + p1)
    print("2" +"\t"  +str(f2) +"\t\t" + p2)
    print("3" +"\t"  +str(f3) +"\t\t" + p3)
    print("4" +"\t"  +str(f4) +"\t\t" + p4)
    print("5" +"\t"  +str(f5) +"\t\t" + p5)
    print("6" +"\t"  +str(f6) +"\t\t" + p6)

    
    print("------------------------------\n Total rolls =", Total,"rolls")
    
rollingFunction()


