# Advanced-Search-system-
The system searches for the most matched word in the dictionary and provides the most matched word in the data structure.

Note:
This system helps for people who dont know the actual spelling of the data they are looking for.
Hence, helps people to find words that most matches with thier search. 

![image](https://user-images.githubusercontent.com/67412675/110909915-c2878280-8338-11eb-81d0-4389bb65a92e.png)


This program was built to search for names which can have different pronounciation at all over the world.
Depending on native pronounciation, any name could be spelled at different tone, hence giving a harsh time to find details or info realted to the person.

![image](https://user-images.githubusercontent.com/67412675/110910030-e8ad2280-8338-11eb-9abe-5f658c28cfba.png)

Any person can search for names, without worrying about spelling format. Here I have used mainly it for, phone contact basis. While iphone usually ignores the name, if the search result doesnt match with the actual name in list/dictionary in iphone data fields.

Output:
![image](https://user-images.githubusercontent.com/67412675/110910354-4ccfe680-8339-11eb-9d02-d134c9f1caff.png)

Note: all the contact details are false, dont use in real life to contact anyone.


inner workings:
![image](https://user-images.githubusercontent.com/67412675/110910456-77ba3a80-8339-11eb-8731-dd06111ab7e4.png)

I have used matching of characters to characters in serial index.
Count length of comparing strings.
Each count section is based on matching of characters.
Use of set() in rows specified to 3 characters at each, to match corresponding.

After all the points are aggregrated to the main counts, the list is displayed on descending order, hence after matching it with above dictionary, the most highest count is displayed.


![image](https://user-images.githubusercontent.com/67412675/110910829-f8793680-8339-11eb-87eb-91ba171365e8.png)

Above image, highest count for 'Shantos" is "santosh".

Thank you. This is all custom build code, none of code is referenced from others.


