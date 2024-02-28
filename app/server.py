from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from langserve import add_routes
from rag_gemini_multi_modal import chain as rag_gemini_multi_modal_chain
import os
app = FastAPI()


@app.get("/")
async def redirect_root_to_docs():
    return RedirectResponse("/docs")


# Edit this to add the chain you want to add
add_routes(app, rag_gemini_multi_modal_chain, path='/rag-gemini-multi-modal')

if __name__ == "__main__":
    import uvicorn
    # os.environ["GOOGLE_API_KEY"] = api_key.google_apikey

    uvicorn.run(app, host="0.0.0.0", port=8000)
