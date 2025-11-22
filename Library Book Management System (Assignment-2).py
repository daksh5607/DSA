import sys
class BookNode:
    def __init__(self, book_id, title, author, status="Available"):
        self.BookID = book_id
        self.BookTitle = title
        self.AuthorName = author
        self.Status = status
        self.next = None
    def __str__(self):
        return f"| ID: {self.BookID:<4} | Title: {self.BookTitle:<30} | Author: {self.AuthorName:<20} | Status: {self.Status:<10} |"
class BookListManager:
    def __init__(self):
        self.head = None
    def insertBook(self, book_id, title, author):
        if not isinstance(book_id, int) or book_id <= 0:
            print("ERROR: BookID must be a positive integer.")
            return
        if self.searchBook(book_id):
            print(f"ERROR: Book with ID {book_id} already exists. Cannot insert.")
            return
        new_node = BookNode(book_id, title, author)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        print(f"SUCCESS: Book '{title}' (ID: {book_id}) added to the library.")
    def deleteBook(self, book_id):
        current = self.head
        previous = None
        if current and current.BookID == book_id:
            book_title = current.BookTitle
            self.head = current.next
            print(f"SUCCESS: Book '{book_title}' (ID: {book_id}) deleted.")
            return True
        while current and current.BookID != book_id:
            previous = current
            current = current.next
        if not current:
            print(f"ERROR: Book with ID {book_id} not found for deletion.")
            return False
        book_title = current.BookTitle
        previous.next = current.next
        print(f"SUCCESS: Book '{book_title}' (ID: {book_id}) deleted.")
        return True
    def searchBook(self, book_id):
        current = self.head
        while current:
            if current.BookID == book_id:
                return current
            current = current.next
        return None
    def displayBooks(self):
        print("\n" + "="*80)
        print("                 📚 CURRENT LIBRARY BOOK LIST 📚")
        print("="*80)
        if not self.head:
            print("The library is currently empty.")
            print("="*80)
            return
        current = self.head
        while current:
            print(current)
            current = current.next
        print("="*80)
class TransactionStack:
    def __init__(self):
        self.items = []
    def push(self, transaction):
        self.items.append(transaction)
    def pop(self):
        if not self.isEmpty():
            return self.items.pop()
        return None
    def isEmpty(self):
        return len(self.items) == 0
    def viewTransactions(self):
        print("\n" + "~"*80)
        print("                  📝 TRANSACTION HISTORY (Last is TOP) 📝")
        print("~"*80)
        if self.isEmpty():
            print("No transactions recorded yet.")
            print("~"*80)
            return
        for i, transaction in enumerate(reversed(self.items)):
            book_id, operation, old_status, new_status = transaction
            print(f"[{len(self.items) - i}] Operation: {operation:<7} | BookID: {book_id:<4} | Status Change: {old_status} -> {new_status}")
        print("~"*80)
class LibrarySystem:
    def __init__(self):
        self.BookList = BookListManager()
        self.TransactionStack = TransactionStack()
    def issueBook(self, book_id):
        book_node = self.BookList.searchBook(book_id)
        if not book_node:
            print(f"ERROR: Cannot issue. Book with ID {book_id} not found.")
            return
        if book_node.Status == "Issued":
            print(f"WARNING: Book '{book_node.BookTitle}' (ID: {book_id}) is already Issued. No transaction recorded.")
            return
        old_status = book_node.Status
        book_node.Status = "Issued"
        transaction = (book_id, "ISSUE", old_status, "Issued")
        self.TransactionStack.push(transaction)
        print(f"SUCCESS: Book '{book_node.BookTitle}' (ID: {book_id}) has been **ISSUED**.")
        self.BookList.displayBooks()
    def returnBook(self, book_id):
        book_node = self.BookList.searchBook(book_id)
        if not book_node:
            print(f"ERROR: Cannot return. Book with ID {book_id} not found.")
            return
        if book_node.Status == "Available":
            print(f"WARNING: Book '{book_node.BookTitle}' (ID: {book_id}) is already Available. No transaction recorded.")
            return
        old_status = book_node.Status
        book_node.Status = "Available"
        transaction = (book_id, "RETURN", old_status, "Available")
        self.TransactionStack.push(transaction)
        print(f"SUCCESS: Book '{book_node.BookTitle}' (ID: {book_id}) has been **RETURNED**.")
        self.BookList.displayBooks()
    def undoTransaction(self):
        last_transaction = self.TransactionStack.pop()
        if not last_transaction:
            print("\nWARNING: No recent transactions to undo. Stack is empty.")
            return
        book_id, operation, old_status, new_status = last_transaction
        book_node = self.BookList.searchBook(book_id)
        if not book_node:
            print(f"CRITICAL ERROR: Book ID {book_id} not found during undo. Data inconsistency.")
            return
        book_node.Status = old_status
        print(f"\n✅ UNDO SUCCESSFUL: Reverted last **{operation}** operation for Book ID {book_id}.")
        print(f"Book '{book_node.BookTitle}' status reverted to: **{book_node.Status}**.")
        self.BookList.displayBooks()
    def run_menu(self):
        while True:
            print("\n" + "="*50)
            print("  Library Book Management System (Console)")
            print("="*50)
            print("1. Insert New Book")
            print("2. Delete Book")
            print("3. Search Book")
            print("4. Issue Book")
            print("5. Return Book")
            print("6. Undo Last Transaction (Stack Pop)")
            print("7. View All Books (Linked List)")
            print("8. View Transactions (Stack)")
            print("9. Exit")
            print("="*50)
            try:
                choice = int(input("Enter your choice (1-9): "))
                if choice == 1:
                    book_id = int(input("Enter Book ID (Integer): "))
                    title = input("Enter Book Title: ")
                    author = input("Enter Author Name: ")
                    self.BookList.insertBook(book_id, title, author)
                elif choice == 2:
                    book_id = int(input("Enter Book ID to delete: "))
                    self.BookList.deleteBook(book_id)
                    self.BookList.displayBooks()
                elif choice == 3:
                    book_id = int(input("Enter Book ID to search: "))
                    book = self.BookList.searchBook(book_id)
                    if book:
                        print("\nSEARCH RESULT:")
                        print(book)
                    else:
                        print(f"Book with ID {book_id} not found.")
                elif choice == 4:
                    book_id = int(input("Enter Book ID to issue: "))
                    self.issueBook(book_id)
                elif choice == 5:
                    book_id = int(input("Enter Book ID to return: "))
                    self.returnBook(book_id)
                elif choice == 6:
                    self.undoTransaction()
                elif choice == 7:
                    self.BookList.displayBooks()
                elif choice == 8:
                    self.TransactionStack.viewTransactions()
                elif choice == 9:
                    print("Exiting Library System. Goodbye!")
                    sys.exit(0)
                else:
                    print("Invalid choice. Please enter a number between 1 and 9.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")
            except Exception as e:
                print(f"An unexpected error occurred: {e}")
if __name__ == "__main__":
    library = LibrarySystem()
    print("\n[Initial Setup: Populating Library with Sample Books]")
    library.BookList.insertBook(101, "Data Structures Fundamentals", "Sam")
    library.BookList.insertBook(102, "The C Programming Language", "Margret")
    library.BookList.insertBook(103, "Operating System Concepts", "Anand")
    library.BookList.displayBooks()
    library.run_menu()
