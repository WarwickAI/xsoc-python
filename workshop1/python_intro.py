# /// script
# requires-python = ">=3.11"
# dependencies = ["marimo==0.24.0", "segno==1.6.6"]
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
    import segno

    colab_url = "https://colab.research.google.com/github/WarwickAI/xsoc-python/blob/main/workshop1/python_lab.ipynb"
    colab_qr = mo.vstack(
        [
            mo.Html(segno.make(colab_url).svg_inline(scale=6, light="#fff")),
            mo.md("[bit.ly/4B5n863](https://bit.ly/4B5n863)"),
        ],
        align="center",
    )


@app.cell(hide_code=True)
def welcome():
    mo.hstack(
        [
            mo.md(f"""
            # Workshop 1

            The Python course is run by Warwick AI (WAI), CodeSoc and UWCS.

            No previous Python experience is needed.
            """),
        ],
        widths=[2, 1],
        align="center",
    )
    return


@app.cell(hide_code=True)
def today():
    mo.md("""
    ## Today’s session takes 90 minutes

    | Start | Duration | Activity |
    |---|---|---|
    | 18:30 | 20 minutes | Values and conversion |
    | 18:50 | 20 minutes | Lab 1 |c
    | 19:20 | 20 minutes | Decisions and debugging |
    | 19:40 | 20 minutes | Lab 2 |
    """)
    return


@app.cell(hide_code=True)
def python_path():
    mo.md("""
    ## Course plan

    | Session | Week | Start | Topics | Run by |
    |---|---|---|---|---|
    | 1 | 2 | 18:30 | Variables, casting, decisions and errors | WAI + UWCS |
    | 2 | 3 | 18:00 | Loops, lists and functions | WAI |
    | 3 | 4 | 18:00 | A small project | UWCS |
    | 4 | 5 | 18:00 | Dictionaries and an introduction to classes | CodeSoc |
    | 5 | 7 | 18:00 | A bigger project and practice using documentation | CodeSoc |
    | 6 | 8 | 18:30 | Python for data science with pandas | WAI |
    """)
    return


