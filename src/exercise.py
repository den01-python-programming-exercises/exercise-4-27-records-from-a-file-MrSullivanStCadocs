def main():
    #write your code below this line
    import csv
    nameOfFile = input("Name of the file:")
    
    with open(nameOfFile) as f:
      reader = csv.reader(f,delimiter=',')
      for row in reader:
        if(str(1) in row[1]):
          print(row[0] + ", age: " + row[1] + " year")
        else:
          print(row[0] + ", age: " + row[1] + " years")
        
    


if __name__ == '__main__':
    main()
