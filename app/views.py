from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, Cart, Orders, Address, Payment
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.db.models import Q
from django.core.exceptions import ValidationError
from django.contrib import messages


# Create your views here.
def index(request):
    allproducts = Product.objects.all()
    context = {"allproducts": allproducts}
    return render(request, "index.html", context)


def validate_password(password):
    # Check minimum length
    if len(password) < 8:
        raise ValidationError("Password must be at least 8 characters long.")

    # Check maximum length
    if len(password) > 128:
        raise ValidationError("Password cannot exceed 128 characters.")

    # Initialize flags for character checks
    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False
    special_characters = "@$!%*?&"

    # Check for character variety
    for char in password:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isdigit():
            has_digit = True
        elif char in special_characters:
            has_special = True

    if not has_upper:
        raise ValidationError("Password must contain at least one uppercase letter.")
    if not has_lower:
        raise ValidationError("Password must contain at least one lowercase letter.")
    if not has_digit:
        raise ValidationError("Password must contain at least one digit.")
    if not has_special:
        raise ValidationError(
            "Password must contain at least one special character (e.g., @$!%*?&)."
        )

    # Check against common passwords
    common_passwords = [
        "password",
        "123456",
        "qwerty",
        "abc123",
    ]  # Add more common passwords
    if password in common_passwords:
        raise ValidationError("This password is too common. Please choose another one.")


def signup(request):
    if request.method == "POST":
        uname = request.POST["uname"]
        email = request.POST["email"]
        upass = request.POST["upass"]
        ucpass = request.POST["ucpass"]
        context = {}
        try:
            validate_password(upass)
        except ValidationError as e:
            context["errmsg"] = str(e)
            return render(request, "signup.html", context)

        if uname == "" or email == "" or upass == "" or ucpass == "":
            context["errmsg"] = "Field can't be empty"
            return render(request, "signup.html", context)
        elif upass != ucpass:
            context["errmsg"] = "Password and confirm password doesn't match"
            return render(request, "signup.html", context)
        elif uname.isdigit():
            context["errmsg"] = "Username cannot consist solely of numbers."
            return render(request, "signup.html", context)
        else:
            try:
                userdata = User.objects.create(
                    username=uname, email=email, password=upass
                )
                userdata.set_password(upass)
                userdata.save()
                return redirect("/signin")
            except:
                context["errmsg"] = "User Already exists"
                return render(request, "signup.html", context)
    else:
        context = {}
        context["errmsg"] = ""
        return render(request, "signup.html", context)


def signin(request):
    if request.method == "POST":
        email = request.POST["email"]
        upass = request.POST["upass"]
        context = {}
        if email == "" or upass == "":
            context["errmsg"] = "Field can't be empty"
            return render(request, "signin.html", context)
        else:
            user = User.objects.get(email=email)  # Retrieve user by email
            userdata = authenticate(username=user.username, password=upass)
            print(userdata)
            if userdata is not None:
                login(request, userdata)
                return redirect("/")
            else:
                context["errmsg"] = "Invalid username and password"
                return render(request, "signin.html", context)
    else:
        return render(request, "signin.html")


def userlogout(request):
    logout(request)
    return redirect("/")


def request_password_reset(request):
    if request.method == "POST":
        email = request.POST.get("email")
        context = {}

        # Check if the email exists
        try:
            user = User.objects.get(email=email)
            # Redirect to the password reset page
            return redirect("reset_password", username=user.username)
        except User.DoesNotExist:
            context["errmsg"] = "No account found with that email."
            return render(request, "request_password_reset.html", context)

    return render(request, "request_password_reset.html")


def reset_password(request, username):
    try:
        user = User.objects.get(username=username)

        if request.method == "POST":
            new_password = request.POST.get("new_password")
            try:
                validate_password(new_password)
                user.set_password(new_password)  # Hash the password
                user.save()
                messages.success(request, "Your password has been reset successfully.")
                return redirect(
                    "signin"
                )  # Redirect to the signin page after successful reset

            except ValidationError as e:
                messages.error(request, str(e))  # Show the validation error message
                return render(
                    request, "reset_password.html", {"username": username}
                )  # Stay on the same page

        return render(request, "reset_password.html", {"username": username})

    except User.DoesNotExist:
        messages.error(request, "User not found.")
        return redirect("request_password_reset")


# working
def earringslist(request):
    allproducts = Product.productmanager.earrings_list()
    context = {"allproducts": allproducts}
    return render(request, "index.html", context)


def cocktailringlist(request):
    allproducts = Product.productmanager.cocktail_ring_list()
    context = {"allproducts": allproducts}
    return render(request, "index.html", context)


def necklacelist(request):
    allproducts = Product.productmanager.necklace_list()
    context = {"allproducts": allproducts}
    return render(request, "index.html", context)


def banglelist(request):
    allproducts = Product.productmanager.bangle_list()
    context = {"allproducts": allproducts}
    return render(request, "index.html", context)


