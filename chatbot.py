import re

# Canteen menu
menu = {
    "veg sandwich": 40,
    "cheese sandwich": 60,
    "pav bhaji": 70,
    "masala dosa": 55,
    "samosa": 15,
    "tea": 10,
    "coffee": 15
}

word_to_number = {
    'one': 1, 'two': 2, 'three': 3, 'four': 4,
    'five': 5, 'six': 6, 'seven': 7, 'eight': 8,
    'nine': 9, 'ten': 10 
}

order = []

def show_menu():
    print("📋 Here's our menu:")
    for item, price in menu.items():
        print("- " + item.title() + " : ₹" + str(price))
    print()

    
    

def show_bill():
    if not order:
        print("🧾 You haven't ordered anything yet.\n")
        return
    total = 0
    print("🧾 Here's your bill:")
    [('samosa', 2)]
    for item, qty in order:
        price = menu[item] * qty
        total += price
        print("- " + item.title() + " x " + str(qty) + " = ₹" + str(price))
    print("Total: ₹" + str(total) + "\n")

def parse_order(user_input):
    added = []
    user_input = user_input.lower()

    # Replace word numbers with digits
    for word, number in word_to_number.items():
        user_input = user_input.replace(word, str(number))

    # Loop through each menu item
    for item in menu:
        # Search for "number + item" like "2 samosa" or "3 pav bhaji"
        pattern = r'(\d+)\s+' + re.escape(item)
        print("Pattern:", pattern)
        matches = re.findall(pattern, user_input)
        print("Matches:", matches)

        for match in matches:
            qty = int(match)
            order.append((item, qty))
            added.append(str(qty) + " x " + item.title())

        # # Also check for item without number (default to 1)
        # if item in user_input and not re.search(r'\d+\s+' + re.escape(item), user_input):
        #     order.append((item, 1))
        #     added.append("1 x " + item.title())

    return added


def canteen_bot():
    print("🤖 Welcome to the Canteen Chatbot!")
    print("Type your message (e.g., 'I want 2 samosas and one tea') or 'menu', 'bill', 'bye' to exit.\n")
    
    while True:
        user_input = input("You: ").strip().lower()
        if user_input in ["exit", "bye"]:
            print("👋 Goodbye! Your order has been cleared.")
            break
        elif "order" in user_input:
            print("📝 Please tell me what you would like to order.")
        elif "hi" in user_input or "hello" in user_input:
            print("👋 Hello! How can I assist you today?")
        elif "help" in user_input:
            print("🆘 I can help you with your order. Just tell me what you want!")
        elif "thank" in user_input:
            print("😊 You're welcome! If you need anything else, just let me know.")
        elif "menu" in user_input:
            show_menu()
        elif "bill" in user_input or "total" in user_input:
            show_bill()
        else:
            added_items = parse_order(user_input)
            if added_items:
                print("✅ Added to your order: " + ", ".join(added_items) + "\n")
            else: 
                print("🤔 I'm not sure what you mean. Try something like 'I want 2 samosas and one tea.'\n")

if __name__ == "__main__":
    canteen_bot()
