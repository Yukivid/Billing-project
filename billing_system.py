import mysql.connector as sql,random , datetime as dt
import pickle
import matplotlib.pyplot as plt
import random
from tkinter import *
root = Tk()


print("                            BILLINS SYSTEM PROJECT                                  ")
print("This is our python project (Billing System)")
print("We have created 2 Billing System")
print( "1.Electric Billing System")
print( "2.Pharmacy Billing System")
D=int(input("Enter the choice for seeing the project: "))

if D==1:
    
    "Creating table in MySQL"
    conn=sql.connect(host='localhost',user='root',password='yukivid',database='ebs')
    c1=conn.cursor()
    '''
    c1.execute('create table newuser(username VARCHAR(100) primary key,password VARCHAR(100),confirmpasswd VARCHAR(100));')
    c1.execute('create table AddNewCustomer(accountno INT primary key,name VARCHAR(25), password VARCHAR(100), bankname VARCHAR(25) , bankbranch VARCHAR(25) , address VARCHAR(100) , areacode INT(6) , phoneno INT(255),email VARCHAR(10000) , boxid VARCHAR(25));')
    c1.execute('create table Transaction(name VARCHAR(25),accountno INT(10), unit INT(10), toda VARCHAR(25),totamt INT(10), totalamt INT(10), p VARCHAR(25) ,fine INT(50),dues INT(50),month INT(10),foreign key(accountno) references AddNewCustomer(accountno));')
    c1.execute('create table Management(accountno INT(10),username VARCHAR(100),unit INT(10),month INT(10));')
    print("tables created")
    '''

    if conn.is_connected():
        print("successfully connected")
        c = "YES" or "yes" or "Yes"
        V = "YES" or "yes" or "Yes"
        c1 = conn.cursor()

        while c == "YES" or "yes" or "Yes":
            print('*******WELCOME TO ELECTRIC BILLING SYSTEM**********')
            print(dt.datetime.now())
            print("1.NEW USER")
            print("2.EXISTING USER")
            print("3.MANAGEMENT")
            print("4.EXIT")

            choice1 = int(input("ENTER THE CHOICE: "))
            if choice1 == 1:
                f1=open("NEWUSER.txt","ab+")
                l=[]
                username=input("Enter your username : ")
                password=input("Enter your password: ")
                confirmpasswd=input("Confirm your password: ")
                l.append(str(username)+" "+str(password)+" "+str(confirmpasswd))
                pickle.dump(l,f1)
                f1.close()

                if password == confirmpasswd:
                    info1="insert into newuser values('{}','{}','{}')".format(username,password,confirmpasswd)
                    c1.execute(info1)
                    conn.commit()
                    c=input("do you want to continue?(yes or no)")

                else:
                    print('your confirm password is incorrect ')
                    print('Try Again')
                    c = input("do you want to continue?(Yes or No)")

                    
            elif choice1==2:
                username=input("Enter your username: ")
                password=input("Enter your password: ")
                info2="select * from newuser where username='{}'and password='{}'".format(username,password)
                c1.execute(info2)
                data=c1.fetchall()
    
                for row in data:
                    x=row[0]
                    y=row[1]
                if username==x:
                    if password==y:

                        while V=='YES'or'yes'or'Yes':
                            if any(data):
                                print("**********WELCOME TO ELECTRICITY BILLING SYSTEM********")
                                print("1.ACCOUNT SETTING")
                                print("2.TRANSACTION")
                                print("3.VIEW CUSTOMER DETAILS")
                                print("4.GRAPHICAL REPRESENTATION")
                                print("5.EXIT")
                                choice2=int(input("ENTER YOUR CHOICE: "))


                                if choice2 == 1:
                                    print("1.NEW CUSTOMER")
                                    print("2.DELETE EXISTING ACCOUNT")
                                    choice12=int(input("ENTER YOUR CHOICE: "))


                                    if choice12==1:
                                        f=open("NEWCUSTOMER.txt","a+")
                                        name=input("Enter your name: ")
                                        accountno=random.randrange(1000000,9999999,10)
                                        print("Your accountno is",accountno)
                                        password=input("Enter your password: ")
                                        bankname=input("Enter your BANK NAME: ")
                                        bankbranch = input("Enter your BANK BRANCH: ")
                                        address=input("Enter your address: ")
                                        areacode=int(input("Enter your AREA PIN CODE: "))
                                        phoneno=int(input("Enter your PHONE NUMBER: "))
                                        email=input("Enter the email: ")
                                        boxid=input("Enter the meter box ID: ")
                                        f.write(str(accountno)+" "+str(boxid)+" "+bankname+" "+bankbranch+" "+name+" "+str(password)+" "+address+" "+str(areacode)+" "+str(phoneno)+" "+email+"\n")
                                        f.close()
                                        info3="insert into AddNewCustomer values('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(accountno,name,password,bankname,bankbranch,address,areacode,phoneno,email,boxid)
                                        c1.execute(info3)
                                        conn.commit()

                                        V=input("do you want to continue?(yes or no)")
                                        if V =="yes":
                                            continue
                                        else:
                                            break


                                    elif choice12==2:
                                        acc = int(input("ENTER YOUR ACCOUNT NUMBER: "))
                                        unit = int(input("ENTER THE AMOUNT OF UNITS CONSUMED LAST MONTH: "))
                                        info37=c1.execute("select * from transaction where accountno={} and unit={}".format(acc,unit))
                                        c1.execute(info37)
                                        data=c1.fetchall()

                                        for i in data:
                                            p=i[6]
                                            d=i[8]
                                        p1=p.lower()
                                        paid=input("Enter wethere u have paid the bill or not(yes or no): ")
                                        paid1=paid.lower()

                                        if paid1=="yes":
                                            if ((paid1==p1)and(d==0))==True:
                                                acc = input("ENTER YOUR ACCOUNT NUMBER: ")
                                                use = input("ENTER YOUR USERNAME: ")
                                                info6=c1.execute("delete from Transaction where accountno='{}'".format(acc))
                                                info7=c1.execute("delete from AddNewCustomer where accountno='{}'".format(acc))
                                                info8=c1.execute("delete from newuser where username ='{}'".format(use))
                                                c1.execute(info6)
                                                c1.execute(info7)
                                                c1.execute(info8)
                                                conn.commit()
                                                print("THANLKS FOR USING THE SOFTWARE ,YOUR ACCOUNT IS SUCCESSFULLY DELETED")
                                                V=input("do you want to continue?(yes or no)")
                                                if V =="yes":
                                                    continue
                                                else:
                                                    break
                                            else:
                                                print("Sry,dear1 customer u cannot delete the account(as u have not paid the bill)")
                                        elif (paid1=="no"):
                                            print("Sry,dear customer u cannot delete the account(as u have not paid the bill)")
                                        else:
                                            print("Dear customer u have entered wrong input")


                                    else:
                                        print("INVALID INPUT")

                                elif choice2 == 2:
                                    name=input("Enter your name: ")
                                    accountno=int(input("Enter your account number : "))
                                    password=str(input("Enter your password : "))
                                    info9 = "select * from addnewcustomer where accountno= "+str(accountno)
                                    c1.execute(info9)
                                    data1=c1.fetchall()

                                    for row in data1:
                                        x=row[0]
                                        y=row[2]

                                    if accountno==x:
                                        if  password==y:
                                            acc = int(input("ENTER YOUR ACCOUNT NUMBER: "))
                                            toda=dt.date.today()
                                            year=toda.year
                                            month=toda.month
                                            info307=c1.execute("select * from Management where accountno={} and month={}".format(acc,month))
                                            c1.execute(info307)
                                            data_X=c1.fetchall()
                                            for row in data_X:
                                                unit=row[2]
                                            print('Dear customer , you have used',unit,'unit of electricity.')
                                            print("Rule:No due should be kept,only full amount is accepted")
                                            print("Thts why we have given u 15 days of timegap")
                                            reading_date=dt.date(year,month,day=1)
                                            deadline=reading_date+dt.timedelta(days=14)
                                            print('Dear customer , you have to pay the bill before',deadline,'else u must the fine also')
                                            def no_of_days(d1,d2):
                                                return(d2-d1).days
                                            d1=toda
                                            d2=deadline
                                            n=no_of_days(d1,d2)
                                        
                                            if n>=0:
                                                if n==0:
                                                    print('Dear customer,it is the last day for paying the bill')
                                                    fine=0
                                                else:
                                                    print('Dear customer,u have',n,'day for paying the bill')
                                                    fine=0
                                            else:
                                                n1=abs(n)
                                                print('Dear customer,u have exeded the timelimit by',n1,'days')
                                                if n1==1:
                                                    fine=10
                                                elif (n1==2)or(n1==3):
                                                    fine=22
                                                elif (n1==4)or(n1==5)or(n1==6):
                                                    fine=33
                                                elif (n1==7)or(n1==8)or(n1==9):
                                                    fine=45
                                                elif (n1==10)or(n1==11)or(n1==12)or(n1==13):
                                                    fine=60
                                                elif (n1==14)or(n1==15)or(n1==16):
                                                    fine=100
                                                else:
                                                    fine=500


                                            if unit<=100:
                                                amount=0
                                            elif unit<=200:
                                                amount=(unit-100)*1.5
                                            elif unit<=500:
                                                amount1=100*1.5
                                                amount2=100*2
                                                amount3=(unit-200)*3
                                                amount=amount1+amount2+amount3
                                            else:
                                                amount1=100*1.5
                                                amount2=100*3.5
                                                amount3=300*4.6
                                                amount4=(unit-500)*6.6
                                                amount=amount1+amount2+amount3+amount4

                                            m=input("Enter the  month you want to pay the due: ")
                                            if m == 'January'or'january'or'JANUARY'or'JAN'or'jan'or'Jan'or'1':
                                                month=1
                                            elif m == 'February'or'february'or'FEBRUARY'or'Feb'or'FEB'or'feb'or'2':
                                                month=2
                                            elif m == 'March'or'march'or'MARCH'or'Mar'or'mar'or'MAR'or'3':
                                                month=3
                                            elif m == 'April'or'april'or'APRIL'or'APR'or'Apr'or'apr'or'4':
                                                month=4
                                            elif m == 'MAY'or'May'or'may'or'5':
                                                month=5
                                            elif m == 'JUNE'or'June'or'june'or'JUN'or'Jun'or'jun'or'6':
                                                month=6
                                            elif m == 'JULY'or'July'or'july'or'JUL'or'Jul'or'jul'or'7':
                                                month=7
                                            elif m == 'AUGUST'or'August'or'august'or'AUG'or'Aug'or'aug'or'8':
                                                month=8
                                            elif m == 'SEPTEMBER'or'September'or'september'or'SEPT'or'Sept'or'sept'or'9':
                                                month=9
                                            elif m == 'OCTOBER'or'October'or'october'or'OCT'or'Oct'or'oct'or'10':
                                                month=10
                                            elif m == 'NOVEMBER'or'November'or'november'or'NOV'or'Nov'or'nov'or'11':
                                                month=11
                                            else:
                                                month=12
    
                                            info38=c1.execute("select * from transaction where accountno={} and month={}".format(accountno,month))
                                            c1.execute(info38)
                                            data=c1.fetchall()
                                            if data==[]:
                                                d1=0
                                            else:
                                                for i in data:
                                                    d=i[8]
                                                if d=="None":
                                                    d1=0
                                                else:
                                                    d1=d
            
                                            totalamt=round(amount+fine+d1)
                                            print("Dear customer the total amount you got to pay is",totalamt)
                                            totamt=int(input("Enter the amount u are going to pay: " ))
                                            p=input("Please enter YES to transact")
                                            if p == "YES"or"yes"or"Yes":
                                                print("Transaction successfuil")
                                                print("You have paid bill")
                                            else:
                                                print("plz pay the bill sooner")

                                            dues=totalamt-totamt
                                            if dues==0 :
                                                print("There is no dues")
                                            elif dues<0:
                                                a=abs(dues)
                                                print("Dear customer,u may have mistakenly paid extra",a,"amount ,it would be refunded within a week")
                                            else:
                                                print("Dear customer,u may have paid a partial amount.Please try to pay the rest of the",dues," amount as soon as possible")
                                            
                                            info8="insert into transaction values('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(name,accountno,unit,toda,totamt,totalamt,p,fine,dues,month)
                                            c1.execute(info8)
                                            conn.commit()
                                       
                                        else:
                                            print("wrong password")
                                            u=input("do you want to retry?(yes or no)")
                                            if u =="yes":
                                                continue
                                            else:
                                                break
                                    else:
                                        print("wrong accountno")
                                        w=input("do you want to retry?(yes or no)")
                                        if w =="yes":
                                            continue
                                        else:
                                            break
                                    V=input("do you want to continue?(yes or no)")
                                    if V =="yes":
                                        continue
                                    else:
                                        break

                                elif choice2 == 3:
                                    accountno=int(input("Enter your account number : "))
                                    info9 = "select * from addnewcustomer where accountno= "+str(accountno)
                                    c1.execute(info9)
                                    data1=c1.fetchall()
                                
                                    for row in data1:
                                        print("Person name: ",row[1])
                                        print("Account Number: ",row[0])
                                        print("bankname: ",row[3])
                                        print("bankbranch: ",row[4])
                                        print("Residancial address: ",row[5])
                                        print("area code: ",row[6])
                                        print("phone number: ",row[7])
                                        print("email: ",row[8])
                                        print("Your meter device ID: ",row[9])
                                    info10 = "select * from transaction where accountno = " + str(accountno)
                                    c1.execute(info10)
                                    data2=c1.fetchall()

                                    for row in data2:
                                        print("unit consumed: ",row[2])
                                        print("paid on: ",row[3])
                                        print("amount to be paid : ",row[5])
                                        print("amount you have paid : ",row[4])

                                    V=input("do you want to continue?(yes or no)")
                                    if V =="yes":
                                        continue
                                    else:
                                        break


                                elif choice2 == 4:
                                    info11="select accountno,totalamt from Transaction"
                                    c1.execute(info11)
                                    L1,L2,=[],[]
                                    for i in c1.fetchall():
                                        L1.append(i[0])
                                        L2.append(i[1])
                                    plt.plot(L1,L2)
                                    plt.title("GRAPH")
                                    plt.show()

                                    V=input("do you want to continue?(yes or no)")
                                    if V =="yes":
                                        continue
                                    else:
                                        break


                                elif choice2 == 5:
                                    print("          THANK YOU!!!! VISIT AGAIN!!!!             ")
                                    break


                                else:
                                    print("Invalid Input")
                                    print("username / password is incorrect")
                                    break

                                c=input("do you want to try again?(yes or no)")
                                if c =="yes":
                                    continue
                                else:
                                    break

                    else:
                        print("wrong password")
                        u=input("do you want to retry?(yes or no)")
                        if u =="yes":
                            continue
                        else:
                            break

                else:
                    print("wrong username")
                    u=input("do you want to retry?(yes or no)")
                    if u =="yes":
                        continue
                    else:
                        break
            elif choice1 == 3:
                code = "AZ_123MN09"
                z=input("Enter the secure password for recording: ")
                if z == code :
                    accountno =int(input("Enter your account number : "))
                    unit =int(input("Enter the units consumed in this month : "))
                    username=input("Enter your name of the user: ")
                    month=input("Enter the month the units are recorded: ")
                    info99="insert into Management values('{}','{}','{}','{}')".format(accountno,username,unit,month)
                    c1.execute(info99)
                    conn.commit()

                else:
                    print("YOU CAN'T ACCESS THIS PART !!!")


            elif choice1 == 4:
                print("   THANK YOU!!!! VISIT AGAIN!!!!   ")
                c="no"
                break

            else:
                print("Invalid choice")
                c=input("do you want to try again?(yes or no)")

    else:
        print("Not Successfully Connected")
    
