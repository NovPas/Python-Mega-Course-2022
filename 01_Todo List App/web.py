import streamlit as st
import os

# Initialize an empty list to store tasks
tasks = []

# Define the path to save the tasks file
file_path = "tasks.txt"


# Define a function to save the tasks to a file
def save_tasks():
    with open(file_path, "w") as f:
        for task in tasks:
            f.write(task + "\n")


# Check if the tasks file exists, and if so, read in the tasks
if os.path.exists(file_path):
    with open(file_path, "r") as f:
        tasks = [line.strip() for line in f.readlines()]


def task_add():
    tasks.append(st.session_state.new_task)
    save_tasks()


# Define the Streamlit app
def app():
    # Set the page title
    st.set_page_config(page_title="To-Do List App")

    # Add a title to the app
    st.title("To-Do List App!")

    for i, task in enumerate(tasks):
        checkbox = st.checkbox(task, key=i)
        if checkbox:
            tasks.pop(i)
            save_tasks()
            st.experimental_rerun()

    st.text_input(label='', placeholder='add new task', on_change=task_add, key='new_task')


if __name__ == "__main__":
    app()
    st.session_state
