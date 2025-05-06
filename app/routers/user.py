from collections import defaultdict

from fastapi import APIRouter, Form, HTTPException
from fastapi.responses import HTMLResponse, RedirectResponse, Response
from fastapi.requests import Request
from fastapi.templating import Jinja2Templates

from app.services.category import CategoryService
from app.services.currency import CurrencyService
from app.services.income import IncomeService
from app.services.outcome import OutcomeService
from app.services.user import UserService

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/register", response_class=HTMLResponse)
async def register_form(request: Request):
    return templates.TemplateResponse("register.html", {"request": request})

@router.get("/info", response_class=HTMLResponse)
async def info(request: Request):
    return templates.TemplateResponse("info.html", {"request": request})

@router.post("/register", response_class=HTMLResponse)
async def register_user(
    request: Request,
    login: str = Form(...),
    password: str = Form(...),
    name: str = Form(...),
    surname: str = Form(...)
):
    user_id = UserService().register(login, password, name, surname)
    if user_id is None:
        return RedirectResponse("/register?error=user_exists", status_code=303)
    print(f"New user: {login}, {password}, {name}, {surname}")
    return RedirectResponse("/login", status_code=303)

@router.get("/login", response_class=HTMLResponse)
async def login_form(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

@router.post("/login", response_class=HTMLResponse)
async def login_user(
    request: Request,
    response: Response,
    login: str = Form(...),
    password: str = Form(...),
):
    user = UserService().login(login, password)
    if user is None:
        return RedirectResponse("/login?error=wrong_data", status_code=303)
    return RedirectResponse(f"/?user_id={user[0]}", status_code=303)


@router.get("/", response_class=HTMLResponse)
async def home(request: Request):
    user_id = request.query_params.get("user_id")
    # if not user_id:
    #     return RedirectResponse("/login", status_code=303)

    incomes = IncomeService().get_all(user_id)
    outcomes = OutcomeService().get_all(user_id)
    categories = CategoryService().get_all()
    currencies = CurrencyService().get_currencies()

    income_sums = defaultdict(float)
    for i in incomes:
        income_sums[i[5]] += i[3]

    outcome_sums = defaultdict(float)
    for o in outcomes:
        outcome_sums[o[5]] += o[3]

    return templates.TemplateResponse("home.html", {
        "request": request,
        "user_id": user_id,
        "incomes": incomes,
        "outcomes": outcomes,
        "categories": categories,
        "currencies": currencies,
        "income_sums": income_sums,
        "outcome_sums": outcome_sums
    })


@router.post("/income/create")
async def create_income(
    user_id: str = Form(...),
    category_id: str = Form(...),
    amount: float = Form(...),
    currency_id: str = Form(...),
    description: str = Form(None)
):
    IncomeService().create(user_id, category_id, amount, currency_id, description)
    return RedirectResponse(f"/?user_id={user_id}", status_code=303)


@router.post("/outcome/create")
async def create_outcome(
    user_id: str = Form(...),
    category_id: str = Form(...),
    amount: float = Form(...),
    currency_id: str = Form(...),
    date: str = Form(...),
    description: str = Form(None)
):
    OutcomeService().create(user_id, category_id, amount, currency_id, date, description)
    return RedirectResponse(f"/?user_id={user_id}", status_code=303)

@router.get("/get_categories")
async def get_categories():
    categories = CategoryService().get_all()
    return categories

@router.get("/get_currencies")
async def get_currencies():
    currencies = CurrencyService().get_currencies()
    return currencies

@router.post("/income/delete/{income_id}")
async def delete_income(income_id: int, user_id: str = Form(...)):
    IncomeService().delete_by_id(user_id, income_id)
    return RedirectResponse(f"/?user_id={user_id}", status_code=303)

@router.post("/income/update/{income_id}")
async def update_income(
    income_id: int,
    user_id: str = Form(...),
    category_id: str = Form(...),
    amount: float = Form(...),
    currency_id: str = Form(...),
    description: str = Form(None)
):
    IncomeService().update_by_id(user_id, income_id, category_id, amount, currency_id, description)
    return RedirectResponse(f"/?user_id={user_id}", status_code=303)

@router.post("/outcome/delete/{outcome_id}")
async def delete_outcome(outcome_id: int, user_id: str = Form(...)):
    OutcomeService().delete_by_id(user_id, outcome_id)
    return RedirectResponse(f"/?user_id={user_id}", status_code=303)

@router.post("/outcome/update/{outcome_id}")
async def update_outcome(
    outcome_id: int,
    user_id: str = Form(...),
    category_id: str = Form(...),
    amount: float = Form(...),
    currency_id: str = Form(...),
    date: str = Form(...),
    description: str = Form(None)
):
    OutcomeService().update_by_id(user_id,outcome_id, category_id, amount, currency_id, date, description)
    return RedirectResponse(f"/?user_id={user_id}", status_code=303)