
print_queue = []

documents = ["Doc1", "Doc2", "Doc3"]

for document in documents:
    print_queue.append(document)
    print(document, "added to the print queue")

while len(print_queue) > 0:
    document = print_queue.pop(0)
    print("Printing", document, "...")

print("All documents have been printed!")