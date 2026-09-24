import streamlit as st
import random
from langchain_ollama import ChatOllama
from langchain_core.messages import SystemMessage, HumanMessage

# ---------- SETUP ----------
st.set_page_config(page_title="SmartCart AI", page_icon="🛒")

PRODUCTS = [
    {"name":"Laptop","price":55000,"cat":"Electronics","rating":4.5,
     "desc":"Suitable for coding, study and office work."},
    {"name":"Smartphone","price":25000,"cat":"Electronics","rating":4.3,
     "desc":"Good camera and battery life."},
    {"name":"Headphones","price":3000,"cat":"Accessories","rating":4.2,
     "desc":"Wireless headphones with clear audio."},
    {"name":"Smart Watch","price":5000,"cat":"Wearables","rating":4.4,
     "desc":"Fitness tracking and notifications."},
    {"name":"Bluetooth Speaker","price":2500,"cat":"Accessories","rating":4.1,
     "desc":"Portable speaker with powerful sound."},
    {"name":"Running Shoes","price":3500,"cat":"Fashion","rating":4.6,
     "desc":"Comfortable shoes for workouts."},
    {"name":"Backpack","price":1800,"cat":"Fashion","rating":4.3,
     "desc":"Lightweight backpack for college and travel."},
    {"name":"Coffee Maker","price":4500,"cat":"Home","rating":4.2,
     "desc":"Easy-to-use coffee maker."}
]

if "cart" not in st.session_state:
    st.session_state.cart = {}

if "orders" not in st.session_state:
    st.session_state.orders = {}

if "messages" not in st.session_state:
    st.session_state.messages = []


# ---------- OLLAMA ----------
@st.cache_resource
def get_llm():
    return ChatOllama(
        model="llama3.2:latest",
        temperature=0,
        base_url="http://127.0.0.1:11434"
    )

try:
    llm = get_llm()
    ollama_ok = True
except:
    ollama_ok = False


def catalog():
    return "\n".join(
        f"{p['name']} - ₹{p['price']} - {p['cat']} - {p['desc']}"
        for p in PRODUCTS
    )


def ask_ai(question):
    prompt = f"""
You are SmartCart AI, an e-commerce shopping assistant.

Use ONLY these products:
{catalog()}

Rules:
- Recommend only products from the catalog.
- Never invent products or prices.
- Help with budget, travel, college, fitness, office,
  study, gifts and daily use.
- Explain why a product is suitable.
- For non-shopping questions say:
  "I can only help with SmartCart shopping questions."
- Keep the answer short.
"""
    return llm.invoke([
        SystemMessage(content=prompt),
        HumanMessage(content=question)
    ]).content


# ---------- SIDEBAR ----------
st.sidebar.title("🛒 SmartCart AI")

page = st.sidebar.radio("Menu", [
    "Home", "Products", "Cart",
    "AI Assistant", "Compare",
    "Order Tracking", "Checkout"
])

st.sidebar.info("AI: Llama 3.2\nRuntime: Ollama")


# ---------- HOME ----------
if page == "Home":

    st.title("🛒 SmartCart AI")
    st.write("AI-powered E-Commerce Website")

    c1, c2, c3 = st.columns(3)
    c1.metric("Products", len(PRODUCTS))
    c2.metric("AI Model", "Llama 3.2")
    c3.metric("Runtime", "Ollama")

    st.success(
        "AI helps customers choose and compare products "
        "according to their needs and budget."
    )


# ---------- PRODUCTS ----------
elif page == "Products":

    st.title("🛍️ Products")

    search = st.text_input("Search product")
    category = st.selectbox(
        "Category",
        ["All"] + sorted(set(p["cat"] for p in PRODUCTS))
    )

    products = [
        p for p in PRODUCTS
        if (category == "All" or p["cat"] == category)
        and search.lower() in p["name"].lower()
    ]

    for p in products:

        st.subheader(p["name"])
        st.write(
            f"₹{p['price']} | ⭐ {p['rating']} | {p['cat']}"
        )
        st.write(p["desc"])

        if st.button(f"Add {p['name']}", key=p["name"]):
            st.session_state.cart[p["name"]] = \
                st.session_state.cart.get(p["name"], 0) + 1
            st.success("Added to cart")