def mangalsutralist(request):
    allproducts = Product.productmanager.mangal_sutra_list()
    context = {"allproducts": allproducts}
    return render(request, "index.html", context)


def chainlist(request):
    allproducts = Product.productmanager.chain_list()
    context = {"allproducts": allproducts}
    return render(request, "index.html", context)


def engagementringlist(request):
    allproducts = Product.productmanager.engagement_ring_list()
    context = {"allproducts": allproducts}
    return render(request, "index.html", context)


def braceletlist(request):
    allproducts = Product.productmanager.bracelet_list()
    context = {"allproducts": allproducts}
    return render(request, "index.html", context)


def elfearcuffslist(request):
    allproducts = Product.productmanager.elfearcuffslist()
    context = {"allproducts": allproducts}
    return render(request, "index.html", context)


def weddingringslist(request):
    allproducts = Product.productmanager.wedding_rings_list()
    context = {"allproducts": allproducts}
    return render(request, "index.html", context)


def ankletslist(request):
    allproducts = Product.productmanager.anklets_list()
    context = {"allproducts": allproducts}
    return render(request, "index.html", context)


def broochlist(request):
    allproducts = Product.productmanager.brooch_list()
    context = {"allproducts": allproducts}
    return render(request, "index.html", context)


def solitaireringlist(request):
    allproducts = Product.productmanager.solitaire_ring_list()
    context = {"allproducts": allproducts}
    return render(request, "index.html", context)


def toeringlist(request):
    allproducts = Product.productmanager.toe_ring_list()
    context = {"allproducts": allproducts}
    return render(request, "index.html", context)


def medallionlist(request):
    allproducts = Product.productmanager.medallion_list()
    context = {"allproducts": allproducts}
    return render(request, "index.html", context)


def hairpinlist(request):
    allproducts = Product.productmanager.hairpin_list()
    context = {"allproducts": allproducts}
    return render(request, "index.html", context)


def searchproduct(request):
    query = request.GET.get("q")
    errmsg = ""
    if query:
        allproducts = Product.objects.filter(
            Q(productname__icontains=query)
            | Q(category__icontains=query)
            | Q(description__icontains=query)
        )
        if len(allproducts) == 0:
            errmsg = "No result found!!"
    else:
        allproducts = Product.objects.all()

    context = {"allproducts": allproducts, "errmsg": errmsg}
    return render(request, "index.html", context)


def showpricerange(request):
    if request.method == "GET":
        return render(request, "index.html")
    else:
        r1 = request.POST["min"]
        r2 = request.POST.get("max")
        if r1 is not None and r2 is not None and r1.isdigit() and r2.isdigit():
            allproducts = Product.objects.filter(price__range=(r1, r2))
            print(allproducts)
            context = {"allproducts": allproducts}
            return render(request, "index.html", context)
        else:
            allproducts = Product.objects.all()
            context = {"allproducts": allproducts}
            return render(request, "index.html", context)


def sortingbyprice(request):
    sortoption = request.GET.get("sort")
    if sortoption == "low_to_high":
        allproducts = Product.objects.order_by("price")  # asc order
    elif sortoption == "high_to_low":
        allproducts = Product.objects.order_by("-price")  # desc order
    else:
        allproducts = Product.objects.all()

    context = {"allproducts": allproducts}
    return render(request, "index.html", context)


def showcarts(request):
    user = request.user
    allcarts = Cart.objects.filter(userid=user.id)
    totalamount = 0

    for x in allcarts:
        totalamount += x.productid.price * x.qty

    totalitems = len(allcarts)
    # totalitems = len(allcarts)

    if request.user.is_authenticated:
        context = {
            "allcarts": allcarts,
            "username": user,
            "totalamount": totalamount,
            "totalitems": totalitems,
        }
    else:
        context = {
            "allcarts": allcarts,
            "totalamount": totalamount,
            "totalitems": totalitems,
        }

    return render(request, "showcarts.html", context)


def addtocart(request, productid):
    if request.user.is_authenticated:
        user = request.user
    else:
        user = None

    allproducts = get_object_or_404(Product, productid=productid)
    cartitem, created = Cart.objects.get_or_create(productid=allproducts, userid=user)
    if not created:
        cartitem.qty += 1
    else:
        cartitem.qty = 1

    cartitem.save()
    return redirect("/showcarts")


def removecart(request, productid):
    user = request.user
    cartitems = Cart.objects.get(productid=productid, userid=user.id)
    cartitems.delete()
    return redirect("/showcarts")


def updateqty(request, qv, productid):
    allcarts = Cart.objects.filter(productid=productid)
    if qv == 1:
        total = allcarts[0].qty + 1
        allcarts.update(qty=total)
    else:
        if allcarts[0].qty > 1:
            total = allcarts[0].qty - 1
            allcarts.update(qty=total)
        else:
            allcarts = Cart.objects.filter(productid=productid)
            allcarts.delete()

    return redirect("/showcarts")