elif D==2:

    class Pharmacy_Billing(object):


        def __init__(self, root):
            self.root = root
            self.root.maxsize(width=1370, height=720)
            self.root.minsize(width=1370, height=720)
            self.root.title("Pharmacy Billing System")
            self.customer_name = StringVar()
            self.customer_contact_number = StringVar()

            x = random.randint(1, 9999)
            self.cus_invoice_no = StringVar()

            self.cus_invoice_no.set(str(x))
            self.medicol_advance = IntVar()
            self.toseran_forte = IntVar()
            self.imodium = IntVar()
            self.mefenamic = IntVar()
            self.amoxicillin = IntVar()
            self.tiki_tiki_star = IntVar()
            self.neutrilin_drops = IntVar()
            self.profan_tlc = IntVar()
            self.ceelin_plus = IntVar()
            self.cheriper = IntVar()
            self.lidocaine_ointment = IntVar()
            self.canesten_cream = IntVar()
            self.tabeta_ointment = IntVar()
            self.nerisone_ointment = IntVar()
            self.clotrimazole_cream = IntVar()
            self.total_medicine = StringVar()
            self.total_vitamins = StringVar()
            self.total_cream_ointment = StringVar()
            self.tax_medicine = StringVar()
            self.tax_vitamins = StringVar()
            self.tax_cream_ointment = StringVar()

            bg_color = "#000000"
            fg_color = "red"
            lbl_color = 'red'

            title = Label(self.root, text="Pharmacy Billing System", bd=12, relief=RAISED, fg=fg_color, bg=bg_color,
                          font=("Calibri", 36, "bold"), pady=3).pack(fill=X)

            F1 = LabelFrame(text="Customer Information", font=("Calibri", 12, "bold"), fg="gold", bg=bg_color,
                            relief=RAISED, bd=10)
            F1.place(x=0, y=80, relwidth=1)

            customername_lbl = Label(F1, text="Customer Name", bg=bg_color, fg=fg_color,
                               font=("Calibri", 15, "bold")).grid(row=0, column=0, padx=10, pady=5)
            customername_en = Entry(F1, bd=8, relief=RAISED, textvariable=self.customer_name)
            customername_en.grid(row=0, column=1, ipady=4, ipadx=30, pady=5)

            customercontact_lbl = Label(F1, text="Phone No", bg=bg_color, fg=fg_color, font=("Calibri", 15, "bold")).grid(
                        row=0, column=2, padx=20)
            customercontact_en = Entry(F1, bd=8, relief=RAISED, textvariable=self.customer_contact_number)
            customercontact_en.grid(row=0, column=3, ipady=4, ipadx=30, pady=5)

            customerinvoice_lbl = Label(F1, text="Invoice No.", bg=bg_color, fg=fg_color, font=("Calibri", 15, "bold"))
            customerinvoice_lbl.grid(row=0, column=4, padx=20)
            customerinvoice_en = Entry(F1, bd=8, relief=RAISED, textvariable=self.cus_invoice_no)
            customerinvoice_en.grid(row=0, column=5, ipadx=30, ipady=4, pady=5)

            invoice_btn = Button(F1, text="Enter", bd=7, relief=RAISED, font=("Calibri", 12, "bold"), bg=bg_color,
                                fg=fg_color)
            invoice_btn.grid(row=0, column=6, ipady=5, padx=60, ipadx=19, pady=5)
 
            F2 = LabelFrame(self.root, text='Medicine Capsule', bd=10, relief=RAISED, bg=bg_color, fg="gold",
                                font=("Calibri", 13, "bold"))
            F2.place(x=5, y=180, width=325, height=380)

            medicol_advance_lbl = Label(F2, font=("Calibri", 15, "bold"), fg=lbl_color, bg=bg_color, text="Medicol Advance")
            medicol_advance_lbl.grid(row=0, column=0, padx=10, pady=20)
            medicol_advance_en = Entry(F2, bd=8, relief=RAISED, textvariable=self.medicol_advance)
            medicol_advance_en.grid(row=0, column=1, ipady=5, ipadx=5)

            toseran_lbl = Label(F2, font=("Calibre", 15, "bold"), fg=lbl_color, bg=bg_color, text="Toseran Forte")
            toseran_lbl.grid(row=1, column=0, padx=10, pady=20)
            toseran_en = Entry(F2, bd=8, relief=RAISED, textvariable=self.toseran_forte)
            toseran_en.grid(row=1, column=1, ipady=5, ipadx=5)

            imodium_lbl = Label(F2, font=("Calibre", 15, "bold"), fg=lbl_color, bg=bg_color, text="Imodium")
            imodium_lbl.grid(row=2, column=0, padx=10, pady=20)
            imodium_en = Entry(F2, bd=8, relief=RAISED, textvariable=self.imodium)
            imodium_en.grid(row=2, column=1, ipady=5, ipadx=5)

            mefenamic_lbl = Label(F2, font=("Calibre", 15, "bold"), fg=lbl_color, bg=bg_color, text="Mefenamic")
            mefenamic_lbl.grid(row=3, column=0, padx=10, pady=20)
            mefenamic_en = Entry(F2, bd=8, relief=RAISED, textvariable=self.mefenamic)
            mefenamic_en.grid(row=3, column=1, ipady=5, ipadx=5)

            amoxicillin_lbl = Label(F2, font=("Calibre", 15, "bold"), fg=lbl_color, bg=bg_color, text="Amoxicillin")
            amoxicillin_lbl.grid(row=4, column=0, padx=10, pady=20)
            amoxicillin_en = Entry(F2, bd=8, relief=RAISED, textvariable=self.amoxicillin)
            amoxicillin_en.grid(row=4, column=1, ipady=5, ipadx=5)

            F2 = LabelFrame(self.root, text='Vitamins', bd=10, relief=RAISED, bg=bg_color, fg="gold",
                            font=("Calibre", 13, "bold"))
            F2.place(x=330, y=180, width=325, height=380)

            tikitiki_lbl = Label(F2, font=("Calibre", 15, "bold"), fg=lbl_color, bg=bg_color, text="Tiki Tiki Star")
            tikitiki_lbl.grid(row=0, column=0, padx=10, pady=20)
            tikitiki_en = Entry(F2, bd=8, relief=RAISED, textvariable=self.tiki_tiki_star)
            tikitiki_en.grid(row=0, column=1, ipady=5, ipadx=5)

            neutrilin_lbl = Label(F2, font=("Calibre", 15, "bold"), fg=lbl_color, bg=bg_color, text="Neutrilin Drops")
            neutrilin_lbl.grid(row=4, column=0, padx=10, pady=20)
            neutrilin_en = Entry(F2, bd=8, relief=RAISED, textvariable=self.neutrilin_drops)
            neutrilin_en.grid(row=4, column=1, ipady=5, ipadx=5)

            profan_lbl = Label(F2, font=("Calibre", 15, "bold"), fg=lbl_color, bg=bg_color, text="Profan Tlc")
            profan_lbl.grid(row=1, column=0, padx=10, pady=20)
            profan_en = Entry(F2, bd=8, relief=RAISED, textvariable=self.profan_tlc)
            profan_en.grid(row=1, column=1, ipady=5, ipadx=5)

            ceelin_lbl = Label(F2, font=("Calibre", 15, "bold"), fg=lbl_color, bg=bg_color, text="Ceelin Plus")
            ceelin_lbl.grid(row=2, column=0, padx=10, pady=20)
            ceelin_en = Entry(F2, bd=8, relief=RAISED, textvariable=self.ceelin_plus)
            ceelin_en.grid(row=2, column=1, ipady=5, ipadx=5)

            cheriper_lbl = Label(F2, font=("Calibre", 15, "bold"), fg=lbl_color, bg=bg_color, text="Cheriper")
            cheriper_lbl.grid(row=3, column=0, padx=10, pady=20)
            cheriper_en = Entry(F2, bd=8, relief=RAISED, textvariable=self.cheriper)
            cheriper_en.grid(row=3, column=1, ipady=5, ipadx=5)



            F2 = LabelFrame(self.root, text='Cream and Ointment', bd=10, relief=RAISED, bg=bg_color, fg="gold", font=("Calibre", 13, "bold"))
            F2.place(x=655, y=180, width=325, height=380)

            licodaine_lbl = Label(F2, font=("Calibre", 15, "bold"), fg=lbl_color, bg=bg_color, text="Lidocaine Ointment")
            licodaine_lbl.grid(row=0, column=0, padx=10, pady=20)
            licodaine_en = Entry(F2, bd=10, relief=RAISED, textvariable=self.lidocaine_ointment)
            licodaine_en.grid(row=0, column=1, ipady=5, ipadx=5)

            canesten_lbl = Label(F2, font=("Calibre", 15, "bold"), fg=lbl_color, bg=bg_color, text="Canesten Cream")
            canesten_lbl.grid(row=1, column=0, padx=10, pady=20)
            canesten_en = Entry(F2, bd=8, relief=RAISED, textvariable=self.canesten_cream)
            canesten_en.grid(row=1, column=1, ipady=5, ipadx=5)

            tabeta_lbl = Label(F2, font=("Calibre", 15, "bold"), fg=lbl_color, bg=bg_color, text="Tabeta Ointment")
            tabeta_lbl.grid(row=2, column=0, padx=10, pady=20)
            tabeta_en = Entry(F2, bd=8, relief=RAISED, textvariable=self.tabeta_ointment)
            tabeta_en.grid(row=2, column=1, ipady=5, ipadx=5)

            nerizone_lbl = Label(F2, font=("Calibre", 15, "bold"), fg=lbl_color, bg=bg_color, text="Nerizone Ointemnt")
            nerizone_lbl.grid(row=3, column=0, padx=10, pady=20)
            nerizone_en = Entry(F2, bd=8, relief=RAISED, textvariable=self.nerisone_ointment)
            nerizone_en.grid(row=3, column=1, ipady=5, ipadx=5)

            clotrimazole_lbl = Label(F2, font=("Calibre", 15, "bold"), fg=lbl_color, bg=bg_color, text="CLotrimazole Cream")
            clotrimazole_lbl.grid(row=4, column=0, padx=10, pady=20)
            clotrimazole_en = Entry(F2, bd=8, relief=RAISED, textvariable=self.clotrimazole_cream)
            clotrimazole_en.grid(row=4, column=1, ipady=5, ipadx=5)

            F3 = Label(self.root, bd=10, relief=RAISED)
            F3.place(x=1010, y=180, width=350, height=350)

            receipt_title = Label(F3, text="Receipt Area", font=("Lucida", 13, "bold"), bd=7, relief=RAISED)
            receipt_title.pack(fill=X)

            scroll_y = Scrollbar(F3, orient=VERTICAL)
            self.txt = Text(F3, yscrollcommand=scroll_y.set)
            scroll_y.pack(side=RIGHT, fill=Y)
            scroll_y.config(command=self.txt.yview)
            self.txt.pack(fill=BOTH, expand=1)

            F4 = LabelFrame(self.root, text='Total Menu', bd=10, relief=RAISED, bg=bg_color, fg="gold",
                            font=("Calibri", 13, "bold"))
            F4.place(x=0, y=560, relwidth=1, height=145)
 
            medicine_lbl = Label(F4, font=("Calibri", 15, "bold"), fg=lbl_color, bg=bg_color, text="Total Medicine")
            medicine_lbl.grid(row=0, column=0, padx=10, pady=0)
            medicine_en = Entry(F4, bd=8, relief=RAISED, textvariable=self.total_medicine)
            medicine_en.grid(row=0, column=1, ipady=2, ipadx=5)

            vitamins_lbl = Label(F4, font=("Calibri", 15, "bold"), fg=lbl_color, bg=bg_color, text="Total Vitamins")
            vitamins_lbl.grid(row=1, column=0, padx=10, pady=5)
            vitamins_en = Entry(F4, bd=8, relief=RAISED, textvariable=self.total_vitamins)
            vitamins_en.grid(row=1, column=1, ipady=2, ipadx=5)

            cream_lbl = Label(F4, font=("Calibri", 15, "bold"), fg=lbl_color, bg=bg_color, text="Total Cream and Ointment")
            cream_lbl.grid(row=2, column=0, padx=10, pady=5)
            cream_en = Entry(F4, bd=8, relief=RAISED, textvariable=self.total_cream_ointment)
            cream_en.grid(row=2, column=1, ipady=2, ipadx=5)

            taxmedicine_lbl = Label(F4, font=("Calibri", 15, "bold"), fg=lbl_color, bg=bg_color, text="Medicine Tax")
            taxmedicine_lbl.grid(row=0, column=2, padx=30, pady=0)
            taxmedicine_en = Entry(F4, bd=8, relief=RAISED, textvariable=self.tax_medicine)
            taxmedicine_en.grid(row=0, column=3, ipady=2, ipadx=5)

            vitamins_lbl = Label(F4, font=("Calibri", 15, "bold"), fg=lbl_color, bg=bg_color, text="Vitamins Tax")
            vitamins_lbl.grid(row=1, column=2, padx=30, pady=5)
            vitamins_en = Entry(F4, bd=8, relief=RAISED, textvariable=self.tax_vitamins)
            vitamins_en.grid(row=1, column=3, ipady=2, ipadx=5)

            ointment_lbl = Label(F4, font=("Calibri", 15, "bold"), fg=lbl_color, bg=bg_color, text="Cream and Ointment Tax")
            ointment_lbl.grid(row=2, column=2, padx=10, pady=5)
            ointment_en = Entry(F4, bd=8, relief=RAISED, textvariable=self.tax_cream_ointment)
            ointment_en.grid(row=2, column=3, ipady=2, ipadx=5)

            total_btn = Button(F4, text="Total", bg=bg_color, fg=fg_color, font=("lucida", 12, "bold"), bd=7, relief=RAISED,
                                command=self.total_section)
            total_btn.grid(row=1, column=4, ipadx=20, padx=30)

            generatebill_button = Button(F4, text="Generate Bill", bg=bg_color, fg=fg_color, font=("lucida", 12, "bold"), bd=7, relief=RAISED, command=self.billing_section)
            generatebill_button.grid(row=1, column=5, ipadx=20)

            clear_button = Button(F4, text="Clear", bg=bg_color, fg=fg_color, font=("lucida", 12, "bold"), bd=7, relief=RAISED, command=self.clear)
            clear_button.grid(row=1, column=6, ipadx=20, padx=30)

            exit_buttonn = Button(F4, text="Exit", bg=bg_color, fg=fg_color, font=("lucida", 12, "bold"), bd=7, relief=RAISED, command=self.exit)
            exit_buttonn.grid(row=1, column=7, ipadx=20)


        def total_section(self):
            self.total_medicine_prices = (
                (self.medicol_advance.get() * 12) +
                (self.toseran_forte.get() * 12) +
                (self.imodium.get() * 15) +
                (self.mefenamic.get() * 38) +
                (self.amoxicillin.get() * 5)
            )
            self.total_medicine.set("Rs. " + str(self.total_medicine_prices))
            self.tax_medicine.set("Rs. " + str(round(self.total_medicine_prices * 0.05)))

            self.total_vitamins_prices = (
                (self.tiki_tiki_star.get() * 150) +
                (self.neutrilin_drops.get() * 250) +
                (self.profan_tlc.get() * 350) +
                (self.ceelin_plus.get() * 250) +
                (self.cheriper.get() * 400)

            )
            self.total_vitamins.set("Rs. " + str(self.total_vitamins_prices))
            self.tax_vitamins.set("Rs. " + str(round(self.total_vitamins_prices * 0.05)))

            self.total_cream_ointment_prices = (
                (self.lidocaine_ointment.get() * 340) +
                (self.canesten_cream.get() * 450) +
                (self.tabeta_ointment.get() * 420) +
                (self.nerisone_ointment.get() * 580) +
                (self.clotrimazole_cream.get() * 600)
            )
            self.total_cream_ointment.set("Rs. " + str(self.total_cream_ointment_prices))
            self.tax_cream_ointment.set("Rs. " + str(round(self.total_cream_ointment_prices * 0.05)))
 

        def welcome_customer(self):
            self.txt.delete('1.0', END)
            self.txt.insert(END, "Welcome To R&D Pharmacy Store\n")
            self.txt.insert(END, f"\nInvoice No. : {str(self.cus_invoice_no.get())}")
            self.txt.insert(END, f"\nCustomer Name : {str(self.customer_name.get())}")
            self.txt.insert(END, f"\nContact No. : {str(self.customer_contact_number.get())}")
            self.txt.insert(END, "\nProduct: Quantity: Price:")
            self.txt.insert(END, "\n___________________________________")



        def clear(self):
            self.txt.delete('1.0', END)



        def billing_section(self):
            self.welcome_customer()

            if self.medicol_advance.get() != 0:
                self.txt.insert(END, f"\nMedicol Advance {self.medicol_advance.get()} {self.medicol_advance.get() * 12}")

            if self.toseran_forte.get() != 0:
                self.txt.insert(END, f"\nToseran Forte {self.toseran_forte.get()} {self.toseran_forte.get() * 12}")

            if self.imodium.get() != 0:
                self.txt.insert(END, f"\nImodium {self.imodium.get()} {self.imodium.get() * 15}")

            if self.mefenamic.get() != 0:
                self.txt.insert(END, f"\nMefenamic {self.mefenamic.get()} {self.mefenamic.get() * 38}")

            if self.amoxicillin.get() != 0:
                self.txt.insert(END, f"\nAmoxicillin {self.amoxicillin.get()} {self.amoxicillin.get() * 5}")

            if self.tiki_tiki_star.get() != 0:
                self.txt.insert(END, f"\nTiki Tiki Star {self.tiki_tiki_star.get()} {self.tiki_tiki_star.get() * 150}")

            if self.neutrilin_drops.get() != 0:
                self.txt.insert(END, f"\nNeutrilin Drops {self.neutrilin_drops.get()} {self.neutrilin_drops.get() * 250}")

            if self.profan_tlc.get() != 0:
                self.txt.insert(END, f"\nProfan Tlc {self.profan_tlc.get()} {self.profan_tlc.get() * 350}")

            if self.ceelin_plus.get() != 0:
                self.txt.insert(END, f"\nCeelin Plus {self.ceelin_plus.get()} {self.ceelin_plus.get() * 250}")

            if self.cheriper.get() != 0:
                self.txt.insert(END, f"\nCheriper {self.cheriper.get()} {self.cheriper.get() * 400}")

            if self.lidocaine_ointment.get() != 0:
                self.txt.insert(END, f"\nLicodaine Ointment {self.lidocaine_ointment.get()} {self.lidocaine_ointment.get() * 340}")

            if self.canesten_cream.get() != 0:
                self.txt.insert(END, f"\nCanesten Cream {self.canesten_cream.get()} {self.canesten_cream.get() * 450}")

            if self.tabeta_ointment.get() != 0:
                self.txt.insert(END, f"\nTabeta Ointment {self.tabeta_ointment.get()} {self.tabeta_ointment.get() * 420}")

            if self.nerisone_ointment.get() != 0:
                self.txt.insert(END, f"\nNerizone Ointment {self.nerisone_ointment.get()} {self.nerisone_ointment.get() * 580}")

            if self.clotrimazole_cream.get() != 0:
                self.txt.insert(END, f"\nClotrimazole Cream {self.clotrimazole_cream.get()} {self.clotrimazole_cream.get() * 20}")

            self.txt.insert(END, "\n___________________________________")
            self.txt.insert(END,
                            f"\n Total : {self.total_medicine_prices + self.total_vitamins_prices + self.total_cream_ointment_prices + self.total_medicine_prices * 0.05 + self.total_vitamins_prices * 0.05 + self.total_cream_ointment_prices * 0.05}")


        def exit(self):
            self.root.destroy()


    object = Pharmacy_Billing(root)
    root.mainloop()


else:
    print("INVALID INPUT")
