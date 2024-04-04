#write a program that sorts PhoneBook
def stripFormatting(number):
    """Remove formatting characters from a phone number."""
    return ''.join(filter(str.isdigit, number))

def padWithZeros(number, length):
    """pad the number with leading eroes to match the specified length"""
    return number.zfill(length)

def findMaxLength(numbers):
    """Find the maximum length of numbers in the list."""
    return max(len(number) for number in numbers)

def countingSortByDigit(numbers, digitPosition, radix=10):
    """Sort the numbers based on the digit at specified position"""
    output = [0] * len(numbers)
    count = [0] * radix

    #we can count the occurences of each digit at DigitPosition
    for number in numbers:
        index = int(number[digitPosition]) if digitPosition < len(number) else 0
        count[index] += 1

    #Counted values Accumulation
    for i in range(1, radix):
        count[i] += count[i - 1]

    #Build the output array
    for number in reversed(numbers):
        index = int(number[digitPosition]) if digitPosition < len(number) else 0
        output[count[index] - 1] = number
        count[index] -= 1

    return output

def radixSort(numbers):
    """Sort the numbers using Radix Sort"""
    maxLength = findMaxLength(numbers)
    for digitPosition in range(maxLength - 1, -1, -1):
        numbers = countingSortByDigit(numbers, digitPosition)

    return numbers

def preprocessPhoneNumbers(phoneNumbers):
    """Preprocess the list of phone numbers by standardizing their format"""
    standardizedNumbers = [stripFormatting(number) for number in phoneNumbers]
    maxLength = findMaxLength(standardizedNumbers)
    return [padWithZeros(number, maxLength) for number in standardizedNumbers]

def main():
    n = int(input("Enter the number of phone numbers: "))
    rawPhoneNumbers = [input(f"Enter phone number {i+1}: ") for i in range(n)]

    #preprocessing on the raw numbers
    standardizedNumbers = preprocessPhoneNumbers(rawPhoneNumbers)

    #Srting of the raw numbers which were preprocessed
    sortedNumbers = radixSort(standardizedNumbers)    

    #Display sorted Numbers
    print("\nSorted Phone Numbers: ")
    for number in sortedNumbers:
        print(number)

if __name__ == "__main__":
    main()