# ---------- CART ----------
elif page == "Cart":

    st.title("🛒 Cart")

    total = 0

    if not st.session_state.cart:
        st.info("Your cart is empty.")

    for name, qty in list(st.session_state.cart.items()):

        p = next(x for x in PRODUCTS if x["name"] == name)
        amount = p["price"] * qty
        total += amount

        st.write(f"*{name}* × {qty} = ₹{amount}")

        if st.button(f"Remove {name}", key="r"+name):
            del st.session_state.cart[name]
            st.rerun()

    st.subheader(f"Total: ₹{total}")


# ---------- AI ASSISTANT ----------
elif page == "AI Assistant":

    st.title("🤖 AI Shopping Assistant")

    if not ollama_ok:
        st.error("Ollama is not running.")
    else:

        if st.button("Test Ollama"):
            try:
                r = llm.invoke(
                    [HumanMessage(
                        content="Reply only: OLLAMA CONNECTED"
                    )]
                )
                st.success(r.content)
            except Exception as e:
                st.error(str(e))

        st.caption(
            "Example: Which product is suitable for travel?"
        )

        for m in st.session_state.messages:
            with st.chat_message(m["role"]):
                st.write(m["content"])

        q = st.chat_input("Ask about products...")

        if q:

            st.session_state.messages.append(
                {"role":"user", "content":q}
            )

            with st.chat_message("user"):
                st.write(q)

            try:
                answer = ask_ai(q)
            except Exception as e:
                answer = f"AI error: {e}"

            st.session_state.messages.append(
                {"role":"assistant", "content":answer}
            )

            with st.chat_message("assistant"):
                st.write(answer)

        if st.button("Clear Chat"):
            st.session_state.messages = []
            st.rerun()


# ---------- COMPARE ----------
elif page == "Compare":

    st.title("📊 Compare Products")

    names = st.multiselect(
        "Select up to 3 products",
        [p["name"] for p in PRODUCTS],
        max_selections=3
    )

    selected = [
        p for p in PRODUCTS if p["name"] in names
    ]

    if selected:

        for p in selected:
            st.write(
                f"*{p['name']}* — ₹{p['price']} "
                f"— ⭐ {p['rating']}"
            )

        if st.button("Compare Using AI"):

            question = (
                "Compare these products and explain "
                "which type of customer each suits:\n"
                + catalog()
            )

            st.write(ask_ai(question))


# ---------- ORDER TRACKING ----------
elif page == "Order Tracking":

    st.title("📦 Order Tracking")

    order_id = st.text_input("Enter Order ID")

    if st.button("Track"):

        if order_id in st.session_state.orders:
            st.success(
                f"Status: {st.session_state.orders[order_id]}"
            )
        else:
            st.error("Order not found.")


# ---------- CHECKOUT ----------
elif page == "Checkout":

    st.title("💳 Checkout")

    if not st.session_state.cart:
        st.info("Cart is empty.")
    else:

        total = sum(
            next(p["price"] for p in PRODUCTS if p["name"] == name) * qty
            for name, qty in st.session_state.cart.items()
        )

        st.write(f"Total Amount: ₹{total}")

        name = st.text_input("Name")
        phone = st.text_input("Phone")
        address = st.text_area("Address")

        payment = st.selectbox(
            "Payment",
            ["Cash on Delivery", "UPI", "Card"]
        )

        if st.button("Place Order"):

            order_id = "SC" + str(random.randint(100000, 999999))

            st.session_state.orders[order_id] = "Order Placed"

            st.session_state.cart = {}

            st.success("Order placed successfully!")
            st.info(f"Your Order ID: {order_id}")