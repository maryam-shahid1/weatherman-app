import sys

n = len(sys.argv)

print("total number of arguments: ", n)

print("\nName of Python script:", sys.argv[0])
 
print("\nArguments passed:", end = " ")
for i in range(1, n):
    print(sys.argv[i], end = " ")

f = open("weatherfiles/Murree_weather_2004_Aug.txt","r")
print(f.read())

