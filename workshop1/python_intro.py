# /// script
# requires-python = ">=3.11"
# dependencies = ["marimo==0.24.0"]
# ///

import marimo

__generated_with = "0.24.0"
app = marimo.App(
    width="medium",
    app_title="Workshop 1",
    layout_file="layouts/python_intro.slides.json",
)

with app.setup(hide_code=True):
    import marimo as mo


@app.cell(hide_code=True)
def welcome():
    mo.md("""
    # Workshop 1

    The Python course is run by Warwick AI, CodeSoc and UWCS.

    No previous Python experience is needed.
    """)
    return


@app.cell(hide_code=True)
def today():
    mo.md("""
    ## Today’s session takes 90 minutes

    | Start | Duration | Activity |
    |---|---|---|
    | 18:30 | 20 minutes | Values and conversion |
    | 18:50 | 20 minutes | Lab 1 |
    | 19:10 | 10 minutes | Break |
    | 19:20 | 20 minutes | Decisions and debugging |
    | 19:40 | 20 minutes | Lab 2 |
    """)
    return


@app.cell(hide_code=True)
def python_path():
    mo.md("""
    ## Python Course plan

    | Session | Week | Start | What you will build on | Organising society |
    |---|---|---|---|---|
    | 1 | 2 | 18:30 | Variables, casting, decisions and errors | WAI + UWCS |
    | 2 | 3 | 18:00 | Loops, lists and functions | WAI |
    | 3 | 4 | 18:00 | A small project | UWCS |
    | 4 | 5 | 18:00 | Dictionaries and an introduction to classes | CodeSoc |
    | 5 | 7 | 18:00 | A bigger project and practice using documentation | CodeSoc |
    | 6 | 8 | 18:30 | Python for data science with pandas | WAI |

    WAI stands for Warwick AI. All sessions meet on Wednesdays in MS.05 and end at 20:00.
    """)
    return


@app.cell(hide_code=True)
def variables():
    mo.vstack(
        [
            mo.md("""
            ## A variable is a named box

            Think of a variable as a box with a name on it, so you can refer to its value later.
            Choose a name that tells you what the value means.
            """),
            mo.hstack(
                [
                    mo.md("""
                    ```python
                    capacity = 60
                    booked = 25
                    booked = 30
                    ```
                    """),
                    mo.mermaid("""
                    graph LR
                        subgraph capacity
                            C["60"]
                        end
                        subgraph booked
                            B["30"]
                        end
                        O["25"] -.->|"replaced by booked = 30"| B
                    """),
                ],
                widths=[1, 1],
                align="center",
            ),
            mo.md("""
            `=` means **assign**: put the value on the right into the box on the left.
            A box holds one value at a time, so `booked = 30` throws away the `25`.

            This is not a maths equation. In maths, `x = x + 1` has no solution.
            In Python, `booked = booked + 1` takes `30` out, adds 1 and puts `31` back.
            """),
        ]
    )
    return


@app.cell(hide_code=True)
def assignment():
    mo.vstack(
        [
            mo.md("""
            ## Python reads the boxes, then fills a new one

            Python works out the right-hand side first, then stores the result.
            """),
            mo.hstack(
                [
                    mo.md("""
                    ```python
                    capacity = 60
                    booked = 25
                    spaces = capacity - booked
                    ```
                    """),
                    mo.mermaid("""
                    graph LR
                        subgraph capacity
                            C["60"]
                        end
                        subgraph booked
                            B["25"]
                        end
                        subgraph spaces
                            S["35"]
                        end
                        C -->|"copy 60"| E["60 - 25"]
                        B -->|"copy 25"| E
                        E -->|"store 35"| S
                    """),
                ],
                widths=[1, 1],
                align="center",
            ),
            mo.md("""
            Reading a box copies its value, so `capacity` and `booked` still hold `60` and `25`.

            `spaces` does not update itself. If you change `booked` to `30`, run
            `spaces = capacity - booked` again to update `spaces` to `30`.
            """),
        ]
    )
    return


@app.cell(hide_code=True)
def values():
    mo.md("""
    ## A value has a type

    The value’s type affects what you can do with it.

    `60` is an integer, and `2.5` is a float.

    `"60"` is a string containing text, and `True` is a Boolean value.

    `"6" + "0"` joins two strings to give `"60"`.
    """)
    return


@app.cell
def demo_values():
    # capacity = 60
    # booked = 25
    # spaces = ...  # Calculate the remaining spaces.
    # spaces
    mo.md("""
    ## Demo: name a value
    Calculate the spaces remaining from the room capacity and booking count.
    """)
    return


@app.cell
def demo_casting():
    # tickets_text = "25"
    # tickets_text + "1"
    # int(tickets_text) + 1
    # int("twenty-five")  # Read the error, then repair this line.
    mo.md("""
    ## Demo: turn text into a number
    Convert a sign-up count from text to an integer before adding another booking.
    """)
    return


@app.cell
def demo_booking_cost():
    # group_size_text = "4"
    # ticket_price = 2.50
    # group_size = ...  # Convert the booking count to an integer.
    # total_cost = ...  # Multiply the count by the ticket price.
    # total_cost
    mo.md("""
    ## Demo: price a group booking
    Four friends book tickets at £2.50 each. The form gives us the count as text.
    Convert the count to an integer and calculate the total cost.
    """)
    return


