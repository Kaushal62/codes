def selectionsort(ipdic, sort_by):
    items = list(ipdic.items())
    print("Items before sorting:", items)
    
    for i in range(len(items)-1):
        min_index = i 
        for j in range(i+1, len(items)):
            if sort_by == 0:  # Sort by distance (value)
                if items[j][1] < items[min_index][1]:
                    min_index = j
            elif sort_by == 1:  # Sort by city name (key)
                if items[j][0] < items[min_index][0]:
                    min_index = j
        items[i], items[min_index] = items[min_index], items[i]
    
    return dict(items)


# Input distances
distances = list(map(int, input("Enter distances for each city (SPACE SEPARATED):\n").split()))

# Input cities
cities = input("\nEnter city names (SPACE SEPARATED):\n").split()

# Validate input lengths
if len(distances) != len(cities):
    print("Number of distances and cities must be the same.")
    exit()

# Create dictionary: city -> distance
dic = dict(zip(cities, distances))
print("\nCity-Distance Dictionary:\n", dic)

# Menu
while True:
    try:
        print("\nMenu:")
        print("1. Sort by Weights (distance)\n2. Sort by Name (alphabet)\n3. Exit")
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            print("\nSorted by Distances:")
            for city, dist in selectionsort(dic, 0).items():
                print(f"{city}: {dist}")
        elif choice == 2:
            print("\nSorted Alphabetically:")
            for city, dist in selectionsort(dic, 1).items():
                print(f"{city}: {dist}")
        elif choice == 3:
            print("Program Exited")
            break
        else:
            print("Invalid choice.")
    except ValueError:
        print("Invalid input. Please enter a number.")
    except Exception as e:
        print(f"An error occurred: {e}")