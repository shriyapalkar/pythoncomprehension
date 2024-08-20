#filter even no from list
even_numbers=[num for num in range(1,10) if num%2==0]
print(even_numbers)

word='python'
vowels='a','e','i','o','u'
#list comprehension
result=[char for char in word if char in vowels]
print(result)


