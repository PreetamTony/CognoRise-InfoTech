import random
import string

def generate_password(length, complexity):
  char_sets = {
    "low": string.ascii_lowercase,
    "medium": string.ascii_lowercase + string.digits,
    "high": string.ascii_lowercase + string.digits + string.punctuation + string.ascii_uppercase
  }


  if complexity not in char_sets:
    raise ValueError("Invalid complexity level. Choose from low, medium, or high.")

  characters = char_sets[complexity]

  password = "".join(random.choice(characters) for _ in range(length))

  return password

def main():

  while True:
    try:
      length = int(input("Enter desired password length: "))
      complexity = input("Enter desired complexity (low, medium, high): ").lower()
      break
    except ValueError:
      print("Invalid input. Please enter a valid integer for length and choose from low, medium, or high complexity.")

  password = generate_password(length, complexity)

  print(f"Your generated password is: {password}")

if __name__ == "__main__":
  main()
