kolichestvo = int(input("Skolko chisel budet v spiske?\n"))

my_list = [int(input("Vvedite chisla iz spiska")) for i in range(kolichestvo)]

new_list1 = [x for x in my_list if x < 5]
new_list2 = [x/2 for x in my_list]
new_list3 = [x*2 for x in my_list if x > 17]

print(new_list1, new_list2, new_list3, sep="\n")

chislo = int(input("Vvedite chislo dlya sozdaniya spiska kvadratov"))
squares = [x**2 for x in range(chislo + 1)]

# print(' '.join(str(x**2) for x in map(int, input().split())))

# print(' '.join(str(x**2) for x in map(int, input().split()) if x % 2 and (x**2) % 10 != 9))
