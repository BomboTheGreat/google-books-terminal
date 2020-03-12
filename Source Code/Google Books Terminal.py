import requests


def main():
    try:
        author, book = "", ""
        key = 'AIzaSyCoXI8ae13vDEegv1hEnbvjdWdQMOrgPBw'
        print("*+*Welcome to Google Book API client*+*\n*+**+**+**+**+**+**+**+**+**+**+**+**+*")
        print("In order to quit you can enter 'q' at any time")
        print("Do you want to search a book via book name, author or both? press 1, 2 or 3 accordingly")
        option = input('(1) Book name\n(2) Author\n(3) Both\n')
        while option not in ('1', '2', '3', 'q'):
            print("invalid input please try again")
            option = input('(1) Book name\n(2) Author\n(3) Both\n')
        if option == 'q':
            print("Thanks for using Google Book API client, goodbye!")
            return
        if option in ('1', '3'):
            book = input("Please enter the desired book name to look for\n")
            if book == 'q':
                print("Thanks for using Google Book API client, goodbye!")
                return
            while book == "":
                book = input("Nothing was entered, Please enter the desired book name to look for\n")
                if book == 'q':
                    print("\nThanks for using Google Book API client, goodbye!")
                    return
        if option in ('2', '3'):
            author = input("Please enter the desired autor name to look for\n")
            author = '+inauthor:' + author
            if author == 'q':
                print("Thanks for using Google Book API client, goodbye!")
                return
            while author == "":
                author = input("Nothing was entered, Please enter the desired author name to look for\n")
                author = '+inauthor:' + author
                if author == 'q':
                    print("\nThanks for using Google Book API client, goodbye!")
                    return
        print('Searching for ' + book + ' written by ' + author)

        book = 'q=intitle:' + book
        r = requests.get('https://www.googleapis.com/books/v1/volumes?' + book + author + '&key=' + key+'&maxResults=40')
        if r.json()['totalItems'] == 0:
            print("No matches were found!")
            option = input("press 1 in order to try searching for a different book again or press 'q' to quit\n")
            while option not in ('1', '2', '3', 'q'):
                print("invalid input please try again")
                option = input("press 1 in order to try searching for a different book again or press 'q' to quit\n")
            if option == 'q':
                print("Thanks for using Google Book API client, goodbye!")
                return
            else:
                return main()
        print('I found ', r.json()['totalItems'], ' matches')
        #print(r.json())
        print('here are the first ', len(r.json()['items']), ' results')
        for i, item in enumerate(r.json()['items']):
            if 'authors' in item['volumeInfo']:
                print('(' + str(i + 1) + ') ' + item['volumeInfo']['title'] + ' written by ' +
                      item['volumeInfo']['authors'][0])
            else:
                print('(' + str(i + 1) + ') ' + item['volumeInfo']['title'])
        option = input('\nPlease enter the book number on which you would you like to get more details\n')
        while not option.isdigit() or int(option) not in (list(range(1, len(r.json()['items']) + 1)) + ['q']):
            print("invalid input please try again")
            option = input('\nPlease enter the book number on which you would you like to get more details\n')
        index = int(option) - 1
        #print(r.json()['items'][index])
        if 'authors' in r.json()['items'][index]['volumeInfo']:
            print('\nAuthor: ' + r.json()['items'][index]['volumeInfo']['authors'][0])

        for att in ('title', 'description', 'publishedDate', 'publisher', 'language','volumeID'):
            if att in r.json()['items'][index]['volumeInfo'].keys():
                print(att.capitalize() + ': ' + r.json()['items'][index]['volumeInfo'][att])
        option = input("\npress 1 in order to try searching for a different book again or press 'q' to quit\n")
        while option not in ('1', '2', '3', 'q'):
            print("invalid input please try again")
            option = input("press 1 in order to try searching for a different book again or press 'q' to quit\n")
        if option == 'q':
            print("Thanks for using Google Book API client, goodbye!")
            return
        else:
            return main()
    except Exception as e:
        print(e)

main()

