
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from starlette.requests import Request
import math

circ_site = FastAPI()


templates = Jinja2Templates(directory="templates")

@circ_site.get("/", response_class=HTMLResponse)
async def csite(request: Request):
    vmsg = "Area of Circle = 3.14159*r*r; where r=radius"
    return templates.TemplateResponse("home.html", {"request": request, "vmsg": vmsg})

@circ_site.get("/circle/{r}", response_class=HTMLResponse)
async def areacircle(request: Request, r: float):
    area = math.pi * r * r
    vresult = f"{area:,.5f}"
    return templates.TemplateResponse("result.html", {"request": request, "vresult": vresult})

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(circ_site, host="0.0.0.0", port=5254)

=== templates/home.html ===
<!DOCTYPE html>
<html>
<head>
    <title>Area of Circle Calculator</title>
</head>
<body>
    <p style="font-family:arial;font-size:20px;">{{ vmsg }}</p>
</body>
</html>

=== templates/result.html ===
<!DOCTYPE html>
<html>
<head>
    <title>Circle Area Result</title>
</head>
<body>
    <p style="font-family:arial;font-size:20px;">{{ vresult }}</p>
</body>
</html>
