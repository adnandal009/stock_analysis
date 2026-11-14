import pandas as pd

# Change this to your dataset file name
data = pd.read_csv("covid-data.csv")

print("==== Data Cleaning ====")
print("1. Handle Missing Values")
print("2. Convert Date Column to DateTime")
print("3. Remove Duplicate Rows")

choice=int(input("Enter Your Choice : "))
try:

    if choice==1:
        print("==== Handle Missing Values ====")
        print("1. Drop Rows with Missing Values")
        print("2. Fill Missing Values with Mean/Median/Mode")
        choice2=int(input("Enter Your Choice : "))
        if choice2==1:
            print("===== Sum of Missing Values =====")
            print(data.isna().sum())
        elif choice2==2:
            print("===== Drop Rows With Missing Values =====")
            if data.isnull().empty:
                print("No Missing Values in Dataset !!")
            else:
                print("====== Before Cleaning =====")
                print()
                print(data.isna().sum())

                print("====== After Cleaning ======")
                print()
                data=data.dropna()
                print(data.isna().sum())
                print()
                print("Data Cleaned Sucessfullly !!")
        elif choice2==3:
            print("===== Replace Missing Values With Specific Value =====")
            print("1. Replace With 0")
            print("2. Replace With Mean")
            print("3. Replace With Median")
            print("4. Replace With Mode")

            ch1=int(input("Enter Your Choice : "))
            if ch1==1:
                data=data.fillna(0)
                print("Missing Values Replaced With 0 Successfully !!")
            elif ch1==2:
                data=data.fillna(data.mean())
                print("Missing Values Replaced With Mean Successfully !!")
            elif ch1==3:
                data=data.fillna(data.median())
                print("Missing Values Replaced With Median Successfully !!")
            elif ch1==4:
                data=data.fillna(data.mode().iloc[0])
                print("Missing Values Replaced With Mode Successfully !!")
            else:
                print("Invalid Choice (1-4)")
        elif choice==2:
            print("==== Convert Date Column to DateTime ====")
            data['Date']=pd.to_datetime(data['Date'])
            print("Date Column Converted to DateTime Successfully !!")
        elif choice==3:

            print("==== Remove Duplicate Records ====")
            print("1. Check For Duplicate Records")
            print("2. Remove Duplicate Records")

            ch=int(input("Enter Your Choice : "))

            if ch==1:
                print("===== Check For Duplicate Records =====")
                print(data.duplicated().sum())
            elif ch==2:
                print("===== Remove Duplicate Records =====")
                if data.duplicated().sum()==0:
                    print("No Duplicate Records Found !!")
                else:
                    print("====== Before Cleaning =====")
                    print()
                    print(data.duplicated().sum())

                    print("====== After Cleaning ======")
                    print()
                    data=data.drop_duplicates()
                    print(data.duplicated().sum())
                    print()
                    print("Duplicate Records Removed Sucessfully !!")
            else:
                print("Invalid Choice (1-2)")
        else:
            print("Invalid Choice (1-3)")
except:
    print("Error Occured !! Please Check Your Code")