words={
    "car":"voiture",
    "dog":"chein",
    "cat":"chat",
    "table":"table",
    "chair":"chase",
    "book":"livre",
}
user_input=input("Enter english word: ").lower()
if user_input in words:
    print(f"The french word for {user_input} is {words.get(user_input)}")
else:
    print(f"{user_input}is not in the dictionary")