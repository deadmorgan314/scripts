from reactpy import component, run, html
@component
def App():
    return html.div(
        html.h1("Hello World!"),
        html.h2("Hello World!"),
        html.p("Some text"),
        html.input(),
        html.button("Don`t click me!")
    )
run(App)