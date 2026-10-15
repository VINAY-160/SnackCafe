from fastapi import FastAPI,Query,HTTPException
from models import MenuItem,MenuResponse
from data import menu_items

app=FastAPI(
    title="Chai Point Menu API",
    description=("Read only menu API for kiosk display and mobile apps")
)

@app.get("/")
def read_root():
    return {
        "message":"Welcome to Chai Point Menu API"
    }

# /menu -> Path Parameter
# /menu?category="chai"&available=true -> Query Parameters

@app.get("/menu",response_model=MenuResponse)
def get_menu(category: str | None =Query(None,description=("Filter by category chai or combos or snack"))):
    if category:
        filtered=[]
        for items in menu_items:
            if category.lower()==items["category"]:
                filtered.append(items)
        if not filtered:
            raise HTTPException(status_code=404,detail=f"No items found in category:{category}")
        return MenuResponse(count=len(filtered),items=filtered)
        
    return MenuResponse(count=len(menu_items),items=menu_items)

@app.get("/menu/{items_id}",response_model=MenuItem)
def get_MenuById(items_id:int):
    for items in menu_items:
        if items["id"]==items_id:
            return items
    raise HTTPException(status_code=404,detail=f"No items found with id:{items_id}") 