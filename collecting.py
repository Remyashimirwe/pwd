#first 1
movies = ("The Shawshank Redemption", "The Godfather", "The Dark Knight", "Pulp Fiction", "The Lord of the Rings: The Return of the King")
print(movies[0])
size = len(movies)
print(movies[size-1])
# the second one
book = {"title": "Growing in Mind","author": "Simon v", "year": 1992, "pages": 160}
print(book)
# the third one
numbers = (10,20,30,40,50)
print(numbers[0])
print(numbers[1])
print(numbers[3])
print(numbers[4])

for number in numbers:
    print(number)

pythonsentence = "hello world hello python world"
print(pythonsentence.count("hello world"))

pythongrades = {"Alice": 85, "Bob": 92, "Charlie": 78, "Diana": 95}
sums = pythongrades.values()
total = 0
n= len(sums)
for sum in sums:
    total += sum
average = total/n
print(f"the average is : {average}")
phonebook = {}
phonebook["name"]= "king"
phonebook["phone_number"] ="9384278794832"
del phonebook["name"]
print(phonebook)