@app.cell(hide_code=True)
def variables():
    mo.vstack(
        [
            mo.md("""
            ## A variable is a named box

            A variable is a box with a name on it, so you can refer to its value later.
            Choose a name that says what the value means.
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
        ]
    )
    return


@app.cell(hide_code=True)
def assign_not_equals():
    mo.md("""
    ## `=` means assign, not equals

    Put the value on the right into the box on the left.
    A box holds one value at a time, so `booked = 30` throws away the `25`.

    This is not a maths equation. In maths, `x = x + 1` has no solution.
    In Python, `booked = booked + 1` takes `30` out, adds 1 and puts `31` back.
    """)
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
                    spaces = 60 - 25c
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
        ]
    )
    return


@app.cell(hide_code=True)
def boxes_keep_values():
    mo.md("""
    ## Each box keeps its own value

    Reading a box copies its value, so `capacity` and `booked` still hold `60` and `25`.

    `spaces` does not update itself. If you change `booked` to `30`, run
    `spaces = capacity - booked` again to get `30`.
    """)
    return


@app.cell(hide_code=True)
def values():
    mo.md("""
    ## A value has a type

    The type decides what you can do with the value.

    `60` is an integer and `2.5` is a float.

    `"60"` is a string of text and `True` is a Boolean.

    `"6" + "0"` joins two strings to give `"60"`.
    """)
    return


@app.cell
def demo_casting():
    tickets_text = "4"
    price_text = "3.75"
    cost = int(tickets_text) * float(price_text)
    str(cost)
    "Total: £" +str(cost)
    return


@app.cell(hide_code=True)
def lab_one():
    mo.hstack(
        [
            mo.md(f"""
            ## Lab 1 takes 20 minutes

            No need to save a copy :)
            """),
            colab_qr,
        ],
        widths=[2, 1],
        align="center",
    )
    return


@app.cell(hide_code=True)
def decisions():
    mo.md("""
    ## A comparison asks a yes-or-no question

    `=` assigns a value. `==` compares two values.

    A comparison gives a Boolean: `True` or `False`.

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

            If there is room, accept another booking. Otherwise, say the room is full.
            """),
            mo.hstack(
                [
                    mo.md("""
                    ```python
                    booked = 25
                    capacity = 60
                    if booked < capacity:
                        print("You can book a place")
                        print("test)
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
        ]
    )
    return


@app.cell(hide_code=True)
def if_branches():
    mo.md("""
    ## The condition picks one branch

    The condition is `True`, so this prints **You can book a place** and skips the `else` branch.
    With `booked = 60`, it would print **The room is full** instead.

    The colon starts a branch. Press Tab to indent the code inside it.
    `else` runs when the condition is `False`.
    """)
    return


@app.cell(hide_code=True)
def price_controls():
    age = mo.ui.slider(5, 80, value=30, label="age", show_value=True)
    is_member = mo.ui.switch(label="is_member")
    return age, is_member


@app.cell(hide_code=True)
def elif_flow(age, is_member):
    _branches = [
        ("age < 12", age.value < 12, "0.00"),
        ("is_member", is_member.value, "1.50"),
        ("age >= 65", age.value >= 65, "2.00"),
    ]
    _taken = next((i for i, (_, true, _) in enumerate(_branches) if true), 3)

    _lines = [(f"age = {age.value}", ""), (f"is_member = {is_member.value}", "")]
    for _i, (_condition, _, _price) in enumerate(_branches):
        _check = "True" if _i == _taken else "False" if _i < _taken else "not checked"
        _lines.append((f"{'if' if _i == 0 else 'elif'} {_condition}:", _check))
        _lines.append((f"    price = {_price}", "runs" if _i == _taken else ""))
    _lines.append(("else:", ""))
    _lines.append(("    price = 2.50", "runs" if _taken == 3 else ""))
    _code = "\n".join(f"{c:<20}# {n}" if n else c for c, n in _lines)

    _path_edges = [2 * i + 1 for i in range(min(_taken, 3))] + ([2 * _taken] if _taken < 3 else [])
    _checked = [f"D{i}" for i in range(min(_taken + 1, 3))]
    _skipped = [f"D{i}" for i in range(_taken + 1, 3)] + [f"P{i}" for i in range(4) if i != _taken]
    _flow = f"""
    graph TB
        D0{{"age #lt; 12?"}} -->|True| P0["price = 0.00"]
        D0 -->|False| D1{{"is_member?"}}
        D1 -->|True| P1["price = 1.50"]
        D1 -->|False| D2{{"age #gt;= 65?"}}
        D2 -->|True| P2["price = 2.00"]
        D2 -->|False| P3["price = 2.50"]
        classDef checked stroke:#eb6834,stroke-width:3px
        classDef taken fill:#eb6834,stroke:#eb6834,color:#fff
        classDef skipped fill:#f4f4f2,stroke:#d6d5d0,color:#a9a8a3
        class {",".join(_checked)} checked
        class P{_taken} taken
        class {",".join(_skipped)} skipped
        linkStyle {",".join(map(str, _path_edges))} stroke:#eb6834,stroke-width:3px
    """

    _status = (
        f"`{_branches[_taken][0]}` is the first `True` condition, so `price = {_branches[_taken][2]}`."
        if _taken < 3
        else "No condition is `True`, so the `else` branch runs: `price = 2.50`."
    )

    mo.vstack(
        [
            mo.md("""
            ## elif checks conditions in order

            Python runs the branch under the first `True` condition and skips the rest.
            """),
            mo.hstack([age, is_member], justify="start", gap=2),
            mo.hstack(
                [mo.md(f"```python\n{_code}\n```"), mo.mermaid(_flow)],
                widths=[1, 1],
                align="center",
            ),
            mo.md(_status),
        ]
    )
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
            mo.md("For example, a misspelled variable name causes a `NameError`."),
        ]
    )
    return


@app.cell
def demo_errors():
    capacity = 60
    booked = 25
    if booked < capacity:
        message = "Spaces left: " + str(capacity - booked)
    else:
        mesage = "Full"
    message
    return


@app.cell(hide_code=True)
def learn():
    mo.md("""
    ## Reading documentation

    How do you round a number to one decimal place?

    Find the function in the Python documentation, check what inputs it needs, then use it.
    """)
    return


@app.cell
def demo_documentation():
    round(3.7)
    # round(0.5)
    # round(1.5)
    round(2.5)
    return


@app.cell(hide_code=True)
def lab_two():
    mo.hstack(
        [
            mo.md(f"""
            ## Lab 2 takes 20 minutes

            Go to **Lab 2** in [Colab]({colab_url}).

            1. Predict and test the messages for 25, 60 and 61 bookings.
            2. Read two errors and fix the code.
            3. Use the documentation to round a room’s occupancy percentage.

            Finish with the checkpoint. Group bookings and a logic bug are optional extensions.
            """),
            colab_qr,
        ],
        widths=[2, 1],
        align="center",
    )
    return


if __name__ == "__main__":
    app.run()
