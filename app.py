from shiny import *
import uvicorn
import os
  
runID = os.environ['DOMINO_RUN_ID']
userID = os.environ['DOMINO_PROJECT_OWNER']
projectID = os.environ['DOMINO_PROJECT_NAME']

path_prefix = f"/{userID}/{projectID}/r/notebookSession/{runID}"

app_ui = ui.page_fluid(
    ui.input_slider("n", "N", min=0, max=100, value=20),
    ui.output_text_verbatim("txt", placeholder=True),
)

# A reactive.Value which is exists outside of the session.
shared_val = reactive.Value(None)


def server(input: Inputs, output: Outputs, session: Session):
    @reactive.Calc
    def r():
        if input.n() is None:
            return
        return input.n() * 2

    @output
    @render.text
    async def txt():
        val = r()
        return f"n*2 is {val}, session id is {session.id}"


app = App(app_ui, server)

if __name__ == "__main__":
  uvicorn.run("app:app",host="0.0.0.0",port=8888)