@app.cell(hide_code=True)
def lab_one():
    mo.md("""
    ## Lab 1 takes 20 minutes

    Open **python_lab.ipynb** in Colab and go to **Lab 1**.

    1. Predict expression results, then check their types.
    2. Calculate spaces and income, then update the booking count.
    3. Convert a form’s text into an updated booking count.

    Start with the notebook instructions. Try the extension if you have time.
    """)
    return


@app.cell(hide_code=True)
def break_time():
    mo.md("""
    ## 10-minute break

    The session resumes at **19:20**.
    """)
    return


@app.cell(hide_code=True)
def decisions():
    mo.md("""
    ## A comparison asks a yes-or-no question

    Use `=` to assign a value and `==` to compare two values.

    Comparisons produce a Boolean value: `True` or `False`.

    ```python
    booked = 25
    capacity = 60
    booked < capacity   # True: fewer bookings than places
    booked == capacity  # False: the room is not exactly full
    ```

    A program can use that answer to decide what to do next.
    """)
    return


@app.cell(hide_code=True)
def if_statements():
    mo.vstack(
        [
            mo.md("""
            ## An if statement chooses what happens next

            Think: **if there is room, accept another booking. Otherwise, say the room is full.**
            """),
            mo.hstack(
                [
                    mo.md("""
                    ```python
                    booked = 25
                    capacity = 60
                    if booked < capacity:
                        print("You can book a place")
                    else:
                        print("The room is full")
                    ```
                    """),
                    mo.mermaid("""
                    graph TB
                        Q{"booked #lt; capacity?"} -->|True| A["You can book a place"]
                        Q -->|False| B["The room is full"]
                    """),
                ],
                widths=[1, 1],
                align="center",
            ),
            mo.md("""
            The condition is `True`, so this prints **You can book a place** and skips the `else` branch.
            With `booked = 60`, it would print **The room is full** instead.

            The colon starts a branch. Press Tab to indent the code inside it.
            `else` handles a false condition. To check another condition first, add an `elif` branch before `else`.
            """),
        ]
    )
    return


@app.cell
def demo_simple_decision():
    # capacity = 60
    # booked = 25
    # if booked < capacity:
    #     booking_message = "You can book a place"
    # else:
    #     booking_message = "The room is full"
    # booking_message
    # Predict the message for booked = 25 and booked = 60, then run each.
    mo.md("""
    ## Demo: predict the branch
    Predict which message appears for 25 bookings, then for exactly 60.
    Change the booking count and run the code to check each prediction.
    """)
    return


@app.cell
def demo_decisions():
    # capacity = 60
    # booked = 25
    # if booked > capacity:
    #     message = ...
    # elif ...:  # Check whether the room is exactly full.
    #     message = ...
    # else:
    #     message = ...
    # message
    # Test booked = 25, 60 and 61.
    mo.md("""
    ## Demo: is there room?
    Use `if`, `elif` and `else` to handle bookings below, at and above the room limit.
    """)
    return


@app.cell(hide_code=True)
def errors():
    mo.vstack(
        [
            mo.md("## Fixing errors"),
            mo.mermaid("""
            graph LR
                R["1. Read the error type and<br/>message on the last line"] --> F["2. Find the relevant<br/>line of your code"]
                F --> X["3. Fix the cause<br/>of the error"] --> U["4. Rerun the code<br/>to check the fix"]
                U -->|still an error| R
            """),
            mo.md("A misspelled variable name can cause a `NameError`."),
        ]
    )
    return


@app.cell
def demo_errors():
    # booking_count = 10
    # booking_cout
    # spaces = 40 - "25"
    # spaces
    mo.md("""
    ## Demo: fix two errors
    Uncomment the first two lines and run the cell. Use the `NameError` message to find the misspelled name.

    Fix the name, then uncomment the remaining lines. Resolve the `TypeError`
    by converting the text to an integer before subtracting.
    """)
    return


@app.cell(hide_code=True)
def learn():
    mo.md("""
    ## Reading documentation

    For example: how can you round a number to one decimal place?

    Look up the function in the Python documentation, identify the inputs it needs,
    then use it in your code.
    """)
    return


@app.cell
def demo_documentation():
    # distance = 3.76
    # rounded_distance = ...  # Use the documentation to round to one decimal place.
    # rounded_distance
    # Compare round(distance, 1) with round(distance).
    mo.md("""
    ## Demo: use round() from the documentation
    We want to round a distance of 3.76 km to one decimal place.

    Open the [Python documentation for `round`](https://docs.python.org/3/library/functions.html#round).
    Read the first paragraph: what do `number` and `ndigits` mean?

    Use those inputs to write and run a call to `round`.
    What changes if you leave out `ndigits`?
    """)
    return


@app.cell(hide_code=True)
def lab_two():
    mo.md("""
    ## Lab 2 takes 20 minutes

    Go to **Lab 2** in Colab.

    1. Predict and test the messages for 25, 60 and 61 bookings.
    2. Read two errors, explain their causes and repair the code.
    3. Use the documentation to round a room’s occupancy percentage.

    Finish with the checkpoint. Group bookings and a logic bug are optional extensions.
    """)
    return


if __name__ == "__main__":
    app.run()
