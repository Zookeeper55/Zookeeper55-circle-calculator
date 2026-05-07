from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from starlette.requests import Request
import uvicorn


cyl_site = FastAPI()


templates = Jinja2Templates(directory="templates")

@cyl_site.get("/", response_class=HTMLResponse)
async def ylsite(request: Request):
    """
    GET path: /
    Displays the volume formula for a cylinder
    """
    vmsg = "Volume of Cylinder = 3.14159*r*r*h; where r=radius, h=height"
    return templates.TemplateResponse("home.html", {"request": request, "vmsg": vmsg})

@cyl_site.get("/cylinder/{r}/{h}", response_class=HTMLResponse)
async def volcylinder(request: Request, r: float, h: float):
    """
    GET path: /cylinder/r/h
    Computes and displays the volume of a cylinder
    r: radius (float)
    h: height (float)
    """
   
    volume = 3.14159 * r * r * h
   
    vresult = f"{volume:,.3f}"
    return templates.TemplateResponse("result.html", {"request": request, "vresult": vresult})

if __name__ == "__main__":
    uvicorn.run(cyl_site, host="0.0.0.0", port=1753)
