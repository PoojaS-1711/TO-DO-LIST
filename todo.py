import streamlit as st

# Initialize session state
if "tasks" not in st.session_state:
    st.session_state.tasks = []

st.title("📝 To-Do List with Categories & Priority")

# Task input
with st.form("task_form"):
    task_text = st.text_input("Enter task")
    category = st.selectbox("Category", ["Work", "Personal", "Study", "Other"])
    priority = st.selectbox("Priority", ["High 🔴", "Medium 🟡", "Low 🟢"])
    submitted = st.form_submit_button("➕ Add Task")

    if submitted:
        if task_text:
            st.session_state.tasks.append({
                "text": task_text,
                "category": category,
                "priority": priority,
                "done": False
            })
            st.success("Task added!")
        else:
            st.warning("Please enter a task.")

st.markdown("---")

# Display tasks
for i, task in enumerate(st.session_state.tasks):
    st.write(f"### Task {i+1}")

    # Layout for checkbox and edit/delete
    col1, col2, col3 = st.columns([0.1, 0.7, 0.2])
    is_done = col1.checkbox("Done", value=task["done"], key=f"done_{i}")
    new_text = col2.text_input("Edit Task", value=task["text"], key=f"text_{i}")
    delete = col3.button("❌ Delete", key=f"del_{i}")

    # Category and priority display
    col4, col5 = st.columns(2)
    new_category = col4.selectbox("Category", ["Work", "Personal", "Study", "Other"], index=["Work", "Personal", "Study", "Other"].index(task["category"]), key=f"cat_{i}")
    new_priority = col5.selectbox("Priority", ["High 🔴", "Medium 🟡", "Low 🟢"], index=["High 🔴", "Medium 🟡", "Low 🟢"].index(task["priority"]), key=f"prio_{i}")

    # Update task state
    st.session_state.tasks[i]["text"] = new_text
    st.session_state.tasks[i]["category"] = new_category
    st.session_state.tasks[i]["priority"] = new_priority
    st.session_state.tasks[i]["done"] = is_done

    # Handle delete
    if delete:
        st.session_state.tasks.pop(i)
        st.experimental_rerun()

    st.markdown("---")
