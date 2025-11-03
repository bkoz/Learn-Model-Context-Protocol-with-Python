from starlette.applications import Starlette
from starlette.responses import JSONResponse
from starlette.routing import Route


async def homepage(request):
    return JSONResponse({'hello': 'world'})

async def health(request):
    return JSONResponse({'health': 'is OK'})

app = Starlette(debug=True, routes=[
    Route('/', homepage), Route('/health', health)
])

# uvicorn main:app